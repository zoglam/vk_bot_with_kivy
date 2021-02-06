# vk_bot_with_kivy
- [Cmd](#cmd)
- [Buildozer](#buildozer)
- [Wol via http](#wol-via-http)

# Cmd
Prepare
```sh
python3 -m pip install -r requirements.txt 
```
Run
```sh
python3 main.py
```
# Buildozer
Build apk
```sh
buildozer android debug
```

# Wol via http
```
https://api.vk.com/method/messages.send?user_id=<VK_ID>&message=Включить%20PC&v=5.37&access_token=<TOKEN>
```