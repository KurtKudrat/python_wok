#password_management.py is a password locker program .

import sys, pyperclip


passwords ={'email':'dfjdfhhej',
			'blog':'fhhkd23484',
			'massage':'kjkjduh87&'}


if len(sys.argv) < 2:
		print('Usage: py pw.py [account] - copy account password')
		sys.exit
account = sys.argv[1]
print(account)


if account in passwords:
	pyperclip.copy(passwords[account])
	print ('password for '+account+ 'copied to clipbord')
else:
	print ('There is no Account called '+account)