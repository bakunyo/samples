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

### プロジェクトの設定
`mydjango/settings.py` で以下の項目を編集

- DATABASES
  - DB作成権限を持つユーザーを指定すること
- TIME_ZONE

### DB, Table作成
```
python3 manage.py migrate
```
auth系などデフォルトのテーブルが作成される

マイグレーションはモデル定義から生成する

### モデルの定義
- django.db.models.Model を継承する
- {app}/models.py に記述する

#### フィールドの種類
- models.CharField
  - max_length の指定が必要。Table定義、Validationに使われる
- models.DateTimeField
- models.IntegerField

```
  pub_date = models.DateTime('date published')
```
の第1引数は人が読める用のフィールド定義

### アプリケーションの追加
`mydjango/settings.py` の INSTALLED_APPS に 'polls' を追加する

#### migrationファイルの作成
```
python3 manage.py makemigrations polls
```

#### migrationファイルをSQLで表示
```
python3 manage.py sqlmigrate polls {migration no}
```

### DB定義変更の3ステップ
- モデルを変更する({app}/models.py)
- migrationを生成する `python3 manage.py makemigrations {app}
- migrationを適用する `python3 manage.py migrate`


