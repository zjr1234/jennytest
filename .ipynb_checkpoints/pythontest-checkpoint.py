# test.py

import sys  #引入模块
rslt=[]
rslt = sys.argv[0]
print (rslt[1])
output_string1=rslt[1][0][0]
output_string2=rslt[1][1][0]

def fun(output_string1,output_string2):
    list=[]
    list.append(output_string1)
    list.append(output_string2)
    return list
