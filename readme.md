# 설치

#### 1. FastAPI & unicon 설치

```bash
pip3 install fastapi uvicorn
```

#### 2. 애플리케이션 실행
```bash
uvicorn main:app --reload
```

# Uvicorn

### 개요

`Uvicorn`은 Python 웹 애플리케이션을 실행하기 위한 고성능 ASGI(Asynchronous Server Gateway Interface) 서버

FastAPI 등 Python 웹 프레임워크에서 주로 사용됨

### 기능 및 특징

#### 1. 고성능:

Uvicorn은 HTTP 프로토콜 구현을 위해 `uvloop`와 `httptools`를 사용하여 높은 성능을 제공

#### 2. 비동기 지원:

Uvicorn은 비동기로 동작함

#### 3. ASGI 표준 준수:

ASGI는 WSGI의 후속 표준으로, 비동기와 동기 호출을 모두 지원함.

결과적으로 더 다양한 프레임워크와 호환하여 사용할 수 있음

#### 4. TLS/SSL 지원:

HTTPS 연결을 위해 TSL/SSL 지원을 제공함

#### 5. Hot Reloading:

개발 모드에서 코드 변경 시 자동으로 서버를 재시작하는 기능을 제공함

### 고급 사용

#### HTTPS 설정

- Uvicorn은 인증서 파일을 지정하여 HTTPS 서버를 실행할 수 있음

```bash
uvicorn main:app --host 0.0.0.0 --port 443 --ssl-keyfile=./key.pem --ssl-certfile=./cert.pem
```

#### 워커 프로세스 커스텀

- 더 많은 동시 연결을 처리하기 위해 워크 프로세스를 사용할 수 있음

```bash
uvicorn main:app --workers 4
```

#### 설정 파일 사용

- 더 복잡한 설정이 필요한 경우 config.json 파일을 만들어 설정을 정의할 수 있음

```json
{
  "host": "0.0.0.0",
  "port": 8000,
  "reload": true,
  "workers": 2
}
```

```bash
uvicorn main:app --config config.json
```

# ASGI

ASGI(Asynchronous Server Gateway Interface)는 Python 웹 서버와 애플리케이션 간의 비동기 인터페이스 표준이다.
WSGI(Web Server Gateway Interface)의 비동기 버전으로 볼 수 있으며, 비동기 프로그래밍을 지원하는 현대적인 Python 웹 애플리케이션과 프레임워크를 위한 표준을 제공함

### ASGI 특징

#### 1. 비동기 지원

- ASGI는 비동기 I/O를 지원하여, 더 많은 동시 연결을 효율적으로 처리할 수 있다.

#### 2. 다양한 프로토콜 제공

- HTTP뿐만 아니라 WebSocket, MQTT 등 다양한 프로토콜을 다룰 수 있음

# 싱글스레드 이벤트 루프

FastApi는 기본적으로 싱글스레드 이벤트 루프 기반으로 동작한다. 
이는 FastAPI가 ASGI 표준을 따르는 비동기 프레임워크이기 때문이다.

### 이벤트 루프와 비동기 모델

FastAPI와 같은 비동기 프레임워크는 단일 스레드에서 실행되는 이벤트 루프를 통해 여러 작업을 동시에 처리한다.

#### 이벤트 루프:

- 단일 스레드에서 실행됨
- 비동기 작업을 스케줄링하고, I/O 작업이 완료될 때까지 기다리지 않고 다른 작업을 처리한다.

#### 비동기 함수:

- async def로 정의되며, await 키워드를 사용하여 비동기 작업을 기다린다.
- I/O 작업(예: 파일 읽기/쓰기, 네트워크 요청) 동안 블로킹되지 않고, 이벤트 루프가 다른 작업을 처리할 수 있게 한다.

### Uvicorn과 다중 워커

FastAPI가 단일 스레드 이벤트 루프 기반으로 동작하지만, Uvicorn과 같은 ASGI 서버를 사용하여 여러 워커 프로세스를 실행할 수 있다.

이는 다중 코어 시스템에서 병렬 처리를 가능하게 하여 성능을 향상시킬 수 있다.

ex:
```shell
uvicorn main:app --workers 4
```
여기서 --workers 4는 4개의 워커 프로세스를 실행하라는 의미임.

각 워커는 별도의 프로세스로 실행되며, 자체 이벤트 루프를 갖는다. 

이렇게 하면 애플리케이션이 여러 코어를 활용하여 더 높은 동시성을 달성할 수 있다.