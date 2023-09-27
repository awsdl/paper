# -*- coding = 'uft-8' -*-

import re
import os

from SuffixExpression import SuffixExpression

class Answer:

    exp_list = []
    exercisefile  = ""
    answerfile  = ""

    def __init__(self):
        print("Answer")

    def expression_result(self,exp_list):
        """
        求表达式的结果
        """

        self.exp_list  =exp_list
        if os.path.exists('Answer.txt'):   # 清空上一次的答案
            with open('Answer.txt', 'r+') as file:
                file.truncate(0)

        for i, exp in enumerate(self.exp_list):
            order_str = str(i + 1)
            suffixExpression  = SuffixExpression(exp)
            #print("------suffixExpression:{}---------".format(str(suffixExpression.suffixToValue()) ))
            exp_value = str(suffixExpression.suffixToValue()) + '\n'
            result = "Answer"+order_str + ': ' + exp_value

            with open('Answer.txt', 'a+', encoding='utf-8') as f:
                f.write(result)

    def delete_last_line(self,file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(lines[:-1])


    def check_answer(self,exercisefile,answerfile):
        """
        校对答案
        """
        w_num = 0
        c_num = 0
        exercise_answer = []
        c_list = []  # 正确题目序号
        w_list = []  # 错误题目序号
        self.exercisefile = exercisefile
        self.answerfile  = answerfile
        try:
            with open(self.exercisefile, 'r', encoding='utf-8') as f:
                for line in f:
                    # 匹配出正则表达式

                    exp_str = re.findall(r'Question\d+: (.*) =\n', line)
                    if exp_str:
                        exp = exp_str[0]
                    else:
                        continue
                    p  = SuffixExpression(exp)

                    exp_value = str(p.suffixToValue())

                    exercise_answer.append(exp_value)
        except IOError:
            print('please check if the path is correct')
    # 表达式列表是否为空
        try:
            with open(self.answerfile, 'r', encoding='utf-8') as f:
                for i, line in enumerate(f):
                    ans_str = re.findall(r'Answer\d+: (.*)\n', line)
                    # 容错
                    if ans_str:
                        ans = ans_str[0]
                    else:
                        continue
                    # 是否正确
                    if ans == exercise_answer[i]:
                        print("你的题号 ["+str(i+1)+"] 做对了")
                        c_num += 1
                        c_list.append(i + 1)
                    else:
                        print("你的题号 ["+str(i+1)+"] 这个答案是错的，应该是这个 "+exercise_answer[i])
                        w_num += 1
                        w_list.append(i + 1)
            with open('Grade.txt', 'w+', encoding='utf-8') as f:
                correct_str = 'Correct: ' + str(c_num) + ' ' + str(c_list) + '\n'
                wrong_str = 'Wrong: ' + str(w_num) + ' ' + str(w_list)
                print(correct_str)
                print(wrong_str)
                f.write(correct_str)
                f.write(wrong_str)
        except IOError:
            print('please check if the path is correct')
    def input_answer(self,exercisefile,answerfile):

        self_answer = []
        self.exercisefile = exercisefile
        self.answerfile = answerfile

        try:
            with open(self.answerfile, 'r+', encoding='utf-8') as file:
                with open(self.exercisefile, 'r', encoding='utf-8') as f:
                  for i, line in enumerate(f):

                        print(line)

                        ans = input()
                        ans_str = "Answer"+str(i)+": "+ans
                        file.write(ans_str+"\n")




        except IOError:
            print('please check if the path is correct')

if __name__ == '__main__':
    # exp_file = r'Exercises.txt'
    # ans_file = r'Answer.txt'
    exp_file = 'Exercises.txt'
    ans_file = 'Answer.txt'
    o  =  Answer()
    o.input_answer(exp_file,ans_file)
    o.delete_last_line(ans_file)
    o.check_answer(exp_file,ans_file)
