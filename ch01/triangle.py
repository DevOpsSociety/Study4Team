# for 변수 in 반복할_객체:
#   실행할 코드


print('직각삼각형 그리기')
num = int(input('변의 길이: '))

for i in range(num): 
    print('*' * (i + 1))
    
area = (num ** 2) / 2.0
print('넓이: ', area)