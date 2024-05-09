# ScreenshotToSkype
Take webpage screenshot and upload to Skype group

# Installation
- Install all requirement in requirements.txt
`pip install -r requirements.txt`

- Add .env variables as follows:
```
skype_usr=skype_email
skype_pwd=skype_password
skype_group_id=group_id_to_post
```

- You can get group ids via this code
```python
sk = Skype(email, password)

sk.chats.recent()

for chat in sk.chats:
    print(chat.id)
```