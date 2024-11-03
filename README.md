シンプルなパスワード生成アプリケーションです。
文字数とチェックボックスの条件を指定すると、その指定したパスワードが生成されます。

docker環境で構築をしたため、コードをDL後、下記コマンドを実行します。

docker build -t passwordapp -f docker/Dockerfile .  

docker run -p 5000:5000 passwordapp 

