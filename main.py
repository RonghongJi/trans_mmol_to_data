import pandas as pd
import numpy as np
import time
import sys
import getopt
from Data_Processing import *
from To_Data import *
def printUsage():
	print ('''usage: main.py -i <input> -o <output>
       main.py --in=<input> --out=<output>''')
       

def input_info():
	inputarg=""
	utputarg=""
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["in=","out="])
		# 使用sys.argv[1:]过滤掉第一个参数（它是执行脚本的名字，不应算作参数的一部分）
		# h是一个开关选项，i带一个参数，o带一个参数
		# 调用getopt函数。函数返回两个列表：opts和args。opts为分析出的格式信息。
		# args为不属于格式信息的剩余的命令行参数。opts是一个两元组的列表。每个元素为：(选项串,附加参数)。如果没有附加参数则为空串''。
	except getopt.GetoptError:
		printUsage()
		sys.exit(-1)
	for opt,arg in opts:
		if opt == '-h':
			printUsage()
		elif opt in ("-i", "--in"):
			inputarg = arg
		elif opt in ("-o","--out"):
			utputarg = arg
	print ('输入:' + inputarg)
	print ('输出:' + utputarg)
    return inputarg, utputarg





if __name__ == '__main__':

    inputarg, utputarg = input_info()
    data_mmol = pd.read_table(inputarg, header = None)
    # data_xyz = pd.read_table('../BF4.xyz', header = None)

    element_dict, styl_dict = Init_data()
    data_dict = Get_data(element_dict, styl_dict, data_mmol)
    to_data(element_dict, styl_dict, data_dict,utputarg)

