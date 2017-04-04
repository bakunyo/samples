# Django Tutorial
https://docs.djangoproject.com/ja/1.9/intro/tutorial01/

### djangoアプリの作成
```
django-admin startproject {project-name}
```

### ローカル起動
```
python3 manage.py runserver

# python3 manage.py runserver 0.0.0.0:8000
# LAN内からのアクセスにはALLOWS_HOSTで許可が必要
```

#### プロジェクトとアプリケーション
とあるWEBサイト: プロジェクト
その中に含まれる機能(ブログ、DB、投票など): アプリケーション

プロジェクトの中に複数のアプリケーションをつくっていくイメージ

```
# アプリケーションの作成
python3 manage.py startapp polls
```
