# 구구단을 짜시오 9,8,6,5순으로
def showDan(dan):
    for i in range(1, 9+1):
        print("{} * {} = {}".format(dan,i,i*dan))

showDan(9)
showDan(8)
showDan(6)
showDan(5)
