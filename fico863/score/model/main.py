# -*- coding: utf-8 -*-

import calc_x
import run_model
import stat863
import calc_relate
import interpret
import pandas as pd
from datetime import datetime


def convertime(date):
    # return date.date()
    try:
        date = datetime.strptime(date[:10], "%Y-%m-%d")

    except:
        date = datetime.strptime(date[:10], "%Y.%m.%d")

    return date


def convert(loan, loancard, creditcard):
    if loan.shape[0] == 0:
        pass
    else:
        loan['DATEOPENED'] = loan['DATEOPENED'].map(convertime)
        loan['DATECLOSED'] = loan['DATECLOSED'].map(convertime)
        loan['STATENDDATE'] = loan['STATENDDATE'].map(convertime)
        loan['REPORTDATE'] = loan['REPORTDATE'].map(convertime)
        loan['RECENTPAYDATE'] = loan['RECENTPAYDATE'].map(convertime)
        loan['datedelta'] = loan['REPORTDATE'] - loan['DATEOPENED']
        loan['datedelta'] = loan['datedelta'].astype('timedelta64[Y]')

    if loancard.shape[0] == 0:
        pass
    else:
        loancard['REPORTDATE'] = loancard['REPORTDATE'].map(convertime)
        loancard['DATEOPENED'] = loancard['DATEOPENED'].map(convertime)
        loancard['STATENDDATE'] = loancard['STATENDDATE'].map(convertime)
        loancard['datedelta'] = loancard['REPORTDATE'] - loancard['DATEOPENED']
        loancard['datedelta'] = loancard['datedelta'].astype('timedelta64[Y]')

    if creditcard.shape[0] == 0:
        pass
    else:
        creditcard['REPORTDATE'] = creditcard['REPORTDATE'].map(convertime)
        creditcard['DATEOPENED'] = creditcard['DATEOPENED'].map(convertime)
        creditcard['RECENTPAYDATE'] = creditcard['RECENTPAYDATE'].map(
            convertime)
        creditcard['datedelta'] = creditcard['REPORTDATE'] - creditcard[
            'DATEOPENED']
        creditcard['datedelta'] = creditcard['datedelta'].astype(
            'timedelta64[Y]')

    return (loan, loancard, creditcard)


def calc_X(X_data, loan, loancard, creditcard, query):
    X_data = calc_x.calcX24MonthStast(loan, X_data)

    X_data = calc_x.calcXRecentOpenLoanNum(loan, X_data)

    X_data = calc_x.calcXCreditLength(loan, X_data)

    X_data = calc_x.calcXLoancard24Month(loancard, X_data)

    X_data = calc_x.calcXLoancardGuaranteeway(loancard, X_data)

    X_data = calc_x.calcXLoancardTimeRelate(loancard, X_data)
    X_data = calc_x.calcXGuaranteeWay(loan, X_data)
    X_data = calc_x.calcXLoanRecentPay(loan, X_data)
    X_data = calc_x.calcXOther(loan, X_data)
    X_data = calc_x.calcXloancard(loancard, X_data)
    X_data = calc_x.calcXCreditcard(creditcard, X_data)
    X_data = calc_x.calcXQuery(query, X_data)
    return X_data


def calc_score(loantype, loan, loancard, creditcard, query, special):
    (loan, loancard, creditcard) = convert(loan, loancard, creditcard)

    X_data = pd.DataFrame(pd.Series(loan.CERTIFICATECODE.unique()))
    X_data.columns = ['CERTIFICATECODE']
    # 得到计算后的特征数据
    X_data = calc_X(X_data, loan, loancard, creditcard, query)
    X_data.index = X_data.CERTIFICATECODE
    del X_data['CERTIFICATECODE']
    X_data = X_data.fillna(0)

    X_data_new = pd.DataFrame(pd.Series(X_data.index))
    X_data_new.columns = ['CERTIFICATECODE']
    X_data_new = calc_relate.calc_X_new(X_data_new, loan, loancard, special)
    X_data_new.index = X_data_new.CERTIFICATECODE
    X_data_new = X_data_new.fillna(0)
    del X_data_new['CERTIFICATECODE']
    lens = len(X_data)
    result = {}
    for i in range(lens):
        (fea_imp, pro, sc, creditlimit, ratio, rank,
         dimen_interp) = do_calc(loantype, pd.DataFrame(X_data.iloc[i, :]).T,
                                 pd.DataFrame(X_data_new.iloc[i, :]).T)
        result['score'] = sc
        result['pro'] = pro[0]
        result['creditlimit'] = creditlimit
        result['ratio'] = ratio
        result['rank'] = rank
        result['fea_imp_first'] = fea_imp[0]
        result['fea_imp_sec'] = fea_imp[1]
        result['fea_imp_third'] = fea_imp[2]
        result['dimen_interp'] = dimen_interp
    return result


def do_calc(loantype, X_data, X_data_new):
    # 11,12,13,21,31,41,51,81,99
    # 得到排序后的特征重要度
    fea_imp_ori = run_model.getCoefImp(X_data, loantype, 4)
    # 得到违约率预测值
    res = run_model.runLinearModel(X_data, loantype, 4)
    # 得到违约率在该模型下对应的分数并写入到文件
    sc = stat863.getScore(res[0][1], loantype, 4)
    # 得到分数的统计量，额度、违约率、排行
    (creditlimit, ratio, personAll, personPart) = stat863.getStat(sc, loantype,
                                                                  4)
    rank = personPart / float(personAll) * 100
    rank = str(rank) + '%'
    # 得到五个维度的解读
    dimen_interp = interpret.get_fd_interp(X_data, X_data_new, loantype, 4)
    return (fea_imp_ori, res, 100 - sc, creditlimit, ratio, rank, dimen_interp)
