#python programm to find size of a tuple
#import sys
#tup=('sar','kk','dv','rud')
#print("size "+ str(sys.getsizeof(tup)) + " bytes")
#_____________________________________________________________________________
#Python – Sum of tuple elements
#tup=(1,5,4,3)
#tup=list(tup)
#s=0

#for i in tup:
#    s= s+i
#print(s)



#by creating function
#def sumtup(tuple):
#    tuple=list(tuple)
#    s=0
#    for i in tuple:
#        s = s+i
#    return s
#tup=(5,4,5,6)
#print(sumtup(tup))
#___________________________________________________________________________________
#Python program to create a list of tuples from given list having number and its cube in each tuple
#list=[1,2,3,4,5,6]
#mt=[]

#for i in list:
#    tup=(i,i*i*i)
#    mt.append(tup)
#mt=tuple(mt)
#print(mt)
#________________________________________________________________________________
#Update each element in tuple list
#
#print(tup)
#change='sarthak'
#tup=list(tup)
#c=0
#for i in tup:
#    tup[c]=change
#    c += 1
#tup=tuple(tup)
#print(tup)
#_________________________________________________________________________________
#update a specific element in a tuple
#tup=('sar,0','dv,1','hr,2','khu,3')
#print(tup)
#change=int(input("enter element you wish to change:- "))
#wht_to_change=input("enter what you want to change:- ")
#tup=list(tup)
#for i in tup:
#    tup[change]=wht_to_change
#tup=tuple(tup)
#print(tup)
#__________________________________________________________________________
# Assigning Subsequent Rows to Matrix first row elements
list = [[5, 8, 9], [2, 0, 9], [5, 4, 2], [2, 3, 9]]




#a = list[0]
#b = list[1:len(list)]
#dic=dict()
#print(len(a))
#for i in range(0,3):
#    dic[a[i]]=b[i]
#print(dic)
#_____________________________________________________________________________
#Lambda with if and else in Python
#sq= lambda x: x*x if(x>0) else print("none")

#print(sq(-1))
#____________________________________________________________________________________
#Sorting string using order defined by another string
