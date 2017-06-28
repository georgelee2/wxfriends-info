# -*- coding: utf-8 -*-

import itchat
from xlwt import *

f=Workbook(encoding='utf-8')
table =f.add_sheet('friends')

itchat.auto_login(enableCmdQR=True)

friends = itchat.get_friends(update=True)[0:]

labels = ['Sex', 'Province', 'City', 'NickName', 'Alias', 'RemarkName', 'Signature']
for i, j in enumerate(labels):
	str_exp = 'table.write(0,i,j)'
	exec(str_exp)

num = 0
for i in friends:
	user = friends[num]
	num = num + 1
	table.write(num,0,user['Sex'])
	table.write(num,1,user['Province'])
	table.write(num,2,user['City'])
	table.write(num,3,user['NickName'])
	table.write(num,4,user['Alias'])
	table.write(num,5,user['RemarkName'])
	table.write(num,6,user['Signature'])

f.save("friends.xls")
