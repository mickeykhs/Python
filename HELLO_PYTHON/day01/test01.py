# 1~100까지의 정수중 3의 배수의 합을 구하시오.
a = list(range(1,101))
total = 0
for i in a:
    if i % 3 == 0:
        total += i
print("total", total)

# for i in range(1,101):
#    print(i);
