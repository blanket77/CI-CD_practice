# CI-CD_practice

python --version : 3.10.10

pytest는 test_*.py 형식의 파일과 test_로 시작하는 함수를 자동으로 찾아 실행함

# Project Structure

```plaintext
my-app/
├── app.py                   # Flask 애플리케이션 진입점
├── requirements.txt         # 필요한 패키지 목록
├── test_app.py              # pytest로 작성된 테스트 코드
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions CI 설정 파일
├── README.md                # 프로젝트 설명 파일
