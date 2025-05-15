# num = int(input("입력:"))

# if num % 2 == 0:
#     print("짝수.")
# else:
#     print("홀수")



# for dan in range(2,10):
#     print(f"--- {dan}단 ---")
#     for i in range(1,10):
#         print(f"{dan} x {i} = {dan * i}")
#         print()

# numbers = [10,20,30,40,50]
# average = sum(numbers) / len(numbers)
# print(average)


# def is_palindrome(word):
#     return word == word[::-1]  #단어 뒤집기기

# text = input("입력: ")
# if is_palindrome(text):
#     print("팰린드롬.")
# else:
#     print("팰린드롬이 아닙니다.")


height = 5
for i in range(1, height + 1):
    print(" " * (height - i) + "*" * i)
