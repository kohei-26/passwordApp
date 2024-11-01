from flask import Flask, render_template,request
import random


app = Flask(__name__)

@app.route('/',methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
       
       password = ""
       max = request.form.get("max")
       
       if max == "文字数制限なし":
           max = random.randint(20, 40)
       else:
           try:
                max = int(max)  # maxが数値であることを保証
           except ValueError:
                max = 8  # maxが整数でない場合のデフォルト値を設定

       number = request.form.get("number") =="1"
       upper = request.form.get("upper") == "2"
       special = request.form.get("special") == "3"

       lowChar = "abcdefghijklmnopqrstuvwxyz"
       numberChar = "0123456789"
       upperChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
       specialChar = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

       passlist = "abcdefghijklmnopqrstuvwxyz"

       if number:
            passlist += numberChar
       if upper:
            passlist += upperChar
       if special:
            passlist += specialChar
       if not (number or upper or special):
            passlist = lowChar

        # パスワード生成
       for _ in range(max):
            password += random.choice(passlist)

       return render_template('index.html', password=password)

       return render_template('index.html', password = password)
    
    return render_template('index.html', password="")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,  debug=True)
