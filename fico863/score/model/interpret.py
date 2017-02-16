import math
import calc_relate
import run_model

creditLimit = ['cloanavglimit', 'existype11', 'recent3loantotallimit',
               'recent6loantotallimit', 'recent9loantotallimit',
               'type71recentopenavgcreditlimit', 'LoanInUseTermsFreq7AvgLimit',
               'Type51InUseGuaranteeway9AvgLimit', 'LoanInUseAvgLimit',
               'LoanCurAmountPastDue180', 'Type51CurAmountPastDue',
               'Type81CurAmountPastDue']

recentBehavior = ['recent3loanno', 'recent6loanno', 'recent6type11loanno',
                  'recent6type12loanno', 'recent6type13loanno',
                  'recent6type21loanno', 'recent6type31loanno',
                  'recent6type41loanno', 'recent6type51loanno',
                  'recent6type99loanno', 'recent9loanno', 'type71recentopenno',
                  'type21recentpayno', 'type1113recentpayno',
                  'type41recentpayno', 'type99recentpayno', 'recent3type81no',
                  'recent6type81no', 'recent9type81no']

creditLength = ['recentloantime', 'recenttype81time', 'type81maxcreditlength',
                'type81avgcreditlength', 'type81mincreditlength',
                'type41maxcreditlength', 'type81longestlength',
                'otherloanavglength', 'loanavglength', 'loanlongestlength',
                'loaninuseavgterm', 'inuseloancreditduration']

accountNo = ['loanno', 'loaninuseguaranteeway4no', 'type81guaranteeway4no',
             'type81guaranteeway9no', 'guaranteeway2no', 'guaranteeway4no',
             'guaranteeway2ratio', 'guaranteeway4ratio',
             'inuseguaranteeway2no', 'inuseguaranteeway2ratio',
             'loaninusefreq8no', 'loaninusefreq7no', 'type81recentopenno',
             'type71loanrecentpayno', 'loan_balance_num', 'type81_balance_num',
             'type81cardno']

creditHistory = [
    'loanmonth24laststatnumno', 'loanmonth24curtermpastdue',
    'loanmonth24ncount', 'loanmonth24statcno', 'loanmonth24stat123no',
    'loanmonth24stat7no', 'loanmonth24nratio', 'type81month24curtermpastdue',
    'type81month24nratio', 'type81month24stat23no', 'type81stat24nratio',
    'type81ncount', 'type81statallno', 'type81statcno', 'type81stat123no',
    'type81stat7no', 'type71curtermpastdue', '51oneyearnratio', 'cloannratio',
    'type11nratio', 'type71oneyear23no', 'SpecMonthChange',
    'Type81InUseMaxBalanceOverLimit', 'Type81InUseAvgBalanceOverLimit',
    'LoanInUseMaxPastDueAmountOverBalance',
    'LoanInUseAvgPastDueAmountOverBalance', 'LoanInUseAvgBalanceOverLimit',
    'LoanInUseMaxBalanceOverLimit', 'LoanInUseMaxActualPayAmountOverBalance',
    'LoanInUseAvgActualPayAmountOverBalance', 'Type81Month24LastTwoCRatio'
]


def get_fd_interp(X_data_ori, X_data_new, loantype, M):
    ori_imp = run_model.getCoefImp(X_data_ori, loantype, M)
    new_imp = calc_relate.calc_X_coef(X_data_new, loantype)
    data = {}

    for fea_ori in ori_imp:
        data[fea_ori[0]] = (fea_ori[1], fea_ori[2], fea_ori[3])
    for fea_new in new_imp:
        data[fea_new[0]] = (fea_new[1], fea_new[2], fea_new[3])
    personid = X_data_ori.index[0]
    if personid != X_data_new.index[0]:
        raise TypeError('personid diff, ori_id : ' + str(personid) +
                        ', new_id : ' + str(X_data_new.index[0]))
    (creditLimitD, creditLimitRate) = get_d_interp(
        data, creditLimit, 'creditLimit', personid, loantype)
    (recentBehaviorD, recentBehaviorRate) = get_d_interp(
        data, recentBehavior, 'recentBehavior', personid, loantype)
    (creditLengthD, creditLengthRate) = get_d_interp(
        data, creditLength, 'creditLength', personid, loantype)
    (accountNoD, accountNoRate) = get_d_interp(data, accountNo, 'accountNo',
                                               personid, loantype)
    (creditHistoryD, creditHistoryRate) = get_d_interp(
        data, creditHistory, 'creditHistory', personid, loantype)
    dimen_interp = [(creditLimitD, creditLimitRate),
                    (recentBehaviorD, recentBehaviorRate),
                    (creditLengthD, creditLengthRate),
                    (accountNoD, accountNoRate),
                    (creditHistoryD, creditHistoryRate)]
    return dimen_interp


def get_d_interp(data, dimension, dimension_name, personid, loantype):
    weights = []
    score = 0.0
    not_in_dimension = []

    for fea in dimension:
        if fea.lower() in data:
            weights.append(data[fea.lower()][1])
            score += data[fea.lower()][0]
        else:
            not_in_dimension.append(fea)
    if len(dimension) != len(weights):
        raise TypeError('feature not in dimension! dimension name : ' +
                        dimension_name + ', \n' + 'not in dimension feature' +
                        str(not_in_dimension))
    variances = 0.0

    for weight in weights:
        variances += weight * weight
    std = math.sqrt(variances)

    if score <= -std:
        return (dimension_name, 'excellent')
    elif score > -std and score <= 0:
        return (dimension_name, 'good')
    elif score > 0 and score <= std:
        return (dimension_name, 'median')
    else:
        return (dimension_name, 'bad')
