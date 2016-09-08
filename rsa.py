import random

# Itself (nothing)
def c(c, a, b):
	return c(c,b,a%b) if a % b else True if b == 1 else False

# Nothing
def d(m,l):
	return l + [list(i if (l[-1]*i)%m != 1 else next(iter(())) for i in range(1,m))[-1] + 1]

# Needs c
def e(c, l):
	return l + [([16]+list(i if not c(c,i,l[2]) else next(iter(())) for i in range(17,(l[0]-1)*(l[1]-1))))[-1] + 1]

# Needs d and e
def key(l):
	return d((l[0]-1)*(l[1]-1),e((lambda c,a,b: c(c,b,a%b) if a % b else True if b == 1 else False), l + [l[0]*l[1]]))

# Needs getprime, k, randint, argv
def gen(r,b):
	return key([getprime(r(0, 2**(int(b)-1)),primecheck,int(b)) for i in range(2)])

# Needs randint, primecheck, argv
def getprime(r,p,b):
	return ([r-1] + list(i if not p(i) else next(iter(())) for i in range(r, 2**b)))[-1]+1

def primecheck(p):
	return True if len(list(i if p % i else next(iter(())) for i in range(2,(p//2) + 1))) == (p//2)-1 else False

print((lambda a, r, m: m.get(a[1])(r, *a[2:]) if a[1] in m.keys() else "")(__import__("sys").argv, __import__("random").randint, {"code":(lambda r,g,k,m: pow(int(g),int(k),int(m))), "gen":gen}))
