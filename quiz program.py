import random

list = [
    {"문제" : "1. 파이썬은 인터프리터 언어이다.", "정답" : "O"},
    {"문제" : "2. print('Hello')를 실행하면 나오는 결과는?", "보기" : ["1. hello", "2. Hello", "3. 'Hello'", "4. print('hello')", "5. print"], "정답" : "2"},
    {"문제" : "3. 5*3+4 = ?", "보기" : ["1. 35", "2. 27", "3. 17", "4. 19", "5. 23"], "정답" : "4"},
    {"문제" : "4. 컴퓨터의 cpu는 데이터를 저장하는 장치이다.", "정답" : "X"}
]

score = 0

random.shuffle(list)

for i in list:
    print(i["문제"])
    if "보기" in i:
        for e in i["보기"]:
            print(e)
    answer = input("정답을 입력하세요 :").upper()
    if answer == i["정답"]:
        print("정답입니다.\n")
        score += 1
    else:
        print(f"정답이 아닙니다. 정답은 {i['정답']} 입니다.\n")
    
print(f"문제가 끝났습니다. 당신의 총 {len(list)}문제 중 {score}문제를 맞췄습니다.\n")
print(f"당신의 점수는 {score}점 입니다.")
    