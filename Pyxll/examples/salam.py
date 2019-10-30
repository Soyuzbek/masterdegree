from pyxll import xl_func

@xl_func
def salam(name):
	return f'assalaamu aleykum, {name}'

@xl_func
def revfactorial(fact):
	result = 0
	while fact > 1:
		result +=1
		fact /= result
	return result-1
