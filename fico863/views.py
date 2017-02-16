# -*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from .score import score
from .parser import parse_and_save
from . import models
import json
import itertools


def render_template(template, **kwargs):
    new_kwargs = {"settings": settings}

    if "settings" in kwargs:
        kwargs.pop("settings")

    if "request" in kwargs:
        request = kwargs["request"]

    if "current_nav" not in kwargs:
        if "breadcrumbs" in kwargs and kwargs['breadcrumbs']:
            kwargs["current_nav"] = kwargs["breadcrumbs"][-1]["title"]
        else:
            kwargs["current_nav"] = None

    new_kwargs.update(kwargs)

    if request:
        instance = RequestContext(request)
        return render_to_response(template,
                                  new_kwargs,
                                  context_instance=instance)

    return render_to_response(template, new_kwargs)


def index(request):
    return render_template("fico863/index.html", request=request)


def upload(request):
    if request.method == "POST":
        files = request.FILES["avatar"].read()
        certificate_code, report_date = parse_and_save(files)
        TEN_MINS = 10 * 60
        cache.set("CERTIFICATECODE", certificate_code, TEN_MINS)
        cache.set("REPORTDATE", report_date, TEN_MINS)
        return redirect(reverse('fico863.views.preview', args=[]))
    else:
        return render_template("fico863/format_choose.html", request=request)


@login_required
def manual_input(request):
    return render_template("fico863/manual_input.html", request=request)


@login_required
def preview(request):
    iterator = itertools.count()
    person_id = cache.get('CERTIFICATECODE')
    report_date = cache.get("REPORTDATE")
    single_data = [
        'Report', 'Person', 'Couple', 'CreditTips', 'WithInTimeLimit',
        'OverdraftOverdue', 'OutstandingLoans',
        'NoPinAccurateBorrowWriteDownCard', 'QueryRecordSummary'
    ]
    multiple_data = [
        'Address', 'Profession', 'Loan', 'DebitCard', 'SemiCreditCard',
        'HousingProvidentFundPaymentRecord', 'CreditApprovalQueryRecordDetail'
    ]
    single_dict = {}
    multiple_dict = {}

    for item in single_data:
        model = getattr(models, item)
        query_set = model.objects.filter(CERTIFICATECODE=person_id,
                                         REPORTDATE=report_date)
        if query_set:
            query_set = query_set[0]
        single_dict[item] = query_set
    for item in multiple_data:
        model = getattr(models, item)
        query_set = model.objects.filter(CERTIFICATECODE=person_id,
                                         REPORTDATE=report_date)
        multiple_dict[item] = query_set

    return render_template(
        "fico863/preview.html",
        request=request,
        Report=single_dict['Report'],
        Person=single_dict['Person'],
        Couple=single_dict['Couple'],
        CreditTips=single_dict['CreditTips'],
        WithInTimeLimit=single_dict['WithInTimeLimit'],
        OverdraftOverdue=single_dict['OverdraftOverdue'],
        OutstandingLoans=single_dict['OutstandingLoans'],
        NoPinAccurateBorrowWriteDownCard=single_dict[
            'NoPinAccurateBorrowWriteDownCard'],
        QueryRecordSummary=single_dict['QueryRecordSummary'],
        Address=multiple_dict['Address'],
        Profession=multiple_dict['Profession'],
        Loan=multiple_dict['Loan'],
        DebitCard=multiple_dict['DebitCard'],
        SemiCreditCard=multiple_dict['SemiCreditCard'],
        HousingProvidentFundPaymentRecord=multiple_dict[
            'HousingProvidentFundPaymentRecord'],
        CreditApprovalQueryRecordDetail=multiple_dict[
            'CreditApprovalQueryRecordDetail'],
        iterator=iterator)


@login_required
def save(request):
    if request.method == 'POST':
        person_id = request.POST.get('person_id')
        report_date = request.POST.get('report_date')
        TEN_MINS = 10 * 60
        cache.set("CERTIFICATECODE", person_id, TEN_MINS)
        cache.set("REPORTDATE", report_date, TEN_MINS)
        info = request.POST.get('info')
        info = json.loads(info)
        for key, value in info.iteritems():
            _save_data(person_id, report_date, key, value)
    else:
        pass
    return


@login_required
def report(request):
    front_report = score(11)
    person = models.Person.objects.get(id=1)
    return render_template("fico863/report.html",
                           request=request,
                           front_report=front_report,
                           person=person)


@login_required
def credit_score(request):
    try:
        loantype = cache.get('loantype')
    except:
        loantype = None

    if loantype:
        front_report = score(loantype)
        history = models.QueryHistory(USERID=request.user.id)
        history.CERTIFICATECODE = cache.get("CERTIFICATECODE")
        history.SCORE = front_report.get("score")
        history.SCOREDETAIL = front_report
        history.save()
        return render_template("fico863/credit_score.html",
                               request=request,
                               front_report=front_report)
    else:
        return render_template("fico863/credit_score.html", request=request)


@login_required
def loan_option(request):
    if request.method == "POST":
        loantype = int(request.POST.get('loantype'))
        cache.set("loantype", loantype, 10 * 60)
        print "########################"
        return redirect(reverse('fico863.views.credit_score', args=[]))
    else:
        return render_template("fico863/loan_option.html", request=request)


@login_required
def query_history(request):
    if request.method == "GET":
        user_id = request.user.id
        query_histories = models.QueryHistory.objects.filter(USERID=user_id)
        return render_template("fico863/query_history.html",
                               request=request,
                               histories=query_histories)
    else:
        print request.POST
        history_id = request.POST.get("id")
        creditaudit = request.POST.get("CREDITAUDIT")
        payment = request.POST.get("PAYMENT")
        history = models.QueryHistory.objects.get(id=history_id)
        if creditaudit:
            history.CREDITAUDIT = creditaudit
        if payment:
            history.PAYMENT = payment
        history.save()


def _save_data(person_id, report_date, model_name, model_data):
    initial_model = getattr(models, model_name)
    model = initial_model()
    model.REPORTDATE = report_date
    model.CERTIFICATECODE = person_id
    if type(model_data) == list:
        for item in model_data:
            for key, value in item.iteritems():
                setattr(model, key, value)
        model.save()
    elif type(model_data) == dict:
        for key, value in model_data.iteritems():
            setattr(model, key, value)
        model.save()

    else:
        pass
