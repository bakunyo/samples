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

### コンソール起動
```
$ python3 manage.py shell

>>> from polls.models import Question, Choice
>>> Question.objects.all()
[]

>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q
<Question: Question object>
>>> q.save()

>>> q.id
1
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2017, 4, 5, 2, 54, 30, 537805, tzinfo=<UTC>)

# メソッド一覧
>>> dir(q)
```

`def __str__` を定義することで、Console上の表現を指定できる

### Modelが使えるメソッド
```
>>> Question() # インスタンス化
>>> q.save() # DBに保存

>>> Question.objects.all() # 全インスタンス
>>> Question.objects.filter(id=1) # 検索
>>> Question.objects.filter(question_text__startwith='What') # 前方一致

>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)

>>> Question.objects.get(id=2) # raise error

>>> q.choice_set.all() # 関連するChoice全て
>>> c = q.choice_set.create(choice_text="Not much", votes=0) # Choice作成
>>> c.question
>>> q.choice_set.count() # 件数
>>> c.delete() # 削除
```

### Admin
#### superuserの作成
```
python3 manage.py createsuperuser
```

http://127.0.0.1:8000/admin/ でログインできるようになる

#### adminにpollsを追加する
`polls/admin.py` に以下を追加

```
from .models import Question

admin.site.register(Question)
```

- 追加／編集／削除が可能
- Historyが自動的に記録される


### URLConf
- urls でリクエストURLとViewを結びつける
- リクエストパラメータはurls.py に記述する

templateを使ったrender(shortcut)
```
def index(request):
  latest_questions = Question.objects.order_by('-pub_date')[:5]
  context = { 'latest_questions': latest_questions }
  return render(request, 'polls/index.html', context)
```

url ヘルパー
```
  <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```
`urls.py` に `detail` が定義されていること。
名前空間の指定
```
  <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```
`mydjango/urls.py` で `namespace` により名前空間を指定する必要がある


### form処理
有用なヘルパー

- csrf_token
- forloop.counter

### 汎用ビュー
ステップ

- URLConfを変換する
- 古い不要なビューを削除する
- 新しいビューにDjangoの汎用ビューを設定する

汎用ビューの種類は以下の2種類。どちらもviews.genericを利用する

- ListView
- DetailView

#### ListView
- template_name でテンプレートを指定(デフォルトは `{app}/{model}_list.html`)
- context_object_name で渡す変数名を指定(デフォルトは `{model}_list`)
- get_queryset で渡すリストの中身を定義

#### DetailView
- template_name でテンプレートを指定(デフォルトは `{app}/{model}_detail.html`)
- model を使ってどのモデルに関するViewなのかを指定
- context_object_name で渡す変数名を指定(デフォルトは `{model}`)
- urls.py では`<pk>`を使ってidを渡す

### Test
#### テストの準備
- テストは `{app}/test*.py` に書く
- TestCase のサブクラスが対象になる
- testで始まるメソッドがテストとして実行される
- assertEqual で検証される

#### テストの実行
```
python3 manage.py test [{app}]
```

#### Viewのテスト
```
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
>>> from django.test import Client
>>> client = Client()
>>> response = client.get('/')
>>> response.status_code
404
>>> response = client.get('/polls/')
>>> response.status_code
200
>>> response.content
b'\n  <ul>\n  \n      <li><a href="/polls/1/">What&#39;s new?</a></li>\n  \n      <li><a href="/polls/2/">Next question</a></li>\n  \n  </ul>\n\n'
>>> response.context['latest_questions']
[<Question: What's new?>, <Question: Next question>]
```


