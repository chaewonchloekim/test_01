import random


def baseball(array):

	array=[];

	for i in range(1,10):
		array.append(i)

	random.shuffle(array)

	print"=====start!====="
	b=[0,0,0]
	count=1
	for i in range(100):
		print"=====%2dth trial! cheer up! :) ===="  %count
		count = count + 1
		x=int(input("insert 3 number:"))
		if x ==0:
			break
		for i in range(3):
			b[2-i] = x%10
			x /=10
		print b

		ball=0;
		strike=0;
		for n in range(3):
			for m in range(3):
				if array[n] == b[m]:
					if n==m:
						strike = strike + 1
					else :
						ball = ball+1
		print "%d strike, %d ball!"%(strike,ball)
		if strike ==3:
			print "victory :) !!"
			break
		print "======game ended====="
return b
