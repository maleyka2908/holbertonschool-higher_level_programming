#!/usr/bin/python3
"""
A script that adds all arguments to a Python list,
and then saves them to a file.
"""
import sys
import os

# Əvvəlki tapşırıqlardakı funksiyaları import edirik
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# 1. Fayl mövcuddursa, daxilindəki siyahını yüklə, yoxdursa boş siyahı yarat
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# 2. Skriptin adından sonra gələn bütün arqumentləri siyahıya əlavə et
# sys.argv[0] skriptin öz adıdır, ona görə [1:]-dən başlayırıq
items.extend(sys.argv[1:])

# 3. Yenilənmiş siyahını fayla saxla
save_to_json_file(items, filename)
