country = input('請輸入你的國家:')
age = int(input('請輸入你的年齡:'))
if country == '中國':
	if age >=18:
		print('可以考駕照')
	else:
		print('no!')
elif country == '英國':
     if age >= 17:
     	print('可以考駕照')
     else:
     	print('No!')
		