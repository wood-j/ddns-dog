# introduction

this is an automatic script to update dns target ip of aliyun 2nd level domain

# setup env

```
pip3 install -r requirements.txt
```

# how to run

```
python3 main.py
```

# config.json

automatic generate config file if not exists, update this config file configure to your own

```
{
    "access_key": "",
    "access_passwd": "",
    "domain": "",
    "rr": ""
}
```

1. access_key: access key of your aliyun account
2. access_passwd: access password of your aliyun account
3. domain: top level domain, sample: `google.com`
4. rr: second level domain header, sample: `doc`

how to get access key:

https://usercenter.console.aliyun.com/#/manage/ak

# warning

access key and password has admin authority of your aliyun account.
it is absolutely important and dangerous.
so, keep it safe and don not publish in public.