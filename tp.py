def hash(string):
	q = ''
	p = 'gnflvo;mfnjk'
	r = 'xDtiEg3q!'
	q += p
	for i in string:
		q = q + i + 'a'	
	q += r
	return q

def dehash(q):
	sreing = ''
	p = 'gnflvo;mfnjk'
	r = 'xDtiEg3q!'
	q -= p
	for i in q:
		string += i - 'a'
	string -= r
	return string
	
pas = input("Enter password : ")
print(hash(pas))

print(dehash(hash(pas)))

