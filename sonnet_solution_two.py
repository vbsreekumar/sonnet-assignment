import pandas as pd
import numpy as np
import sonnet_helper as sh
import random

# Function for calculating Pearson correlation.
def co_rel(a,b):
    m = 594
    a_c = a.min() - m
    b_c = b.min() - m
    return np.sum(a_c * b_c) / np.sqrt(np.sum(a_c ** 2) * np.sum(b_c ** 2))

# Returns a list containing the recommendation relation between given sonnet and every other sonnet.
def recommend_sonnet_list(sn, M):
    s = M[sn]
    import numpy as np
    r = []
    for t in M.columns:
        if t == sn:
            continue
        corr = co_rel(M[sn], M[t])
        if np.isnan(corr):
            continue
        else:
            cs = ''
            if(corr == 1):
                cs = "recommended"
            else:
                cs = "not recommended"
            r.append((t, cs))
    r.sort(key=lambda tup: tup[1], reverse=True)
    return r

# Returns top 5 recommended sonnets in relation with the given sonnet.
def recommend_sonnets(sn, M , num):
    s = M[sn]
    import numpy as np
    r = []
    only_rec = []
    for t in M.columns:
        if t == sn:
            continue
        corr = co_rel(M[sn], M[t])
        if np.isnan(corr):
            continue
        else:
            cs = ''
            if(corr == 1):
                cs = "recommended"
                only_rec.append((t,cs))
            else:
                cs = "not recommended"
            r.append((t, cs))
    return random.sample(only_rec, 3)

def print_tuple(l):
    for i,j in l:
        print('%d : %s' % (i, j))

def print_singlet(l):
    for i,j in l:
        print('%d' % (i))

# Accessing csv file containing the data that can be used for calculating the correlation.
df = pd.read_csv('sonnet_csv.csv')
M = df.pivot_table(index=['sonnet_type'], columns=['sonnet_number'], values='sonnet_length')

recx = []
choice = int(input('1. Relation list of a sonnet\n2. Recommendations of sonnet'))
if choice==1:
    sn = int(input('Enter sonnet number'))
    le = recommend_sonnet_list(sn, M)
    print('--')
    print_tuple(le)
    print('--')
elif choice==2:
    sn = int(input('Enter sonnet number'))
    rr= recommend_sonnets(sn, M, 5)
    print('Top 5 recommendations are:')
    print_singlet(rr)
    print('--')
j = int(input('Select sonnet number from the list of recommedations to display'))
print('--')
print(sh.get_sonnet(j))
print('--')
