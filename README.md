# FastAPI 간단 예제 프로젝트

## 🛠️ 사용 기술
- Python 3.12
- FastAPI
- Uvicorn
- SQLAlchemy (ORM)
- Pydantic
- Mysql: latest
- Docker

## 🚀 시작하기
1. 저장소 클론하기
   ```bash
   git clone https://github.com/yourname/fastapi-crud-example.git
   cd fastapi-crud-example
   ```
2. 의존성 설치
   ```bash
   pip install -r requirements.txt
   ```
3. `.env` 파일 생성 후 데이터베이스 연결 정보 설정
   db user 및 pw는 프로젝트에 맞게 설정

4. Docker compose 실행행
   ```bash
   docker-compose up -d
   ```
5.  서버 실행
   ```bash
   uvicorn app.main:app --reload
   ```

## 📂 주요 파일 구조
```
app/
├─ main.py            # FastAPI 앱 진입점
├─ core/
│  ├─ models.py       # DB 모델 정의
|  ├─ config.py       # setting 값 설정정
|  ├─ database.py     # db 연결
|  ├─ dependecy.py    #의존성 주입
└─ api/
   └─ v1/
       ├─ routers.py       # 라우터 모음
       └─ users/
        ├─ users_crud.py    # repository 계층
        ├─ users_schemas.py # Pydantic 스키마
        ├─ users_endpoint.py # controller 계층
        ├─ users_service.py # 비즈니스 로직(service 계층)
        
```

## 🎉 API 문서 확인
- Swagger UI: `http://localhost:8000/docs`

## 주요 기능
- 사용자 생성
- 사용자 조회 (ID, 이메일)
- 사용자 삭제
