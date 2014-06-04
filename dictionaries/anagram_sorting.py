"""
 take an input list of strings and 
 output as a list of lists grouped by anagrams

['art', 'tar', 'ant', 'tan', 'car'] -> [['ant', 'tan'], ['car'], ['art', 'tar']]
"""

def anagram_sort(l):
	out = []
	d = {}
	for string in l:
		new = sorted(string)
		new = ''.join(new)
		if d.get(new): 
			d[new].append(string)
		else: 
			d[new] = [string]
	for key in d.keys():
		out.append(d[key])
	return out

l = ['art', 'tar', 'ant', 'tan', 'car'] 
print anagram_sort(l)

