from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/hook', methods=['POST'])
def webhook():
    bash_path = r"C:\Program Files\Git\bin\bash.exe"
    script_path = r"C:\Users\quant.QUANT\Desktop\2025\CI_CD_practice\CI-CD_practice\Flask_Webhook\auto_deploy.sh"

    result = subprocess.run([bash_path, script_path], capture_output=True, text=True)
    print("✅ Webhook received")

    if result.returncode != 0:
        print("❌ 실행 실패")
        print(result.stderr)
    else:
        print("✅ 실행 성공")
        print(result.stdout)

    return '', 204

if __name__ == '__main__':
    app.run(port=6000)
