# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r"^$", "fico863.views.index", name='index'),
    url(r"^account/", include("account.urls")),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^upload/$", "fico863.views.upload", name="upload"),
    url(r"^preview/$", "fico863.views.preview", name="preview"),
    url(r"^save/$", "fico863.views.save", name="save"),
    url(r"^report/$", "fico863.views.report", name="report"),
    url(r"^credit-score/$", "fico863.views.credit_score", name="credit_score"),
    url(r"^loan-option/$", "fico863.views.loan_option", name="loan_option"),
    url(r"^query-history/$", "fico863.views.query_history", name="query_history"),
    url(r"^manual-input/$", "fico863.views.manual_input", name="manual_input"),

]
