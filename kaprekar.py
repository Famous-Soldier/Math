#https://github.com/Famous-Soldier

def inf():
    i = 0
    while True:
        yield i
        i += 1

def chk(i):
	n=i**2 ; n=str(n)
	l=len(n)
	if l % 2 == 0:
		P1 = n[:len(n)//2]
		P2 = n[len(n)//2:]
		P1 = int(P1)
		P2 = int(P2)
		if P1 + P2 == i:
			return True
		else:
			return False




for i in inf():
    if chk(i) == True:
    	print('Found kaprekar :',i)
