# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import datetime
import time


def convertime(dateStr):
    # if type(dateStr) == 'numpy.float64':
    # print dateStr
    # print dateStr
    return datetime.datetime.strptime(dateStr, '%Y-%m-%d')


def count24NumNo(statStr):
    if statStr == None:
        return 0
    n = 0
    n = statStr.count('1') + statStr.count('2') + statStr.count(
        '3') + statStr.count('4') + statStr.count('5') + statStr.count(
            '6') + statStr.count('7')
    return n


def count24NNo(statStr):
    if statStr == None:
        return 24
    n = 0
    n = statStr.count('N') + statStr.count('*') + statStr.count('C')
    return n


def countcard24NNo(statStr):
    if statStr == None:
        return 24
    return statStr.count('N') + statStr.count('C')


def count12NNo(statStr):
    if statStr == None:
        return 12
    n = 0
    n = statStr.count('N', 12) + statStr.count('*', 12) + statStr.count('C',
                                                                        12)
    return n


def count24CNo(statStr):
    if statStr == None:
        return 1
    n = 0
    n = statStr.count('C')
    return n


def count24123No(statStr):
    if statStr == None:
        return 0
    n = 0
    n = statStr.count('1') + statStr.count('2') + statStr.count('3')
    return n


def count2423No(statStr):
    if statStr == None:
        return 0
    n = 0
    n = statStr.count('2') + statStr.count('3')
    return n


def count247No(statStr):
    if statStr == None:
        return 0
    n = 0
    n = statStr.count('7')
    return n


def calcNRatio(statStr):
    if statStr == None:
        return 1.0
    n = statStr.count('N') + statStr.count('C') + statStr.count('*')
    num = 24 - statStr.count('/')
    print num
    return n / float(num + 1e-16)


def calcCardNRatio(statStr):
    if statStr == None:
        return 1.
    n = statStr.count('N') + statStr.count('C')
    num = 24 - statStr.count('/')
    return n / float(num + 1e-16)


def cardNRatio(statStr):
    if statStr == None:
        return 1.
    n = statStr.count('N') + statStr.count('c')
    num = 24 - statStr.count('/')
    return n / float(num + 1e-16)


def oneYearNRatio(statStr):
    if statStr == None:
        return 1.
    n = statStr.count('N', 12) + statStr.count('C', 12) + statStr.count('*',
                                                                        12)
    num = 12 - statStr.count('/', 12)
    return n / float(num + 1e-16)


def oneYear23No(statStr):
    if statStr == None:
        return 0
    n = statStr.count('2', 12) + statStr.count('3', 12)
    return n


def curTermPastDue(statStr):
    if statStr == None:
        return 0
    if statStr[-1] in '123456':
        return int(statStr[-1])
    elif statStr[-1] == '7':
        if statStr.count('7') == 24:
            return 30
        else:
            count = 0
            for i in range(23, -1, -1):
                if statStr[i] not in '1234567':
                    break
                else:
                    count += 1
            return count
    else:
        return 0


def calcX24MonthStast(data, X_data):
    if data.shape[0] == 0:
        X_data['loanmonth24laststatnumno'] = 0
        X_data['loanmonth24curtermpastdue'] = 0
        X_data['loanmonth24ncount'] = 0
        X_data['loanmonth24statcno'] = 0
        X_data['loanmonth24stat123no'] = 0
        X_data['loanmonth24stat7no'] = 0
        X_data['loanmonth24nratio'] = 0
        X_data['loanno'] = 0
        X_data['loanavglength'] = 0
        X_data['loanlongestlength'] = 0
        X_data['recentloantime'] = 0
    else:
        # 24月状态数字的个数
        data['24MonthNumNo'] = data['PAYSTAT24MONTH'].map(count24NumNo)
        loan24MonthNumNo = data[['CERTIFICATECODE', '24MonthNumNo']].groupby(
            'CERTIFICATECODE').sum()
        loan24MonthNumNo.columns = ['loanmonth24laststatnumno']
        X_data = pd.merge(X_data,
                          loan24MonthNumNo,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del data['24MonthNumNo'], loan24MonthNumNo
        # 贷款当前逾期期数
        # data['loanCurPastDue']=data['PAYSTAT24MONTH'].map(curTermPastDue)
        loanCurPastDue = data[['CERTIFICATECODE', 'CURTERMSPASTDUE']].groupby(
            'CERTIFICATECODE').sum()
        loanCurPastDue.columns = ['loanmonth24curtermpastdue']
        X_data = pd.merge(X_data,
                          loanCurPastDue,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        # del data['loanCurPastDue'],
        del loanCurPastDue
        # 24月状态N的个数
        data['24MonthNNo'] = data['PAYSTAT24MONTH'].map(count24NNo)
        loan24MonthNNo = data[['CERTIFICATECODE', '24MonthNNo']].groupby(
            'CERTIFICATECODE').sum()
        loan24MonthNNo.columns = ['loanmonth24ncount']
        X_data = pd.merge(X_data,
                          loan24MonthNNo,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del data['24MonthNNo'], loan24MonthNNo
        # 24月状态C的个数
        data['24MonthCNo'] = data['PAYSTAT24MONTH'].map(count24CNo)
        loan24MonthCNo = data[['CERTIFICATECODE', '24MonthCNo']].groupby(
            'CERTIFICATECODE').sum()
        loan24MonthCNo.columns = ['loanmonth24statcno']
        X_data = pd.merge(X_data,
                          loan24MonthCNo,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del data['24MonthCNo'], loan24MonthCNo
        # 24月状态123的个数
        data['24Month123No'] = data['PAYSTAT24MONTH'].map(count24123No)
        loan24Month123No = data[['CERTIFICATECODE', '24Month123No']].groupby(
            'CERTIFICATECODE').sum()
        loan24Month123No.columns = ['loanmonth24stat123no']
        X_data = pd.merge(X_data,
                          loan24Month123No,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del data['24Month123No'], loan24Month123No
        # 24月状态7的个数
        data['24Month7No'] = data['PAYSTAT24MONTH'].map(count247No)
        loan24Month7No = data[['CERTIFICATECODE', '24Month7No']].groupby(
            'CERTIFICATECODE').sum()
        loan24Month7No.columns = ['loanmonth24stat7no']
        X_data = pd.merge(X_data,
                          loan24Month7No,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del data['24Month7No'], loan24Month7No
        # 24月正常还款的比例
        data['24MonthNRatio'] = data['PAYSTAT24MONTH'].map(calcNRatio)
        loan24MonthNRatio = data[['CERTIFICATECODE', '24MonthNRatio']].groupby(
            'CERTIFICATECODE').mean()
        loan24MonthNRatio.columns = ['loanmonth24nratio']
        X_data = pd.merge(X_data,
                          loan24MonthNRatio,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del loan24MonthNRatio, data['24MonthNRatio']
        # 贷款的个数
        openAccountNo = data[['CERTIFICATECODE', 'REPORTDATE']].groupby(
            'CERTIFICATECODE').count()
        openAccountNo.columns = ['loanno']
        X_data = pd.merge(X_data,
                          openAccountNo,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del openAccountNo
        # 贷款平均使用年限
        data['yearPast'] = data['STATENDDATE'] - data['DATEOPENED']
        data['yearPast'] = data['yearPast'].astype('timedelta64[Y]')
        loanAvgCreditLength = data[['CERTIFICATECODE', 'yearPast']].groupby(
            'CERTIFICATECODE').mean()
        loanAvgCreditLength.columns = ['loanavglength']
        X_data = pd.merge(X_data,
                          loanAvgCreditLength,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del loanAvgCreditLength
        # 贷款最长使用年限
        loanMaxCreditLength = data[['CERTIFICATECODE', 'yearPast']].groupby(
            'CERTIFICATECODE').max()
        loanMaxCreditLength.columns = ['loanlongestlength']
        X_data = pd.merge(X_data,
                          loanMaxCreditLength,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del loanMaxCreditLength, data['yearPast']
        # 最近开户的贷款距现在的时间
        loanMinCreditLength = data[['CERTIFICATECODE', 'datedelta']].groupby(
            'CERTIFICATECODE').min()
        loanMinCreditLength.columns = ['recentloantime']
        X_data = pd.merge(X_data,
                          loanMinCreditLength,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del loanMinCreditLength

    return X_data


def calcXRecentOpenLoanNum(data, X_data):
    if data.shape[0] == 0:
        X_data['recent3loanno'] = 0
        X_data['recent3loantotallimit'] = 0
        X_data['recent6loanno'] = 0
        X_data['recent6loantotallimit'] = 0
        X_data['recent6type11loanno'] = 0
        X_data['recent6type12loanno'] = 0
        X_data['recent6type13loanno'] = 0
        X_data['recent6type21loanno'] = 0
        X_data['recent6type31loanno'] = 0
        X_data['recent6type41loanno'] = 0
        X_data['recent6type51loanno'] = 0
        X_data['recent6type99loanno'] = 0
        X_data['recent9loanno'] = 0
        X_data['recent9loantotallimit'] = 0
    else:
        recent3data = data[data['datedelta'] < 0.25]
        # 最近3个月新开贷款个数
        if recent3data.shape[0] == 0:
            X_data['recent3loanno'] = 0
        else:
            recent3OpenNo = recent3data[['CERTIFICATECODE', 'REPORTDATE'
                                         ]].groupby('CERTIFICATECODE').count()
            recent3OpenNo.columns = ['recent3loanno']
            X_data = pd.merge(X_data,
                              recent3OpenNo,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recent3OpenNo
        # 最近3个月新开贷款授信总额度
        if recent3data.shape[0] == 0:
            X_data['recent3loantotallimit'] = 0
        else:
            recent3OpenSum = recent3data[['CERTIFICATECODE', 'CREDITLIMIT'
                                          ]].groupby('CERTIFICATECODE').sum()
            recent3OpenSum.columns = ['recent3loantotallimit']
            X_data = pd.merge(X_data,
                              recent3OpenSum,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recent3OpenSum
        del recent3data
        recent6data = data[data['datedelta'] < 0.5]
        # 最近6个月新开贷款数
        if recent6data.shape[0] == 0:
            X_data['recent6loanno'] = 0
        else:
            recent6OpenNo = recent6data[['CERTIFICATECODE', 'REPORTDATE'
                                         ]].groupby('CERTIFICATECODE').count()
            recent6OpenNo.columns = ['recent6loanno']
            X_data = pd.merge(X_data,
                              recent6OpenNo,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recent6OpenNo
        # 最近6个月新开贷款授信额度总和
        if recent6data.shape[0] == 0:
            X_data['recent6loantotallimit'] = 0
        else:
            recent6OpenSum = recent6data[['CERTIFICATECODE', 'CREDITLIMIT'
                                          ]].groupby('CERTIFICATECODE').sum()
            recent6OpenSum.columns = ['recent6loantotallimit']
            X_data = pd.merge(X_data,
                              recent6OpenSum,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recent6OpenSum

        # 最近6个月新开个人住房贷款数
        recentOpen11 = recent6data[recent6data['LOANTYPE'] == 11]
        if recentOpen11.shape[0] == 0:
            X_data['recent6type11loanno'] = 0
        else:
            recentOpen11No = recentOpen11[['CERTIFICATECODE', 'REPORTDATE'
                                           ]].groupby('CERTIFICATECODE').count(
            )
            recentOpen11No.columns = ['recent6type11loanno']
            X_data = pd.merge(X_data,
                              recentOpen11No,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recentOpen11No
        del recentOpen11
        # 最近6个月新开商品房贷款数
        recentOpen12 = recent6data[recent6data['LOANTYPE'] == 12]
        if recentOpen12.shape[0] == 0:
            X_data['recent6type12loanno'] = 0
        else:
            recentOpen12No = recentOpen12[['CERTIFICATECODE', 'REPORTDATE'
                                           ]].groupby('CERTIFICATECODE').count(
            )
            recentOpen12No.columns = ['recent6type12loanno']
            X_data = pd.merge(X_data,
                              recentOpen12No,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recentOpen12No
        del recentOpen12
        # 最近6个月新开个人住房公积金贷款数
        recentOpen13 = recent6data[recent6data['LOANTYPE'] == 13]
        if recentOpen13.shape[0] == 0:
            X_data['recent6type13loanno'] = 0
        else:
            recentOpen13No = recentOpen13[['CERTIFICATECODE', 'REPORTDATE'
                                           ]].groupby('CERTIFICATECODE').count(
            )
            recentOpen13No.columns = ['recent6type13loanno']
            X_data = pd.merge(X_data,
                              recentOpen13No,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recentOpen13No
        del recentOpen13
        # 最近6个月新开汽车贷款数
        recentOpen21 = recent6data[recent6data['LOANTYPE'] == 21]
        if recentOpen21.shape[0] == 0:
            X_data['recent6type21loanno'] = 0
        else:
            recentOpen21No = recentOpen21[['CERTIFICATECODE', 'REPORTDATE'
                                           ]].groupby('CERTIFICATECODE').count(
            )
            recentOpen21No.columns = ['recent6type21loanno']
            X_data = pd.merge(X_data,
                              recentOpen21No,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recentOpen21No
        del recentOpen21
        # 最近6个月新开个人助学贷款数
        recentOpen31 = recent6data[recent6data['LOANTYPE'] == 31]
        if recentOpen31.shape[0] == 0:
            X_data['recent6type31loanno'] = 0
        else:
            recentOpen31No = recentOpen31[['CERTIFICATECODE', 'REPORTDATE'
                                           ]].groupby('CERTIFICATECODE').count(
            )
            recentOpen31No.columns = ['recent6type31loanno']
            X_data = pd.merge(X_data,
                              recentOpen31No,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recentOpen31No
        del recentOpen31
        # 最近6个月新开个人经营性贷款数
        recentOpen41 = recent6data[recent6data['LOANTYPE'] == 41]
        if recentOpen41.shape[0] == 0:
            X_data['recent6type41loanno'] = 0
        else:
            recentOpen41No = recentOpen41[['CERTIFICATECODE', 'REPORTDATE'
                                           ]].groupby('CERTIFICATECODE').count(
            )
            recentOpen41No.columns = ['recent6type41loanno']
            X_data = pd.merge(X_data,
                              recentOpen41No,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recentOpen41No
        del recentOpen41
        # 最近6个月新开农户贷款数
        recentOpen51 = recent6data[recent6data['LOANTYPE'] == 51]
        if recentOpen51.shape[0] == 0:
            X_data['recent6type51loanno'] = 0
        else:
            recentOpen51No = recentOpen51[['CERTIFICATECODE', 'REPORTDATE'
                                           ]].groupby('CERTIFICATECODE').count(
            )
            recentOpen51No.columns = ['recent6type51loanno']
            X_data = pd.merge(X_data,
                              recentOpen51No,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recentOpen51No
        del recentOpen51
        # 最近6个月新开其他贷款数
        recentOpen99 = recent6data[recent6data['LOANTYPE'] == 99]
        if recentOpen99.shape[0] == 0:
            X_data['recent6type99loanno'] = 0
        else:
            recentOpen99No = recentOpen99[['CERTIFICATECODE', 'REPORTDATE'
                                           ]].groupby('CERTIFICATECODE').count(
            )
            recentOpen99No.columns = ['recent6type99loanno']
            X_data = pd.merge(X_data,
                              recentOpen99No,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recentOpen99No
        del recentOpen99, recent6data
        recent9data = data[data['datedelta'] < 0.75]
        # 最近9个月新开贷款个数
        if recent9data.shape[0] == 0:
            X_data['recent9loanno'] = 0
        else:
            recent9OpenNo = recent9data[['CERTIFICATECODE', 'REPORTDATE'
                                         ]].groupby('CERTIFICATECODE').count()
            recent9OpenNo.columns = ['recent9loanno']
            X_data = pd.merge(X_data,
                              recent9OpenNo,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recent9OpenNo
        # 最近9个月新开贷款授信总额度
        if recent9data.shape[0] == 0:
            X_data['recent9loantotallimit'] = 0
        else:
            recent9OpenSum = recent9data[['CERTIFICATECODE', 'CREDITLIMIT'
                                          ]].groupby('CERTIFICATECODE').sum()
            recent9OpenSum.columns = ['recent9loantotallimit']
            X_data = pd.merge(X_data,
                              recent9OpenSum,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recent9OpenSum
        del recent9data

    return X_data


def calcXCreditLength(data, X_data):
    if data.shape[0] == 0:
        X_data['loaninuseguaranteeway4no'] = 0
        X_data['loaninuseavgterm'] = 0
        X_data['loan_balance_num'] = 0
    else:
        inUseLoan = data[(data['STAT_FLAG'] == 1) & (data['BALANCE'] > 0)]
        # 正在使用担保方式为4的个数
        inUseLoanGuarantee4 = inUseLoan[inUseLoan['GUARANTEEWAY'] == 4]
        if inUseLoanGuarantee4.shape[0] == 0:
            X_data['loaninuseguaranteeway4no'] = 0
        else:
            inUseLoanGuarantee4No = inUseLoanGuarantee4[
                ['CERTIFICATECODE', 'REPORTDATE']].groupby(
                    'CERTIFICATECODE').count()
            inUseLoanGuarantee4No.columns = ['loaninuseguaranteeway4no']
            X_data = pd.merge(X_data,
                              inUseLoanGuarantee4No,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del inUseLoanGuarantee4No
        del inUseLoanGuarantee4
        # 正在使用的贷款平均授信时长
        if inUseLoan.shape[0] == 0:
            X_data['loaninuseavgterm'] = 0
        else:
            inUseLoan['duration'] = inUseLoan['DATECLOSED'] - inUseLoan[
                'DATEOPENED']
            inUseLoan['duration'] = inUseLoan['duration'].astype(
                'timedelta64[Y]')
            inUseLoanAvgCreditLength = inUseLoan[['CERTIFICATECODE', 'duration'
                                                  ]].groupby(
                                                      'CERTIFICATECODE').mean()
            inUseLoanAvgCreditLength.columns = ['loaninuseavgterm']
            X_data = pd.merge(X_data,
                              inUseLoanAvgCreditLength,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del inUseLoanAvgCreditLength
        del inUseLoan
        # 有欠款的账户数量
        inPayLoan = data[data['BALANCE'] > 0]
        if inPayLoan.shape[0] == 0:
            X_data['loan_balance_num'] = 0
        else:
            inPayLoanNo = inPayLoan[['CERTIFICATECODE', 'REPORTDATE']].groupby(
                'CERTIFICATECODE').count()
            inPayLoanNo.columns = ['loan_balance_num']
            X_data = pd.merge(X_data,
                              inPayLoanNo,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del inPayLoanNo
        del inPayLoan
    return X_data


def calcXLoancard24Month(data, X_data):
    if data.shape[0] == 0:
        X_data['type81month24curtermpastdue'] = 0
        X_data['type81month24nratio'] = 0
        X_data['type81month24stat23no'] = 0
    else:
        # 贷记卡当前逾期期数
        # data['loancardCurPastDue']=data['PAYSTAT24MONTH'].map(curTermPastDue)
        loancardCurPastDue = data[['CERTIFICATECODE', 'CURTERMSPASTDUE'
                                   ]].groupby('CERTIFICATECODE').max()
        loancardCurPastDue.columns = ['type81month24curtermpastdue']
        X_data = pd.merge(X_data,
                          loancardCurPastDue,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        #del data['loancardCurPastDue'],
        del loancardCurPastDue
        # 24月正常还款的比例
        data['24MonthNRatio'] = data['PAYSTAT24MONTH'].map(calcCardNRatio)
        loancard24MonthNRatio = data[['CERTIFICATECODE', '24MonthNRatio'
                                      ]].groupby('CERTIFICATECODE').mean()
        loancard24MonthNRatio.columns = ['type81month24nratio']
        X_data = pd.merge(X_data,
                          loancard24MonthNRatio,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del loancard24MonthNRatio, data['24MonthNRatio']
        # 贷记卡24月状态为23的个数
        data['24Month23No'] = data['PAYSTAT24MONTH'].map(count2423No)
        loancard24Month23No = data[['CERTIFICATECODE', '24Month23No']].groupby(
            'CERTIFICATECODE').sum()
        loancard24Month23No.columns = ['type81month24stat23no']
        X_data = pd.merge(X_data,
                          loancard24Month23No,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del loancard24Month23No, data['24Month23No']
        # print 'calcXLoancard24Month : ' ,X_data.shape
    return X_data


def calcXLoancardGuaranteeway(data, X_data):
    if data.shape[0] == 0:
        X_data['type81guaranteeway4no'] = 0
        X_data['type81guaranteeway9no'] = 0
    else:
        # 贷记卡担保方式为4的个数
        loancardGuarantee4 = data[data['GUARANTEEWAY'] == 4]
        if loancardGuarantee4.shape[0] == 0:
            X_data['type81guaranteeway4no'] = 0
        else:
            loancardGuarantee4No = loancardGuarantee4[
                ['CERTIFICATECODE', 'REPORTDATE']].groupby(
                    'CERTIFICATECODE').count()
            loancardGuarantee4No.columns = ['type81guaranteeway4no']
            X_data = pd.merge(X_data,
                              loancardGuarantee4No,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del loancardGuarantee4No
        del loancardGuarantee4
        # 贷记卡担保方式为9的个数
        loancardGuarantee9 = data[data['GUARANTEEWAY'] != 4]
        if loancardGuarantee9.shape[0] == 0:
            X_data['type81guaranteeway9no'] = 0
        else:
            loancardGuarantee9No = loancardGuarantee9[
                ['CERTIFICATECODE', 'REPORTDATE']].groupby(
                    'CERTIFICATECODE').count()
            loancardGuarantee9No.columns = ['type81guaranteeway9no']
            X_data = pd.merge(X_data,
                              loancardGuarantee9No,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del loancardGuarantee9No
        del loancardGuarantee9
    return X_data


def calcXLoancardTimeRelate(data, X_data):
    if data.shape[0] == 0:
        X_data['type81longestlength'] = 0
        X_data['recenttype81time'] = 0
        X_data['recent3type81no'] = 0
        X_data['recent6type81no'] = 0
        X_data['recent9type81no'] = 0
        X_data['type81_balance_num'] = 0
    else:
        data['yearPast'] = data['STATENDDATE'] - data['DATEOPENED']
        data['yearPast'] = data['yearPast'].astype('timedelta64[Y]')
        # 贷记卡最长使用年限
        loancardLongestLength = data[['CERTIFICATECODE', 'yearPast']].groupby(
            'CERTIFICATECODE').max()
        loancardLongestLength.columns = ['type81longestlength']
        X_data = pd.merge(X_data,
                          loancardLongestLength,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del loancardLongestLength, data['yearPast']
        # 最近开户的贷记卡距现在的时间
        recentOpenLoancard = data[['CERTIFICATECODE', 'datedelta']].groupby(
            'CERTIFICATECODE').min()
        recentOpenLoancard.columns = ['recenttype81time']
        X_data = pd.merge(X_data,
                          recentOpenLoancard,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del recentOpenLoancard
        # 最近3个月开户的贷记卡个数
        recent3LoancardOpen = data[data['datedelta'] < 0.25]
        if recent3LoancardOpen.shape[0] == 0:
            X_data['recent3type81no'] = 0
        else:
            recent3LoancardOpenNo = recent3LoancardOpen[
                ['CERTIFICATECODE', 'REPORTDATE']].groupby(
                    'CERTIFICATECODE').count()
            recent3LoancardOpenNo.columns = ['recent3type81no']
            X_data = pd.merge(X_data,
                              recent3LoancardOpenNo,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recent3LoancardOpenNo
        del recent3LoancardOpen
        # 最近6个月开户的贷记卡个数
        recent6LoancardOpen = data[data['datedelta'] < 0.5]
        if recent6LoancardOpen.shape[0] == 0:
            X_data['recent6type81no'] = 0
        else:
            recent6LoancardOpenNo = recent6LoancardOpen[
                ['CERTIFICATECODE', 'REPORTDATE']].groupby(
                    'CERTIFICATECODE').count()
            recent6LoancardOpenNo.columns = ['recent6type81no']
            X_data = pd.merge(X_data,
                              recent6LoancardOpenNo,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recent6LoancardOpenNo
        del recent6LoancardOpen
        # 最近9个月开户的贷记卡个数
        recent9LoancardOpen = data[data['datedelta'] < 0.75]
        if recent9LoancardOpen.shape[0] == 0:
            X_data['recent9type81no'] = 0
        else:
            recent9LoancardOpenNo = recent9LoancardOpen[
                ['CERTIFICATECODE', 'REPORTDATE']].groupby(
                    'CERTIFICATECODE').count()
            recent9LoancardOpenNo.columns = ['recent9type81no']
            X_data = pd.merge(X_data,
                              recent9LoancardOpenNo,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recent9LoancardOpenNo
        del recent9LoancardOpen
        # 有欠款的贷记卡数量
        inPayLoan = data[data['BALANCE'] > 0]
        if inPayLoan.shape[0] == 0:
            X_data['type81_balance_num'] = 0
        else:
            inPayLoanNo = inPayLoan[['CERTIFICATECODE', 'REPORTDATE']].groupby(
                'CERTIFICATECODE').count()
            inPayLoanNo.columns = ['type81_balance_num']
            X_data = pd.merge(X_data,
                              inPayLoanNo,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del inPayLoanNo
        del inPayLoan
    return X_data


def calcXGuaranteeWay(data, X_data):
    if data.shape[0] == 0:
        X_data['guaranteeway2no'] = 0
        X_data['openAccountNo'] = 0
        X_data['guaranteeway4no'] = 0
        X_data['guaranteeway4ratio'] = 0
        X_data['inuseguaranteeway2no'] = 0
        X_data['inuseguaranteeway2ratio'] = 0
        X_data['existype11'] = 0
    else:
        # 担保方式为2的个数
        guaranteeway2 = data[data['GUARANTEEWAY'] == 2]
        if guaranteeway2.shape[0] == 0:
            X_data['guaranteeway2no'] = 0
        else:
            guaranteeway2No = guaranteeway2[['CERTIFICATECODE', 'REPORTDATE'
                                             ]].groupby(
                                                 'CERTIFICATECODE').count()
            guaranteeway2No.columns = ['guaranteeway2no']
            X_data = pd.merge(X_data,
                              guaranteeway2No,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del guaranteeway2No
        del guaranteeway2
        # 担保方式为2的个数与总贷款数的占比
        openAccountNo = data[['CERTIFICATECODE', 'REPORTDATE']].groupby(
            'CERTIFICATECODE').count()
        openAccountNo.columns = ['openAccountNo']
        X_data = pd.merge(X_data,
                          openAccountNo,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        X_data['guaranteeway2ratio'] = X_data['guaranteeway2no'] / X_data[
            'openAccountNo']
        del openAccountNo
        # 担保方式为4的个数
        guaranteeway4 = data[data['GUARANTEEWAY'] == 4]
        if guaranteeway4.shape[0] == 0:
            X_data['guaranteeway4no'] = 0
        else:
            guaranteeway4No = guaranteeway4[['CERTIFICATECODE', 'REPORTDATE'
                                             ]].groupby(
                                                 'CERTIFICATECODE').count()
            guaranteeway4No.columns = ['guaranteeway4no']
            X_data = pd.merge(X_data,
                              guaranteeway4No,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del guaranteeway4No
        del guaranteeway4
        # 担保方式为4的个数与总贷款数的占比
        X_data['guaranteeway4ratio'] = X_data['guaranteeway4no'] / X_data[
            'openAccountNo']
        del X_data['openAccountNo']
        # 正在使用的担保方式为2的个数
        inUseLoan = data[(data['STAT_FLAG'] == 1) & (data['BALANCE'] > 0)]
        inUseLoanGuarantee2 = inUseLoan[inUseLoan['GUARANTEEWAY'] == 2]
        if inUseLoanGuarantee2.shape[0] == 0:
            X_data['inuseguaranteeway2no'] = 0
        else:
            inUseLoanGuarantee2No = inUseLoanGuarantee2[
                ['CERTIFICATECODE', 'REPORTDATE']].groupby(
                    'CERTIFICATECODE').count()
            inUseLoanGuarantee2No.columns = ['inuseguaranteeway2no']
            X_data = pd.merge(X_data,
                              inUseLoanGuarantee2No,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del inUseLoanGuarantee2No
        del inUseLoanGuarantee2
        # 正在使用的担保方式为2的个数与正在还款的贷款数的占比
        if inUseLoan.shape[0] == 0:
            X_data['inuseguaranteeway2ratio'] = 0
        else:
            inUseLoanNo = inUseLoan[['CERTIFICATECODE', 'REPORTDATE']].groupby(
                'CERTIFICATECODE').count()
            inUseLoanNo.columns = ['inUseLoanNo']
            X_data = pd.merge(X_data,
                              inUseLoanNo,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            X_data['inuseguaranteeway2ratio'] = X_data[
                'inuseguaranteeway2no'] / X_data['inUseLoanNo']
            del inUseLoanNo
        # del X_data['inUseLoanNo'],inUseLoan
        del inUseLoan
        # 有无房贷
        data['existype11'] = data['LOANTYPE'] == 11
        isType11 = data[['CERTIFICATECODE', 'existype11']].groupby(
            'CERTIFICATECODE').max()
        isType11.columns = ['existype11']
        isType11['existype11'] = isType11['existype11'].astype(int)
        X_data = pd.merge(X_data,
                          isType11,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del data['existype11'], isType11
    return X_data


def calcXLoanRecentPay(data, X_data):
    if data.shape[0] == 0:
        X_data['type21recentpayno'] = 0
        X_data['type1113recentpayno'] = 0
        X_data['type41recentpayno'] = 0
        X_data['type99recentpayno'] = 0
    else:
        data['recentPayDateDelta'] = data['REPORTDATE'] - data['RECENTPAYDATE']
        data['recentPayDateDelta'] = data['recentPayDateDelta'].astype(
            'timedelta64[M]')
        recentPay = data[data['recentPayDateDelta'] < 6]
        # 近期有还款的车贷账户数量
        recentPayCar = recentPay[recentPay['LOANTYPE'] == 21]
        if recentPayCar.shape[0] == 0:
            X_data['type21recentpayno'] = 0
        else:
            recentPayCarNo = recentPayCar[['CERTIFICATECODE', 'REPORTDATE'
                                           ]].groupby('CERTIFICATECODE').count(
            )
            recentPayCarNo.columns = ['type21recentpayno']
            X_data = pd.merge(X_data,
                              recentPayCarNo,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recentPayCarNo
        del recentPayCar
        # 近期有还款的个人住房与公积金房贷账户数量
        recentPayHouse = recentPay[(recentPay['LOANTYPE'] == 11) | (recentPay[
            'LOANTYPE'] == 13)]
        if recentPayHouse.shape[0] == 0:
            X_data['type1113recentpayno'] = 0
        else:
            recentPayHouseNo = recentPayHouse[['CERTIFICATECODE', 'REPORTDATE'
                                               ]].groupby(
                                                   'CERTIFICATECODE').count()
            recentPayHouseNo.columns = ['type1113recentpayno']
            X_data = pd.merge(X_data,
                              recentPayHouseNo,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recentPayHouseNo
        del recentPayHouse
        # 近期有还款的个人经营性贷款账户数量
        recentPayBusiness = recentPay[recentPay['LOANTYPE'] == 41]
        if recentPayBusiness.shape[0] == 0:
            X_data['type41recentpayno'] = 0
        else:
            recentPayBusinessNo = recentPayBusiness[
                ['CERTIFICATECODE', 'REPORTDATE']].groupby(
                    'CERTIFICATECODE').count()
            recentPayBusinessNo.columns = ['type41recentpayno']
            X_data = pd.merge(X_data,
                              recentPayBusinessNo,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recentPayBusinessNo
        del recentPayBusiness
        # 近期有还款的其他贷款账户数量
        recentPayOther = recentPay[recentPay['LOANTYPE'] == 99]
        if recentPayOther.shape[0] == 0:
            X_data['type99recentpayno'] = 0
        else:
            recentPayOtherNo = recentPayOther[['CERTIFICATECODE', 'REPORTDATE'
                                               ]].groupby(
                                                   'CERTIFICATECODE').count()
            recentPayOtherNo.columns = ['type99recentpayno']
            X_data = pd.merge(X_data,
                              recentPayOtherNo,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recentPayOtherNo
        del recentPayOther
        del data['recentPayDateDelta'], recentPay
    return X_data


def calcXOther(data, X_data):
    if data.shape[0] == 0:
        X_data['type41maxcreditlength'] = 0
        X_data['51oneyearnratio'] = 0
        X_data['cloannratio'] = 0
        X_data['cloanavglimit'] = 0
        X_data['otherloanavglength'] = 0
        X_data['loaninusefreq8no'] = 0
        X_data['loaninusefreq7no'] = 0
        X_data['type11nratio'] = 0
        X_data['inuseloancreditduration'] = 0
    else:
        # 个人经营性贷款最长信用年限
        type41Loan = data[data['LOANTYPE'] == 41]
        type41Loan['yearPast'] = type41Loan['STATENDDATE'] - type41Loan[
            'DATEOPENED']
        type41Loan['yearPast'] = type41Loan['yearPast'].astype(
            'timedelta64[Y]')
        if type41Loan.shape[0] == 0:
            X_data['type41maxcreditlength'] = 0
        else:
            type41CreditLength = type41Loan[['CERTIFICATECODE', 'yearPast'
                                             ]].groupby('CERTIFICATECODE').max(
            )
            type41CreditLength.columns = ['type41maxcreditlength']
            X_data = pd.merge(X_data,
                              type41CreditLength,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del type41CreditLength
        del type41Loan
        # 农户贷款一年内正常还款占比
        type51Loan = data[data['LOANTYPE'] == 51]
        if type51Loan.shape[0] == 0:
            X_data['51oneyearnratio'] = 0
        else:
            type51Loan['oneYearNRatio'] = type51Loan['PAYSTAT24MONTH'].map(
                oneYearNRatio)
            type51OneYearRatio = type51Loan[['CERTIFICATECODE', 'oneYearNRatio'
                                             ]].groupby(
                                                 'CERTIFICATECODE').mean()
            type51OneYearRatio.columns = ['51oneyearnratio']
            X_data = pd.merge(X_data,
                              type51OneYearRatio,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del type51OneYearRatio
        del type51Loan
        # 已结清账户正常还款比例
        clearLoan = data[(data['STAT_FLAG'] == 2) & (data['BALANCE'] == 0)]
        if clearLoan.shape[0] == 0:
            X_data['cloannratio'] = 0
        else:
            clearLoan['nratio'] = clearLoan['PAYSTAT24MONTH'].map(calcNRatio)
            clearLoanOneYearNNo = clearLoan[
                ['CERTIFICATECODE', 'nratio']].groupby('CERTIFICATECODE').mean(
            )
            clearLoanOneYearNNo.columns = ['cloannratio']
            X_data = pd.merge(X_data,
                              clearLoanOneYearNNo,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del clearLoanOneYearNNo
        # 已结清贷款平均贷款额度
        if clearLoan.shape[0] == 0:
            X_data['cloanavglimit'] = 0
        else:
            clearLoanAvgLimit = clearLoan[['CERTIFICATECODE', 'CREDITLIMIT'
                                           ]].groupby('CERTIFICATECODE').sum()
            clearLoanAvgLimit.columns = ['cloanavglimit']
            X_data = pd.merge(X_data,
                              clearLoanAvgLimit,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del clearLoanAvgLimit
        del clearLoan
        # 其他贷款平均信用年限
        type99Loan = data[data['LOANTYPE'] == 99]
        type99Loan['yearPast'] = type99Loan['STATENDDATE'] - type99Loan[
            'DATEOPENED']
        type99Loan['yearPast'] = type99Loan['yearPast'].astype(
            'timedelta64[Y]')
        if type99Loan.shape[0] == 0:
            X_data['otherloanavglength'] = 0
        else:
            type99CreditLength = type99Loan[['CERTIFICATECODE', 'yearPast'
                                             ]].groupby(
                                                 'CERTIFICATECODE').mean()
            type99CreditLength.columns = ['otherloanavglength']
            X_data = pd.merge(X_data,
                              type99CreditLength,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del type99CreditLength
        del type99Loan
        # 正在使用贷款还款频率为一次性的数量
        inUseLoan = data[(data['BALANCE'] > 0) & (data['STAT_FLAG'] == 1)]
        inUseTermsfreq8 = inUseLoan[inUseLoan['TERMSFREQ'] == 8]
        if inUseTermsfreq8.shape[0] == 0:
            X_data['loaninusefreq8no'] = 0
        else:
            inUseTermsfreq8No = inUseTermsfreq8[['CERTIFICATECODE',
                                                 'REPORTDATE']].groupby(
                                                     'CERTIFICATECODE').count()
            inUseTermsfreq8No.columns = ['loaninusefreq8no']
            X_data = pd.merge(X_data,
                              inUseTermsfreq8No,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del inUseTermsfreq8No
        del inUseTermsfreq8
        # 正在使用贷款还款频率为不定期(其他)的数量
        inUseTermsfreq7 = inUseLoan[inUseLoan['TERMSFREQ'] == 7]
        if inUseTermsfreq7.shape[0] == 0:
            X_data['loaninusefreq7no'] = 0
        else:
            inUseTermsfreq7No = inUseTermsfreq7[['CERTIFICATECODE',
                                                 'REPORTDATE']].groupby(
                                                     'CERTIFICATECODE').count()
            inUseTermsfreq7No.columns = ['loaninusefreq7no']
            X_data = pd.merge(X_data,
                              inUseTermsfreq7No,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del inUseTermsfreq7No
        del inUseTermsfreq7
        # 个人住房贷款24月还款状态正常(N)的占比
        type11Loan = data[data['LOANTYPE'] == 11]
        if type11Loan.shape[0] == 0:
            X_data['type11nratio'] = 0
        else:
            type11Loan['24MonthNRatio'] = type11Loan['PAYSTAT24MONTH'].map(
                calcNRatio)
            type1124MonthNratio = type11Loan[['CERTIFICATECODE',
                                              '24MonthNRatio']].groupby(
                                                  'CERTIFICATECODE').mean()
            type1124MonthNratio.columns = ['type11nratio']
            X_data = pd.merge(X_data,
                              type1124MonthNratio,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del type11Loan['24MonthNRatio'], type1124MonthNratio
        del type11Loan
        # 正在使用的贷款平均授信期
        if inUseLoan.shape[0] == 0:
            X_data['inuseloancreditduration'] = 0
        else:
            # print 'inUseLoan.shape : '
            # print inUseLoan.shape
            inUseLoan['CreditDuration'] = inUseLoan['DATECLOSED'] - inUseLoan[
                'DATEOPENED']
            inUseLoan['CreditDuration'] = inUseLoan['CreditDuration'].astype(
                'timedelta64[Y]')
            inUseLoanCreditDuration = inUseLoan[['CERTIFICATECODE',
                                                 'CreditDuration']].groupby(
                                                     'CERTIFICATECODE').mean()
            inUseLoanCreditDuration.columns = ['inuseloancreditduration']
            X_data = pd.merge(X_data,
                              inUseLoanCreditDuration,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del inUseLoanCreditDuration
        del inUseLoan
    return X_data
    ################

    # loancard


def calcXloancard(data, X_data):
    if data.shape[0] == 0:
        X_data['type81maxcreditlength'] = 0
        X_data['type81avgcreditlength'] = 0
        X_data['type81stat24nratio'] = 0
        X_data['type81ncount'] = 0
        X_data['type81statallno'] = 0
        X_data['type81statcno'] = 0
        X_data['type81stat123no'] = 0
        X_data['type81stat7no'] = 0
        X_data['type81cardno'] = 0
        X_data['type81mincreditlength'] = 0
        X_data['type81recentopenno'] = 0
    else:
        data['yearPast'] = data['STATENDDATE'] - data['DATEOPENED']
        data['yearPast'] = data['yearPast'].astype('timedelta64[Y]')
        # 贷记卡最大信用年限
        loancardMaxCreditLength = data[['CERTIFICATECODE', 'yearPast'
                                        ]].groupby('CERTIFICATECODE').max()
        loancardMaxCreditLength.columns = ['type81maxcreditlength']
        X_data = pd.merge(X_data,
                          loancardMaxCreditLength,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del loancardMaxCreditLength
        # 贷记卡平均信用年限
        loancardAvgCreditLength = data[['CERTIFICATECODE', 'yearPast'
                                        ]].groupby('CERTIFICATECODE').mean()
        loancardAvgCreditLength.columns = ['type81avgcreditlength']
        X_data = pd.merge(X_data,
                          loancardAvgCreditLength,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del loancardAvgCreditLength, data['yearPast']
        # 贷记卡24月状态为N的占比
        data['24MonthNRatio'] = data['PAYSTAT24MONTH'].map(cardNRatio)
        loancard24MonthNRatio = data[['CERTIFICATECODE', '24MonthNRatio'
                                      ]].groupby('CERTIFICATECODE').mean()
        loancard24MonthNRatio.columns = ['type81stat24nratio']
        X_data = pd.merge(X_data,
                          loancard24MonthNRatio,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del data['24MonthNRatio'], loancard24MonthNRatio
        # 24月状态N的个数
        data['24MonthNNo'] = data['PAYSTAT24MONTH'].map(countcard24NNo)
        loancard24MonthNNo = data[['CERTIFICATECODE', '24MonthNNo']].groupby(
            'CERTIFICATECODE').sum()
        loancard24MonthNNo.columns = ['type81ncount']
        X_data = pd.merge(X_data,
                          loancard24MonthNNo,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del data['24MonthNNo'], loancard24MonthNNo
        # 24月状态数字的个数
        data['24MonthNumNo'] = data['PAYSTAT24MONTH'].map(count24NumNo)
        loancard24MonthNumNo = data[['CERTIFICATECODE', '24MonthNumNo'
                                     ]].groupby('CERTIFICATECODE').sum()
        loancard24MonthNumNo.columns = ['type81statallno']
        X_data = pd.merge(X_data,
                          loancard24MonthNumNo,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del data['24MonthNumNo'], loancard24MonthNumNo

        # 24月状态C的个数
        data['24MonthCNo'] = data['PAYSTAT24MONTH'].map(count24CNo)
        loancard24MonthCNo = data[['CERTIFICATECODE', '24MonthCNo']].groupby(
            'CERTIFICATECODE').sum()
        loancard24MonthCNo.columns = ['type81statcno']
        X_data = pd.merge(X_data,
                          loancard24MonthCNo,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del data['24MonthCNo'], loancard24MonthCNo
        # 24月状态123的个数
        data['24Month123No'] = data['PAYSTAT24MONTH'].map(count24123No)
        loancard24Month123No = data[['CERTIFICATECODE', '24Month123No'
                                     ]].groupby('CERTIFICATECODE').sum()
        loancard24Month123No.columns = ['type81stat123no']
        X_data = pd.merge(X_data,
                          loancard24Month123No,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del data['24Month123No'], loancard24Month123No
        # 24月状态7的个数
        data['24Month7No'] = data['PAYSTAT24MONTH'].map(count247No)
        loancard24Month7No = data[['CERTIFICATECODE', '24Month7No']].groupby(
            'CERTIFICATECODE').sum()
        loancard24Month7No.columns = ['type81stat7no']
        X_data = pd.merge(X_data,
                          loancard24Month7No,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del data['24Month7No'], loancard24Month7No
        # 贷记卡个数
        loancardNo = data[['CERTIFICATECODE', 'REPORTDATE']].groupby(
            'CERTIFICATECODE').count()
        loancardNo.columns = ['type81cardno']
        X_data = pd.merge(X_data,
                          loancardNo,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del loancardNo
        # 最近一次贷记卡开卡距今的时间
        loancardMinLength = data[['CERTIFICATECODE', 'datedelta']].groupby(
            'CERTIFICATECODE').min()
        loancardMinLength.columns = ['type81mincreditlength']
        X_data = pd.merge(X_data,
                          loancardMinLength,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del loancardMinLength
        # 最近6个月开户的贷记卡个数
        recent6LoancardOpen = data[data['datedelta'] < 0.5]
        if recent6LoancardOpen.shape[0] == 0:
            X_data['type81recentopenno'] = 0
        else:
            recent6LoancardOpenNo = recent6LoancardOpen[
                ['CERTIFICATECODE', 'REPORTDATE']].groupby(
                    'CERTIFICATECODE').count()
            recent6LoancardOpenNo.columns = ['type81recentopenno']
            X_data = pd.merge(X_data,
                              recent6LoancardOpenNo,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recent6LoancardOpenNo
        del recent6LoancardOpen
        # 最近6个月开户的贷记卡授信总额度
        # recent6LoancardOpen=data[data['datedelta']<0.5]
        # if recent6LoancardOpen.shape[0] == 0:
        #   X_data['Type81Recent6OpenLimitSum']=0
        # else:
        #   recent6LoancardOpenSum=recent6LoancardOpen[['CERTIFICATECODE','CREDITLIMIT']].groupby('CERTIFICATECODE').sum()
        #   recent6LoancardOpenSum.columns=['Type81Recent6OpenLimitSum']
        #   X_data=pd.merge(X_data,recent6LoancardOpenSum,left_on='CERTIFICATECODE',right_index=True,how='outer')
        #   del recent6LoancardOpen,recent6LoancardOpenSum
    return X_data


def calcXCreditcard(data, X_data):

    data['recentPayDateDelta'] = data['REPORTDATE'] - data['RECENTPAYDATE']
    data['recentPayDateDelta'] = data['recentPayDateDelta'].astype(
        'timedelta64[M]')
    if data.shape[0] == 0:
        X_data['type71loanrecentpayno'] = 0
        X_data['type71recentopenavgcreditlimit'] = 0
        X_data['type71curtermpastdue'] = 0
        X_data['type71recentopenno'] = 0
        X_data['type71oneyear23no'] = 0
    else:
        recentPay = data[data['recentPayDateDelta'] < 6]
        # 近期有还款的准贷记卡数量
        if recentPay.shape[0] == 0:
            X_data['type71loanrecentpayno'] = 0
        else:
            recentPayNo = recentPay[['CERTIFICATECODE', 'REPORTDATE']].groupby(
                'CERTIFICATECODE').count()
            recentPayNo.columns = ['type71loanrecentpayno']
            X_data = pd.merge(X_data,
                              recentPayNo,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
        del data['recentPayDateDelta'], recentPay
        # 最近6个月开户的准贷记卡授信总额度
        recent6CreditcardOpen = data[data['datedelta'] < 0.5]
        if recent6CreditcardOpen.shape[0] == 0:
            X_data['type71recentopenavgcreditlimit'] = 0
        else:
            recent6CreditcardOpenSum = recent6CreditcardOpen[
                ['CERTIFICATECODE', 'CREDITLIMIT']].groupby(
                    'CERTIFICATECODE').mean()
            recent6CreditcardOpenSum.columns = [
                'type71recentopenavgcreditlimit'
            ]
            X_data = pd.merge(X_data,
                              recent6CreditcardOpenSum,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recent6CreditcardOpenSum

        # 准贷记卡当前逾期期数
        data['type71pastdue'] = data['PAYSTAT24MONTH'].map(curTermPastDue)
        type71curtermpastdue = data[['CERTIFICATECODE', 'type71pastdue'
                                     ]].groupby('CERTIFICATECODE').max()
        type71curtermpastdue.columns = ['type71curtermpastdue']
        X_data = pd.merge(X_data,
                          type71curtermpastdue,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del data['type71pastdue'], type71curtermpastdue
        # 最近6个月开户的准贷记卡个数
        if recent6CreditcardOpen.shape[0] == 0:
            X_data['type71recentopenno'] = 0
        else:
            recent6CreditcardOpenNo = recent6CreditcardOpen[
                ['CERTIFICATECODE', 'REPORTDATE']].groupby(
                    'CERTIFICATECODE').count()
            recent6CreditcardOpenNo.columns = ['type71recentopenno']
            X_data = pd.merge(X_data,
                              recent6CreditcardOpenNo,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='outer')
            del recent6CreditcardOpenNo
        del recent6CreditcardOpen
        # 准贷记卡12月内23状态次数
        data['recent1223No'] = data['PAYSTAT24MONTH'].map(oneYear23No)
        creditcardOneYear23No = data[['CERTIFICATECODE', 'recent1223No'
                                      ]].groupby('CERTIFICATECODE').sum()
        creditcardOneYear23No.columns = ['type71oneyear23no']
        X_data = pd.merge(X_data,
                          creditcardOneYear23No,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del data['recent1223No'], creditcardOneYear23No

    return X_data


def calcXQuery(data, X_data):
    if data.shape[0] == 0:
        X_data['queryno'] = 0
    else:
        # 历史查询次数
        queryNo = data[['CERTIFICATECODE', 'QUERYDATE']].groupby(
            'CERTIFICATECODE').count()
        queryNo.columns = ['queryno']
        X_data = pd.merge(X_data,
                          queryNo,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='outer')
        del queryNo
    return X_data
