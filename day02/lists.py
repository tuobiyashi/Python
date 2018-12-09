names = "ZhangYang GuYun XiangPeng XuLiangChen"
names = ["ZhangYang", "GuYun", "XiangPeng", "XuLiangChen"]
names.append("LeiHaiDong")  # 列表追加
names.insert(1, "ChengRongHua")  # 插入：下标+str
names[2] = "XieDi"  # 修改

print(names)

print(names[0], names[2])

print(names[1:3])  # 切片：取中间两位顾首不顾尾）

print(names[-2:])  # 切片：取后面两位

print(names[:3])  # 切片  print(names[0:3])

# delete 删除的三种方法
names.remove("ChenRongHua")
del names[1]
names.pop()  # 默认删除最后一位，输入下标删除指定 del names[1]=names.pop(1)
print(names)

# 打印索引值
print(names.index("XieDi"))

# 统计个数
print(names.count("ChenRongHua"))

# 反转
names.reverse()

# 排序
names.sort()

# 合并列表
names2 = [1, 2, 3, 4]
names.extend(names2)
print(names, names2)
