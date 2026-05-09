[app]
title = M-Browser Pro
package.name = mbrowser
package.domain = org.mubarak
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.1,google-generativeai,certifi
orientation = portrait
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1
