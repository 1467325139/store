'''
    猜数字游戏：
        1.系统随机产生一个随机数字（0~1000）
        2.用户从键盘输入数字，与随机数字进行比对 （让用户循环输入20）
            若大了：温馨提示，大了
            若小了：温馨提示，小了
            猜中
        3.循环：一直到猜中为止，退出程序。
    技术分析：
    1.随机数
        random
    2.input
    3.判断
        if ...elif ...else
    4.循环
        while : 当型循环条件型循环
    5.退出程序
        break
    任务：
        加入初始化金币功能，猜错1次扣500金币。
        猜中直接奖励10000，询问是否继续第二轮随机数猜测。

        10次没猜中，系统直接锁定。
'''


import random
num = random.randint(0,1000)                    #随机生成的数字
count = 0                                       #输入的次数
gold = 5000                                      #初始金币5000
level = 1
while count <= 20:
    count = count + 1
    gold = gold - 500                           #每次游戏扣500个金币
    chose = input("请输入本次猜的数字：")          #玩家输入数字
    chose = int(chose)
# 判断
    if chose > num and gold >0:
        print("大了！大了！再小点！","你还有",gold,"个金币")
    elif chose < num and gold > 0:
        print("小了！小了！再大点！","你还有",gold,"个金币")
    elif chose == num:
        gold = gold + 10000
        print("恭喜通过第",level,"关，本关幸运数字为：",num,"，本次猜了",count,"次，奖励你10000个金币，你现在有",gold,"个金币")
        ask = int(input("是否继续游戏？输入1继续游戏，输入2游戏结束:"))
        if ask == 1:
            import random
            num = random.randint(0, 1000)
            level = level + 1
            count = 0
        else:
          break                               #循环结束
    else:
        print("你币没了，游戏结束! 正确数字为:",num)

