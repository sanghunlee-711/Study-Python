
#list = [1,2,3,4,6,7,822,234,33]
"""
for i in range(10):
    if i % 2 != 0:
        print(i)
        print(i)
        print(i)
        print(i)

for i in range(10):
    if i%2 == 0:
        continue #제외하는 경우를 첫번째에 처리해줌으로서 핵심이 되는 블록이 깊은 블록으로 가는것을 방지한다.
    print(i)
    print(i)
    print(i)
    print(i)

price =[100,20,30,50,20,20,20]

for i, pr in enumerate(price):
    if pr == 20:
        print("20dollar price is No {}".format(i+1))
        break


dic = {"key2":"value1"}

if "key1" in dic and dic["key1"] == "value1":
    print("key1 is exist and the value1")
else:
    print("nope")

"""

"""#공백을 두고 만드는 경우
n = int(input())
a = list(map(int, input().split()))
sum = 0 
for i in a:
    sum += i

print(sum)    
"""
#공백없이 값을 받을때는 굳이 split을 쓰지 않아도 되느군..
sum = 0
inp = int(input())
num = input()
for each in num:
    sum += int(each)
print(sum)

inp = input()

    if 