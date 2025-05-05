# Dockerfile은 Docker 이미지를 만들기 위한 설정 파일입니다.

# 베이스 이미지 설정
FROM python:3.10-slim 

# 작업 디렉토리 생성하고 /app으로 설정
# 컨테이너 내에서 작업할 디렉토리를 설정합니다.
# 이 디렉토리는 컨테이너가 시작될 때 자동으로 생성됩니다.
# 이 디렉토리로 이동하여 이후의 모든 명령어가 이 디렉토리에서 실행됩니다.
WORKDIR /app

# 코드 복사 : 현재 디렉토리의 모든 파일을 컨테이너의 /app 디렉토리에 복사
# .dockerignore 파일을 사용하여 복사하지 않을 파일을 지정할 수 있습니다.
# 첫번째 .는 현재 디렉토리를 의미하고, 두번째 .은 컨테이너 내의 /app 디렉토리를 의미합니다.
COPY . .

# 필요한 패키지 설치 --no-cache-dir 옵션은 캐시를 사용하지 않고 패키지를 설치합니다.
# 이 옵션을 사용하면 이미지 크기를 줄일 수 있습니다.
RUN pip install --no-cache-dir -r requirements.txt

# Flask 앱 실행 (run.py 기준)
CMD ["python", "run.py"]
