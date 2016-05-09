mylist = [0] *101
n = 1

while n <= 100:

    for i in range(1,101):
        if i % n == 0:
            mylist[i] = mylist[i] + 1

    n = n + 1

opened = [0]

for k in range(1,101):
    if mylist[k] % 2 ==1:
        opened.append(k)

print ("The following doors are open:", opened[1:])
