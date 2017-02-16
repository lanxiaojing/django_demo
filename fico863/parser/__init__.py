# -*- coding: utf-8 -*-

from .parse_html import parse_page
from .write_parsed_html_to_mysql import JsonStructure, DBOperation
from bs4 import BeautifulSoup
from ..models import Report, QueryRecordSummary, CreditApprovalQueryRecordDetail, Person, Couple, Address, Profession, Loan, DebitCard, SemiCreditCard, SpecialTransaction
import json


def parse_and_save(files):
    soup = get_soup(files)
    res = parse_page(soup)
    json_res = json.dumps(res)
    json_res = json_res.decode('unicode-escape')
    # with open('somefile.txt', 'a') as the_file:
    #     the_file.write(json_res)
    json_res = json.loads(json_res)
    tables = {
        "report": Report,
        "query_record_summary": QueryRecordSummary,
        "credit_approval_query_record_detail": CreditApprovalQueryRecordDetail,
        "person": Person,
        "couple": Couple,
        "address": Address,
        "profession": Profession,
        "loan": Loan,
        "debit_card": DebitCard,
        "semi_credit_card": SemiCreditCard,
        "special_transaction": SpecialTransaction,
    }
    structurer = JsonStructure(json_res)
    structurer.struct_all()
    db_operation = DBOperation()
    db_operation.save(tables, infos=structurer)
    certificate_code = structurer.person.get("CERTIFICATECODE")
    report_date = structurer.person.get("REPORTDATE")
    return certificate_code, report_date


def get_soup(files):
    return BeautifulSoup(''.join(files), 'lxml')
