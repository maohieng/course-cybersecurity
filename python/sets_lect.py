set1 = {"green", "red", "blue", "red"} # Create a set
#print the set
print(set1)
#create a set from a list [7, 1, 2, 23, 2, 4, 5] and print
set2=set([7, 1, 2, 23, 2, 4, 5])
print('create a set from a list [7, 1, 2, 23, 2, 4, 5]:', set2)
print(type(set2))
#check red is in set 1 or not?
checkred="red" in set1
print('check red is in set1:', checkred)
#Check min,max,sum,len of set2
print('Min, Max, Len, Sum:', min(set2), max(set2), len(set2), sum(set2))
#union set1 with {"green", "yellow"} 
SetU={"green", "yellow"}
u= SetU | set1
print('Union 2 sets:',  u)

#Set difference of set1 and {"green", "yellow"} 
set3 = set1.difference({"green", "yellow"})
print('Difference using difference:', set3)
print('Difference using -:', set1 - {"green", "yellow"})
#Set intersection and exclusive of set1 and {"green", "yellow"} 
inter_set = set1 & SetU
print('Intersection &:', inter_set)
sym_set = set1 ^ SetU
print(sym_set)
#obtain a list from a set
ob_list = list(set1)
print(ob_list)
#compare set1 and {"green", "red", "blue"}
set4 = {"green", "red", "blue"}
print(set1 == set4)

#add "yellow" to set 1
set1.add("yellow")
print(set1)

#remove "blue" from set1
set1.remove("blue")
print(set1)