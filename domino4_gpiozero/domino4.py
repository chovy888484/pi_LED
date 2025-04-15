# gpiozero 라이브러리에서 LEDBoard 클래스 임포트
# LEDBoard는 여러 개의 LED를 하나의 객체로 묶어서 제어할 수 있게 해줌
from gpiozero import LEDBoard
from time import sleep  # 시간 지연을 위한 sleep 함수

# LED 핀들을 지정하여 LEDBoard 객체 생성
# BCM 번호 기준으로 GPIO 26, 19, 27, 17번 핀에 연결된 LED를 제어함
leds = LEDBoard(26, 19, 27, 17)

print("도미노 LED 시작 (Ctrl+C로 종료)")

try:
    # 무한 반복: LED를 순서대로 켰다 꺼지도록 반복
    while True:
        # LED 개수만큼 순회
        for i in range(len(leds)):
            leds.off()       # 모든 LED를 먼저 끔 (이전 LED를 끄는 역할도 포함됨)
            leds[i].on()     # 현재 순번에 해당하는 LED를 켬
            sleep(0.7)       # 0.7초 동안 대기하여 LED가 켜진 상태를 유지
except KeyboardInterrupt:
    # Ctrl+C 등으로 프로그램 종료 시 실행됨
    leds.off()              # 모든 LED를 꺼서 정리
    print("\n종료됨")       # 종료 메시지 출력
