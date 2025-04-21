from gpiozero import LED, Button     # LED와 버튼 제어를 위한 gpiozero 모듈 임포트
from signal import pause             # 무한 대기(pause)를 위해 signal 모듈에서 pause 임포트

# 4개의 GPIO 핀에 연결된 LED 객체 리스트 생성 (BCM 핀 번호 사용)
leds = [LED(p) for p in [26, 19, 27, 17]]

# 버튼 객체 생성 (GPIO 25번 핀 사용, 내부 풀업 저항 활성화)
button = Button(25, pull_up=True)

# 버튼이 눌렸을 때: 모든 LED를 켜는 람다 함수 실행
button.when_pressed = lambda: [led.on() for led in leds]

# 버튼에서 손을 뗐을 때: 모든 LED를 끄는 람다 함수 실행
button.when_released = lambda: [led.off() for led in leds]

# 프로그램이 종료되지 않고 버튼 이벤트를 계속 대기하도록 유지
pause()
