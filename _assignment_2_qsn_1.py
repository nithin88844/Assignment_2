# Q. Write a python program to get a list, sorted in increasing order by the last element in each tuple 
#    from a given list of non-empty tuples.

t = list(tuple(map(int,input().split())) for r in range(int(input('enter no of rows : '))))  

def last(n):
	return n[-1]

def sort(tuples):
	return sorted(tuples, key=last)

a=t
print("Sorted:")
print(sort(a))
