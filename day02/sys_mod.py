'''
import sys

# print(sys.path) # 打印环境变量
print(sys.argv)  # 打印路径
'''

import os

# cmd_res=os.system("ls")  # 执行命令，不保存结果

cmd_res = os.popen("ls").read()
print("-->", cmd_res)

os.mkdir("new_dir")
