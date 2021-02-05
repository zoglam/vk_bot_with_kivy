[app]

# (str) Title of your application
title = Smart server

# (str) Package name
package.name = smart_server

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (list) List of inclusions using pattern matching
source.include_patterns = controllers/**,templates/**

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = tests,bin,venv,.buildozer,.git,.vscode

# (list) List of exclusions using pattern matching
source.exclude_patterns = license,*.md,*.txt,.gitignore

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3==3.7.9,hostpython3==3.7.9,kivy,kivymd,vk_api,requests,urllib3,chardet,idna
0
# (str) Icon of the application
icon.filename = templates/logo/icon.ico

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = all

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 1.11.1

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
#android.presplash_color = #FFFFFF

# (string) Presplash animation using Lottie format.
# see https://lottiefiles.com/ for examples and https://airbnb.design/lottie/
# for general documentation.
# Lottie files can be created using various tools, like Adobe After Effect or Synfig.
#android.presplash_lottie = "path/to/lottie/file.json"

# (list) Permissions
android.permissions = INTERNET,ACCESS_BACKGROUND_LOCATION

# (int) Target Android API, should be as high as possible.
android.api = 30

# (int) Minimum API your APK will support.
android.minapi = 23

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = armeabi-v7a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1