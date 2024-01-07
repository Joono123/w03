#q1
# def is_odd(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False

#q2
# def avg_numbers(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result / len(args)
#
# print(avg_numbers(1,5))
# print(avg_numbers(1,2,3,4,5))

# #q3
# input1 = int(input("첫 번째 숫자를 입력하세요: "))
# input2 = int(input("두 번째 숫자를 입력하세요: "))
#
# total = input1 + input2
# print("두 수의 합은 %s입니다." % total)

#q4 - 3번

#q5
# f1 = open("test.txt", 'w')
# f1.write("Life is too short")
# f1.close()
#
# f2 = open("test.txt", 'r')
# print(f2.read())

#q6
# user_input = input("저장할 내용을 입력하세요: ")
# f = open('text.txt', 'a')
# f.write(user_input)
# f.write('\n')
# f.close()

#q7
# f = open('test.txt, 'r')
# body = f.read()
# f.close()
# body = body.replace(java, python)
# f = open{'test.txt', 'w')
# f.write(body)
# f.close()

#q8
import sys

numbers = sys.argv[1:]
result = 0
for number in numbers:
    result += int(number)

print(result)
