import random

dice = random.randint(1,6)
answer1 = int(input("민규주사위\n"))
answer2 = int(input("준우주사위\n"))
if dice == answer1:
    print("민규정답")
elif dice == answer2:
    print("준우정답")
else:
    print("오답")