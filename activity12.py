import getpass

username = 'user1'
password = 'araykopo23'

u = input('input Username ---> ')
p = getpass.getpass('input Password ---> ')

if username == u and p == password :
	print("ACCESS GRANTED")
else :
	print("ACCESS DENIED")
