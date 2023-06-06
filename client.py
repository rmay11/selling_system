import sys
import mysql_connect
#登录
def user_login():
    msg = "失败"
    count = 0
    while True:
        uname = input("请输入账号：")
        upwd = input("请输入密码：")
        sql="select * from test.users where user=\""+uname+"\" and password=md5(\""+upwd+"\")"
        #print(sql)
        cursor_1=mysql_connect.cursor
        cursor_1.execute(sql)
        data=cursor_1.fetchone()
        if(data):
            msg="成功"

        if(msg == "失败"):
            count += 1
            if count < 3:
                print("用户名密码错误！请重新登录", "输入第", count, "次")
            else:
                print("用户已锁定！")
                break
        else:
            break
    return msg
# 显示商品列表
def showProduct():
    sql="select * from test.goods"
    cursor_2=mysql_connect.cursor
    cursor_2.execute(sql)
    data=cursor_2.fetchall()
    if(data!=None):
        print("---------------产品信息---------------")
        print("编号----名称----价格----折扣----折扣价格")
        for i in data:
            print("-" + str(i[0]) + "-----" + i[1] + "----" + str(i[2]) + "-----" + str(i[3]) + "-------" + str(i[3] * i[2]) + "-")





# 主程序开始
while True:
    result = user_login()
    if result == "成功":
        while True:
            print("---------------主菜单---------------")
            print("-1、显示商品列表")
            print("-2、退出")
            choice = int(input("请输入您的选项（1-2）"))
            if choice == 1:
                showProduct()

            elif choice == 2:
                print("------------系统已退出")
                break

    break
