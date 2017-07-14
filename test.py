
# -*- coding: utf-8 -*-
#导入其他模块的符号集，Urllib 模块提供了读取web页面数据的接口，
#使我们可以像读取本地文件一样读取www和ftp上的数据
import urllib.request
import re
import html.parser as h 
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
#定义函数，urllib.urlopne()打开一个url地址，read()方法读取url上的数据，
#返回网页，即将页面下载下来
def getHtml(url):
    page = urllib.request.urlopen(url)
    #print(page.info())
    html = page.read()
    return html

#输出该网页内容
#print (html)

#获取图片
def getImg(html):
    reg = r'<img src=\"(.+?\.jpg)\">'
    imgre = re.compile(reg)
    #html=html.encode('utf-8')
    imglist = re.findall(imgre,html)
    print("the informations of images")
    print(imglist)
    x=0
    for imgre in imglist:
        urllib.request.urlretrieve(imgre,'%s.jpg'%x)
        x=x+1

def getAuthor(html):
	#作者姓名
    reau=r'<div id=\"gsc_prf_in\">(.*?)</div>'
    #author=re.compile(reau)  
    author_list=re.findall(reau,html,re.S|re.M)
    print('the name of author:')
    for content in author_list:
        print(content)

    #作者信息
    reau1=r'<div class=\"gsc_prf_il\">(.*?)</div>' 
    author_list=re.findall(reau1,html,re.S|re.M)
    #print("the author_list is:",author_list)
    print('the informations of author:')
    for content in author_list:
        if "href" not in content:
    	    print(content)
        else:
    	    print('the research direction of author:')
    	    reau3=r'<a href=.*?>(.*?)</a>'
    	    author_direction=re.findall(reau3,content,re.S|re.M)
    	    print(author_direction)
    	    #if content in author_direction:
    	        #print(content)
    	    #print(content)
    #print(author_list)
    reau2=r'<div class=\"gsc_prf_il\" id=\"gsc_prf_ivh\">(.*?)</div>'
    author_list=re.findall(reau2,html,re.S|re.M)
    print('the email of author:')
    for content in author_list:
    	print(content)

    #发表过的论文，论文信息存在html的table标签内,tr行td列
    res_tr=r'<tr class=\"gsc_a_tr\">(.*?)</tr>'#第一行
    m_tr=re.findall(res_tr,html,re.S|re.M)
    for line in m_tr:
        res_td=r'<td class=\"gsc_a_t\">(.*?)</td>'#第一列
        m_td=re.findall(res_td,line,re.S|re.M)
        for mm in m_td:
            if "href" in mm:#第一列内a标签
                restr = r'<a href=.*?>(.*?)</a>'
                h = re.findall(restr,mm,re.S|re.M)
                print("The name of the paper:")
                print(h),
            if "class" in mm:#第一列内div标签
                restr=r'<div class=\"gs_gray\">(.*?)</div>'
                h2=re.findall(restr,mm,re.S|re.M)
                print("author names,Magazine name and date of publication:")
                print(h2)

    #合作过的学者信息,信息在html的ul标签内
    res_ul=r'<ul class=\"gsc_rsb_a\">(.*?)</ul>'
    m_ul=re.findall(res_ul,html,re.S|re.M)
    for line in m_ul:
        if "href" in line:
            #print(line)
            restr=r'<a class=\"gsc_rsb_aa\" href=.*?>(.*?)</a>'
            h3=re.findall(restr,line,re.S|re.M)
            print("the name of cooperative scholars:")
            #h3=unicode(h3).encode("utf-8")
            print(h3)

    
    #页面内的url
    res_url = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
    link = re.findall(res_url, html, re.I|re.S|re.M)
    print('the url list:')
    for url in link:
        print (url)
        
url=["https://scholar.google.com/citations?user=hNTyptAAAAAJ&hl=en","https://scholar.google.com/citations?user=Jj00ksMAAAAJ&hl=en","https://scholar.google.com/citations?user=09kJn28AAAAJ&hl=en","https://scholar.google.com/citations?user=q92q8SMAAAAJ&hl=en"]
y=0
for u in url:
    #print(url[0])
    #print(url[1])
    html = getHtml(url[y])
    #print(html)
    html=html.decode('ISO-8859-1')#ISO-8859-1
    getAuthor(html)
    #getImg(html)
    y=y+1