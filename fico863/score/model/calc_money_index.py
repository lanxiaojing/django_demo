# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np


def lastTwo(strs):
    if strs == None:
        return 0
    if strs[-2] in '1234567' and strs[-1] in '1234567C':
        return 1
    return 0


def lastC(strs):
    if strs[-1] == 'C':
        return 1
    return 0


def calc_X_loanmoney(data, X_data):
    if data.shape[0] == 0:
        X_data['loancuramountpastdue180'] = 0
        X_data['loaninusetermsfreq7avglimit'] = 0
        X_data['recent12loantotallimit'] = 0
    else:
        # 贷款当前逾期181天以上还款额度
        loanPastDue180Amount = data[['CERTIFICATECODE', 'AMOUNTPASTDUE180'
                                     ]].groupby('CERTIFICATECODE').sum()
        loanPastDue180Amount.columns = ['loancuramountpastdue180']
        X_data = pd.merge(X_data,
                          loanPastDue180Amount,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='left')
        del loanPastDue180Amount
        # 正在使用贷款还款频率为不定期的平均金额
        inuseloanfreq7 = data[(data['BALANCE'] != 0) & (data['STAT_FLAG'] == 1)
                              & (data['TERMSFREQ'] == 7)]
        if inuseloanfreq7.shape[0] == 0:
            X_data['loaninusetermsfreq7avglimit'] = 0
        else:
            loaninusetermsfreq7avglimit = inuseloanfreq7[
                ['CERTIFICATECODE', 'CREDITLIMIT']].groupby(
                    'CERTIFICATECODE').mean()
            loaninusetermsfreq7avglimit.columns = [
                'loaninusetermsfreq7avglimit'
            ]
            X_data = pd.merge(X_data,
                              loaninusetermsfreq7avglimit,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='left')
            del loaninusetermsfreq7avglimit
        del inuseloanfreq7
        # 最近12个月新开贷款账户总额度
        data['monthDur'] = data['STATENDDATE'] - data['DATEOPENED']
        data['monthDur'] = data['monthDur'].astype('timedelta64[Y]')
        recent12 = data[data['monthDur'] <= 1]
        if recent12.shape[0] == 0:
            X_data['recent12loantotallimit'] = 0
        else:
            recent12loantotallimit = recent12[['CERTIFICATECODE', 'CREDITLIMIT'
                                               ]].groupby(
                                                   'CERTIFICATECODE').sum()
            recent12loantotallimit.columns = ['recent12loantotallimit']
            X_data = pd.merge(X_data,
                              recent12loantotallimit,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='left')
            del recent12loantotallimit
        del recent12, data['monthDur']
    return X_data


def calc_X_special(data, X_data):
    # 展期/缩期时长
    if data.shape[0] == 0:
        X_data['specmonthchange'] = 0
    else:
        specmonthchange = data[['CERTIFICATECODE', 'SPECIALMONTH']].groupby(
            'CERTIFICATECODE').sum()
        specmonthchange.columns = ['specmonthchange']
        X_data = pd.merge(X_data,
                          specmonthchange,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='left')
        del specmonthchange
    return X_data


def calc_X_51loan(data, X_data):
    if data.shape[0] == 0:
        X_data['type51curamountpastdue'] = 0
        X_data['type51inuseguaranteeway9avglimit'] = 0
    else:
        # 农户贷款当前逾期总期数
        type51 = data[data['LOANTYPE'] == 51]
        if type51.shape[0] == 0:
            X_data['type51curamountpastdue'] = 0
        else:
            type51curamountpastdue = type51[['CERTIFICATECODE',
                                             'CURAMOUNTPASTDUE']].groupby(
                                                 'CERTIFICATECODE').sum()
            type51curamountpastdue.columns = ['type51curamountpastdue']
            X_data = pd.merge(X_data,
                              type51curamountpastdue,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='left')
            del type51curamountpastdue
        del type51
        # 正在使用的农户贷款担保方式为9的平均金额
        inusetype51 = data[(data['LOANTYPE'] == 51) & (data[
            'GUARANTEEWAY'] == 9) & (data['BALANCE'] != 0) & (data['STAT_FLAG']
                                                              == 1)]
        if inusetype51.shape[0] == 0:
            X_data['type51inuseguaranteeway9avglimit'] = 0
        else:
            type51inuseguaranteeway9avglimit = inusetype51[
                ['CERTIFICATECODE', 'CREDITLIMIT']].groupby(
                    'CERTIFICATECODE').mean()
            type51inuseguaranteeway9avglimit.columns = [
                'type51inuseguaranteeway9avglimit'
            ]
            X_data = pd.merge(X_data,
                              type51inuseguaranteeway9avglimit,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='left')
            del type51inuseguaranteeway9avglimit
        del inusetype51
    return X_data


def calc_X_loancardmoney(data, X_data):
    if data.shape[0] == 0:
        X_data['type81curamountpastdue'] = 0
        X_data['type81guaranteeway4avglimit'] = 0
        X_data['type81inuseavgbalanceoverlimit'] = 0
        X_data['type81inuseguaranteeway4avglimit'] = 0
        X_data['type81inusemaxbalanceoverlimit'] = 0
    else:
        # 贷记卡当前逾期金额
        type81CurTermPastDue = data[['CERTIFICATECODE', 'CURAMOUNTPASTDUE'
                                     ]].groupby('CERTIFICATECODE').sum()
        type81CurTermPastDue.columns = ['type81curamountpastdue']
        X_data = pd.merge(X_data,
                          type81CurTermPastDue,
                          left_on='CERTIFICATECODE',
                          right_index=True,
                          how='left')
        del type81CurTermPastDue
        # 贷记卡担保方式为4的平均额度
        guarantee4 = data[data['GUARANTEEWAY'] == 4]
        if guarantee4.shape[0] == 0:
            X_data['type81guaranteeway4avglimit'] = 0
        else:
            type81guaranteeway4abglimit = guarantee4[
                ['CERTIFICATECODE', 'CREDITLIMIT']].groupby(
                    'CERTIFICATECODE').mean()
            type81guaranteeway4abglimit.columns = [
                'type81guaranteeway4avglimit'
            ]
            X_data = pd.merge(X_data,
                              type81guaranteeway4abglimit,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='left')
            del type81guaranteeway4abglimit
        del guarantee4

        # 正在使用贷记卡账户当前平均透支金额占授信额比
        inuseloancard = data[data['STAT_FLAG'] == 1]
        if inuseloancard.shape[0] == 0:
            X_data['type81inuseavgbalanceoverlimit'] = 0
        else:
            inuseloancard['maxdebtoverlimit'] = inuseloancard[
                'MAXDEBT'] / inuseloancard['CREDITLIMIT']
            type81inuseavgbalanceoverlimit = inuseloancard[
                ['CERTIFICATECODE', 'maxdebtoverlimit']].groupby(
                    'CERTIFICATECODE').mean()
            type81inuseavgbalanceoverlimit.columns = [
                'type81inuseavgbalanceoverlimit'
            ]
            X_data = pd.merge(X_data,
                              type81inuseavgbalanceoverlimit,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='left')
            del type81inuseavgbalanceoverlimit
        # 正在使用贷记卡账户担保方式为4的平均金额
        inuseloancard4 = inuseloancard[inuseloancard['GUARANTEEWAY'] == 4]
        if inuseloancard4.shape[0] == 0:
            X_data['type81inuseguaranteeway4avglimit'] = 0
        else:
            type81inuseguaranteeway4avglimit = inuseloancard4[
                ['CERTIFICATECODE', 'CREDITLIMIT']].groupby(
                    'CERTIFICATECODE').mean()
            type81inuseguaranteeway4avglimit.columns = [
                'type81inuseguaranteeway4avglimit'
            ]
            X_data = pd.merge(X_data,
                              type81inuseguaranteeway4avglimit,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='left')
            del type81inuseguaranteeway4avglimit
        # 正在使用贷记卡账户当前最大透支金额占授信额比
        if inuseloancard.shape[0] == 0:
            X_data['type81inusemaxbalanceoverlimit'] = 0
        else:
            type81inusemaxbalanceoverlimit = inuseloancard[
                ['CERTIFICATECODE', 'maxdebtoverlimit']].groupby(
                    'CERTIFICATECODE').max()
            type81inusemaxbalanceoverlimit.columns = [
                'type81inusemaxbalanceoverlimit'
            ]
            X_data = pd.merge(X_data,
                              type81inusemaxbalanceoverlimit,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='left')
            del type81inusemaxbalanceoverlimit
        del inuseloancard
    return X_data


def calc_X_loan(data, X_data):
    if data.shape[0] == 0:
        X_data['loaninuseavglimit'] = 0
        X_data['loaninusemaxpastdueamountoverbalance'] = 0
        X_data['loaninuseavgpastdueamountoverbalance'] = 0
        X_data['loaninuseavgbalanceoverlimit'] = 0
        X_data['loaninusemaxbalanceoverlimit'] = 0
        X_data['loaninusemaxactualpayamountoverbalance'] = 0
        X_data['loaninuseavgactualpayamountoverbalance'] = 0
    else:
        inuseloan = data[(data['BALANCE'] != 0) & (data['STAT_FLAG'] == 1)]
        inuseloan['pastdueoverbalance'] = inuseloan[
            'CURAMOUNTPASTDUE'] / inuseloan['BALANCE']
        # 正在使用贷款平均贷款额度
        if inuseloan.shape[0] == 0:
            X_data['loaninuseavglimit'] = 0
        else:
            loaninuseavglimit = inuseloan[['CERTIFICATECODE', 'CREDITLIMIT'
                                           ]].groupby('CERTIFICATECODE').mean()
            loaninuseavglimit.columns = ['loaninuseavglimit']
            X_data = pd.merge(X_data,
                              loaninuseavglimit,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='left')
            del loaninuseavglimit
        # 正在使用贷款最大平均当前逾期金额占本金余额之比，先求商，再求平均或最大
        if inuseloan.shape[0] == 0:
            X_data['loaninusemaxpastdueamountoverbalance'] = 0
        else:
            loanInuseMaxPastDueOverBalance = inuseloan[
                ['CERTIFICATECODE', 'pastdueoverbalance']].groupby(
                    'CERTIFICATECODE').max()
            loanInuseMaxPastDueOverBalance.columns = [
                'loaninusemaxpastdueamountoverbalance'
            ]
            X_data = pd.merge(X_data,
                              loanInuseMaxPastDueOverBalance,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='left')
            del loanInuseMaxPastDueOverBalance
        # 正在使用贷款平均当前逾期金额占本金余额之比
        if inuseloan.shape[0] == 0:
            X_data['loaninuseavgpastdueamountoverbalance'] = 0
        else:
            loanInuseMeanPastDueOverBalance = inuseloan[
                ['CERTIFICATECODE', 'pastdueoverbalance']].groupby(
                    'CERTIFICATECODE').mean()
            loanInuseMeanPastDueOverBalance.columns = [
                'loaninuseavgpastdueamountoverbalance'
            ]
            X_data = pd.merge(X_data,
                              loanInuseMeanPastDueOverBalance,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='left')
            del loanInuseMeanPastDueOverBalance
        del inuseloan['pastdueoverbalance']
        # 正在使用贷款平均本金余额占贷款额度之比
        inuseloan['balanceoverlimit'] = inuseloan['BALANCE'] / inuseloan[
            'CREDITLIMIT']
        if inuseloan.shape[0] == 0:
            X_data['loaninuseavgbalanceoverlimit'] = 0
        else:
            loaninuseavgbalanceoverlimit = inuseloan[
                ['CERTIFICATECODE', 'balanceoverlimit']].groupby(
                    'CERTIFICATECODE').mean()
            loaninuseavgbalanceoverlimit.columns = [
                'loaninuseavgbalanceoverlimit'
            ]
            X_data = pd.merge(X_data,
                              loaninuseavgbalanceoverlimit,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='left')
            del loaninuseavgbalanceoverlimit
        # 正在使用贷款最大本金余额占贷款额度比
        if inuseloan.shape[0] == 0:
            X_data['loaninusemaxbalanceoverlimit'] = 0
        else:
            loaninusemaxbalanceoverlimit = inuseloan[
                ['CERTIFICATECODE', 'balanceoverlimit']].groupby(
                    'CERTIFICATECODE').max()
            loaninusemaxbalanceoverlimit.columns = [
                'loaninusemaxbalanceoverlimit'
            ]
            X_data = pd.merge(X_data,
                              loaninusemaxbalanceoverlimit,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='left')
            del loaninusemaxbalanceoverlimit
        del inuseloan['balanceoverlimit']
        # 正在使用贷款最大本月实际还款金额占本金余额比
        inuseloan['actualPayOverBalance'] = inuseloan[
            'ACTUALPAYAMOUNT'] / inuseloan['BALANCE']
        if inuseloan.shape[0] == 0:
            X_data['loaninusemaxactualpayamountoverbalance'] = 0
        else:
            loaninusemaxactualpayamountoverbalance = inuseloan[
                ['CERTIFICATECODE', 'actualPayOverBalance']].groupby(
                    'CERTIFICATECODE').max()
            loaninusemaxactualpayamountoverbalance.columns = [
                'loaninusemaxactualpayamountoverbalance'
            ]
            X_data = pd.merge(X_data,
                              loaninusemaxactualpayamountoverbalance,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='left')
            del loaninusemaxactualpayamountoverbalance
        # 正在使用贷款平均本月实际还款金额占本金余额比
        if inuseloan.shape[0] == 0:
            X_data['loaninuseavgactualpayamountoverbalance'] = 0
        else:
            loaninuseavgactualpayamountoverbalance = inuseloan[
                ['CERTIFICATECODE', 'actualPayOverBalance']].groupby(
                    'CERTIFICATECODE').mean()
            loaninuseavgactualpayamountoverbalance.columns = [
                'loaninuseavgactualpayamountoverbalance'
            ]
            X_data = pd.merge(X_data,
                              loaninuseavgactualpayamountoverbalance,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='left')
            del loaninuseavgactualpayamountoverbalance
        del inuseloan['actualPayOverBalance'], inuseloan
    return X_data


def calc_X_loancard24(data, X_data):
    if data.shape[0] == 0:
        X_data['type81month24lasttwocratio'] = 0
    else:
        # 贷记卡24月状态最后两位出现C的占比
        data['lasttwo'] = data['PAYSTAT24MONTH'].map(lastTwo)
        lasttwo = data[data['lasttwo'] > 0]
        lasttwo['lastC'] = lasttwo['PAYSTAT24MONTH'].map(lastC)
        lasttwoC = lasttwo[['CERTIFICATECODE', 'lastC']].groupby(
            'CERTIFICATECODE').sum()
        lasttwoC.columns = ['lastTwoC']
        lasttwoP = lasttwo[['CERTIFICATECODE', 'lastC']].groupby(
            'CERTIFICATECODE').count()
        lasttwoP.columns = ['lastTwoP']
        lasttwoAll = pd.merge(lasttwoC,
                              lasttwoP,
                              left_index=True,
                              right_index=True,
                              how='left')
        if lasttwoAll.shape[0] == 0:
            X_data['type81month24lasttwocratio'] = 0
        else:
            lasttwoAll['type81month24lasttwocratio'] = lasttwoAll[
                'lastTwoC'] / lasttwoAll['lastTwoP']
            type81month24lasttwocratio = lasttwoAll[
                ['type81month24lasttwocratio']]
            X_data = pd.merge(X_data,
                              type81month24lasttwocratio,
                              left_on='CERTIFICATECODE',
                              right_index=True,
                              how='left')
            del type81month24lasttwocratio
        del data['lasttwo'], lasttwo, lasttwoC, lasttwoP, lasttwoAll
    return X_data
