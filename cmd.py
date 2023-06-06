import mysql_connect
import sys

#后台登录
def admin_login():
    msg = "失败"
    count = 0
    while True:
        uname = input("请输入账号：")
        upwd = input("请输入密码：")
        sql="select * from test.admin where user=\""+uname+"\" and password=md5(\""+upwd+"\")"
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
            print("-" + str(i[0]) + "-----" + i[1] + "----" + str(i[2]) + "-----" + str(i[3])+"-------"+str(i[3]*i[2])+"-")

# 增加商品信息
def addProduct():
    print("----------添加商品信息----------")
    mc = input("请输入产品名称:")
    jg = float(input("请输入产品价格:"))
    zk = float(input("请输入折扣(0.1-1):"))
    sql_2='select * from goods where name="'+mc+'"'
    cursor_4=mysql_connect.cursor
    cursor_4.execute(sql_2)
    data=cursor_4.fetchall()
    if(data):
        print("-----该商品已存在！------")
        print("-------------------------------")
        return 0
    else:
        sql='insert into goods(name,price,discout)values("'+mc+'",'+str(jg)+','+str(zk)+')'
        cursor_3=mysql_connect.cursor
        cursor_3.execute(sql)
        row=cursor_3.rowcount
        if(row>0):
            print("商品" + mc + "添加成功")
            print("-------------------------------")
            showProduct()
# 删除商品
def delproduct():
    showProduct()
    while True:
        uid=input("请输入你要删除商品的编号：")
        sql_1='select * from goods where id='+uid+''
        #print(sql_1)
        cursor_5=mysql_connect.cursor
        cursor_5.execute(sql_1)
        data=cursor_5.fetchall()
        #print(data)
        if(data):
            sql_2 = 'delete from goods where id=' + uid + ''
            cursor_6=mysql_connect.cursor
            cursor_6.execute(sql_2)
            row=cursor_6.rowcount
            if(row>0):
                print("删除成功！")
                showProduct()

        else:
            print("你所输入的编号不存在！请重新输入")
        jx = int(input("取消输入请按1，继续请按2: "))
        if jx == 1:
            break
        elif jx == 2:
            continue
#商品信息更新
def setinfomation():
    showProduct()
    while True:
        uid=input("请输入你要更新信息商品的编号: ")
        sql_1 = 'select * from goods where id=' + uid + ''
        cursor_7 = mysql_connect.cursor
        cursor_7.execute(sql_1)
        data = cursor_7.fetchall()
        if (data):
            nm=input("请输入你要设置的名字: ")
            pr=input("请输入你要设置的价格: ")
            zk=input("请输入你要设置的折扣: ")
            sql_2='update goods set name="'+nm+'",price='+pr+',discout='+zk+''
            cursor_8=mysql_connect.cursor
            cursor_8.execute(sql_2)
            row=cursor_8.rowcount
            if(row>0):
                print("修改成功！")
                showProduct()
        else:
            print("你所输入的编号不存在！请重新输入")
        jx = int(input("取消输入请按1，继续请按2: "))
        if jx == 1:
            break
        elif jx == 2:
            continue
#展示所有用户
def user_show():
    sql = "select * from users"
    cursor_9 = mysql_connect.cursor
    cursor_9.execute(sql)
    data = cursor_9.fetchall()
    if (data != None):
        print("------------------用户信息--------------------------")
        print("----用户名------------------密码--------------------")
        for i in data:
            print("----" + i[0] + "-----" + str(i[1]) + "----" )
#添加用户
def user_add():
    user_show()
    while True:
        print("----------添加用户信息----------")
        name=input("请输入你要添加的用户名： ")
        sql_1 = 'select * from users where user="' + name + '"'
        #print(sql_1)
        cursor_10 = mysql_connect.cursor

        cursor_10.execute(sql_1)
        data = cursor_10.fetchall()
        if (data):
            print("该用户名已存在！请重新输入")
        else:
            passwd=input("请输入密码(6位)： ")
            sql_2='insert into users(user,password)values("'+name+'",md5("'+passwd+'"))'
            cursor_11=mysql_connect.cursor
            cursor_11.execute(sql_2)
            row=cursor_11.rowcount
            if(row>0):
                print("添加成功！")
                user_show()
        jx = int(input("取消输入请按1，继续请按2: "))
        if jx == 1:
            break
        elif jx == 2:
            continue

#删除用户
def user_drop():
    user_show()
    while True:
        print("----------删除用户----------")
        name=input("请输入你要删除的用户名： ")
        sql_1 = 'select * from users where user="' + name + '"'
        # print(sql_1)
        cursor_12 = mysql_connect.cursor
        cursor_12.execute(sql_1)
        data = cursor_12.fetchall()
        if (data):
            sql_2='delete from users where user="'+name+'"'
            cursor_13=mysql_connect.cursor
            cursor_13.execute(sql_2)
            row=cursor_13.rowcount
            if(row>0):
                print("删除成功")
                user_show()
        else:
            print("该用户不存在！")
        jx = int(input("取消输入请按1，继续请按2: "))
        if jx == 1:
            break
        elif jx == 2:
            continue
#用户密码重置
def user_reset():
    user_show()
    while True:
        print("----------重置用户密码----------")
        name = input("请输入你要重置的用户名： ")
        sql_1 = 'select * from users where user="' + name + '"'
        # print(sql_1)
        cursor_12 = mysql_connect.cursor
        cursor_12.execute(sql_1)
        data = cursor_12.fetchall()
        if (data):
            sql_2='update users set password=md5("123456")'
            cursor_13=mysql_connect.cursor
            cursor_13.execute(sql_2)
            row=cursor_13.rowcount
            if(row>=0):
                print("用户密码已重置为初始密码，初始密码为123456")
                user_show()
        else:
            print("该用户不存在！")
        jx = int(input("取消输入请按1，继续请按2: "))
        if jx == 1:
            break
        elif jx == 2:
            continue


# 主程序开始
if __name__=='__main__':
    while True:
        result = admin_login()
        if result == "成功":
            while True:
                print("---------------主菜单---------------")
                print("-1、显示商品列表")
                print("-2、增加商品信息")
                print("-3、删除商品")
                print("-4、修改商品信息")
                print("-5、展示用户列表")
                print("-6、添加用户")
                print("-7、删除用户")
                print("-8、重置用户密码")
                print("-9、退出")
                choice = int(input("请输入您的选项（1-9）: "))
                if choice == 1:
                    showProduct()
                elif choice == 2:
                    addProduct()
                elif choice == 3:
                    delproduct()
                elif choice == 4:
                    setinfomation()
                elif choice == 5:
                    user_show()
                elif choice == 6:
                    user_add()
                elif choice == 7:
                    user_drop()
                elif choice == 8:
                    user_reset()
                elif choice == 9:
                    print("------------系统已退出")
                    break
        break