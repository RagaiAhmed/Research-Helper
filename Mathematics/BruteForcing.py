"""
Some old code I can't remember what it does
MAJOR ADVICE: ALWAYS COMMENT YOUR CODE EVEN IF IT WAS A QUICK TEST
"""

params = [[2,8,9,80],
[3,7,8,83],
[4,6,7,106],
[5,3,4,137]]
from itertools import permutations
from math import prod

def gen_terms(params,depth=1):
    terms= []
    for i in range(depth):
        terms.extend(prod(x) for x in(permutations(params,i+1)))
    return terms

def apply_coeff(terms,coeff):
    res= []
    for index,val in enumerate(terms):
        res.append(val*coeff[index])
    return res

def gen_coeff(lim,num):
    if num ==0:
        yield []
    else:
        for i in gen_coeff(lim,num-1):
            for j in range(-lim,lim+1):
                yield i+[j]


def print_rule():
    for x in params:
        a,b,c,res = x
        print("b+c*({})+d*({})+e*({}) = {}".format(a*a*a,a*a*a*a,a*a*a*a,res))
        print(",")

print_rule()

if __name__ == "__main__":
    founds = []
    depth = 3
    rng = 2
    pars = [(gen_terms(p[:-1],depth),p[-1] )for p in params]
    coeff = gen_coeff(rng,len(pars[0][0]))
    for c in coeff:
        state = True
        diff=None
        for p in pars:
            res = apply_coeff(p[0],c)
            sm = sum(res)
            if diff is None:
                diff = p[1] - sm
            sm +=diff
            state &=sm==p[1]
            if(not state): break
        if(state):
            print("LOLLLL !!")
            print("FOUND IT XD !!")
            founds.append(c)

    print(founds)
