#准备数据
IC_bank = {
    3:{"username":"2",
       "password":"2",
       "country":"2",
       "province":"2",
       "street":"2",
       "door":"2",
       "money":1000,
       "bank_name":"中国工商银行回龙观支行"}
}
bank_name = "中国工商银行回龙观支行"
import random,datetime
now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 转账手续费
msg_info = '''\033[1;31;5m
******************************************************************************************************
                            今日银行消息：
                        【今日银行转账手续费通知：】
                        1.转账2000元以下。    异地同行或跨行转账手续费是ATM转账是1.6元/笔.
                        2.转账2000-5000元。   异地同行或跨行转账手续费是ATM转账是4元/笔.
                        3.转账5000-10000元。  异地同行或跨行转账手续费是ATM转账是8元/笔
                        4.转账10000-50000元。 异地同行或跨行转账手续费是ATM转账是12元/笔。
                        5.转账50000元以上。   异地同行或跨行转账手续费是ATM转账金额的0.03%，最高50元。
******************************************************************************************************
\033[0m
'''

# 跨行转账费计算
def cost(movemoney):
    if movemoney <= 2000:
        return 1.6
    elif movemoney > 2000 and movemoney <= 5000:
        return 4
    elif movemoney > 5000 and movemoney <=10000:
        return 8
    elif movemoney > 10000 and movemoney <= 50000:
        return 12
    else:
        return movemoney*0.3




# 判断银行数据库是否已满
def bank_adduser(username,password,country,province,street,door,type,money,account):
    # 是否已满
    if len(IC_bank) >= 100:
        return 3
    # 是否存在
    if account in IC_bank:
        return 2
    # 正常开户
    IC_bank[account] = {
        "username":username,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":money,
        "type":type,
        "bank_name":bank_name
    }
    return 1


#  1、开户
def adduser():
    username = input("请输入用户名：")
    password = input("请输入密码：")
    country = input("亲输入国籍：")
    province = input("请输入省份：")
    street = input("请输入街道：")
    door = input("请输入门牌号：")
    type = random.randint(1,3)
    money = int(input("亲初始化您的开卡余额："))
    account = random.randint(10000000,99999999)
    status = bank_adduser(username,password,country,province,street,door,type,money,account)
    if status == 3:
        print("对不起，银行库已满，请携带证件到其他银行办理！")
    if status == 2:
        print("对不起，您已开过户！请不要重复开户！")
    if status == 1:
        print("恭喜，开户成功！以下是您的开户信息：")
        info = '''
        -----------------------------
                个人信息
            账号：%s
            用户名：%s
            密码：*****
            地址：
                国籍：%s
                省份：%s
                街道：%s
                门牌号：%s
            余额：%s
            开户行名称：%s
            开户日期：%s
        -------------------------------
        '''
        print(info % (account,username,country,province,street,door,money,bank_name,now_time))

#  2、存钱
def depositmoney():
    account = int(input("请输入账号："))
    if account in IC_bank:
        deposit = int(input("请输入存款金额："))
        IC_bank[account]["money"] += deposit
        print("存款成功，以下是您的存款凭证")
        info = '''
        -----------------------------
                  存款凭证
            账号：%s
            存款金额：%s
            账户余额：%s
            开户行名称：%s
            存款日期：%s
        -------------------------------
        '''
        print(info  % (account,deposit,IC_bank[account]["money"],bank_name,now_time))
        return True
    else:
        print("账号不存在")

# 3、取钱
def takemoney():
    account = int(input("请输入账号："))
    password = input("请输入密码：")
    if account in IC_bank:
        if password == IC_bank[account]["password"]:
            retrieve = int(input("请输入取钱金额："))
            if retrieve <= IC_bank[account]["money"]:
                IC_bank[account]["money"] -= retrieve
                print("取款成功,以下是您的取款凭证")
                info = '''
                        -----------------------------
                                  取款凭证
                            账号：%s
                            取款金额：%s
                            账户余额：%s
                            开户行名称：%s
                            取款日期：%s
                        -------------------------------
                        '''
                print(info % (account,retrieve, IC_bank[account]["money"], bank_name,now_time))
            else:
                print("钱不够")
                return 3
        else:
            print("密码不对")
            return 2
    else:
        print("账号不存在")
        return 1

# 4.1 转账
def transfermoney():
    account_1 = int(input("请输入账号："))
    password = input("请输入密码：")
    if account_1 in IC_bank:
        if password == IC_bank[account_1]["password"]:
            account_2 = int(input("请输入要转账的账号："))
            if account_2 in IC_bank:
                movemoney = int(input("请输入转账金额："))
                if movemoney <= IC_bank[account_1]["money"]:
                    IC_bank[account_1]["money"] -= movemoney
                    IC_bank[account_2]["money"] += movemoney
                    print("转账成功,")
                    info = '''
                            -----------------------------
                                       转账凭证
                             转出账号：%s
                             转入账号：%s
                             转账金额：%s
                             转出账户余额：%s
                             开户行名称：%s
                             转账日期：%s
                             -------------------------------
                            '''
                    print(info % (account_1,account_2,movemoney,IC_bank[account_1]["money"], bank_name,now_time))
                    return 0
                else:
                    print("钱不够")
                    return 3
            else:
                print("账号不存在")
                return 1
        else:
            print("密码输入错误")
            return 2
    else:
        print("账号输入错误")
        return 1


# 4.2 跨行转账
def step_bank_transfermoney():
    account_1 = int(input("请输入转出账户："))
    account_2 = int(input("请输入转入账户："))
    from AGRICULTURAL_BANK import bank
    if account_1 in IC_bank and account_2 in IC_bank:
        transfermoney()
    elif account_1 in IC_bank and account_2 in bank:
        password = input("请输入转出账户密码：")
        if password == IC_bank[account_1]["password"]:
            movemoney = int(input("请输入转出金额："))
            n = cost(movemoney)
            if movemoney <= int(IC_bank[account_1]["money"]):
                IC_bank[account_1]["money"] = int(IC_bank[account_1]["money"]) - movemoney - n
                bank[account_2]["money"] = int(bank[account_2]["money"]) + movemoney
                print("转入成功,以下是您的转账信息")
                info = '''
                    -----------------------------
                              转账凭证
                     转出账号：%s
                     转入账号：%s
                     转账金额：%s
                     手续费：%s
                     转出账户余额：%s
                     开户行名称：%s
                     转账日期：%s
                     -------------------------------
                    '''
                print(info % (account_1, account_2, movemoney, n,IC_bank[account_1]["money"],bank_name, now_time))
            else:
                print("金额不对！！！")
        else:
            print("密码不正确！！")
    else:
        print("账户不正确！！！")





# 5、查询功能
def demand():
    account = int(input("请输入账号："))
    password = input("请输入密码：")
    if account in IC_bank:
        if password == IC_bank[account]["password"]:
            print("以下是您的信息：")
            info = '''
                   -----------------------------
                           个人信息
                       账号：%s
                       用户名：%s
                       密码：%s
                       地址：
                           国籍：%s
                           省份：%s
                           街道：%s
                           门牌号：%s
                       余额：%s
                       开户行名称：%s
                       查询日期：%s
                   -------------------------------
                   '''
            print(info % (account, IC_bank[account]["username"],IC_bank[account]["password"],IC_bank[account]["country"], IC_bank[account]["province"], IC_bank[account]["street"], IC_bank[account]["door"], IC_bank[account]["money"], bank_name,now_time))
        else:
            print("密码输入错误")
    else:
        print("账号不存在")

#界面显示
def welcone():
    print("****************************")
    print("    中国农业银行账户管理系统   ")
    print("****************************")
    print("          1、开户            ")
    print("          2、存钱            ")
    print("          3、取钱            ")
    print("          4、转账            ")
    print("          5、查询            ")
    print("          6、Bye！           ")
    print("*****************************")

#核心功能
def index():
    while True:
        welcone()
        chose = input("请输入业务编号：")
        if chose == "1":
            adduser()
        elif chose == "2":
            depositmoney()
        elif chose == "3":
            takemoney()
        elif chose == "4":
            print(msg_info)
            step_bank_transfermoney()
        elif chose == "5":
            demand()
        elif chose == "6":
            print("欢迎下次光临")
            break
        else:
            print("业务编号输入错误")

if __name__ == '__main__':
    index()










