# Jason Angell
# Therm & Stat
# 2/10/2015

from copy import deepcopy as dc

hist = []
def printos(arrayO):
    print '[',
    for i in range(len(arrayO)):
        for j in range(arrayO[i]):
            print '*',
        if arrayO[i] == 0:
            print ' ',
        if i < len(arrayO) - 1:
            print '|',
    print ']'
    hist.append(dc(arrayO))

def inhist(o):
    for l in range(len(hist)):
        if hist[l] == o:
            return 1
    return 0

def energytree(n, o):
    # n is energy, o is oscillators
    if n == 0:
        printos(o)
        return
    if n == 1:
        for i in range(len(o)):
            o[i] += 1
            if inhist(o) == 0:
                printos(o)
            o[i] -= 1
    else:
        for j in range(len(o)):
            o[j] += 1
            energytree(n - 1, o)
            o[j] -= 1

def runenergy(energy, size):
    a = []
    for n in range(size):
        a.append(0)
    energytree(energy, a)

# to run with arbitrary energy and oscillators:
# replace 1 with the energy and 3 with the number of oscillators you want
runenergy(2, 4) 