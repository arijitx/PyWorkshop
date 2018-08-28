# take the number of inputs
n = int(input())

#initalize db
db = {}

# iterate over n to get the inputs
for i in range(n):
	[name,passwd] = input().split(' ')
	if name in db:
		db[name].append(passwd)
	else:
		db[name] = [passwd]

# query
qn = int(input())

# iterate over queries
for i in range(qn):
	[name,passwd] = input().split(' ')
	if name in db:
		if passwd in db[name]:
			print('Accepted')
		else:
			print('Rejected')
	else:
		print('Rejected')

