# 🔌 Raspberry Pi GPIO LED Projects (gpiozero)

<img src= "https://github.com/chovy888484/pi_LED/blob/b631e44a0b057dc64e1f5714fbd4c50d454dd20d/images/%E1%84%86%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB2.png">

이 저장소는 **Raspberry Pi의 GPIO 핀을 사용한 4가지 LED 제어 예제**를 담고 있습니다.  
Python의 [`gpiozero`](https://gpiozero.readthedocs.io/) 라이브러리를 사용하여 간결하고 직관적으로 작성되었습니다.

---
## 🎥 시연 영상
👉 [영상 보러 가기 (YouTube)](https://youtu.be/BlbjoJ85mbI)

> ⬆️ 링크 클릭

## 📁 프로젝트 목록

| 프로젝트 이름 | 설명 |
|---------------|------|
| ⬆️ `mission1.py` | 버튼을 누르고 있는 동안만 모든 LED ON |
| 🔄 `mission2.py` | 버튼을 누를 때마다 LED 전체 ON/OFF 전환 |
| 🔁 `mission3.py` | 버튼을 누르면 LED가 순차적으로 도미노처럼 점등 |
| 🔢 `mission4.py` | 버튼을 누를 때마다 0~15까지 4비트 이진 카운팅 |

---

## 🧰 하드웨어 구성

- Raspberry Pi (모델 4/5 등)
- 5mm LED × 4개
- 330Ω 저항 × 5개
- 버튼 (푸시 스위치) × 1개
- 브레드보드, 점퍼 와이어
- 사용 핀 (BCM 번호 기준)
  - **LED**: 26 (LSB), 19, 27, 17 (MSB)
  - **버튼**: 25

<img src= https://github.com/chovy888484/pi_LED/blob/1b207d69b1db4307b81b8b74e6eebe9d19f0efa9/images/mission2.jpg width="400" alt="회로 사진">

---

## ▶️ 실행 방법

1. 의존 패키지 설치 (한 번만 하면 됨)

```bash
sudo apt update
pip install gpiozero
```

2. 원하는 코드 실행

```bash
python3 mission1.py
# 또는
python3 mission2.py
.
.
```

---


🧠 주요 코드 설명

`mission1.py`
버튼을 누르고 있는 동안 모든 LED ON

손을 떼면 자동으로 OFF

`mission2.py`
버튼을 누를 때마다 전체 LED 상태 토글

ON → OFF → ON 반복


`mission3.py`
버튼을 누르면 LED가 순서대로 켜졌다 꺼짐

도미노처럼 흐르며 한 번 점등


`mission4.py`
버튼을 누를 때마다 숫자 1씩 증가 (0~15)

LED 4개에 이진수로 출력
콘솔에 Count: 0101처럼 출력됨

