from gpiozero import LED, Button     # LED와 버튼 제어용 모듈
from signal import pause             # 프로그램 유지용 (무한 대기)

# LSB → MSB 순서로 4개의 LED 핀 지정 (BCM 번호 기준)
leds = [LED(p) for p in [26, 19, 27, 17]]

# 버튼 핀 지정 (GPIO 25번 사용)
button = Button(25)

count = 0  # 현재 카운트 상태 (0~15 범위)

# 숫자 값을 이진수로 변환하여 LED에 출력하는 함수
def update():
    global count
    count = (count + 1) % 16            # 0~15 사이로 순환 증가
    for i, led in enumerate(leds):      # 각 비트 위치에 대해
        led.value = (count >> i) & 1    # 해당 비트가 1이면 ON, 0이면 OFF
    print(f"Count: {count:04b}")        # 현재 값을 이진수(4자리)로 출력

# 버튼이 눌릴 때 update 함수 실행
button.when_pressed = update

pause()  # 이벤트 처리를 위해 프로그램을 계속 실행
