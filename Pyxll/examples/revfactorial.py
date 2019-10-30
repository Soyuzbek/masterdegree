from pyxll import xl_func

def recurs(num):
	if num == 1:
		return 1
	return num/recurs(num-1)


@xl_func
def revfactorial(fact):
	return recurs(num)
