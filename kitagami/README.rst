

=================================
Flask 処理部分
=================================


・ GIFアドレス取得

http://210.140.144.197:8080/gifmagazine　

にGet もしくは Postすると、JSONが帰ってきます。

・　Like数のカウントアップ

http://210.140.144.197:8080/gifmagazine/like

の先に[gifurl]を記述してGetもしくはPostしてください。

例

http://210.140.144.197:8080/gifmagazine/like?gifurl=http://cinemagraphs.com/images/demo/coco-eyes-mirror-429.gif



・Flaskのバックエンド起動コマンド

>>nohup python Flask.py &

停止は

ps -C python 
kill ~

