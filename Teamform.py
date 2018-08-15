# If the m value is more than half of total scores, take the highest elements directly 

def teamFormation(score, team, m):
    x = score
    res = 0
    if len(score) == team:
        res = sum(x)
    else:
        if (len(score) <= m*2):
            res = sum(sorted(score,reverse=True)[:team])
        else: 
            for i in range(0,team):
                y = x[:m]+x[-m:]
                mx = max(y)
                z = x.index(mx)
                res = res+mx
                if z < m:
                    del x[z]
                else:
                    z = x[::-1].index(mx)
                    del x[-(z+1)]
  
    return res;
