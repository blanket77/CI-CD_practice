from flask import Flask, request
import os
import subprocess

app = Flask(__name__)

@app.route('/hook', methods=['POST'])
def webhook():
    bash_path = r"C:\Program Files\Git\bin\bash.exe"
    script_path = r"C:\Users\quant.QUANT\Desktop\2025\CI_CD_practice\CI-CD_practice\Flask_Webhook\auto_deploy.sh"
    subprocess.run([bash_path, script_path])
    print("!! Webhook received from GitHub!!!")

    # os.system이란 시스템 쉘에서 명령어를 실행하는 함수, cmd를 실행하는 것과 같음
    return '', 204

if __name__ == '__main__': # Flask 서버 실행
    app.run(port=6000)
