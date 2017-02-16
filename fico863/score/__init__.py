# -*- coding: utf-8 -*-

import logging
from django_pandas.io import read_frame
from model.main import calc_score
from ..models import Loan, DebitCard, SemiCreditCard, SpecialTransaction, CreditApprovalQueryRecordDetail


def score(loantype):
    loans_df = _df("loan")
    loancards_df = _df("loancard")
    creditcards_df = _df("creditcard")
    querys_df = _df("query")
    specials_df = _df("special")
    report = calc_score(loantype, loans_df, loancards_df, creditcards_df,
                        querys_df, specials_df)
    return _parse_model_report(report)


def _df(table_name):
    table_names_to_models = {"loan": Loan,
                             "loancard": DebitCard,
                             "creditcard": SemiCreditCard,
                             "query": CreditApprovalQueryRecordDetail,
                             "special": SpecialTransaction}

    fieldnames = {
        "loan":
        ["CERTIFICATECODE", "FINANCENAME", "CREDITLIMIT", "DATEOPENED",
         "DATECLOSED", "LOANTYPE", "TYPENAME", "MONTHDURATION", "CURRENCY",
         "CURRENCYNAME", "TERMSFREQ", "TERMSFREQNAME", "GUARANTEEWAY",
         "GUARANTEEWAYNAME", "SCHEDULEDAMOUNT", "ACTUALPAYAMOUNT", "BALANCE",
         "RECENTPAYDATE", "CLASS5STAT", "CLASS5STATNAME", "BILLINGDATE",
         "STATENDDATE", "MONTHUNPAID", "CURTERMSPASTDUE", "CURAMOUNTPASTDUE",
         "AMOUNTPASTDUE30", "AMOUNTPASTDUE60", "AMOUNTPASTDUE90",
         "AMOUNTPASTDUE180", "STAT_FLAG", "PAYSTAT24MONTH", "REPORTDATE"],
        "loancard":
        ["CERTIFICATECODE", "FINANCENAME", "CREDITLIMIT", "MAXDEBT",
         "DATEOPENED", "DATECLOSED", "CURRENCY", "CURRENCYNAME",
         "GUARANTEEWAY", "GUARANTEEWAYNAME", "SCHEDULEDAMOUNT",
         "ACTUALPAYAMOUNT", "BALANCE", "RECENTPAYDATE", "ACCOUNTDATE",
         "STATENDDATE", "CURTERMSPASTDUE", "CURAMOUNTPASTDUE", "STAT_FLAG",
         "AVG6AMOUNT", "PAYSTAT24MONTH", "REPORTDATE"],
        "creditcard":
        ["CERTIFICATECODE", "FINANCENAME", "CURRENCY", "CURRENCYNAME",
         "GUARANTEEWAY", "GUARANTEEWAYNAME", "CREDITLIMIT", "MAXDEBT",
         "RECENTPAYDATE", "ACTUALPAYAMOUNT", "STATENDDATE", "ACCOUNTDATE",
         "BALANCE", "SHAREAMOUNT", "PAYSTAT24MONTH", "STAT_FLAG", "DATEOPENED",
         "DATECLOSED", "AVG6AMOUNT", "UNPAID180", "REPORTDATE"],
        "query": ["CERTIFICATECODE", "QUERYDATE", "OPER", "QUERYREASONCODE",
                  "QUERYREASONNAME", "REPORTDATE"],
        "special": ["CERTIFICATECODE", "SPECIALDATE", "SPECIALDATE",
                    "SPECIALMONTH", "SPECIALTYPE", "SPECIALMONEY",
                    "SPECIALDETAIL", "REPORTDATE"]
    }

    model = table_names_to_models[table_name]
    qs = model.objects.all()
    df = read_frame(qs, fieldnames=fieldnames[table_name])
    return df


def _parse_model_report(data):
    return ReportParse().parse_report(data)


class ReportParse(object):
    """
    {'creditlimit'   : 349316,
     'dimen_interp'  : [('creditLimit', 'median'),('recentBehavior', 'excellent'),('creditLength', 'bad'),('accountNo', 'good'),('creditHistory', 'good')],
     'fea_imp_first' : ('type81longestlength',2.2181514208548614,-0.303,-7.3206317519962427),
     'fea_imp_sec'   : ('type81ncount',-1.5101950770772876,-0.2368,6.3775129944142215),
     'fea_imp_third' : ('loanmonth24ncount',-0.86639706574008468,-0.2003,4.3254970830758097),
     'pro'           : array([ 0.9449426,  0.0550574]),
     'rank'          : '11.5284219621%',
     'ratio'         : 0.02511,
     'score'         : 31.744034409434974}
    """

    front_report = {}

    def parse_report(self, report):
        for key, val in report.iteritems():
            parser = self._get_parser(key)
            try:
                parser(key, val)
            except:
                logging.error("The score model return wrong values.")
        return self.front_report

    def _get_parser(self, key):
        return {"creditlimit": self._parse_general,
                "dimen_interp": self._parse_dimen_interp,
                "fea_imp_first": self._parse_imp,
                "fea_imp_sec": self._parse_imp,
                "fea_imp_third": self._parse_imp,
                "pro": self._parse_pro,
                "rank": self._parse_rank,
                "ratio": self._parse_general,
                "score": self._parse_score}.get(key)

    def _parse_general(self, key, val):
        self.front_report[key] = val

    def _parse_dimen_interp(self, key, val):
        pct = {"excellent": "100%",
               "good": "75%",
               "median": "50%",
               "bad": "25%"}
        front_keys = {"creditLimit": "creditlimit_pct",
                      "recentBehavior": "recentbehavior_pct",
                      "creditLength": "creditlength_pct",
                      "accountNo": "accountno_pct",
                      "creditHistory": "credithistory_pct"}
        for k, v in val:
            self.front_report[front_keys[k]] = pct[v]

    def _parse_imp(self, key, val):
        zhs = {
            "loanmonth24laststatnumno": "24月状态数字的个数",
            "loanmonth24curtermpastdue": "贷款当前逾期期数",
            "loanmonth24ncount": "24月状态N的个数",
            "loanmonth24statcno": "24月状态C的个数",
            "loanmonth24stat123no": "24月状态123的个数",
            "loanmonth24stat7no": "24月状态7的个数",
            "loanmonth24nratio": "24月正常还款的比例",
            "loanno": "贷款的个数",
            "loanavglength": "贷款平均使用年限",
            "loanlongestlength": "贷款最长使用年限",
            "recentloantime": "最近开户的贷款距现在的时间",
            "recent3loanno": "最近3个月新开贷款个数",
            "recent3loantotallimit": "最近3个月新开贷款授信总额度",
            "recent6loanno": "最近6个月新开贷款数",
            "recent6loantotallimit": "最近6个月新开贷款授信额度总和",
            "recent6type11loanno": "最近6个月新开个人住房贷款数",
            "recent6type12loanno": "最近6个月新开商品房贷款数",
            "recent6type13loanno": "最近6个月新开个人住房公积金贷款数",
            "recent6type21loanno": "最近6个月新开汽车贷款数",
            "recent6type31loanno": "最近6个月新开个人助学贷款数",
            "recent6type41loanno": "最近6个月新开个人经营性贷款数",
            "recent6type51loanno": "最近6个月新开农户贷款数",
            "recent6type99loanno": "最近6个月新开其他贷款数",
            "recent9loanno": "最近9个月新开贷款个数",
            "recent9loantotallimit": "最近9个月新开贷款授信总额度",
            "loaninuseguaranteeway4no": "正在使用担保方式为4的个数",
            "loaninuseavgterm": "正在使用的贷款平均授信时长",
            "loan_balance_num": "有欠款的账户数量",
            "type81month24curtermpastdue": "贷记卡当前逾期期数",
            "type81month24nratio": "24月正常还款的比例",
            "type81month24stat23no": "贷记卡24月状态为23的个数",
            "type81guaranteeway4no": "贷记卡担保方式为4的个数",
            "type81guaranteeway9no": "贷记卡担保方式为9的个数",
            "type81longestlength": "贷记卡最长使用年限",
            "recenttype81time": "最近开户的贷记卡距现在的时间",
            "recent3type81no": "最近3个月开户的贷记卡个数",
            "recent6type81no": "最近6个月开户的贷记卡个数",
            "recent9type81no": "最近9个月开户的贷记卡个数",
            "type81_balance_num": "有欠款的贷记卡数量",
            "guaranteeway2no": "担保方式为2的个数",
            "guaranteeway2ratio": "担保方式为2的个数与总贷款数的占比",
            "guaranteeway4no": "担保方式为4的个数",
            "guaranteeway4ratio": "担保方式为4的个数与总贷款数的占比",
            "inuseguaranteeway2no": "正在使用的担保方式为2的个数",
            "inuseguaranteeway2ratio": "正在使用的担保方式为2的个数与正在还款的贷款数的占比",
            "existype11": "有无房贷",
            "type21recentpayno": "近期有还款的车贷账户数量",
            "type1113recentpayno": "近期有还款的个人住房与公积金房贷账户数量",
            "type41recentpayno": "近期有还款的个人经营性贷款账户数量",
            "type99recentpayno": "近期有还款的其他贷款账户数量",
            "type41maxcreditlength": "个人经营性贷款最长信用年限",
            "51oneyearnratio": "农户贷款一年内正常还款占比",
            "cloannratio": "已结清账户正常还款比例",
            "cloanavglimit": "已结清贷款平均贷款额度",
            "otherloanavglength": "其他贷款平均信用年限",
            "loaninusefreq8no": "正在使用贷款还款频率为一次性的数量",
            "loaninusefreq7no": "正在使用贷款还款频率为不定期(其他)的数量",
            "type11nratio": "个人住房贷款24月还款状态正常(N)的占比",
            "inuseloancreditduration": "正在使用的贷款平均授信期",
            "type81maxcreditlength": "贷记卡最大信用年限",
            "type81avgcreditlength": "贷记卡平均信用年限",
            "type81stat24nratio": "贷记卡24月状态为N的占比",
            "type81ncount": "24月状态N的个数",
            "type81statallno": "24月状态数字的个数",
            "type81statcno": "24月状态C的个数",
            "type81stat123no": "24月状态123的个数",
            "type81stat7no": "24月状态7的个数",
            "type81cardno": "贷记卡个数",
            "type81mincreditlength": "最近一次贷记卡开卡距今的时间",
            "type81recentopenno": "最近6个月开户的贷记卡个数",
            "type71loanrecentpayno": "近期有还款的准贷记卡数量",
            "type71recentopenavgcreditlimit": "最近6个月开户的准贷记卡授信总额度",
            "type71curtermpastdue": "准贷记卡当前逾期期数",
            "type71recentopenno": "最近6个月开户的准贷记卡个数",
            "type71oneyear23no": "准贷记卡12月内23状态次数",
            "queryno": "历史查询次数"
        }
        zhs_key = val[0]
        self.front_report[key] = zhs[zhs_key]

    def _parse_pro(self, key, val):
        self.front_report[key] = val[1] * 100
        print self.front_report[key]

    def _parse_rank(self, key, val):
        self.front_report[key] = float(val[:-1])

    def _parse_score(self, key, val):
        self.front_report[key] = val
        if val <= 25:
            val_zh = "很差"
        elif val <= 50:
            val_zh = "中等"
        elif val <= 75:
            val_zh = "良好"
        else:
            val_zh = "优秀"
        self.front_report["score_zh"] = val_zh
