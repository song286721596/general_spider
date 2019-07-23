# -*-coding:utf-8-*-
#@Author: Songzq
#@Time: 2019年07月22日10时
#说明:
#总结:

#使用requests 库和 BeautifulSoup库中的bs4工具
import requests
from bs4 import BeautifulSoup
import xlwt  #保存成excel文件的所用到的
import time

#第七步:定义保存成Excel的函数
def saveExcelData(rankingItems):
    print("开始保存数据......")
    fileTime = time.strftime('%Y_%m_%d', time.localtime())
    fileName = 'China_CollegeRanking_' + fileTime + '.xls'
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('2019中国学校排行')
    college_slice = [rankingItems[i:i+14] for i in range(0,len(rankingItems),14)] #将rankingItems列表切割
    for i in range(int(len(rankingItems)/14)):
        for j in range(len(college_slice[0])):
        # 排行
            ranking = college_slice[i][j]
            sheet.write(i,j,ranking)
    book.save(fileName)


#第一步: 定义url，url为需要爬取的网站地址
url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"

#第二步:定义请求报文头
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

#第三步:获取这个网页的源代码，存放在html_data中
html_data = requests.get(url,headers=header)
html_data.encoding="utf-8" #在请求回来的html_data中发现是utf-8编码，所以这个地方设置成utf-8编码，解决乱码问题。
#print(html_data.text)     #自己测试使用，请求回来的数据是否有问题。

#第四步:生成一个Beautifulsoup对象
soup = BeautifulSoup(html_data.text, 'lxml')
'''补充一下知识： select选择器使用：
 通过类名查找soup.select('.sister')  
 通过 id 名查找 soup.select('#link1') 
 组合查找 组合查找即和写 class 文件时，标签名与类名、id名进行的组合原理是一样的，例如查找 p 标签中，id 等于 link1的内容，二者需要用空格分开soup.select('p #link1')
 直接子标签查找 soup.select("head > title")'''
 #排名
rankings = soup.select("tbody > tr.alt > td")

#第五步: 定义一个列表将rankings中的值存入
rank_info = []
#遍历rankings，将值存入rank_info中
for ranking in rankings:
    rank_info.append(ranking.get_text())

#第六步:调用保存成Excel函数
saveExcelData(rank_info)





