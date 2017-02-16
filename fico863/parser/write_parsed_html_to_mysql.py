# -*- coding: utf-8 -*-


class Consts(object):
    mappings = {
        u"报告基本信息": {
            u"报告编号": u"REPORTID",
            u"查询请求时间": u"REQUESTTIME",
            u"报告时间": u"REPORTDATE"
        },
        u"报告内容": {
            u"报告说明": {
                u"被查询者姓名": u"INFORMANTNAME",
                u"被查询者证件号码": u"CERTIFICATECODE",
                u"查询操作员": u"QUERYOPR",
                u"被查询者证件类型": u"CERTIFICATETYPE",
                u"查询原因": u"QUERYCODE"
            },
            u"查询记录汇总": {
                u"最近1个月内的查询机构数": {
                    u"贷款审批": "",
                    u"信用卡审批": u"CREDITAPPROVAL_ORG"
                },
                u"最近1个月内的查询次数": {
                    u"贷款审批": u"LOANAPPROVAL_QUERY",
                    u"信用卡审批": u"CREDITAPPROVAL_QUERY",
                    u"本人查询": u"PERSONAL_QUERY"
                },
                u"最近2年内的查询次数": {
                    u"贷后管理": u"LOANMANAGE",
                    u"担保资格审查": u"GUARANTEEREVIEW",
                    u"特约商户实名审查": u"MERCNAMEREVIEW"
                }
            },
            u"信贷审批查询记录明细": {
                u"编号": u"",
                u"查询日期": u"QUERYDATE",
                u"查询操作员": u"OPER",
                u"查询原因": u"QUERYREASONNAME"
            },
            u"basics": {
                u"身份信息": {
                    u"性别": u"GENDER",
                    u"出生日期": u"BIRTHDAY",
                    u"婚姻状况": u"MARRIDGE",
                    u"手机号码": u"MOBILEPHONE",
                    u"单位电话": u"WORKPHONE",
                    u"住宅电话": u"HOMEPHONE",
                    u"学历": u"EDUCATION",
                    u"学位": u"DEGREE",
                    u"通讯地址": u"CONTACTADDRESS",
                    u"户籍地址": u"HOUSEHOLD"
                },
                u"配偶信息": {
                    u"姓名": u"COUPLENAME",
                    u"证件类型": u"COUPLECERTYPE",
                    u"证件号码": u"COUPLECERCODE",
                    u"工作单位": u"COUPLECOMPANY",
                    u"联系电话": u"COUPLEPHONE"
                },
                u"居住信息": {
                    u"编号": u"",
                    u"居住地址": u"ADDRESS",
                    u"居住状况": u"LIVINGSTATUS",
                    u"信息更新日期": u"LIVEINFOUPDATEDATE"
                },
                u"职业信息": {
                    u"编号": u"",
                    u"工作单位": u"COMPANY",
                    u"单位地址": u"COMPANYADDRESS",
                    u"职业": u"OCCUPATION",
                    u"行业": u"INDUSTRY",
                    u"职务": u"JOB",
                    u"职称": u"TITLE",
                    u"进入本单位年份": u"WORKSTARTDATE",
                    u"信息更新日期": u"OCCUPATIONUPDATEDATE"
                }
            },
            u"loans": {
                u"detail": u"DETAIL",
                u"GUARANTEEWAYNAME": u"GUARANTEEWAYNAME",
                u"CURRENTNAME": u"CURRENTNAME",
                u"TERMSFREQ": u"TERMSFREQ",
                u"GUARANTEEWAY": u"GUARANTEEWAY",
                u"TYPENAME": u"TYPENAME",
                u"STATENDDATE": u"STATENDDATE",
                u"DATECLOSED": u"DATECLOSED",
                u"CREDITLIMIT": u"CREDITLIMIT",
                u"MONTHDURATION": u"MONTHDURATION",
                u"FINANCENAME": u"FINANCENAME",
                u"DATEOPENED": u"DATEOPENED",
                u"TERMSFREQNAME": u"TERMSFREQNAME",
                u"账户状态": u"STAT_FLAG",
                u'STAT_FLAG': u"STAT_FLAG",
                u"五级分类": u"CLASS5STAT",
                u'CLASS5STAT': u'CLASS5STAT',
                u"本金余额": u"BALANCE",
                u"剩余还款期数": u"MONTHUNPAID",
                u"本月应还款": u"SCHEDUALEDAMOUNT",
                u"应还款日": u"BILLINGDATE",
                u"本月实还款": u"ACTUALPAYAMOUNT",
                u"最近一次还款日期": u"RECENTPAYDATE",
                u"当前逾期期数": u"CURTERMPASTDUE",
                u"当前逾期金额": u"CURAMOUNTPASTDUE",
                u"逾期31-60天未还本金": u"AMOUNTPASTDUE30",
                u"逾期61－90天未还本金": u"AMOUNTPASTDUE60",
                u"逾期91－180天未还本金": u"AMOUNTPASTDUE90",
                u"逾期180天以上未还本金": u"AMOUNTPASTDUE180",
                u"特殊交易类型": u"SPECIALTYPE",
                u"发生日期": u"SPECIALDATE",
                u"变更月数": u"SPECIALMONTH",
                u"发生金额": u"SPECIALMONEY",
                u"明细记录": u"SPECIALDETAIL"
            },
            u"loancards": {
                u"detail": u"DETAIL",
                u"GUARANTEEWAYNAME": u"GUARANTEEWAYNAME",
                u"FINANCENAME": u"FINANCENAME",
                u"SHAREAMOUNT": u"SHAREAMOUNT",
                u"GUARANTEEWAY": u"GUARANTEEWAY",
                u"CURRENCY": u"CURRENCY",
                u"STATENDDATE": u"STATENDDATE",
                u"CREDITLIMIT": u"CREDITLIMIT",
                u"CURRENCYNAME": u"CURRENCYNAME",
                u"DATEOPENED": u"DATEOPENED",
                u"STAT_FLAG": u"STAT_FLAG",
                u"CLASS5STAT": u"CLASS5STAT",
                u"账户状态": u"STAT_FLAG",
                u"已用额度": u"BALANCE",
                u"最近6个月平均使用额度": u"AVG6AMOUNT",
                u"最大使用额度": u"MAXDEBT",
                u"本月应还款": u"SCHEDUALEDAMOUNT",
                u"账单日": u"ACCOUNTDATE",
                u"本月实还款": u"ACTUALPAYAMOUNT",
                u"最近一次还款日期": u"RECENTPAYDATE",
                u"当前逾期期数": u"CURTERMPASTDUE",
                u"当前逾期金额": u"CURAMOUNTPASTDUE"
            },
            u"creditcards": {
                u"detail": u"DETAIL",
                u"GUARANTEEWAYNAME": u"GUARANTEEWAYNAME",
                u"FINANCENAME": u"FINANCENAME",
                u"SHAREAMOUNT": u"SHAREAMOUNT",
                u"GUARANTEEWAY": u"GUARANTEEWAY",
                u"CURRENCY": u"CURRENCY",
                u"STATENDDATE": u"STATENDDATE",
                u"CREDITLIMIT": u"CREDITLIMIT",
                u"CURRENCYNAME": u"CURRENCYNAME",
                u"DATEOPENED": u"DATEOPENED",
                u"账户状态": u"CLASS5STAT",
                u"透支余额": u"BALANCE",
                u"最近6个月平均透支余额": u"AVG6AMOUNT",
                u"最大透支余额": u"MAXDEBT",
                u"账单日": u"ACCOUNTDATE",
                u"本月实还款": u"ACTUALPAYAMOUNT",
                u"最近一次还款日期": u"RECENTPAYDATE",
                u"透支180天以上未付余额": u"UNPAID180",
            }
        }
    }


class JsonStructure(object):
    """结构化解析的HTML
    """

    def __init__(self, parsed_html={}):
        self.parsed_html = parsed_html
        self.report = {}
        self.query_record_summary = {}
        self.credit_approval_query_record_detail = {}
        self.person = {}
        self.couple = {}
        self.address = {}
        self.profession = {}
        self.loan = {}
        self.debit_card = {}
        self.semi_credit_card = {}
        self.special_transaction = {}

    def struct_all(self):
        self.struct_report()
        self.struct_query_record_summary()
        self.struct_credit_approval_query_record_detail()
        self.struct_person()
        self.struct_couple()
        self.struct_address()
        self.struct_profession()
        self.struct_loan()
        self.struct_debit_card()
        self.struct_semi_credit_card()
        self.struct_special_transaction()

    def struct_report(self):
        labels = (u"报告基本信息", u"报告内容", u"报告说明", )
        mappings = Consts.mappings[labels[0]]
        report = self.parsed_html[labels[0]]
        for key, value in report.iteritems():
            self.report[mappings[key]] = value

        mappings = Consts.mappings[labels[1]][labels[2]]
        report = self.parsed_html[labels[1]][labels[2]]
        for key, value in report.iteritems():
            self.report[mappings[key]] = value

    def struct_query_record_summary(self):
        labels = (u"报告内容",
                  u"查询记录汇总",
                  u"最近1个月内的查询机构数",
                  u"最近1个月内的查询次数",
                  u"最近2年内的查询次数", )
        mappings = Consts.mappings[labels[0]][labels[1]][labels[2]]
        report = self.parsed_html[labels[0]][labels[1]][labels[2]]
        for key, value in report.iteritems():
            self.query_record_summary[mappings[key]] = value

        mappings = Consts.mappings[labels[0]][labels[1]][labels[3]]
        report = self.parsed_html[labels[0]][labels[1]][labels[3]]
        for key, value in report.iteritems():
            self.query_record_summary[mappings[key]] = value

        mappings = Consts.mappings[labels[0]][labels[1]][labels[4]]
        report = self.parsed_html[labels[0]][labels[1]][labels[4]]
        for key, value in report.iteritems():
            self.query_record_summary[mappings[key]] = value

        self.query_record_summary[u"REPORTDATE"] = self.report[u"REPORTDATE"]
        self.query_record_summary[u"CERTIFICATECODE"] = self.report.get(u"CERTIFICATECODE", 1)
        self.query_record_summary[u"REPORTID"] = self.report.get(u"REPORTID")

    def struct_credit_approval_query_record_detail(self):
        labels = (u"报告内容", u"信贷审批查询记录明细", )
        mappings = Consts.mappings[labels[0]][labels[1]]
        report = self.parsed_html[labels[0]][labels[1]]
        temp = {}
        result = []
        for key, value in report.iteritems():
            if key == u"编号":
                length = len(value)
            else:
                temp[mappings[key]] = value

        for i in range(0, length):
            d = {}
            d[u"REPORTDATE"] = self.report[u"REPORTDATE"]
            d[u"CERTIFICATECODE"] = self.report.get(u"CERTIFICATECODE", 1)
            d[u"REPORTID"] = self.report.get(u"REPORTID")
            for k, v in temp.iteritems():
                d[k] = v[i]
            result.append(d)

        self.credit_approval_query_record_detail = result

    def struct_person(self):
        labels = (u"报告内容", u"basics", u"身份信息", )
        mappings = Consts.mappings[labels[0]][labels[1]][labels[2]]
        report = self.parsed_html[labels[0]][labels[1]][labels[2]]
        for key, value in report.iteritems():
            self.person[mappings[key]] = value[0]
        self.person[u"REPORTDATE"] = self.report[u"REPORTDATE"]
        self.person[u"CERTIFICATECODE"] = self.report.get(u"CERTIFICATECODE", 1)
        self.person[u"REPORTID"] = self.report.get(u"REPORTID")

    def struct_couple(self):
        labels = (u"报告内容", u"basics", u"配偶信息", )
        mappings = Consts.mappings[labels[0]][labels[1]][labels[2]]
        report = self.parsed_html[labels[0]][labels[1]][labels[2]]
        for key, value in report.iteritems():
            self.couple[mappings[key]] = value[0]
        self.couple[u"REPORTDATE"] = self.report[u"REPORTDATE"]
        self.couple[u"CERTIFICATECODE"] = self.report.get(u"CERTIFICATECODE", 1)
        self.couple[u"REPORTID"] = self.report.get(u"REPORTID")

    def struct_address(self):
        labels = (u"报告内容", u"basics", u"居住信息", )
        mappings = Consts.mappings[labels[0]][labels[1]][labels[2]]
        report = self.parsed_html[labels[0]][labels[1]][labels[2]]
        temp = {}
        result = []
        for key, value in report.iteritems():
            if key == u"编号":
                length = len(value)
            else:
                temp[mappings[key]] = value
        for i in range(0, length):
            d = {}
            d[u"REPORTDATE"] = self.report[u"REPORTDATE"]
            d[u"CERTIFICATECODE"] = self.report.get(u"CERTIFICATECODE", 1)
            d[u"REPORTID"] = self.report.get(u"REPORTID")
            for k, v in temp.iteritems():
                d[k] = v[i]
            result.append(d)
        self.address = result

    def struct_profession(self):
        labels = (u"报告内容", u"basics", u"职业信息", )
        mappings = Consts.mappings[labels[0]][labels[1]][labels[2]]
        report = self.parsed_html[labels[0]][labels[1]][labels[2]]
        temp = {}
        result = []
        for key, value in report.iteritems():
            if key == u"编号":
                pass
            else:
                temp[mappings[key]] = value
                length = len(value)

        for i in range(0, length):
            d = {}
            d[u"REPORTDATE"] = self.report[u"REPORTDATE"]
            d[u"CERTIFICATECODE"] = self.report.get(u"CERTIFICATECODE", 1)
            d[u"REPORTID"] = self.report.get(u"REPORTID")
            for k, v in temp.iteritems():
                d[k] = v[i]
            result.append(d)
        self.profession = result

    def struct_loan(self):
        labels = (u"报告内容", u"loans", )
        excludes = (u"特殊交易类型", u"发生日期", u"变更月数", u"发生金额", u"明细记录", )
        mappings = Consts.mappings[labels[0]][labels[1]]
        report = self.parsed_html[labels[0]][labels[1]]
        result = []
        for loan in report:
            structed_loan = {}
            structed_loan[u"REPORTDATE"] = self.report[u"REPORTDATE"]
            structed_loan[u"CERTIFICATECODE"] = self.report.get(u"CERTIFICATECODE", 1)
            structed_loan[u"REPORTID"] = self.report.get(u"REPORTID")
            for key, value in loan.iteritems():
                if key in excludes:
                    pass
                elif type(value) == list and len(value) > 2:
                    structed_loan[u"PAYSTAT24MONTH"] = ''.join(value)
                elif type(value) == list and len(value) == 1:
                    structed_loan[mappings[key]] = value[0]
                else:
                    structed_loan[mappings[key]] = value
            result.append(structed_loan)
        self.loan = result

    def struct_debit_card(self):
        labels = (u"报告内容", u"loancards", )
        mappings = Consts.mappings[labels[0]][labels[1]]
        report = self.parsed_html[labels[0]][labels[1]]
        result = []
        for loan in report:
            structed_loancard = {}
            structed_loancard[u"REPORTDATE"] = self.report[u"REPORTDATE"]
            structed_loancard[u"CERTIFICATECODE"] = self.report.get(u"CERTIFICATECODE", 1)
            structed_loancard[u"REPORTID"] = self.report.get(u"REPORTID")
            for key, value in loan.iteritems():
                if type(value) == list and len(value) > 2:
                    structed_loancard[u"PAYSTAT24MONTH"] = ''.join(value)
                elif type(value) == list and len(value) == 1:
                    structed_loancard[mappings[key]] = value[0]
                else:
                    structed_loancard[mappings[key]] = value
            result.append(structed_loancard)
        self.debit_card = result

    def struct_semi_credit_card(self):
        labels = (u"报告内容", u"creditcards", )
        mappings = Consts.mappings[labels[0]][labels[1]]
        report = self.parsed_html[labels[0]][labels[1]]
        result = []
        for loan in report:
            structed_semi_credit_card = {}
            structed_semi_credit_card[u"REPORTDATE"] = self.report[u"REPORTDATE"]
            structed_semi_credit_card[u"CERTIFICATECODE"] = self.report.get(u"CERTIFICATECODE", 1)
            structed_semi_credit_card[u"REPORTID"] = self.report.get(u"REPORTID")
            for key, value in loan.iteritems():
                if type(value) == list and len(value) > 2:
                    structed_semi_credit_card[u"PAYSTAT24MONTH"] = ''.join(
                        value)
                elif type(value) == list and len(value) == 1:
                    structed_semi_credit_card[mappings[key]] = value[0]
                else:
                    structed_semi_credit_card[mappings[key]] = value
            result.append(structed_semi_credit_card)
        self.semi_credit_card = result

    def struct_special_transaction(self):
        labels = (u"报告内容", u"loans", )
        includes = (u"特殊交易类型", u"发生日期", u"变更月数", u"发生金额", u"明细记录", )
        mappings = Consts.mappings[labels[0]][labels[1]]
        report = self.parsed_html[labels[0]][labels[1]]
        result = []
        for loan in report:
            structed_special_transaction = {}
            structed_special_transaction[u"REPORTDATE"] = self.report[u"REPORTDATE"]
            structed_special_transaction[u"CERTIFICATECODE"] = self.report.get(u"CERTIFICATECODE", 1)
            structed_special_transaction[u"REPORTID"] = self.report.get(u"REPORTID")
            for key, value in loan.iteritems():
                if key in includes:
                    structed_special_transaction[mappings[key]] = value[0]

            result.append(structed_special_transaction)
        self.special_transaction = result

    def to_dict(self):

        return {
            "report": self.report,
            "query_record_summary": self.query_record_summary,
            "credit_approval_query_record_detail":
            self.credit_approval_query_record_detail,
            "person": self.person,
            "couple": self.couple,
            "address": self.address,
            "profession": self.profession,
            "loan": self.loan,
            "debit_card": self.debit_card,
            "semi_credit_card": self.semi_credit_card,
            "special_transaction": self.special_transaction,
        }


class DBOperation(object):
    def save(self, tables={}, infos=JsonStructure()):
        for name, model in tables.iteritems():
            info = infos.to_dict().get(name)
            self._save(model, info)

    def _save(self, model, rows={}):
        if type(rows) == dict:
            m = model()
            for field, value in rows.iteritems():
                setattr(m, field, value)
            m.save()
        else:
            for row in rows:
                m = model()
                for field, value in row.iteritems():
                    setattr(m, field, value)
                m.save()
