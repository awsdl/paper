from Answer import Answer
from Product import Product
from SuffixExpression import SuffixExpression
import argparse
import os

def main():

    parser = argparse.ArgumentParser(description="小学四则运算游戏")
    parser.add_argument('-n','-na',  type=str, help='题目个数')
    parser.add_argument('-r', '-ra', type=str, help='数值范围')
    parser.add_argument('-e','-ea',type=str, default=" ", help='题目文件')
    parser.add_argument('-a', '-aa',type=str,default=" ", help='答案文件')
    args = parser.parse_args()
    n = int(args.n)
    r = int(args.r)
    e = args.e
    e = e.strip()
    a = args.a
    a = a.strip()
    product  =Product(r,n)
    questions = product.wentiliebiao
    #存储生成的表达式，存进 ： “Exercises.txt”
    answer = Answer()
    answer.expression_result(questions)  #生成题目的答案、

    if os.path.exists(e) and  os.path.exists(a):
        print("check")
        answer.check_answer(e, a)


if __name__ == '__main__':
    main()

