import argparse

class Employee:
    def __init__(self,no_of_emp):
        self.no_of_emp=no_of_emp
        print("Number of Employees",no_of_emp)

    def add(self,a,b):
        print("Addition:",a+b)

    def mul(self,a,b):
        print("Multiplication:",a*b)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('no_of_emp',help="employee",type=int)
    parser.add_argument('a',help="employee",type=int)
    parser.add_argument('b',help="employee",type=int)

    args=parser.parse_args()

    g=Employee(args.no_of_emp)
    g.add(args.a,args.b)
    g.mul(args.a,args.b)