#Create an empty list
Li1=[]
print(Li1)
#Concatenate with [5,6,7,8]
Li2=[5,6,7,8]
#Li3=Li1+Li2
Li1.extend(Li2)
print(Li1)
#add 8,9,1,5,6,7,8,1 elements to that list
Li3=[8,9,1,5,6,7,8,1]
Li1.extend(Li3)
print(Li1)
#Find frequency of 8 (count)
Li4=Li1.count(8)
print(Li4)
#find sum (List) + min + Max
print(sum(Li1))
print(max(Li1))
print(min(Li1))
#find the mean and median of the list
print(sum(Li1)/len(Li1))
#remove duplicates from list and give output in the format of tuple
print(tuple(set(Li1)))
#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9) Concatenate both tuples and remove duplicates from tuple
t1=(1,4,5,6,7,8)
t2=(5,6,7,8,9)
print(tuple(set(t1+t2)))
#Find the common elements between two tuples
s1=set(t1)
s2=set(t2)
s3=s1.intersection(s2)
print(tuple(s3))
#Find the index value of 9 (after concatenation)
t3=t1+t2
print(t3.index(9))
#multiply above elements 3 times
print(t3 *3)
#Create two empty sets and update set1 with 7,8,9,1,2,3,4,5,0 and #update set2 with 4,5,6,0
s1={7,8,9,1,2,3,4,5,0}
s2={4,5,6,0}
s1.update(s1)
s2.update(s2)
print(s1)
print(s2)
#check whether set2 is subset of set1 or no and common elements or no?
print(s1.issubset(s2))
print(s1.isdisjoint(s2))
#remove 8 from set 1 and set 2 ==> and #discard 0 from set1 and set2
s1.remove(8)
s2.remove(8)
s1.discard(0)
s2.discard(0)
print(s1)
print(s2)
#create a dictionary
dict1={}
print(dict1)
dict1={1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
#print all keys in dictionary and convert it into tuple
print(tuple(dict1.keys()))
#Find the average of all numbers available under key "2"
dict2=dict1.keys()
list1=list(dict2)
avg_list=sum(list1)/len(list1)
print(avg_list)
#Extract "bobtn" and "arbeg" from above dictionary
list3=dict1[3]
bob_list=list3[0][0::2]
arb_list=list3[2][:1:-1]
print(bob_list)
print(arb_list)






