#เกมผลรวม
from random import randrange
sum = int(randrange(10,100))
player = 0
while player<sum:
    number = int(input("เดาเลขจำนวนเต็มมา 1 อัลห์: "))
    player+=number
    print("ผลรวมตอนนี้คือ ", player)
    if player == sum:
        print("ชนะะะะะะ")
        break
    elif player > sum:
        print("เกิน ทายใหม่")
        player = 0
        continue