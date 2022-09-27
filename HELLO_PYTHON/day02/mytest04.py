# 홀/짝을 입력하시오 홀
# 나: 홀
# 컴: 홀 0.5 보다 크면 홀 작으면 짝
# 결과 : 승리
from random import random
'''
player = input("홀/짝을 입력하시오=>")
print("나 :", player)

ran = random()
computer = random()
print(computer)
if computer > 0.5:
    print("컴: 홀")
else: 
    print("컴: 짝")
if (player == "홀" and computer>0.5) or (player=="짝" and computer<=0.5):
    print("결과 : 승리")
else:
    print("결과 : 패배")
'''
mine = input("홀/짝을 입력하시오=>")
com =""
result =""

rnd = random()
if rnd >0.5:
    com ="홀"
else:
    com ="짝"
if com == mine:
    result = "승리"
else:
    result = "패배"
print("mine",mine)
print("com",com)
print("result",result)