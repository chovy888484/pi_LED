from gpiozero import LED, Button     # LED와 버튼 제어용 클래스
from signal import pause             # 무한 대기를 위한 함수

# 사용할 GPIO 핀 번호 (BCM 기준, LSB → MSB 순서)
leds = [LED(p) for p in [26, 19, 27, 17]]

# 버튼 객체 생성 (GPIO 25번 핀)
button = Button(25)

# 버튼이 눌릴 때 실행되는 함수
def toggle():
    # 현재 상태와 반대로 설정 (기준은 첫 번째 LED의 상태)
    state = not leds[0].is_lit

    # 모든 LED의 상태를 동일하게 변경
    for led in leds:
        led.value = state

    # 현재 LED 상태 출력 (디버깅용)
    print(f"LED 상태: {'ON' if state else 'OFF'}")

# 버튼 눌림 이벤트에 toggle 함수 연결
button.when_pressed = toggle

# 프로그램이 종료되지 않도록 무한 대기
pause()
