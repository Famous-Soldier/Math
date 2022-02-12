#https://github.com/Famous-Soldier

def inf():
    i = 0
    while True:
        yield i
        i += 1

def chk(i):
	tmp=0
	if i > 10:
		for x in str(i):
			tmp+=int(x)
		if (i % tmp) == 0:
			return True
		else:
			return False

for i in inf():
	if chk(i) == True:
		print('Found harshad :',i)