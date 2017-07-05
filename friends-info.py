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
	for j, k in enumerate(labels):
		str_exp = 'table.write(num,j,user[k])'
		exec(str_exp)

f.save("friends.xls")
