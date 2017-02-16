# -*- coding: utf-8 -*-

from django.db import models


class Report(models.Model):
    """报告基本信息
    """

    REPORTID = models.CharField(max_length=128, null=True, blank=True)
    REQUESTTIME = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    INFORMANTNAME = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATETYPE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)
    QUERYOPR = models.CharField(max_length=128, null=True, blank=True)
    QUERYCODE = models.CharField(max_length=128, null=True, blank=True)


class Person(models.Model):
    """身份信息
    """

    REPORTID = models.CharField(max_length=128, null=True, blank=True)
    GENDER = models.CharField(max_length=128, null=True, blank=True)
    GENDERORGPRO = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)
    BIRTHDAY = models.CharField(max_length=128, null=True, blank=True)
    BIRTHORGPRO = models.CharField(max_length=128, null=True, blank=True)
    MARRIDGE = models.CharField(max_length=128, null=True, blank=True)
    MARRIDGEORGPRO = models.CharField(max_length=128, null=True, blank=True)
    MOBILEPHONE = models.CharField(max_length=128, null=True, blank=True)
    MOBILORGPRO = models.CharField(max_length=128, null=True, blank=True)
    WORKPHONE = models.CharField(max_length=128, null=True, blank=True)
    WORKORGPRO = models.CharField(max_length=128, null=True, blank=True)
    HOMEPHONE = models.CharField(max_length=128, null=True, blank=True)
    HOMEORGPRO = models.CharField(max_length=128, null=True, blank=True)
    EDUCATION = models.CharField(max_length=128, null=True, blank=True)
    EDUORGPRO = models.CharField(max_length=128, null=True, blank=True)
    DEGREE = models.CharField(max_length=128, null=True, blank=True)
    DEGREEORGPRO = models.CharField(max_length=128, null=True, blank=True)
    CONTACTADDRESS = models.CharField(max_length=128, null=True, blank=True)
    CONTACTORGPRO = models.CharField(max_length=128, null=True, blank=True)
    HOUSEHOLD = models.CharField(max_length=128, null=True, blank=True)
    HOUSEORGPRO = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)


class Couple(models.Model):
    """配偶信息
    """

    REPORTID = models.CharField(max_length=128, null=True, blank=True)
    COUPLENAME = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)
    COUPLECERTYPE = models.CharField(max_length=128, null=True, blank=True)
    COUPLECERCODE = models.CharField(max_length=128, null=True, blank=True)
    COUPLECOMPANY = models.CharField(max_length=128, null=True, blank=True)
    COUPLEPHONE = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    ORGINFOPRO = models.CharField(max_length=128, null=True, blank=True)


class Address(models.Model):
    """居住信息
    """

    REPORTID = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)
    ADDRESS = models.CharField(max_length=128, null=True, blank=True)
    LIVINGSTATUS = models.CharField(max_length=128, null=True, blank=True)
    LIVEINFOUPDATEDATE = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    ORGINFOPRO = models.CharField(max_length=128, null=True, blank=True)


class Profession(models.Model):
    """职业信息
    """

    REPORTID = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)
    COMPANY = models.CharField(max_length=128, null=True, blank=True)
    COMPANYADDRESS = models.CharField(max_length=128, null=True, blank=True)
    OCCUPATION = models.CharField(max_length=128, null=True, blank=True)
    INDUSTRY = models.CharField(max_length=128, null=True, blank=True)
    JOB = models.CharField(max_length=128, null=True, blank=True)
    TITLE = models.CharField(max_length=128, null=True, blank=True)
    WORKSTARTDATE = models.CharField(max_length=128, null=True, blank=True)
    OCCUPATIONUPDATEDATE = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    ORGINFOPRO = models.CharField(max_length=128, null=True, blank=True)


class Verification(models.Model):
    """公安部居民身份证核查信息
    """

    REPORTID = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)
    CHECKRESULT = models.CharField(max_length=128, null=True, blank=True)
    GRANTORG = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)


class CreditTips(models.Model):
    """信用提示
    """

    REPORTID = models.CharField(max_length=128, null=True, blank=True)
    HOUSELOANNUM = models.CharField(max_length=128, null=True, blank=True)
    BUSINESSBUILDINGLOANNUM = models.CharField(max_length=128, null=True, blank=True)
    OTHERLOANNUM = models.CharField(max_length=128, null=True, blank=True)
    FIRSTLOANMONTHOPEN = models.CharField(max_length=128, null=True, blank=True)
    LOANCARDNUM = models.CharField(max_length=128, null=True, blank=True)
    FIRSTLOANCARDMONTHOPEN = models.CharField(max_length=128, null=True, blank=True)
    CREDITCARDNUM = models.CharField(max_length=128, null=True, blank=True)
    FIRSTCREDITCARDMONTHOPEN = models.CharField(max_length=128, null=True, blank=True)
    STATEMENTNUM = models.CharField(max_length=128, null=True, blank=True)
    OBJECTIONNUM = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)


class WithInTimeLimit(models.Model):
    """逾期及违约信息概要
    """

    REPORTID = models.CharField(max_length=128, null=True, blank=True)
    BADLOANNUM = models.CharField(max_length=128, null=True, blank=True)
    BADLOANAMOUNT = models.CharField(max_length=128, null=True, blank=True)
    ASSETDISPOSALNUM = models.CharField(max_length=128, null=True, blank=True)
    ASSETDISPOSALAMOUNT = models.CharField(max_length=128, null=True, blank=True)
    GUARANTEECOMPENSATIONNUM = models.CharField(max_length=128, null=True, blank=True)
    GUARANTEECOMPENSATIONAMOUNT = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)


class OverdraftOverdue(models.Model):
    """逾期透支信息汇总
    """

    REPORTID = models.CharField(max_length=128, null=True, blank=True)
    LOANPASTDUENUM = models.CharField(max_length=128, null=True, blank=True)
    LOANPASTDUEMONTH = models.CharField(max_length=128, null=True, blank=True)
    LOANMAXPASTDUEAMOUNT = models.CharField(max_length=128, null=True, blank=True)
    LOANLONGESTPASTDUEMONTHS = models.CharField(max_length=128, null=True, blank=True)
    LOANCARDPASTDUENUM = models.CharField(max_length=128, null=True, blank=True)
    LOANCARDPASTDUEMONTH = models.CharField(max_length=128, null=True, blank=True)
    LOANCARDMAXPASTDUEAMOUNT = models.CharField(max_length=128, null=True, blank=True)
    LOANCARDLONGESTPASTDUEMONTHS = models.CharField(max_length=128, null=True, blank=True)
    CREDITCARDPASTDUENUM = models.CharField(max_length=128, null=True, blank=True)
    CREDITCARDPASTDUEMONTH = models.CharField(max_length=128, null=True, blank=True)
    CREDITCARDMAXPASTDUEAMOUNT = models.CharField(max_length=128, null=True, blank=True)
    CREDITCARDLONGESTPASTDUEMONTHS = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)


class OutstandingLoans(models.Model):
    """未结清贷款信息汇总
    """

    REPORTID = models.CharField(max_length=128, null=True, blank=True)
    INPAYLOANLEGALORG = models.CharField(max_length=128, null=True, blank=True)
    INPAYLOANORG = models.CharField(max_length=128, null=True, blank=True)
    INPAYLOANNUM = models.CharField(max_length=128, null=True, blank=True)
    INPAYLOANTOTALCREDITLIMIT = models.CharField(max_length=128, null=True, blank=True)
    INPAYLOANTOTALBALANCE = models.CharField(max_length=128, null=True, blank=True)
    INPAYLOANRECENT6AVGPAYAMOUNT = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)


class NoPinDebitCards(models.Model):
    """未销户贷记卡信息汇总
    """

    REPORTID = models.CharField(max_length=128, null=True, blank=True)
    INPAYLOANCARDLEGALORG = models.CharField(max_length=128, null=True, blank=True)
    INPAYLOANCARDORGNUM = models.CharField(max_length=128, null=True, blank=True)
    INPAYLOANCARDNUM = models.CharField(max_length=128, null=True, blank=True)
    INPAYLOANCARDTOTALCREDITLIMIT = models.CharField(max_length=128, null=True, blank=True)
    INPAYLOANCARDMAXCREDITLIMIT = models.CharField(max_length=128, null=True, blank=True)
    INPAYLOANCARDMINCREDITLIMIT = models.CharField(max_length=128, null=True, blank=True)
    INPAYLOANCARDBALANCE = models.CharField(max_length=128, null=True, blank=True)
    INPAYLOANCARDRECENT6AVGDEBT = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)


class NoPinAccurateBorrowWriteDownCard(models.Model):
    """未销户准贷记卡信息汇总
    """

    REPORTID = models.CharField(max_length=128, null=True, blank=True)
    INPAYCREDITCARDLEGALINSTITUTES = models.CharField(max_length=128, null=True, blank=True)
    INPAYCREDITCARDINSTITUTES = models.CharField(max_length=128, null=True, blank=True)
    INPAYCREDITCARDNUM = models.CharField(max_length=128, null=True, blank=True)
    INPAYCREDITCARDTOTALCREDITLIMIT = models.CharField(max_length=128, null=True, blank=True)
    INPAYCREDITCARDMAXCREDITLIMIT = models.CharField(max_length=128, null=True, blank=True)
    INPAYCREDITCARDMINCREDITLIMIT = models.CharField(max_length=128, null=True, blank=True)
    INPAYCREDITCARDBALANCE = models.CharField(max_length=128, null=True, blank=True)
    INPAYCREDITCARDRECENT6AVGDEBT = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)


class Guaranty(models.Model):
    """对外担保信息汇总
    """

    REPORTID = models.CharField(max_length=128, null=True, blank=True)
    GUARANTEENUM = models.CharField(max_length=128, null=True, blank=True)
    GUARANTEEAMOUNT = models.CharField(max_length=128, null=True, blank=True)
    GUARANTEEBALANCE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)


class AssetDisposalInfo(models.Model):
    """资产处置信息
    """

    BUSINESSTYPE = models.CharField(max_length=128, null=True, blank=True)
    FINANCENAME = models.CharField(max_length=128, null=True, blank=True)
    DEBTRECEIVEDATE = models.CharField(max_length=128, null=True, blank=True)
    PRINCIPAL = models.CharField(max_length=128, null=True, blank=True)
    LATESTDATE = models.CharField(max_length=128, null=True, blank=True)
    BALANCE = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)


class GuarantorCompensationInfo(models.Model):
    """ 保证人代偿信息
    """

    BUSINESSTYPE = models.CharField(max_length=128, null=True, blank=True)
    ORGNAME = models.CharField(max_length=128, null=True, blank=True)
    LATESTDATE = models.CharField(max_length=128, null=True, blank=True)
    TOTAL_REPAY = models.CharField(max_length=128, null=True, blank=True)
    LASTRECOVERYDATE = models.CharField(max_length=128, null=True, blank=True)
    REPAY_BALANCE = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)


class Loan(models.Model):
    """ 贷款
    """

    DATEOPENED = models.CharField(max_length=128, null=True, blank=True)
    FINANCENAME = models.CharField(max_length=128, null=True, blank=True)
    FINANCETYPE = models.CharField(max_length=128, null=True, blank=True)
    CREDITLIMIT = models.CharField(max_length=128, null=True, blank=True)
    CURRENCYNAME = models.CharField(max_length=128, null=True, blank=True)
    CURRENCY = models.CharField(max_length=128, null=True, blank=True)
    TYPENAME = models.CharField(max_length=128, null=True, blank=True)
    LOANTYPE = models.CharField(max_length=128, null=True, blank=True)
    GUARANTEEWAY = models.CharField(max_length=128, null=True, blank=True)
    GUARANTEEWAYNAME = models.CharField(max_length=128, null=True, blank=True)
    MONTHDURATION = models.CharField(max_length=128, null=True, blank=True)
    TERMSFREQNAME = models.CharField(max_length=128, null=True, blank=True)
    TERMSFREQ = models.CharField(max_length=128, null=True, blank=True)
    DATECLOSED = models.CharField(max_length=128, null=True, blank=True)
    STATENDDATE = models.CharField(max_length=128, null=True, blank=True)
    CLASS5STATNAME = models.CharField(max_length=128, null=True, blank=True)
    CLASS5STAT = models.CharField(max_length=128, null=True, blank=True)
    BALANCE = models.CharField(max_length=128, null=True, blank=True)
    MONTHUNPAID = models.CharField(max_length=128, null=True, blank=True)
    BILLINGDATE = models.CharField(max_length=128, null=True, blank=True)
    SCHEDULEDAMOUNT = models.CharField(max_length=128, null=True, blank=True)
    ACTUALPAYAMOUNT = models.CharField(max_length=128, null=True, blank=True)
    RECENTPAYDATE = models.CharField(max_length=128, null=True, blank=True)
    CURTERMSPASTDUE = models.CharField(max_length=128, null=True, blank=True)
    CURAMOUNTPASTDUE = models.CharField(max_length=128, null=True, blank=True)
    AMOUNTPASTDUE30 = models.CharField(max_length=128, null=True, blank=True)
    AMOUNTPASTDUE60 = models.CharField(max_length=128, null=True, blank=True)
    AMOUNTPASTDUE90 = models.CharField(max_length=128, null=True, blank=True)
    AMOUNTPASTDUE180 = models.CharField(max_length=128, null=True, blank=True)
    PAYSTAT24MONTH = models.CharField(max_length=128, null=True, blank=True)
    STAT_FLAG = models.CharField(max_length=128, null=True, blank=True)
    DETAIL = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)


class DebitCard(models.Model):
    """ 贷记卡
    """

    DATEOPENED = models.CharField(max_length=128, null=True, blank=True)
    DATECLOSED = models.CharField(max_length=128, null=True, blank=True, default="2099-12-31")
    FINANCENAME = models.CharField(max_length=128, null=True, blank=True)
    FINANCETYPE = models.CharField(max_length=128, null=True, blank=True)
    CURRENCYNAME = models.CharField(max_length=128, null=True, blank=True)
    CURRENCY = models.CharField(max_length=128, null=True, blank=True)
    CREDITLIMIT = models.CharField(max_length=128, null=True, blank=True)
    SHAREAMOUNT = models.CharField(max_length=128, null=True, blank=True)
    GUARANTEEWAY = models.CharField(max_length=128, null=True, blank=True)
    GUARANTEEWAYNAME = models.CharField(max_length=128, null=True, blank=True)
    STATENDDATE = models.CharField(max_length=128, null=True, blank=True)
    CLASS5STAT = models.CharField(max_length=128, null=True, blank=True)
    BALANCE = models.CharField(max_length=128, null=True, blank=True)
    AVG6AMOUNT = models.CharField(max_length=128, null=True, blank=True)
    MAXDEBT = models.CharField(max_length=128, null=True, blank=True)
    SCHEDULEDAMOUNT = models.CharField(max_length=128, null=True, blank=True)
    ACCOUNTDATE = models.CharField(max_length=128, null=True, blank=True)
    ACTUALPAYAMOUNT = models.CharField(max_length=128, null=True, blank=True)
    RECENTPAYDATE = models.CharField(max_length=128, null=True, blank=True)
    CURTERMSPASTDUE = models.CharField(max_length=128, null=True, blank=True)
    CURAMOUNTPASTDUE = models.CharField(max_length=128, null=True, blank=True)
    PAYSTAT24MONTH = models.CharField(max_length=128, null=True, blank=True)
    STAT_FLAG = models.CharField(max_length=128, null=True, blank=True)
    DETAIL = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)


class SemiCreditCard(models.Model):
    """ 准贷记卡
    """

    DATEOPENED = models.CharField(max_length=128, null=True, blank=True)
    DATECLOSED = models.CharField(max_length=128, null=True, blank=True, default="2099-12-31")
    FINANCENAME = models.CharField(max_length=128, null=True, blank=True)
    FINANCETYPE = models.CharField(max_length=128, null=True, blank=True)
    CURRENCYNAME = models.CharField(max_length=128, null=True, blank=True)
    CURRENCY = models.CharField(max_length=128, null=True, blank=True)
    CREDITLIMIT = models.CharField(max_length=128, null=True, blank=True)
    SHAREAMOUNT = models.CharField(max_length=128, null=True, blank=True)
    GUARANTEEWAY = models.CharField(max_length=128, null=True, blank=True)
    GUARANTEEWAYNAME = models.CharField(max_length=128, null=True, blank=True)
    STATENDDATE = models.CharField(max_length=128, null=True, blank=True)
    CLASS5STAT = models.CharField(max_length=128, null=True, blank=True)
    BALANCE = models.CharField(max_length=128, null=True, blank=True)
    AVG6AMOUNT = models.CharField(max_length=128, null=True, blank=True)
    MAXDEBT = models.CharField(max_length=128, null=True, blank=True)
    ACCOUNTDATE = models.CharField(max_length=128, null=True, blank=True)
    ACTUALPAYAMOUNT = models.CharField(max_length=128, null=True, blank=True)
    RECENTPAYDATE = models.CharField(max_length=128, null=True, blank=True)
    UNPAID180 = models.CharField(max_length=128, null=True, blank=True)
    PAYSTAT24MONTH = models.CharField(max_length=128, null=True, blank=True)
    DETAIL = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)
    STAT_FLAG = models.CharField(max_length=128, null=True, blank=True)


class SpecialTransaction(models.Model):
    """ 特殊交易
    """

    SPECIALTYPE = models.CharField(max_length=128, null=True, blank=True)
    SPECIALDATE = models.CharField(max_length=128, null=True, blank=True)
    SPECIALMONTH = models.CharField(max_length=128, null=True, blank=True)
    SPECIALMONEY = models.CharField(max_length=128, null=True, blank=True)
    SPECIALDETAIL = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)


class FiveyearPastdue(models.Model):
    """ 五年内逾期记录
    """
    DATEPASTDUE = models.CharField(max_length=128, null=True, blank=True)
    MONTHPASTDUE = models.CharField(max_length=128, null=True, blank=True)
    AMOUNTPASTDUE = models.CharField(max_length=128, null=True, blank=True)
    PASTDUELOANTYPE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)


class TaxesOwed(models.Model):
    """ 欠税记录
    """

    CHARGETAXBUREAU = models.CharField(max_length=128, null=True, blank=True)
    TOTALTAXES = models.CharField(max_length=128, null=True, blank=True)
    TAXESSTATDATE = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)


class CivilJudgmentRecords(models.Model):
    """ 民事判决记录
    """

    FILINGCOURT = models.CharField(max_length=128, null=True, blank=True)
    REASON = models.CharField(max_length=128, null=True, blank=True)
    FILINGDATE = models.CharField(max_length=128, null=True, blank=True)
    ENDTYPE = models.CharField(max_length=128, null=True, blank=True)
    JUDGEMENT = models.CharField(max_length=128, null=True, blank=True)
    EFFECTIVEDATE = models.CharField(max_length=128, null=True, blank=True)
    ACTIONOBJECT = models.CharField(max_length=128, null=True, blank=True)
    ACTIONOBJECTMONEY = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)


class EnforceRecords(models.Model):
    """ 强制执行记录
    """

    EXECCOURT = models.CharField(max_length=128, null=True, blank=True)
    EXECREASON = models.CharField(max_length=128, null=True, blank=True)
    FILINGDATE = models.CharField(max_length=128, null=True, blank=True)
    ENDTYPE = models.CharField(max_length=128, null=True, blank=True)
    CASESTATUS = models.CharField(max_length=128, null=True, blank=True)
    ENDDATE = models.CharField(max_length=128, null=True, blank=True)
    APPACIIONOBJECT = models.CharField(max_length=128, null=True, blank=True)
    APPACTIONOBJECTVALUE = models.CharField(max_length=128, null=True, blank=True)
    EXECACTIONOBJECT = models.CharField(max_length=128, null=True, blank=True)
    EXECACTIONOBJECTVALUE = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)


class AdministrativePunishmentRecord(models.Model):
    """ 行政处罚记录
    """

    PUNISHMENTORG = models.CharField(max_length=128, null=True, blank=True)
    PUNISHMENTCON = models.CharField(max_length=128, null=True, blank=True)
    PUNISHMENTMONEY = models.CharField(max_length=128, null=True, blank=True)
    EFFECTIVEDATE = models.CharField(max_length=128, null=True, blank=True)
    ENDDATE = models.CharField(max_length=128, null=True, blank=True)
    ADMINISTRATIVEREVIEW = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)


class HousingProvidentFundPaymentRecord(models.Model):
    """ 住房公积金参缴记录
    """

    PAYPLACE = models.CharField(max_length=128, null=True, blank=True)
    PAYDATE = models.CharField(max_length=128, null=True, blank=True)
    FIRSTPAYDATE = models.CharField(max_length=128, null=True, blank=True)
    PAYENDDATE = models.CharField(max_length=128, null=True, blank=True)
    PAYSTATUS = models.CharField(max_length=128, null=True, blank=True)
    MONTHPAYMENT = models.CharField(max_length=128, null=True, blank=True)
    PERSONPAYRATIO = models.CharField(max_length=128, null=True, blank=True)
    COMPANYPAYRATIO = models.CharField(max_length=128, null=True, blank=True)
    COMPANYNAME = models.CharField(max_length=128, null=True, blank=True)
    INFOUPDATEDATE = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)


class PensionDepositRecord(models.Model):
    """ 养老保险金缴存记录
    """

    INSUREDPLACE = models.CharField(max_length=128, null=True, blank=True)
    INSUREDDATE = models.CharField(max_length=128, null=True, blank=True)
    INSUREDMONTHS = models.CharField(max_length=128, null=True, blank=True)
    WORKDATE = models.CharField(max_length=128, null=True, blank=True)
    INSUREDSTATUS = models.CharField(max_length=128, null=True, blank=True)
    PERSONPAYBASE = models.CharField(max_length=128, null=True, blank=True)
    MONTHPAYMENT = models.CharField(max_length=128, null=True, blank=True)
    INFOUPDATEDATE = models.CharField(max_length=128, null=True, blank=True)
    INSUREDCOMPANY = models.CharField(max_length=128, null=True, blank=True)
    ABORTREASON = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)


class PensionInsurancePaymentRecords(models.Model):
    """ 养老保险金发放记录
    """

    GRANTPLACE = models.CharField(max_length=128, null=True, blank=True)
    RETIRETYPE = models.CharField(max_length=128, null=True, blank=True)
    RETIREDATE = models.CharField(max_length=128, null=True, blank=True)
    WORKDATE = models.CharField(max_length=128, null=True, blank=True)
    GRANTMONEY = models.CharField(max_length=128, null=True, blank=True)
    ABORTREASON = models.CharField(max_length=128, null=True, blank=True)
    COMPANYNAME = models.CharField(max_length=128, null=True, blank=True)
    INFOUPDATEDATE = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)


class SubsistenceAllowances(models.Model):
    """ 低保救助记录
    """

    PERSONTYPE = models.CharField(max_length=128, null=True, blank=True)
    LOCATION = models.CharField(max_length=128, null=True, blank=True)
    COMPANY = models.CharField(max_length=128, null=True, blank=True)
    FAMILYINCOME = models.CharField(max_length=128, null=True, blank=True)
    APPLYDATE = models.CharField(max_length=128, null=True, blank=True)
    APPROVALDATE = models.CharField(max_length=128, null=True, blank=True)
    INFOUPDATEDATE = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)


class PracticeQualificationRecord(models.Model):
    """ 执业资格记录
    """

    REGISTNAME = models.CharField(max_length=128, null=True, blank=True)
    LEVEL = models.CharField(max_length=128, null=True, blank=True)
    GRANTDATE = models.CharField(max_length=128, null=True, blank=True)
    INVALIDDATE = models.CharField(max_length=128, null=True, blank=True)
    REVOKEDATE = models.CharField(max_length=128, null=True, blank=True)
    GRANTORG = models.CharField(max_length=128, null=True, blank=True)
    ORGPLACE = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)


class AdministrativeRewardRecord(models.Model):
    """ 行政奖励记录
    """

    REWARDORG = models.CharField(max_length=128, null=True, blank=True)
    REWARDCONTENT = models.CharField(max_length=128, null=True, blank=True)
    EFFECTIVEDATE = models.CharField(max_length=128, null=True, blank=True)
    ENDDATE = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)


class VehicleTransactionAndMortgageRecords(models.Model):
    """ 车辆交易和抵押记录
    """

    CARNUMBER = models.CharField(max_length=128, null=True, blank=True)
    ENGINENUMBER = models.CharField(max_length=128, null=True, blank=True)
    BRAND = models.CharField(max_length=128, null=True, blank=True)
    CARTYPE = models.CharField(max_length=128, null=True, blank=True)
    USAGEPROPERTY = models.CharField(max_length=128, null=True, blank=True)
    CARSTATUS = models.CharField(max_length=128, null=True, blank=True)
    MORTGAGEFLAG = models.CharField(max_length=128, null=True, blank=True)
    INFOUPDATEDATE = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)


class TelecomPaymentRecords(models.Model):
    """ 电信缴费记录
    """

    TELECOMOPER = models.CharField(max_length=128, null=True, blank=True)
    BUSINESSTYPE = models.CharField(max_length=128, null=True, blank=True)
    DATEOPENED = models.CharField(max_length=128, null=True, blank=True)
    PAYMENTSTATUS = models.CharField(max_length=128, null=True, blank=True)
    CURMONEYPASTDUE = models.CharField(max_length=128, null=True, blank=True)
    CURMONTHPASTDUE = models.CharField(max_length=128, null=True, blank=True)
    ACCOUNTDATE = models.CharField(max_length=128, null=True, blank=True)
    PAYSTAT24MONTH = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)


class Declare(models.Model):
    """ 本人声明
    """

    STATEMENT = models.CharField(max_length=128, null=True, blank=True)
    ADDINGDATE = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)


class ObjectionAnnotation(models.Model):
    """异议标注
    """

    MARKCONTENT = models.CharField(max_length=128, null=True, blank=True)
    ADDINGDATE = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)


class QueryRecordSummary(models.Model):
    """ 查询记录汇总
    """

    LOANAPPROVAL_ORG = models.CharField(max_length=128, null=True, blank=True)
    CREDITAPPROVAL_ORG = models.CharField(max_length=128, null=True, blank=True)
    LOANAPPROVAL_QUERY = models.CharField(max_length=128, null=True, blank=True)
    CREDITAPPROVAL_QUERY = models.CharField(max_length=128, null=True, blank=True)
    PERSONAL_QUERY = models.CharField(max_length=128, null=True, blank=True)
    LOANMANAGE = models.CharField(max_length=128, null=True, blank=True)
    GUARANTEEREVIEW = models.CharField(max_length=128, null=True, blank=True)
    MERCNAMEREVIEW = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)


class CreditApprovalQueryRecordDetail(models.Model):
    """ 信贷审批查询记录明细
    """

    QUERYDATE = models.CharField(max_length=128, null=True, blank=True)
    OPER = models.CharField(max_length=128, null=True, blank=True)
    QUERYREASONCODE = models.CharField(max_length=128, null=True, blank=True)
    QUERYREASONNAME = models.CharField(max_length=128, null=True, blank=True)
    REPORTDATE = models.CharField(max_length=128, null=True, blank=True)
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)


class QueryHistory(models.Model):
    """普林报告分历史查询记录
    """

    USERID = models.IntegerField()
    CERTIFICATECODE = models.CharField(max_length=128, null=True, blank=True)
    NAME = models.CharField(max_length=128, null=True, blank=True)
    SCORE = models.FloatField(null=True)
    SCOREDETAIL = models.TextField(null=True)
    CREDITAUDIT = models.CharField(max_length=128, null=True, blank=True, default="")
    PAYMENT = models.CharField(max_length=128, null=True, blank=True, default="")
    TIMESTAMP = models.DateTimeField(auto_now_add=True)
