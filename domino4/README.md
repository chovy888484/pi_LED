# 🔁 도미노 LED 순환 제어 (Raspberry Pi + GPIO)

<img src="https://github.com/chovy888484/pi_LED/blob/9b57ecd31cfae4da564b0ae0292d8419b103704e/images/domino.png">

이 프로젝트는 **Raspberry Pi**의 GPIO 핀을 사용하여 **LED가 도미노처럼 순환하며 점등되는 효과**를 구현한 Bash 스크립트입니다.  
스크립트 실행 시 LED는 순서대로 하나씩 켜지고, 이전 LED는 꺼지며, 마지막 LED와 첫 번째 LED 사이도 자연스럽게 연결됩니다.

## 🎬 실행 영상

[![영상]([https://youtu.be/abc123XYZ](https://youtu.be/mCubjcwqom4))

> ⬆️ 링크 클릭


## 🛠️ 사용 환경

- Raspberry Pi 5 (또는 libgpiod 기반 GPIO 지원 보드)
- Raspbian (Debian 기반 Linux)
- `libgpiod` 패키지 설치 필요

## 📦 설치 및 준비

### 1. libgpiod 설치

```bash
sudo apt update
sudo apt install gpiod
```

### 2. 회로구성

- 총 4개의 LED와 저항 연결
- Raspberry Pi GPIO핀: **26, 19, 27, 17** 사용
- 각 핀은 LED의 **양극(+)** 에 연결되고, **음극(-)** 은 저항을 통해 GND로 연결

▶️ 실행 방법

1. 실행권한 부여

```bash
chmod +x domino4.sh
```

2. 스크립트 실행

```bash
sudo ./domino.sh
```
⚠️ 반드시 sudo로 실행해야 GPIO 접근이 가능합니다.

## 💡 동작 설명

- 스크립트는 지정한 4개의 GPIO 핀에 연결된 LED를 무한 반복으로 순서대로 점등합니다.

- 한 번에 하나의 LED만 켜지며, 이전 LED는 꺼지는 방식으로 자연스러운 도미노 흐름을 만듭니다.

- Ctrl + C로 종료 시, 모든 LED를 자동으로 꺼주는 cleanup 함수가 실행됩니다.

## 🧠 코드 요약

- LEDS=(26 19 27 17) : 사용할 GPIO 핀 목록

- gpioset 명령어를 사용하여 LED ON/OFF 제어

- trap을 통해 종료 시 LED를 꺼주는 함수 연결

- **이전 LED 끄기 → 현재 LED 켜기 → sleep → 다음** 으로 이동 방식

## 📸 회로 구성 
<img src="https://github.com/chovy888484/pi_LED/blob/535043cc3ef1441c88c66db4ad5c93fd21f3654d/images/IMG_0577.jpg">


