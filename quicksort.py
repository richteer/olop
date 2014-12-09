(lambda ls, qs: qs(ls, qs))([7,2,6,4,5,1,2], lambda ls, qs: ls if len(ls) == 1 or len(ls) == 0 else qs([i for i in ls[1:] if i < ls[0]], qs) + [ls[0]] + qs([i for i in ls[1:] if i >= ls[0]], qs))
