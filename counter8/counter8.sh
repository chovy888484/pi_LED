#!/bin/bash

# 사용할 GPIO 컨트롤러 이름 (gpioinfo 명령으로 확인 가능)
CHIP=gpiochip0

# 사용할 LED GPIO 핀 번호 (BCM 번호 기준)
# 왼쪽(MSB)부터 오른쪽(LSB) 순서로 배열
LEDS=(27 19 26)

# ==============================
# 스크립트가 종료될 때 실행되는 정리 함수
# Ctrl+C(SIGINT)나 kill(SIGTERM) 시 호출됨
# ==============================
cleanup() {
    echo "종료 중... 모든 LED OFF"
    # 모든 LED를 OFF 상태로 만들기
    for pin in "${LEDS[@]}"; do
        gpioset --mode=exit $CHIP $pin=0
    done
    # 정상 종료
    exit 0
}

# 위에서 정의한 cleanup 함수를
# SIGINT (Ctrl+C), SIGTERM 신호에 연결
trap cleanup SIGINT SIGTERM

# ==============================
# 스크립트 시작 시 모든 LED 초기화 (꺼짐 상태)
# ==============================
for pin in "${LEDS[@]}"; do
    gpioset --mode=exit $CHIP $pin=0
done

echo "LED 이진 카운터 무한 반복 시작!"

# ==============================
# 무한 반복 루프 시작
# ==============================
while true; do

    # 0부터 7까지 반복 (3비트 이진수 범위)
    for i in {0..7}; do
        # 현재 카운트 값을 10진수와 이진수로 출력 (디버깅용)
        echo "Count: $i (Binary: $(printf "%03d" "$(echo "obase=2; $i" | bc)") )"

        # ==============================
        # 각 비트를 추출하여 해당 핀에 출력
        # MSB → LSB 순서로 처리
        # ==============================
        for j in {0..2}; do
            pin=${LEDS[$j]}                       # 현재 제어할 GPIO 핀
            bit=$(( (i >> (2 - j)) & 1 ))         # 비트 시프트로 해당 위치 비트 추출
            gpioset --mode=exit $CHIP $pin=$bit   # 추출한 비트 값으로 LED ON/OFF
        done

        # 각 숫자 사이에 1초 간격 유지
        sleep 1
    done
done
