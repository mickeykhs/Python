# 출력원하는 단수를 입력하세요  5
# 5*1 = 5
# 5*2 = 10

a = input("출력원하는 단수를 입력하세요=> ")
aa = int(a)

for i in range(1, 10):
    print("{} * {} = {}".format(aa,i,aa*i))