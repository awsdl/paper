#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
import math
from fractions import Fraction
import  os

from SuffixExpression import SuffixExpression

from BinaryTree  import BinaryTree

# 已经测试
class Product:

    # 类变量定义
    wentiliebiao = []            # 表达式列表表示
    exStr = ''            # 表达式字符串
    answer = 0                   # 答案
    answerStr = ''              # 答案字符串
    caozuoshugs = 10                # 操作数范围
    caozuofugs = 3                 # 操作符个数
    fenshugailv = 0                 # 出现分数的概率
    biaodashishumu = 100                  #生成表达式的数目



    def __init__(self, caozuoshugs,biaodashishumu):           #类的构造函数
        self.caozuoshugs = caozuoshugs
        self.caozuofugs = 3
        fenshugailv = random.randint(1,10)/100   # "/100"是不想生成分数题目太多
        print("出现分数的概率:{}".format(fenshugailv))
        self.fenshugailv = fenshugailv
        self.biaodashishumu = biaodashishumu
        self.wentiliebiao = self.biaodashishengc()
        self.normalizeExpression(self.wentiliebiao)
        #print(self.wentiliebiao)


    def biaodashishengc(self):
        """
        表达式生成主函数
        """
        expNum = self.biaodashishumu
        expressionList = []
        i = 0

        while i < expNum:
            random_num_operation = random.randint(1,self.caozuofugs)  #运算符的数目
            is_need_parenteses = random.randint(0, 1)    #是否需要加括号
            number_of_oprand = random_num_operation + 1  # 操作数比操作符的数目多1
            exp = []
            for j in range(random_num_operation + number_of_oprand):

                if j % 2 == 0:
                    # 随机生成操作数(含分数）
                    exp.append(self.getOperNum()['operStr'])


                    if j > 1 and exp[j - 1] == '÷' and exp[j] == '0':
                        while True:
                            exp[j - 1] = self.caozuofushengc()
                            if exp[j - 1] == '÷':
                                continue
                            else:
                                break
                else:
                    # 生成运算符
                    exp.append(self.caozuofushengc())

                if j > 3:
                    if exp[j-2] == '÷' :  #为了子表达式为真分数，÷左右又括号除外
                        if exp[j-1] > exp[j-3]:
                            t  = exp[j-1]
                            exp[j - 1] =  exp[j-3]
                            exp[j - 3] = t


                    elif exp[j-2] == '-' :
                        if exp[j-1] < exp[j-3]:
                            t  = exp[j-1]
                            exp[j - 1] =  exp[j-3]
                            exp[j - 3] = t




            # 判断是否要括号
            if is_need_parenteses and number_of_oprand != 2:
                expression = " ".join(self.kuohaoshengc(exp, number_of_oprand))
            else:
                expression = " ".join(exp)

            #判断是否有重复

            if self.biaodashishumu <= 500:
                if self.isRepeat(expressionList, expression) :
                   continue
                else:
                    result = self.calculate(expression)
                    if result == "False" :
                        pass
                    else:

                        expressionList.append(expression)
                        #('第 %d 道题' % int(i + 1))
                        #print(expression)
                        i = i + 1
            else:
                result = self.calculate(expression)
                if result == "False":
                    pass
                else:

                    expressionList.append(expression)
                    # ('第 %d 道题' % int(i + 1))
                    # print(expression)
                    i = i + 1



        return expressionList

    def caozuofushengc(self):  #随机生成操作符
        operators = ['+', '-', '×', '÷']
        return operators[random.randint(0,len(operators) - 1)]



    def kuohaoshengc(self, exp, number_of_oprand):
        """
        生成括号表达式
        """
        expression = []
        num = number_of_oprand
        if exp:
            exp_length = len(exp)
            left_position = random.randint(0, int(num / 2))
            right_position = random.randint(left_position + 1, int(num / 2) + 1)
            mark = -1
            for i in range(exp_length):
                if exp[i] in ['+', '-', '×', '÷']:
                    expression.append(exp[i])
                else:
                    mark += 1
                    if mark == left_position:
                        expression.append('(')
                        expression.append(exp[i])
                    elif mark == right_position:
                        expression.append(exp[i])
                        expression.append(')')
                    else:
                        expression.append(exp[i])
        # 如果生成的括号表达式形如 (1 + 2/3 + 3) 则重新生成
        if expression[0] == '(' and expression[-1] == ')':
            expression = self.kuohaoshengc(exp, number_of_oprand)
            return expression
        return expression

    def getOperNum(self):
        caozuoshugs=self.caozuoshugs
        fenshugailv=self.fenshugailv
        # 将分数出现的概率转换为整形
        fenshugailv *= 100
        fenshugailv=int(fenshugailv)
        # 是否成功生成操作数
        flag = False

        result = {}
        # 若随机生成的100以内的数在概率整形内，则生成分数
        if self.getRandomNum(100) <= fenshugailv :
            operArray = self.getRangeDec()
            result['oper']=operArray[0]/operArray[1]
            result['operStr']=self.DecToStr(operArray)
            result['operArray']=[operArray[0],operArray[1]]
        else:
            oper=self.getRandomNum(caozuoshugs)
            result['oper']=oper
            result['operStr']=str(oper)
            result['operArray'] = [oper,1]
        return result

    def DecToStr(self,operArray):
       #分数转化为字符串带分数
        operNum1 = operArray[0]
        operNum2 = operArray[1]
        if operNum2 == 1:
            return operNum1
        if(operNum1 > operNum2):
            temp = int(operNum1/operNum2)
            operNum1 -= (temp*operNum2)
            return str(temp) + "'" + str(operNum1) + "/" + str(operNum2)
        else:
            return str(operNum1) + "/" + str(operNum2)

    def getRangeDec(self):          #随机生成分数
        caozuoshugs=self.caozuoshugs
        while True:
            # 随机生成两个随机数
            operNum1 = self.getRandomNum(caozuoshugs)
            operNum2 = self.getRandomNum(caozuoshugs)
            # 判断是否为倍数，若是则重新生成随机数
            if (operNum1%operNum2) == 0:
                continue
            # 若operNum1不是operNum2的倍数则已获取到符合要求的 operNum1和 operNum2，退出循环
            else:
                break
        # 将获取到的分子和分母进行化简并返回
        return self.stacdardDec(operNum1, operNum2)

    def stacdardDec(self,operNum1,operNum2):    # 化简分数 接收分子 分母参数
        num  = Fraction(operNum1, operNum2)
        Num1  = int(num.numerator)
        Num2  = int(num.denominator)
        return [Num1,Num2]

    def getFactorList(self, oper):
        l=[]
        for k in range(2, oper+1):
            if (oper % k) == 0:
                l.append(k)
        return l

    def getRandomNum(self, range):
        #随机数
        return random.randint(1, range)

    def getOperSymbol(self, operate):
        # 返回操作符符号
        operSignArray = ['+', '-', '×', '÷']
        return operSignArray[operate - 1]


    def normalizeExpression(self, exp_list):
        """
        规范化输出表达式
        """
        if not exp_list:
            return

        if  os.path.exists("Exercises.txt"):
            with open("Exercises.txt", 'r+') as file:
                file.truncate(0)

        for i, exp in enumerate(exp_list):
            exp_str = "Question"+str(i+1) + ': '+ exp+" ="+"\n"
            with open('Exercises.txt', "a+",encoding='utf-8') as f:
                f.write(exp_str)


    def isRepeat(self, express_set, expression):
        """
        判断重复方法
        """
        suffixExpression = SuffixExpression(expression)
        target_exp_suffix = suffixExpression.re   # 后缀表达式列表
        binaryTree = BinaryTree()
        target_exp_binary_tree = binaryTree.shengcerchashu(target_exp_suffix)
        for item in express_set:
            suffixExpression2 = SuffixExpression(item)
            source_exp_suffix = suffixExpression2.re
            source_exp_binary_tree = binaryTree.shengcerchashu(source_exp_suffix)
            if binaryTree.treeIsSame(target_exp_binary_tree) == binaryTree.treeIsSame(source_exp_binary_tree):
                return True
        return False

    def calculate(self,expression):  # 计算单一表达式的值

        suffixExpression  = SuffixExpression(expression)

        exp_value = str(suffixExpression.suffixToValue())
        result = exp_value

        return result
