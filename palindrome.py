def palindrome(s):
    s= s.lower().replace(" ", "")
    return s == s[::-1]

user_input = input("문자를 입력하세요:")

if palindrome(user_input):
    print("이 문자는 팰린드롬입니다.")
else:
    print("이 문자는 팰린드롬이 아닙니다.")