def CGPAcalc(d,semester_name):
    def flt(semester_name):
        t = semester_name.split('-')
        if t[2] == 'M':
            t[0] += ".05"
        elif t[2] == 'W':
            t[0] += ".1"
        elif t[2] == 'S':
            t[0] += ".00"
        return float(t[0])
    def numb(j):
        if j == 'A+' or j == 'A':
            p = 10
        elif j == 'A-':
            p = 9
        elif j == 'B':
            p = 8
        elif j == 'B-':
            p = 7
        elif j == 'C':
            p = 6
        elif j == 'C-':
            p = 5
        elif j == 'D':
            p = 4
        else:
            p = 0
        return p
    c = []
    for i in d.keys():
        for j in range(len(d[i])):
            if d[i][j][0] not in c:
                c.append(d[i][j][0])
    e = []
    v = []
    b = []
    for j in range(len(c)):
    
        for k in d.keys():
            for o in range(len(d[k])):
                if c[j] == d[k][o][0]:
                    e.append([k, d[k][o][1]])
                    print(e)
        for i in range(len(e)):
            t = e[i][0].split('-')
            if t[2] == 'M':
                t[0] += ".05"
            elif t[2] == 'W':
                t[0] += ".1"
            elif t[2] == 'S':
                t[0] += ".00"
            if flt(semester_name)>=float(t[0]):
                v.append([float(t[0]), e[i][1]])
        g = max(v)
        m = g[1]
        b.append(numb(m))
        e.clear()
        v.clear()
    s=0
    for q in b:
        s+=q
    cgpa=s/len(b)
    return cgpa
semester_name = input()
print(CGPAcalc({'2021-22-M' : (('CS102','F'), ('CS201', 'F'), ('CS101', 'F'), ('CS104','A')), '2021-22-W' : (('CS102', 'B'), ('CS201', 'D'), ('CS101', 'D')),
          '2022-23-M' : (('CS201', 'C'), ('CS101', 'A+'))},semester_name))