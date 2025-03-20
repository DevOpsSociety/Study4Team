# # 숫자 넣으면 그 값을 곱해줌
# num = int(input())
# print(num*num)

# -------------------------------------
# # 숫자 넣은만큼 반복문 돌려서 *갯수가 늘어남
# print('직각삼각형 그리기\n')
# leg = int(input('변의 길이: '))

# for i in range(leg):
#     print('* ' * (i + 1))

# area = (leg ** 2) / 2
# print('넓이:', area)

# -------------------------------------
# 위 코드랑 동일한데 raw_input은 Python2 에서 사용되고
# Python3 부터는 input으로 변경됨
# 입력값을 정수로 반환하려면 int() 사용
print('Right triangle\n')
leg = int(input('leg: '))

for i in range(leg):
    print('* ' * (i + 1))

area = (leg ** 2) / 2.0
print('area:', area)
