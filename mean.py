def mean(num_list):
	try:
		f = sum(num_list)/len(num_list)
		if isinstance(f, complex):
			return NotImplemented
		else:
			return f
	except ZeroDivisionError :
		return 0
	except TypeError as detail :
		msg = "The algebraic mean of a non-numerical list is undefined. Please providea list of numbers."
		raise TypeError(detail.__str__() + "\n" + msg)