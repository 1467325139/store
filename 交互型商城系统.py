'''
    商城：
        1.初始化钱包余额
        2.推个空的购物车
        3.正常购物：
            输入商品的编号
            看是否有这个商品
                有：
                    看钱是否足够
                        够：
                            添加到购物车里
                            余额减去相对应的钱
                        不够：
                            温馨：穷鬼，别瞎弄！请买个其他商品
                没有：
                    买个其他商品，别瞎弄！
        4.打印购物小条
    任务：
        1.购物小条的商品重复打印问题
        2.  10张联想电脑 0.5，  20老干妈优惠券 0.1 ， 15 华为优惠券 0.6
            随机抽取一张优惠券，在结算的时候进行打折，进行结算。
'''
shop = [
    ["联想电脑",5000],
    ["苹果电脑",12000],
    ["华为手环",2000],
    ["机械革命",15000],
    ["老 干 妈",7.5],
    ["卫龙辣条",3],
    ["西   瓜",2]
]


# 1.空的购物车
mycart = []

#  2.初始化您的余额
money = input("请充值购物卡：")
money = int(money)
money_1 = money
# 随机抽取优惠券
import random
bond = random.randint(1,45)
if bond >=1 and bond <=10:
    print("恭喜获得联想电脑5折优惠券，购买时自动使用")
    price = 5000
    rebat = 0.5
    bout = 1
    num = 0
elif bond > 10 and bond <=30:
    print("恭喜获得:老干妈 1折优惠券，购买时自动使用")
    price = 7.5
    rebat = 0.1
    bout = 1
    num = 4
else:
    print("恭喜获得:华为手环 6折优惠券，购买时自动使用")
    price = 2000
    rebat = 0.6
    bout = 1
    num = 2

# 3.正常购物
i = 1
while i <= 20:
    # 展示商品
    for key, value in enumerate(shop):
        print(key, value)
    chose = input("请输入您想要的商品：")
    if chose.isdigit():
        chose = int(chose)
        if chose > len(shop): # len
            print("没有改号商品！请重新输入！")
        else:
            # 钱够不够
            if money > shop[chose][1]:
                mycart.append(shop[chose])
                #使用优惠券
                if chose == num and bout > 0 :
                    rebat_=(shop[chose][1]) * (1 - rebat)
                    bout = bout - 1
                    print("该商品已使用优惠券优惠了：",rebat_,"元")
                else:
                    rebat_ = 0
                money = money - (shop[chose][1]) + rebat_ # 减去价格
                print("恭喜，添加成功！您的余额还剩",money)
            else:
                print("穷鬼，钱不够了，别瞎弄！买其他商品吧！")
    elif chose == "q" or chose == "Q":
        print("结算中……")
        break  # 跳出循环
    else:
        print("对不起，您输入错误，别瞎弄！")

    i = i + 1

#消除重复项



print("以下是您的购物小条，请拿好！")
print("-------------------------------------")
print("编号     商品     单价     数量     合计")
#统计商品出现的次数
for h in range(len(shop)):
    sum = 0
    for key, value in enumerate(mycart):
        if value[1] == shop[h][1]:
            sum += 1
    if sum > 1:
        print(h,"\t",shop[h][0],"\t", shop[h][1],"\t", sum,"\t\t",((shop[h][1])*sum))
    if sum == 1:
        print(h,"\t", shop[h][0],"\t", shop[h][1],"\t",sum,"\t\t",((shop[h][1])*sum))


print("-------------------------------------")
if bout == 0:
 print("本次优惠券优惠：",(price*(1-rebat)),)
print("您本次消费：",(money_1 - money),"元")
print("您的余额还剩：",money,"元")
print("欢迎下次光临！")


































