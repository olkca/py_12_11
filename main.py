import random

mylist = []

for i in range(0, 10):
    x = random.randint(-10, 10)
    mylist.append(x)

print(mylist)
a = max(mylist)
print(a)

s = min(mylist)
print(s)
pos_count, neg_count, zer = 0, 0, 0
num = 0

while (num < len(mylist)):
    if mylist[num] >= 0:
        pos_count += 1
    elif mylist[num] == 0:
        zer += 1
    else:
        neg_count += 1
    num += 1
print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", neg_count)
print("zero numbers in the list: ", zer)
