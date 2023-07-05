import multiprocessing
import os

try:
    os.system("npx tailwindcss -i static/base.css -o static/css/tailwind.css")
except:
    pass

bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() * 2 + 1
print(workers)

# Enable Django's autoreload mechanism
reload = True

# Additional Gunicorn configurations
