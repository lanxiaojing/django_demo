# -*- coding: utf-8 -*-
"""
Created on Wed Mar 09 11:09:56 2016

@author: hello
"""
import parse_loan_detail
import collections
import sys
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')


# 从文档构造beautifulsoup对象
def get_soup(parse_file):
    try:
        files = open(parse_file)

        doc = files.readlines()
        files.close()
    except Exception, e:
        print 'error...', e.args
        return False
    return BeautifulSoup(''.join(doc), 'lxml')


# 得到网页内容构造的BeautifulSoup对象
def parse_page(soup):
    tables = soup.find_all('table')
    results = collections.OrderedDict()
    count = 0
    for table in tables:  # 只解析顶层table
        if count == 1:
            res = parse_table1(table)
            results[u'报告基本信息'] = res
            # parse_table1(table)
        if count == 2:
            returns = parse_table2(table)
            results[u'报告内容'] = returns
        count += 1
        if count > 2:
            break
    return results

# 解析报告内容部分，第一个顶层table


def parse_table1(table):
    trs = table.select(".style1")
    # tr=trs[-1]
    #    infos=tr.get_text()
    #    infos=infos.strip()
    #    fields=infos.split('\n')
    #    res={}
    #    for field in fields:
    #        if field != '':
    #            #print field
    #            res[field[:field.index(':')]]=field[field.index(':'):]
    #    return res
    res = {}
    for tr in trs:
        field = tr.get_text().strip()
        res[field[:field.index(u':')]] = field[field.index(u':') + 1:]
        # print field[:field.index(u':')],'\t',field[field.index(u':')+1:]
    return res

# 解析第二个顶层table


def parse_table2(table):
    tbody = table.find('tbody', recursive=False)
    trs = tbody.find_all('tr', recursive=False)
    lens = len(trs)
    headers = [u'个人基本信息', u'信贷交易信息明细', u'查询记录']
    p_headers = [u'身份信息', u'配偶信息', u'居住信息', u'职业信息']
    credit = [u'贷款', u'贷记卡', u'准贷记卡']
    q_headers = [u'查询记录汇总', u'信贷审批查询记录明细']
    loans = []  # 存储所有贷款
    loancards = []  # 存储所有贷记卡
    creditcards = []  # 存储所有准贷记卡
    b_pre = u''  # 存储大块信息的表格名，作为后面解析的标注
    c_pre = u''  # 存储信贷表格名信息，作为后面解析的标注
    q_pre = u''  # 存储查询表格名信息，作为后面解析的标注
    h_info = u''  # 存储个人基本信息的表格名，作为后面解析的标注
    loan_tmp = collections.OrderedDict()  # 存储一条贷款信息
    loancard_tmp = collections.OrderedDict()  # 存储一条贷记卡信息
    creditcard_tmp = collections.OrderedDict()  # 存储一条准贷记卡信息
    return_back = collections.OrderedDict()
    basics = collections.OrderedDict()  # 记录所有个人基本信息
    for ind in range(lens):
        if ind == 0:  # 解析第二个顶层table中关于报告内容的说明
            tr = trs[0]
            res_b = parse_tr0(tr)
            return_back[u'报告说明'] = res_b
            # print res0
        else:  # 解析第二个顶层table中的其他内容
            tr = trs[ind]
            # 得到主要部分内容的表头，比如个人基本信息、信贷交易信息明细、查询记录
            if tr.has_attr('height') and int(tr['height']) == 40:
                info = tr.get_text().strip()
                info = info.replace(' ', '')
                info = info.replace('\n', '')
                h_info = info
                for header in headers:
                    if header in h_info and c_pre != u'':
                        c_pre = u''
                # print h_info
            else:
                if tr.find('table') == None and tr.get_text().strip(
                ) != '':  # 解析单独行
                    # pass
                    # print tr.get_text().strip()
                    if tr.get_text().strip() in p_headers:  # 个人基本信息
                        b_pre = tr.get_text().strip()
                    elif u'月' in tr.get_text().strip():  # 信贷交易记录的文字信息部分
                        detail_info = tr.get_text().strip()
                        detail_info = detail_info[detail_info.index(u'.') + 1:]
                        if c_pre == u'贷款':
                            loan_tmp[u'detail'] = detail_info
                            #                            print detail_info
                            #                            print detail_info[detail_info.index('.') + 1:]
                            ret = parse_loan_detail.parse_loan(detail_info)
                            # print len(ret)
                            for k, v in ret.items():
                                loan_tmp[k] = v
                                # print k,v
                        elif c_pre == u'贷记卡':
                            loancard_tmp[u'detail'] = detail_info
                            ret = parse_loan_detail.parse_cards(detail_info)
                            # print len(ret)
                            for k, v in ret.items():
                                loancard_tmp[k] = v
                                # print k,v
                        elif c_pre == u'准贷记卡':
                            creditcard_tmp[u'detail'] = detail_info
                            ret = parse_loan_detail.parse_cards(detail_info)
                            # print len(ret)
                            for k, v in ret.items():
                                creditcard_tmp[k] = v
                                # print k,v
                    elif u'）' in tr.get_text().strip():
                        # print tr.get_text().strip()
                        credit_label = tr.get_text().strip()
                        credit_label = credit_label[
                            credit_label.index('）') + 1:]

                        if credit_label in credit:  # 信贷明细，包括贷款、贷记卡、准贷记卡
                            c_pre = credit_label
                            # print c_pre
                    elif tr.get_text().strip() in q_headers:  # 查询
                        q_pre = tr.get_text().strip()
                        # print q_pre
                        # print tr.get_text().strip()

                elif tr.find('table') != None:  # 解析包含内容的table部分
                    if b_pre in p_headers:  # 个人基本信息
                        # 身份信息,配偶信息,居住信息,职业信息
                        basic = parse_btd_table(tr, b_pre)
                        basics[b_pre] = basic
                        # print b_pre,basic
                        b_pre = u''  # 解析完一部分内容将表格名置空
                    elif c_pre in credit:
                        # pass
                        if c_pre == u'贷款':
                            # print c_pre
                            loan_tmp = parse_ctd_table(tr, loan_tmp, c_pre)
                            loans.append(loan_tmp)
                            loan_tmp = collections.OrderedDict()
                            # print c_pre,loans
                        elif c_pre == u'贷记卡':
                            # print c_pre
                            #                            for k,v in loancard_tmp.items():
                            #                                print k,v
                            #                            print '^'*30
                            loancard_tmp = parse_ctd_table(tr, loancard_tmp,
                                                           c_pre)
                            loancards.append(loancard_tmp)
                            #                            for k,v in loancard_tmp.items():
                            #                                print k,v
                            #                            print '^'*30
                            loancard_tmp = collections.OrderedDict()
                            # print c_pre,loancards
                        elif c_pre == u'准贷记卡':
                            # print c_pre
                            creditcard_tmp = parse_ctd_table(
                                tr, creditcard_tmp, c_pre)
                            creditcards.append(creditcard_tmp)
                            creditcard_tmp = collections.OrderedDict()
                            # print c_pre,creditcards
                    elif q_pre in q_headers:
                        # print q_pre
                        if q_pre == u'查询记录汇总':
                            query_sum = parse_qstd_table(tr)
                            return_back[q_pre] = query_sum
                            q_pre = u''
                            # print query_sum
                        elif q_pre == u'信贷审批查询记录明细':
                            # print q_pre
                            query_d = parse_qdtd_table(tr)
                            return_back[q_pre] = query_d
                            q_pre = u''
                            # print query_d
                            # elif pre in
                            # print 'line'
                            # print tr.get_text().strip()
    return_back[u'basics'] = basics
    return_back[u'loans'] = loans
    return_back[u'loancards'] = loancards
    return_back[u'creditcards'] = creditcards
    return return_back
    # print res0


    # 解析查询具体内容
def parse_qdtd_table(tr):
    trs = tr.find_all('tr')
    res = collections.OrderedDict()
    tmp = []
    flag = True
    for tri in trs:
        tds = tri.find_all('td')
        count = 0
        for td in tds:
            # 得到表头
            if td.has_attr('style') == False:
                if count < len(tmp) and flag:
                    tmp = []
                    flag = False
                # print td.get_text().strip()
                tmp.append(td.get_text().strip())
                # print tmp
                # 得到表头对应的值
            else:
                # print tmp
                if tmp[count] in res:
                    res[tmp[count]].append(td.get_text().strip())
                else:
                    res[tmp[count]] = [td.get_text().strip()]
            count += 1
        # print '&'*20
    return res

# 解析查询汇总部分网页内容


def parse_qstd_table(tr):
    trs = tr.find_all('tr')
    tds_t = trs[0].find_all('td')  # 顶层表头
    s_arr = []
    for td in tds_t:
        s_arr.append(td.get_text().strip())
    tds_td = trs[1].find_all('td')  # 具体表头
    sd_arr = []
    for td in tds_td:
        sd_arr.append(td.get_text().strip())
    tds_c = trs[2].find_all('td')  # 表格内容
    c_arr = []
    for td in tds_c:
        c_arr.append(td.get_text().strip())
    # print '*'*20
    res = collections.OrderedDict()

    res_tmp_t = collections.OrderedDict()
    res_tmp_t[sd_arr[0]] = c_arr[0]
    res_tmp_t[sd_arr[1]] = c_arr[1]
    res[s_arr[0]] = res_tmp_t

    res_tmp_td = collections.OrderedDict()
    res_tmp_td[sd_arr[2]] = c_arr[2]
    res_tmp_td[sd_arr[3]] = c_arr[3]
    res_tmp_td[sd_arr[4]] = c_arr[4]
    res[s_arr[1]] = res_tmp_td

    res_tmp_c = collections.OrderedDict()
    res_tmp_c[sd_arr[5]] = c_arr[5]
    res_tmp_c[sd_arr[6]] = c_arr[6]
    res_tmp_c[sd_arr[7]] = c_arr[7]
    res[s_arr[2]] = res_tmp_c
    return res

# 解析信贷表,具体为贷款表、贷记卡表、准贷记卡表


def parse_ctd_table(tr, dic, pre):
    trs = tr.find_all('tr')
    tmp = []
    # flag=True
    # bit=False
    status24 = [u'/', u'*', u'#', u'N', u'1', u'2', u'3', u'4', u'5', u'6',
                u'7', u'C', u'G', u'D', u'Z']
    for tri in trs:
        #        print tri.get_text().strip()
        #        print '*'*20
        tds = tri.find_all('td')
        count = 0
        #        if len(tds)==6:
        #            #print tri.get_text().strip()
        #            #bit=True
        #            print '*'*30
        #            print tri.get_text().strip()
        #            print '*'*30
        for td in tds:
            # 得到表头内容
            if pre == u'贷款':
                if td.has_attr('align') or td.find('strong') or td.find('b'):
                    # print tri.get_text().strip()
                    if count < len(tmp):
                        tmp = []
                        # flag=False
                        # print td.get_text().strip()
                    tmp.append(td.get_text().strip())
                else:
                    #                    print 'count',count
                    #                    print 'tmp',tmps
                    if len(tmp) == 1 and count > 0:
                        dic[tmp[0]].append(td.get_text().strip())
                    elif tmp[count] in dic:
                        dic[tmp[count]].append(td.get_text().strip())
                    else:
                        dic[tmp[count]] = [td.get_text().strip()]

#                    if len(dic[tmp[0]]) == 24:
#                        print dic[tmp[0]]
            elif (td.has_attr('style') == False and
                  td.get_text().strip() not in status24) or (
                      td.has_attr('style') and 'word-break:break-all' not in
                      td['style'] and td.get_text().strip() not in
                      status24) or td.find('br') or td.find('bt'):
                if count < len(tmp):  # and flag
                    tmp = []
                    # flag=False
                    # print td.get_text().strip()
                tmp.append(td.get_text().strip())
#                if bit:
#                    print 1,tmp
#                    bit=False
# print tmp
# 得到表头对应的值
            else:
                #                if bit:
                #                    print 2,tmp
                #                    bit=False
                # print count
                # print tmp
                if len(tmp) == 1 and count > 0:
                    dic[tmp[0]].append(td.get_text().strip())
                elif tmp[count] in dic:
                    dic[tmp[count]].append(td.get_text().strip())
                else:
                    dic[tmp[count]] = [td.get_text().strip()]
#                print len(dic[tmp[0]])
#                if len(dic[tmp[0]]) == 24:
#                        print dic[tmp[0]]
# print count
            count += 1
        # print '&'*20
    return dic

# 解析基本信息表  ，身份信息,配偶信息,居住信息,职业信息


def parse_btd_table(tr, pre):
    trs = tr.find_all('tr')
    res = collections.OrderedDict()
    tmp = []
    flag = True
    for tri in trs:
        tds = tri.find_all('td')
        count = 0
        for td in tds:
            # 得到表头
            if td.has_attr('style') == False:
                if count < len(tmp) and flag:
                    tmp = []
                    flag = False
                # print td.get_text().strip()
                tmp.append(td.get_text().strip())
                # print tmp
                # 得到表头对应的值
            else:
                # print tmp
                if tmp[count] in res:
                    if pre == u'职业信息' and tmp[count] == u'编号':
                        pass
                    else:
                        res[tmp[count]].append(td.get_text().strip())
                else:
                    res[tmp[count]] = [td.get_text().strip()]
            count += 1
        # print '&'*20
    return res


# 解析第二个顶层table中关于报告内容的说明
def parse_tr0(tr):
    fonts = tr.find_all('font')
    report_info = []
    count = 0
    for font in fonts:
        count += 1
        if font.string.strip() != '':
            if font.string.strip() not in report_info:
                # print font.string.strip()
                report_info.append(font.string.strip())
    res = {}
    for i in range(5):
        res[report_info[i]] = report_info[i + 5]
    # print res
    return res

# soup=get_soup('F:/projects/yanghang/sub_model/call_back/html_return/092044000_558.html')
# soup=get_soup('F:/projects/yanghang/sub_model/call_back/html_return/091618171_541.html')
# soup = get_soup('/Users/zhongyid/projects/fico863/091618171_541.html')
# soup=get_soup('F:/projects/yanghang/sub_model/call_back/html_return/091708703_544.html')
# soup=get_soup('F:/projects/yanghang/sub_model/call_back/html_return/092345828_560.html')

# res = parse_page(soup)
# print res
