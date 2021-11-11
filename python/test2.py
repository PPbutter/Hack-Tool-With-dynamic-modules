testdic = {}

c=0

m = ["ab","bc",'cd']

for i in m:
    testdic[i] = [f'{c}']
    c+=1


print(testdic)