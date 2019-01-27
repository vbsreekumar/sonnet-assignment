l = []
with open('sonnet_dataset.txt') as input_data:
    for line in input_data:
        if line.strip() == '0':
            break
    for line in input_data:
        if line.strip() == '155':
            break
        l.append(line.strip())

while '' in l:
    l.remove('')
    
for i in range(len(l)):
    if l[i].isdigit():
        l[i] = int(l[i])
        
sonnet = {}
s= ''
for i in range(len(l)):
    z = i
    if type(l[z])==int:
        j = i
        while(type(l[j])==str):
            s=s+l[j]
            j=j+1
        sonnet[l[i]] = i
sonnet[155] = len(l)

s_d = {}
for i in range(1,155):
    s = ''
    a = sonnet[i]
    b = sonnet[i+1]
    for x in range(a+1, b):
        s+=l[x]
        s_d[i] = s
        
# Obtain the complete dataset in a dictionary format. key=sonnet number and value=sonnet
def get_dataset():
    return s_d

# Obtain the ith sonnet.
def get_sonnet(i):
    return s_d[i]