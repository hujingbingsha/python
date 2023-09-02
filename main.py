# urllib爬取
from urllib import request
import re

# 封装请求对象
url_jiaoshou = 'https://sdmda.bupt.edu.cn/szdw/js.htm'
url_fujiaoshou = 'https://sdmda.bupt.edu.cn/szdw/fjs.htm'
url_jiangshi = 'https://sdmda.bupt.edu.cn/szdw/js1.htm'

import csv

#
# 创建csv文件
fn = '学院教师信息.csv'
with open(fn, 'a', newline='') as csvFile:
    csvWriter = csv.writer(csvFile)  # 建立writer对象
    csvWriter.writerow(["Department", "Name", "Title", "Photo"])


def title(url, m_chang, dtitle):
    # 创建二位数组
    n_kuan = 4
    l = 0
    mat = []
    while l < m_chang:
        r = 0
        line = []
        while r < n_kuan:
            line.append(0)
            r = r + 1
        mat.append(line)
        l = l + 1

    req = request.Request(url)
    # 爬取
    res = request.urlopen(req)
    # 获取相应内容
    html = res.read().decode('utf-8')
    # 解析结果 round_1
    pat_1 = '<span class="name">(.*?)</span>'
    dlist_1 = re.findall(pat_1, html)
    # 遍历
    j = 0
    for h in dlist_1:
        mat[j][1] = h
        j += 1
    # 解析结果 round_2
    pat = '<span class="iden">(.*?)</span>'
    dlist = re.findall(pat, html)
    # 遍历
    j = 0
    for h in dlist:
        mat[j][0] = h
        j += 1

    # 解析结果 round_4
    # 遍历
    j = 0
    for i in range(m_chang):
        mat[j][2] = dtitle
        j += 1
    # 解析结果 round_3
    pat = '<img src="(/__local/.*?\.jpg).*?alt="">'
    dlist = re.findall(pat, html)
    for i in range(m_chang):
        dlist[i] = "https://sdmda.bupt.edu.cn/" + dlist[i]

    # 遍历
    import os
    j = 0
    for h in dlist:
        filename = r'C:\Users\25815\PycharmProjects\pythonProject.jpg'
        request.urlretrieve(h, filename)
        newname = dlist_1[j] + ".jpg"
        os.rename(r'C:\Users\25815\PycharmProjects\pythonProject.jpg', newname)
        mat[j][3] = r"C:\Users\25815\PycharmProjects\pythonProject" + "\\" + dlist_1[j]
        j += 1

    # print(mat)

    import csv
    #
    # 创建csv文件
    fn = '学院教师信息.csv'
    with open(fn, 'a', newline='') as csvFile:
        csvWriter = csv.writer(csvFile)  # 建立writer对象
        for i in mat:
            csvWriter.writerow(i)


title(url_jiaoshou, 10, "教授")
title(url_fujiaoshou, 26, "副教授")
title(url_jiangshi, 19, "讲师")
