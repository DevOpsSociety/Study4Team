# ✅ 1. 숫자 짝수/홀수 판별 
# 문제: 사용자로부터 정수를 입력받아, 짝수인지 홀수인지 출력하세요.
# 정답 코드
num = int(input("숫자를 입력하세요: "))

if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

# ✅ 2. 구구단 출력
# 문제: 2단부터 9단까지 구구단을 출력하세요.
# 정답 코드
for dan in range(2, 10):
    print(f"--- {dan}단 ---")
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")
    print()


# ✅ 3. 리스트 평균 구하기
# 문제: 주어진 숫자 리스트의 평균을 구하세요.
# 정답 코드
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
print("평균:", average)

# ✅ 4. 팰린드롬 판별
# 문제: 문자열을 입력받아 팰린드롬인지 판별하는 함수를 작성하세요.
# 정답 코드
def is_palindrome(word):
    return word == word[::-1]

text = input("단어를 입력하세요: ")
if is_palindrome(text):
    print("팰린드롬입니다.")
else:
    print("팰린드롬이 아닙니다.")


# ✅ 5. 별 피라미드 출력
# 문제: 높이 5인 오른쪽 정렬 별 피라미드를 출력하세요.
# 정답 코드
height = 5
for i in range(1, height + 1):
    print(" " * (height - i) + "*" * i)

