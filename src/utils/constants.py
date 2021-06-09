import os

CACHE_TTL = int(os.environ.get('CACHE_TTL', 86_400))  # 24 hours
CACHE_MAXSIZE = int(os.environ.get('CACHE_MAXSIZE', 128))

LAST_N_DAY_DATA = int(os.environ.get('LAST_N_DAY_DATA', 7))
