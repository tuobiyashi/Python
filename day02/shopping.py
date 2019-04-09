'''
购物车程序
'''
product_list = [
    ('iPhone',5888),
    ('Macbook', 10888),
    ('Bike', 999),
    ('python', 66),
    ('coffee', 25)
]
shopping_list=[]
salary = input("输入你的工资:")
if salary.isdigit():
    salary=int(salary)
    while True:
        for index,item in enumerate(product_list):
            #print(product_list.index(item),item)
            print(index,item)
        user_choice=input("选择要购买的商品>>>：")
        if  user_choice.isdigit():
            user_choice=int(user_choice)
            if user_choice<len(product_list) and user_choice>=0:
                p_item=product_list[user_choice]
                if p_item[1]<=salary:#买得起
                    shopping_list.append(p_item)
                    salary-=p_item[1]
                    print("Added %s into shopping cart,your balance is \033[31;1m%s\033[0m"%(p_item,salary))
                else:
                    print("\033[31;1m你的余额只剩[%s]啦，不够支付商品\033[0m"%salary)
            else:
                print("product code [%s] is not exsit..."%user_choice)
        elif user_choice =='q':
            print('---------shopping list---------')
            for p in shopping_list:
                print(p)
            print("你的余额是：",salary)
            exit()
        else:
            print("输入错误，请重试：")

