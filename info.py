#coding=utf-8
import requests
#import time,random
import xlwt,xlrd
from xlutils.copy import copy
import re
def initRequest(url):
	headers = { 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Connection': 'keep-alive'
		}
	cookies = {}
	s = requests.Session()
	response = s.get(url, headers=headers, cookies = cookies)
	return response

url = ''
WITCH = 13290
id = WITCH
with xlrd.open_workbook('./student.xls') as oldWb:
			table = oldWb.sheets()[0]
			nrows = table.nrows
			newWb = copy(oldWb)
try:
	while id < 300000:
		response = initRequest(url.format(str(id)))
		content = response.text
		
		newWs = newWb.get_sheet(0)
		newWs.write(nrows + id - WITCH, 0, str(id))
	
		aim = re.findall('<small>(.*?)<', content, re.S)
		newWs.write(nrows + id - WITCH, 1, aim[0].replace(' ', ''))
	
		aim = re.findall('(.*?)<', content, re.S)
		newWs.write(nrows + id - WITCH, 2, "".join(aim))
	
		aim = re.findall('.(.*?)<', content, re.S)
		newWs.write(nrows + id - WITCH, 3, "".join(aim))
	
		aim = re.findall('.(.*?)<', content, re.S)
		newWs.write(nrows + id - WITCH, 4, "".join(aim))
	
		aim = re.findall('.(.*?)<', content, re.S)
		newWs.write(nrows + id - WITCH, 5, "".join(aim))
	
		aim = re.findall(':(.*?)"', content, re.S)
		newWs.write(nrows + id - WITCH, 6, "".join(aim))
	
		aim = re.findall('.(\d*?)<', content, re.S)
		newWs.write(nrows + id - WITCH, 7, "".join(aim))
		#time.sleep(0.1)
		print(id)
		id = id + 1
finally:
	newWb.save('./s.xls')
	print("save success")
