#Disjoint set

s1 = set([1,2,3,4])
s2 = set([5,6,7,8])
print(s1 & s2)

#Taking intersection will give empty set because there are no common elements

#Suppose we want to add an edge to the graph that will connect 4 and 8, 1 and 5 thus making it cyclic. We can find which set the elements are in 
#and perform a union on the set
s3 = s1 | s2

#We know there is a cycle in the graph when vertices belong to same set. 