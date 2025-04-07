#!/bin/bash

# 사용할 GPIO 컨트롤러 이름 지정
CHIP=gpiochip0

# 사용할 LED 핀 번호들 (BCM 기준) - LED가 연결된 순서대로 배열
LEDS=(26 19 27 17)

# Ctrl+C (SIGINT) 또는 kill (SIGTERM) 등으로 프로그램이 종료될 때 실행될 함수 정의
# 모든 LED를 꺼서 정리해주고 종료함
cleanup() {
    echo "종료 중... LED 끄는 중"
    for pin in "${LEDS[@]}"; do
        # 각 핀에 대해 LED OFF 신호 (출력을 0으로 설정)
        gpioset --mode=exit $CHIP $pin=0
    done
    exit 0
}

# SIGINT(Ctrl+C), SIGTERM 신호를 받으면 cleanup 함수 호출되도록 설정
trap cleanup SIGINT SIGTERM

echo "자연스러운 순환 도미노 LED 시작!"

# 현재 켤 LED의 인덱스를 0부터 시작
index=0

# 전체 LED 개수 계산
length=${#LEDS[@]}

# 무한 루프 - LED를 계속 도미노처럼 순환 점등
while true; do
    # 현재 켜야 할 핀 번호 추출
    current_pin=${LEDS[$index]}
    
    # 이전에 켜졌던 LED의 인덱스를 계산 (0보다 작아지지 않게 순환 처리)
    # 예: index가 0이면 prev_index는 3이 됨 → 마지막 LED
    prev_index=$(( (index - 1 + length) % length ))
    
    # 이전에 켜졌던 핀 번호 추출
    prev_pin=${LEDS[$prev_index]}

    # 이전 핀의 LED를 끔 (출력 0)
    gpioset --mode=exit $CHIP $prev_pin=0

    # 현재 핀의 LED를 켬 (출력 1)
    gpioset --mode=exit $CHIP $current_pin=1

    # 잠시 대기하여 LED가 켜진 상태를 유지 (0.7초)
    sleep 0.7

    # 다음 LED로 넘어가기 위해 인덱스를 1 증가 (순환 구조)
    index=$(( (index + 1) % length ))
done
