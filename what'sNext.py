while 1:
    st = str(raw_input())
    i = 0
    a = ''
    while st[i] != ' ':
    	a += st[i]
    	i += 1
    i += 1
    b = ''
    while st[i] != ' ':
    	b += st[i]
    	i += 1
    i += 1
    c = ''
    while i < len(st):
    	c += st[i]
    	i += 1
    a1 = int(a)
    a2 = int(b)
    a3 = int(c)
    if a1 == 0 and a2 == 0 and a3 ==0:
    	break
    if a1 - a2 == a2 - a3:
    	print("AP %s" % str(2 * a3 - a2))
    else:
    	print("GP %s" % str(a3 * a3 / a2)) 
