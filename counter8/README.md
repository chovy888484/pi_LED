# 🔢 Mission C - LED Binary Counter (Raspberry Pi + GPIO)

이 프로젝트는 Raspberry Pi의 GPIO 핀을 이용해 **LED로 이진 카운터(0~7)를 표현하는** Bash 스크립트입니다.  
LED는 0.5~1초 간격으로 카운팅되며, **2진수 비트에 따라 ON/OFF가 결정됩니다**.  
스크립트를 실행하면 LED가 **0부터 7까지 반복해서 점등되며**, 사용자가 `Ctrl + C`를 누르면 모든 LED는 꺼집니다.

---

## 🛠️ 시스템 환경

- **보드**: Raspberry Pi 5 (또는 GPIO 제어 가능한 보드)
- **OS**: Raspberry Pi OS / Debian 계열 리눅스
- **패키지**: `libgpiod` (GPIO 제어용 도구)

### 📦 설치 (필요 시)

```bash
sudo apt update
sudo apt install gpiod
```

## 🧰 하드웨어 구성

- 사용 GPIO 핀(BCM 번호 기준):
  - **GPIO 27** -> 최상위 비트(MSB)
  - **GPIO 19** -> 중간비트
  - **GPIO 26** -> 최하위 비트(LSB)
- 각 GPIO 핀은 LED의 **양극(+)** 에 연결하고, **음극(-)** 은 저항을 통해 GND에 연결

## ▶️ 실행 방법

1. 실행권한 부여

```bash
chmod +x counter8.sh
```

2. 실행
```bash
sudo ./counter8.sh
```
⚠️ 반드시 sudo로 실행해야 GPIO 접근이 가능합니다.


## 🔁 동작 방식

- 0부터 7까지의 숫자를 이진수로 변환
- 각 비트에 따라 해당 핀의 LED ON/OFF 제어
- 1초 간격으로 자동 카운트 반복
- Ctrl + c 누르면 모든 LED 꺼지고 종료

# LED Binary Counter 동작 방식

+---------+--------+-------------+-------------+-------------+----------------+
| Decimal | Binary | GPIO 27 (2²)| GPIO 19 (2¹)| GPIO 26 (2⁰)|   LED 상태     |
+---------+--------+-------------+-------------+-------------+----------------+
|   0     |  000   |     OFF     |     OFF     |     OFF     |   ○   ○   ○    |
|   1     |  001   |     OFF     |     OFF     |     ON      |   ○   ○   ●    |
|   2     |  010   |     OFF     |     ON      |     OFF     |   ○   ●   ○    |
|   3     |  011   |     OFF     |     ON      |     ON      |   ○   ●   ●    |
|   4     |  100   |     ON      |     OFF     |     OFF     |   ●   ○   ○    |
|   5     |  101   |     ON      |     OFF     |     ON      |   ●   ○   ●    |
|   6     |  110   |     ON      |     ON      |     OFF     |   ●   ●   ○    |
|   7     |  111   |     ON      |     ON      |     ON      |   ●   ●   ●    |
+---------+--------+-------------+-------------+-------------+----------------+
