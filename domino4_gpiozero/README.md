# 🔁 도미노 LED 순환 제어 (Raspberry Pi + GPIO + GPIOZERO)

<img src="https://github.com/chovy888484/pi_LED/blob/9b57ecd31cfae4da564b0ae0292d8419b103704e/images/domino.png">

이 프로젝트는 **Raspberry Pi**의 GPIO 핀을 사용하여 **LED가 도미노처럼 순환하며 점등되는 효과**를 python으로 구현한 프로젝트입니다.  
[`gpiozero`](https://gpiozero.readthedocs.io/) 라이브러리를 활용해 간결하고 직관적으로 작성되었으며,  
LED는 순서대로 하나씩 켜지고 이전 LED는 꺼지며, 마지막 LED 이후 첫 번째로 자연스럽게 이어집니다.

## 🎬 실행 영상

👉 [영상 보러 가기 (YouTube)]]([https://youtu.be/mCubjcwqom4?si=puU295NH2Ie_GV3d](https://youtu.be/BlbjoJ85mbI))

> ⬆️ 링크 클릭


## 🛠️ 사용 환경

- Raspberry Pi 5 (또는 GPIO 제어 가능한 보드)
- Raspbian (Debian 기반 Linux)
- Python 3
- `gpiozero` 라이브러리 설치 필요

## 📦 설치 및 준비

### 1. gpiozero 설치 (필요 시)

```bash
sudo apt update
pip install gpiozero
```

### 2. 회로구성

- 총 4개의 LED와 저항 연결
- Raspberry Pi GPIO핀: **26, 19, 27, 17** 사용
- 각 핀은 LED의 **양극(+)** 에 연결되고, **음극(-)** 은 저항을 통해 GND로 연결

▶️ 실행 방법

1. 코드 파일 다운로드 또는 복사

파일명: counter8.py

2. 실행
```bash
python3 binary_counter.py
```


## 💡 동작 설명

- 스크립트는 지정한 4개의 GPIO 핀에 연결된 LED를 무한 반복으로 순서대로 점등합니다.

- 한 번에 하나의 LED만 켜지며, 이전 LED는 꺼지는 방식으로 자연스러운 도미노 흐름을 만듭니다.

- Ctrl + C로 종료 시, 모든 LED를 자동으로 꺼주는 cleanup 함수가 실행됩니다.

## 🧠 코드 요약

 - LEDBoard(26, 19, 27, 17) : 4개의 LED를 객체로 묶어 제어

 - leds[i].on() / .off() : 리스트처럼 인덱스로 LED 개별 제어

 - leds.off() : 모든 LED 끄기

 - try ~ except KeyboardInterrupt : 종료 시 정리(cleanup) 처리



## 📸 회로 구성 
<img src="https://github.com/chovy888484/pi_LED/blob/535043cc3ef1441c88c66db4ad5c93fd21f3654d/images/IMG_0577.jpg">


