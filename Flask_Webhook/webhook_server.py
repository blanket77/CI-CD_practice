from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/hook', methods=['POST'])
def webhook():
    print("!! Webhook received from GitHub!")
    os.system('./auto_deploy.sh')  # Docker 컨테이너 재시작 스크립트 
    # os.system이란 시스템 쉘에서 명령어를 실행하는 함수, cmd를 실행하는 것과 같음
    return '', 204

if __name__ == '__main__':
    app.run(port=6000)
