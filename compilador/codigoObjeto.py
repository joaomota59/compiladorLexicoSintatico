from goto import with_goto
@with_goto
def main():
	_t1=5 > 3
	msm=not _t1
	print(msm)
	_t2=4%3
	_t3=55/2
	_t4=_t2+_t3
	_t5=_t4-55
	print(_t5,end='')
	_t6=4//3
	_t7=_t6%3
	_t8=_t7%4
	print(_t8)
	print("oi")
	_t9=-2
	print(_t9)
	_t10=+2
	print(_t10)
	_t11=4**2
	_t12=5+_t11
	_t13="oi"+"s"
	_t14=_t13+"joao"
	print(_t12,_t14)
	print(True,False)
	x=input()
	x=int(x)
	a=input()
	a=str(a)
	n=input()
	n=float(n)
main()
