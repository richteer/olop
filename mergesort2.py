def p(arg):
	print(arg)
	return arg
try:
	(lambda ls, mergesort, merge: mergesort(ls,(0,len(ls)),mergesort,merge))(eval(input()), lambda ls, b, ms, m: b if b[1] - b[0] == 1 else m(ms(ls,p((b[0],(b[1]+b[0])//2)),ms,m),ms(ls,p(((b[1]+b[0])//2,b[1])),ms,m), b, ls, m), lambda l,r,b,n,m: b if p(n) and l[0] == l[1] or r[0] == r[1] else m((l[0]+1,l[1]),r,b,n[:l[0]] + [n[l[0]]] + n[l[0]+1:],m) if n[l[0]] < n[r[0]] else m((l[0]+1,l[1]+1),(r[0]+1,r[1]),b,n[:l[0]] + [n[r[0]]] + n[l[0]:l[1]] + n[r[0]+1:], m))
except Exception as e:
	print(e)
