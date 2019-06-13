# introduction

this is an automatic script to update dns target ip of ali-yun 2nd level domain

# setup env

```
pip3 install -r requirements.txt
```

# how to run

```
python3 main.py
```

# config.json

automatic generate config file if not exists, update this config file to configure your own

```
{
    "access_key": "",
    "access_passwd": "",
    "domain": "google.com",
    "rr": [
        "api",
        "doc"
    ]
}
```

1. access_key: access key of your ali-yun account
2. access_passwd: access password of your ali-yun account
3. domain: top level domain, sample: `google.com`
4. rr: second level domains , sample: `doc`、`api`

how to get access key:

https://usercenter.console.aliyun.com/#/manage/ak

# warning

access key and password has admin authority of your ali-yun account.
it is absolutely important and dangerous.
so, keep it safe and don not publish in public.