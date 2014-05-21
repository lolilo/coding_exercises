a = [1,1,2,2,3,4,4,5,5,6,6]

def find_single(a):
	d = {}
	for i in a:
		if d.get(i):
			del d[i]
		else: 
			d[i] = True
	return d.keys()[0]

print find_single(a)
