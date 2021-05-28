n = int(input())
list1 = map(int, input().split())  #taking space seperated user input
t = tuple(list1)   #type cast as the lists are not hashable
print(hash(t))
