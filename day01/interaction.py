# username=input("username:")
# password=input("password:")
# print(username,password)

name = input("name:")
age = input("age:")
# age = int(input("age:"))
print(type(age))  # 打印字符类型
job = input("job:")
salary = input("salary:")

# 字符串拼接
info = '''
-------info of ''' + name + '''-------
Name:''' + name + '''
Age:''' + age + '''
Job:''' + job + '''
Salary:''' + salary + '''

'''
print(info)

# 占位符 %s string类型  %d int类型
info1 = '''
-------info1 of %s ------age = input("age:")
Name:%s
Age:%s
Job:%s
Salary:%s

''' % (name, name, age, job, salary)
print(info1)

# 格式化输出 变量模式
info2 = '''
------ info2 of {__name} ------
Name:{__name}
Age:{__age}
Job:{__job}
Salary:{__salary}
'''.format(__name=name,
           __age=age,
           __job=job,
           __salary=salary)

print(info2)

# 格式化输出 数组模式
info3='''
------ info3 of {0} ------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
'''.format(name,age,job,salary)

print(info3)