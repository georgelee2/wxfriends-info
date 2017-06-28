# -*- coding: utf-8 -*-

import itchat
from xlwt import *

f=Workbook(encoding='utf-8')
table =f.add_sheet('friends')

itchat.auto_login(enableCmdQR=True)

friends = itchat.get_friends(update=True)[0:]

num = 0
table.write(0,0,'Sex')
table.write(0,1,'Province')
table.write(0,2,'City')
table.write(0,3,'NickName')
table.write(0,4,'Alias')
table.write(0,5,'RemarkName')
table.write(0,6,'Signature')

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
