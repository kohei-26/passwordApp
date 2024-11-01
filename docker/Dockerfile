# ベースイメージの指定
FROM python:3.8-slim

# 作業ディレクトリを設定
WORKDIR /app

# requirements.txtをコピーしてインストール
COPY config/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Flaskアプリケーションのコードとテンプレート・静的ファイルをコピー
COPY src/app.py /app/app.py
COPY src/templates /app/templates
COPY src/static /app/static

# ポートを公開
EXPOSE 5000

# コンテナ起動時のコマンド
CMD ["python", "app.py"]
