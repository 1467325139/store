'''
生产消费模型
需求：
厨师：3个厨师制作面包，篮子容量500个，当篮子满时，等待2秒钟，然后继续判断是否已满若没有满，继续制作一个
顾客：有6个顾客购买面包，每个顾客有3000元，每个面包2.5元，每个顾客每次买一个面包。当篮子面包不够，等待3秒继续购买，直到钱不够为止。
'''


from threading import Thread
import time

bread = 0
price = 2.5

#厨师类
class Meker(Thread):
    maker = ""
    # 制作面包
    def run(self) -> None:
        make = 0
        global bread

        while True:
            if bread < 499:
                bread = bread + 1
                make = make + 1
            elif bread == 499:
                time.sleep(2)
                bread = bread + 1
                make = make + 1
            else:
                print(self.maker, "制作了", make,"个面包")
                break


#顾客类
class Buy(Thread):
    buyneme = ""
    #购买
    def run(self) -> None:
        money = 3000
        shop = 0
        global bread,price
        while True:
            if money >= price:
                if bread == 0:
                    time.sleep(3)
                    bread = bread - 1
                    money = money - price
                    shop = shop + 1
                elif bread > 0:
                    bread = bread - 1
                    money = money - price
                    shop = shop + 1
            else:
                print(self.buyneme,"购买了",shop,"个面包，还剩",money,"元")
                break


m1 = Meker()
m2 = Meker()
m3 = Meker()
b1 = Buy()
b2 = Buy()
b3 = Buy()
b4 = Buy()
b5 = Buy()
b6 = Buy()

m1.maker = "1号厨师"
m2.maker = "2号厨师"
m3.maker = "3号厨师"
b1.buyneme = "1号顾客"
b2.buyneme = "2号顾客"
b3.buyneme = "3号顾客"
b4.buyneme = "4号顾客"
b5.buyneme = "5号顾客"
b6.buyneme = "6号顾客"


m1.start()
m2.start()
m3.start()

b1.start()
b2.start()
b3.start()
b4.start()
b5.start()
b6.start()









