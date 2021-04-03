from collections import deque
first = deque(list(map(int,input().split())))
second = deque(list(map(int,input().split())))
k=0
while (first and second) and k <(10**6):
    k+=1
    if (first[0]>second[0] and (first[0]!=9 and second[0]!=0)):
        first.append(first.popleft())
        first.append(second.popleft())
    else:
        second.append(first.popleft())
        second.append(second.popleft())
if not second :
    print("first",k)
elif not first:
    print("second",k)
else:
    print("botva")