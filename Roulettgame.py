import random
import time
import msvcrt


def wait():
    print(f"\n👉 {player_name}--> [Enter], AI--> [Spacebar]")
    while True:
        key = msvcrt.getch()
        if key == b'\r':
            return 'me'
        elif key == b' ':
            return 'ai'

def reload_chambers():
    chambers = ['BANG'] * 2 + ['CLICK'] * 4
    random.shuffle(chambers)
    return chambers

def print_lives(name, life):
    hearts = '♥ ' * life + '  ' * (3 - life)
    print(f"{name}: {hearts.strip()}")

def blink_life(name, life):
    for _ in range(3):
        print(f"{name}: {'♥ ' * life}".strip(), end='\r')
        time.sleep(0.6)
        print(f"{name}: {'   ' * life}".strip(), end='\r')
        time.sleep(0.4)
    print(f"{name}: {'♥ ' * life}".strip())

#게임 시작
player_name = input("당신의 이름을 입력하세요: ")
print(f"\n {player_name} vs AI - 1라운드 시작\n")

my_life = 3
ai_life = 3
chambers = reload_chambers()
turn = 'me'

while my_life > 0 and ai_life > 0:
    print("\n[현재 상태]")
    print_lives(player_name, my_life)
    print_lives("AI", ai_life)
    print(f"남은 총알 수: {len(chambers)}")

    if turn == 'me':
        choice = wait()
        target = player_name if choice == 'me' else 'AI'

        print(f"\n {target}님에게 총을 겨눕니다...")
        time.sleep(1.2)
        print("..")
        time.sleep(1)
        print("!")
        time.sleep(0.8)
        print("!!!!!!!!")
        time.sleep(0.8)

        bullet = chambers.pop(0)
        if bullet == 'BANG':
            print("💥💥💥💥 ")
            time.sleep(1)

            if choice == 'me':
                my_life -= 1
                blink_life(player_name, my_life)
            else:
                ai_life -= 1
                blink_life("AI", ai_life)

            chambers = reload_chambers()
            print(" 총알 장전 중....")
            time.sleep(1.2)
            turn = 'ai'
        else:
            print("... 공포탄입니다")
            time.sleep(0.8)
            if choice == 'me':
                print("다행히 살아남았습니다. 한 번 더 기회를 얻습니다")
            else:
                print("AI에게 기회가 넘어갑니다.")
                turn = 'ai'

    else:
        choice = random.choice(['me', 'ai'])
        target = player_name if choice == 'me' else 'AI'

        print(f"\n AI가 {target}에게 총을 겨눕니다...")
        time.sleep(1.2)
        print("..")
        time.sleep(1)
        print("!")
        time.sleep(0.8)
        print("!!!!!!!!")
        time.sleep(0.8)

        bullet = chambers.pop(0)
        if bullet == 'BANG':
            print("💥💥💥💥")
            if choice == 'me':
                my_life -= 1
                blink_life(player_name, my_life)
            else:
                ai_life -= 1
                blink_life("AI", ai_life)

            chambers = reload_chambers()
            print("총알을 장전중...")
            time.sleep(1.2)
            turn = 'me'
        else:
            print("... 공포탄입니다!")
            time.sleep(0.8)
            print(" 당신의 차례입니다.")
            turn = 'me'

# 🎬 게임 종료
print("\n💀 GAME OVER 💀")
if my_life <= 0:
    print("😭 당신이 졌습니다.")
elif ai_life <= 0:
    print("🎉 당신이 이겼습니다!")
else:
    print("⚠️ 총알이 모두 소진되어 무승부입니다.")
