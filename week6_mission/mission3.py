from gpiozero import LED, Button     # GPIO 제어를 위한 모듈
from signal import pause             # 프로그램 유지 (무한 대기)
from time import sleep               # 딜레이용 sleep 함수

# 사용할 LED 핀들 (BCM 기준, LSB → MSB 순서)
leds = [LED(p) for p in [26, 19, 27, 17]]

# 버튼 설정 (GPIO 25번 핀에 연결)
button = Button(25)

# 버튼이 눌리면 실행될 도미노 효과 함수
button.when_pressed = lambda: [led.on() or sleep(0.2) or led.off() for led in leds]

pause()  # 프로그램이 종료되지 않도록 무한 대기
