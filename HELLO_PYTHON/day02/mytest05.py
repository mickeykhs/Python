# 첫수를 넣으세요
# 끝수를 넣으세요
# 배수를 넣으세요

# 2에서 4까지 3의 배수의 합은 3입니다.
first = input("첫수를 넣으세요=>")
last = input("끝수를 넣으세요=>")
b = input("배수를 넣으세요=>")
firsti = int(first)
lasti = int(last)
bi = int(b)
sum = 0
c = range(firsti, lasti+1)
for i in c:
    if i%bi== 0:
        sum += i
print("{}에서 {}까지 {}의 배수의 합은 {} 입니다".format(firsti,lasti,bi,sum))