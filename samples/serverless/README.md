# Serverless Framework
Try Serverless with aws-nodejs

## Set up
[Installation](https://serverless.com/framework/docs/providers/aws/guide/installation/)
[Credentials](https://serverless.com/framework/docs/providers/aws/guide/credentials/)

```
$ node -v
v6.6.0

$ npm install -g serverless

$ serverless config credentials --provider aws --key xxxxx --secret xxxxx
```

## Initialize
```
sls create -t aws-nodejs
```

## Develop
Edit `handler.js` and `serverless.yml`

## Deploy
```
sls deploy
```

## Invoke
```
sls invoke -f hello
```

### As API
```
# in serverless.yml
functions:
  hello:
    handler: handler.hello
    events:
      - http:
        path: hello
        method: get
```
