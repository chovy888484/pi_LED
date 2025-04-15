# gpiozero에서 LED 여러 개를 제어할 수 있는 LEDBoard 클래스를 임포트
from gpiozero import LEDBoard

# time.sleep()을 사용하기 위해 time 모듈의 sleep 함수 임포트
from time import sleep

# LEDBoard 객체 생성
# BCM 번호 기준으로 GPIO 27(MSB), 19, 26(LSB) 순서로 핀을 지정
# LED는 왼쪽(MSB)부터 오른쪽(LSB)까지 총 3개 연결되어 있다고 가정
leds = LEDBoard(27, 19, 26)

print("3비트 이진 카운터 시작 (Ctrl+C로 종료)")

try:
    # 무한 루프: 3비트로 표현 가능한 숫자 0~7까지 반복
    while True:
        for i in range(8):  # 0부터 7까지
            # 현재 숫자를 10진수 및 3자리 이진수로 출력 (디버깅용)
            print(f"Count: {i} (Binary: {i:03b})")

            # 각 비트를 추출해서 해당 LED에 반영
            # bit_pos는 0(MSB) → 1 → 2(LSB)
            for bit_pos in range(3):
                # i 값을 오른쪽으로 (2 - bit_pos)만큼 시프트해서 해당 비트 추출
                # & 1 연산으로 해당 비트값만 뽑아냄 (0 또는 1)
                bit = (i >> (2 - bit_pos)) & 1

                # 추출한 비트 값에 따라 LED ON 또는 OFF
                if bit:
                    leds[bit_pos].on()
                else:
                    leds[bit_pos].off()

            # 1초 대기 후 다음 숫자로 넘어감
            sleep(1)

# 키보드로 Ctrl+C를 눌러 종료할 경우 실행되는 부분
except KeyboardInterrupt:
    # 모든 LED를 꺼서 깔끔하게 종료
    leds.off()
    print("\n종료됨")
