import collections

input_list=[]
no_of_integer=[]
for x in range(int(input())):
    no_of_integer.append(int(input()))
    input_list.append(input())

input_length=len(input_list)

def checklist(data):
    data=collections.deque(data.split())
    datalength=len(data)
    ans="Yes"
    for i in range(datalength-1):
        if int(data[0])>=int(data[1]):
            data.popleft()
        elif int(data[-1])>=int(data[-2]):
            data.pop()
        else:
             ans="No"
             break
    return ans

for x in range(input_length):
    print(checklist(input_list[x]))
