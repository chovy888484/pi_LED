# 🔁 도미노 LED 순환 제어 (Raspberry Pi + GPIO)

이 프로젝트는 **Raspberry Pi**의 GPIO 핀을 사용하여 **LED가 도미노처럼 순환하며 점등되는 효과**를 구현한 Bash 스크립트입니다.  
스크립트 실행 시 LED는 순서대로 하나씩 켜지고, 이전 LED는 꺼지며, 마지막 LED와 첫 번째 LED 사이도 자연스럽게 연결됩니다.

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
