__Author__ = 'Shuai Xue'

import random,string
# 生成随机字符串
def RandString(length):
	CharPool = string.ascii_letters+string.digits
	return ''.join([random.choice(CharPool) for i in range(length)])

# 生成键值
def OrderNum(length, order):
	return '%04d' % order

# 生成邀请码
def InviCode(quantity, StrLen, OrdLen):
	HolChar = 'L'
	for index in range(quantity):
		tempString = ''
		yield RandString(StrLen)+HolChar+OrderNum(OrdLen, index)

for InvitationCode in InviCode(200, 15, 4):
	print (InvitationCode)