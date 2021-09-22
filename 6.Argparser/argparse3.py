#action
#store
#store_const
#store_false ,store_true
#append[]
#append_const

import argparse

parser=argparse.ArgumentParser()

parser.add_argument('-s',action='store',dest='simple_value',help='store simple value')
parser.add_argument('-c',action='store_const',dest='constant_value',const=100, help='Store Constant value')

parser.add_argument('-t',action='store_true',default=False,dest='boolen_switch',help='set a switch to true')
parser.add_argument('-f',action='store_false',default=False,dest='boolen_switch',help='set a switch to false')

parser.add_argument('-a',action='append',dest='collection',default=[], help='add repeated values to list')
parser.add_argument('-A',action='append_const',dest='const_collection',const=2109, help='add different values to list')

#parser.add_argument('--version',action='version',version='1.0')

result=parser.parse_args()
print('simple_value=',result.simple_value)
print('constant_value=',result.constant_value)
print("boolen_switch=",result.boolen_switch)
print("collection=",result.collection)
print("const_collection=",result.const_collection)
