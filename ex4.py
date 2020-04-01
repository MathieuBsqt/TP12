def listSum(liste):
    if len(liste)==0:
        return 0
    else:
        print(liste[0:len(liste)-2])
        print(liste[len(liste)-1])
        return listSum(liste[0:len(liste)-1])+liste[len(liste)-1]



print(listSum([])) # 0
print(listSum([42])) # 42
print(listSum([3,1,5,2])) # 11
