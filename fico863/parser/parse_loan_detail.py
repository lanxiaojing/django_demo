# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 09:48:28 2016

@author: hello
"""

# info=u'2014年04月16日商业银行“IC”发放的180,000元（人民币）个人住房贷款，业务号X，组合（含保证）担保，240期，按月归还，2034年04月16日到期。截至2016年01月16日，'
info = u'2009年08月19日商业银行“IC”发放的156,000元（人民币）个人住房公积金贷款，业务号X，其他担保，180期，按月归还。截至2014年08月04日，账户状态为“结清”。'
#info=u'1.	2005年10月20日“工商银行北京分行”发放的500,000元（美元折人民币）住房贷款，业务号001，抵押担保，180期，按月归还，2020年10月20日到期。已变成呆账，最近一次还款日期为2010年11月5日，余额为150,000元。 '
# card=u'2008年03月14日商业银行“EU”发放的贷记卡（人民币账户），业务号X，授信额度1元，共享授信额度1元，信用/免担保。截至2016年01月15日，'
# card=u'2008年03月01日商业银行“NF”发放的贷记卡（人民币账户），业务号X，授信额度10,000元，共享授信额度10,000元，信用/免担保，截至2009年04月25日，账户状态为“销户”。'
card = u'2009年05月09日商业银行“BI”发放的贷记卡（美元账户），业务号X，授信额度折合人民币2,333元，共享授信额度折合人民币0元，信用/免担保，截至2012年03月21日，账户状态为“未激活”。'


def parse_cards(de):
    infos = de.split(u'，')
    # print len(infos)
    dateopen = infos[0][infos[0].index(u'2'):infos[0].index(u'日')]
    dateopen = dateopen.replace(u'年', u'-')
    dateopen = dateopen.replace(u'月', u'-')
    # print dateopen
    financename = infos[0][infos[0].index(u'日') + 1:infos[0].index(u'发')]
    # print financename
    currencyname = infos[0][infos[0].index(u'（') + 1:infos[0].index(u'账')]
    currency = parse_currency(currencyname)
    # print currentname
    creditlimit = infos[2][infos[2].index(u'度') + 1:infos[2].index(u'元')]
    creditlimit = creditlimit.replace(',', '')
    if u'折合人民币' in creditlimit:
        creditlimit = creditlimit[creditlimit.index(u'币') + 1:]
    # print creditlimit
    shareamount = infos[3][infos[3].index(u'度') + 1:infos[3].index(u'元')]
    shareamount = shareamount.replace(',', '')
    if u'折合人民币' in shareamount:
        shareamount = shareamount[shareamount.index(u'币') + 1:]
    # print shareamount
    if de.endswith(u'，'):
        fields = infos[-2].split(u'。')
        # print fields[0],fields[1]
        (guaranteewayame, guaranteeway) = get_guarantee(fields[0])
        # print fields[1]

        statenddate = fields[1][fields[1].index(u'至') + 1:fields[1].index(
            u'日')]
        statenddate = statenddate.replace(u'年', u'-')
        statenddate = statenddate.replace(u'月', u'-')
    else:
        # print infos[4]
        (guaranteewayame, guaranteeway) = get_guarantee(infos[4])
        statenddate = infos[5][infos[5].index(u'至') + 1:infos[5].index(u'日')]
        statenddate = statenddate.replace(u'年', u'-')
        statenddate = statenddate.replace(u'月', u'-')
#    print guaranteewayame
#    print guaranteeway
#    print statenddate
    res = {}
    res[u'DATEOPENED'] = dateopen
    res[u'FINANCENAME'] = financename
    res[u'CURRENCYNAME'] = currencyname
    res[u'CURRENCY'] = currency
    res[u'CREDITLIMIT'] = creditlimit
    res[u'SHAREAMOUNT'] = shareamount
    res[u'GUARANTEEWAYNAME'] = guaranteewayame
    res[u'GUARANTEEWAY'] = guaranteeway
    res[u'STATENDDATE'] = statenddate
    if u'结清' in de or u'销户' in de:
        # print u'结清'
        res[u'STAT_FLAG'] = 2
        res[u'CLASS5STAT'] = u'1'
    elif u'未激活' in de:
        res[u'STAT_FLAG'] = 3
        res[u'CLASS5STAT'] = u'9'
    return res


def parse_currency(currencyname):
    if currencyname == u'人民币':
        return u'1'
    elif currencyname == u'美元':
        return u'2'
    elif currencyname == u'瑞士法郎':
        return u'3'
    elif currencyname == u'加拿大元':
        return u'4'
    elif currencyname == u'英镑':
        return u'5'
    elif currencyname == u'欧元':
        return u'6'
    elif currencyname == u'日元':
        return u'7'
    elif currencyname == u'澳大利亚元':
        return u'8'
    elif currencyname == u'港元':
        return u'9'
    else:
        return u'10'


def get_guarantee(strs):
    guaranteewayame = u''
    guaranteeway = u''
    if u'质押' in strs:
        guaranteewayame = u'质押'
        guaranteeway = u'1'
    elif u'抵押担保' == strs:
        guaranteewayame = u'抵押'
        guaranteeway = u'2'
    elif u'保证' == strs:
        guaranteewayame = u'抵押'
        guaranteeway = u'3'
    elif u'信用/免担保' in strs:
        guaranteewayame = u'信用/免担保'
        guaranteeway = u'4'
    elif u'组合（含保证）' in strs:
        guaranteewayame = u'组合（含保证）'
        guaranteeway = u'5'
    elif u'组合（不含保证）' in strs:
        guaranteewayame = u'组合（不含保证）'
        guaranteeway = u'6'
    elif u'农户联保' == strs:
        guaranteewayame = u'农户联保'
        guaranteeway = u'7'
    elif u'其他' in strs:
        guaranteewayame = u'其他'
        guaranteeway = u'9'
    return (guaranteewayame, guaranteeway)


def get_freq(strs):
    termsfreqname = u''
    termsfreq = u''
    if u'日' in strs:
        termsfreqname = u'日'
        termsfreq = u'1'
    elif u'周' in strs:
        termsfreqname = u'周'
        termsfreq = u'2'
    elif u'月' in strs:
        termsfreqname = u'月'
        termsfreq = u'3'
    elif u'季' in strs:
        termsfreqname = u'季'
        termsfreq = u'4'
    elif u'半年' in strs:
        termsfreqname = u'半年'
        termsfreq = u'5'
    elif u'按年归还' in strs:
        termsfreqname = u'年'
        termsfreq = u'6'
    elif u'不定期' in strs:
        termsfreqname = u'不定期'
        termsfreq = u'7'
    elif u'一次性' in strs:
        termsfreqname = u'一次性'
        termsfreq = u'8'
    elif u'其他' in strs:
        termsfreqname = u'其他'
        termsfreq = u'9'
    return (termsfreqname, termsfreq)


def parse_loan(de):
    infos = de.split(u'，')
    dateopen = infos[0][infos[0].index(u'2'):infos[0].index(u'日')]
    dateopen = dateopen.replace(u'年', u'-')
    dateopen = dateopen.replace(u'月', u'-')
    # print dateopen
    financename = infos[0][infos[0].index(u'日') + 1:infos[0].index(u'发')]
    # print financename
    creditlimit = infos[0][infos[0].index(u'的') + 1:infos[0].index(u'元')]
    creditlimit = creditlimit.replace(',', '')
    # print creditlimit
    currentname = infos[0][infos[0].index(u'（') + 1:infos[0].index(u'）')]
    # print currentname
    typename = info[info.index(u'）') + 1:info.index(u'，')]
    # print typename
    (guaranteewayame, guaranteeway) = get_guarantee(infos[2])
    # print guaranteewayame,guaranteeway
    monthduration = infos[3][:infos[3].index(u'期')]
    # print monthduration
    if de.endswith(u'，'):
        (termsfreqname, termsfreq) = get_freq(infos[4])
        dateclosed = infos[5][:infos[5].index(u'日')]
        dateclosed = dateclosed.replace(u'年', u'-')
        dateclosed = dateclosed.replace(u'月', u'-')
        fields = infos[-2].split(u'。')
        statenddate = fields[1][fields[1].index(u'至') + 1:fields[1].index(
            u'日')]
        statenddate = statenddate.replace(u'年', u'-')
        statenddate = statenddate.replace(u'月', u'-')
    else:
        fields = infos[-2].split(u'。')
        (termsfreqname, termsfreq) = get_freq(fields[0])
        statenddate = fields[1][fields[1].index(u'至') + 1:fields[1].index(
            u'日')]
        statenddate = statenddate.replace(u'年', u'-')
        statenddate = statenddate.replace(u'月', u'-')
        dateclosed = statenddate
#    print termsfreqname,termsfreq
#    print dateclosed
#    print statenddate

    res = {}
    res[u'DATEOPENED'] = dateopen
    res[u'FINANCENAME'] = financename
    res[u'CREDITLIMIT'] = creditlimit
    res[u'CURRENTNAME'] = currentname
    res[u'TYPENAME'] = typename
    res[u'GUARANTEEWAYNAME'] = guaranteewayame
    res[u'GUARANTEEWAY'] = guaranteeway
    res[u'MONTHDURATION'] = monthduration
    res[u'TERMSFREQNAME'] = termsfreqname
    res[u'TERMSFREQ'] = termsfreq
    res[u'STATENDDATE'] = statenddate
    res[u'DATECLOSED'] = dateclosed
    if u'结清' in de or u'销户' in de:
        res[u'STAT_FLAG'] = 2
        res[u'CLASS5STAT'] = u'1'
        # print u'结清'

    return res

# parse_loan(info)
# print '************'
# parse_cards(card)
