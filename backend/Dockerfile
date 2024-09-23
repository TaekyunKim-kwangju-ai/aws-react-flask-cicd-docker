# Python 3.12 이미지를 기반으로 사용
FROM python:3-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일들을 컨테이너로 복사
COPY requirements.txt .

# 필요한 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 포트 5000 노출
EXPOSE 5000

# Flask 앱 실행
CMD ["flask", "run", "--host=0.0.0.0"]
