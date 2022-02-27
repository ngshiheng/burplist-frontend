from environs import Env
from pytz import timezone

env = Env()
env.read_env()

LOCAL_TIMEZONE = timezone('Asia/Singapore')

RECONNECT_TIMEOUT = env.int('RECONNECT_TIMEOUT', default=60)

STATIC = '/static/'

ALLOWED_ORIGINS = env.list('ALLOWED_ORIGINS', default=['*://*.burplist.me'])

# In-memory Caching
# ^^^^^^^^^^^^^^^^^
CACHE_TTL = env.int('CACHE_TTL', default=86_400)  # 24 hours
CACHE_MAXSIZE = env.int('CACHE_MAXSIZE', default=128)

# Database
# ^^^^^^^^
DATABASE_CONNECTION_STRING = '{drivername}://{user}:{password}@{host}:{port}/{db_name}'.format(
    drivername='postgresql',
    user=env.str('PG_USERNAME', default='postgres'),
    password=env.str('PG_PASSWORD', default='developmentpassword'),
    host=env.str('PG_HOST', default='localhost'),
    port=env.int('PG_PORT', default='5432'),
    db_name=env.str('PG_DATABASE', default='burplist'),
)
LAST_N_DAY_DATA = env.int('LAST_N_DAY_DATA', default=7)

# SEO
# ^^^
SEO_TITLE = 'Burplist.me - Search Engine for Craft Beers in Singapore'
SEO_DESCRIPTION = 'The best search engine for craft beers in Singapore. Browse for popular craft beers online and find the best deals across 10+ sites.'

# Misc
# ^^^^
CONTACT_EMAIL = env.str('CONTACT_EMAIL', default='')
FEEDBACK_FORM_URL = env.str('FEEDBACK_FORM_URL', default='')

# Gumroad
# ^^^^^^^
GUMROAD_DISCOUNT_CODE = env.str('GUMROAD_DISCOUNT_CODE', default='')
GUMROAD_URL = f'https://gumroad.com/l/burplist/{GUMROAD_DISCOUNT_CODE}'


# Sentry
# ^^^^^^
SENTRY_DSN = env.str('SENTRY_DSN', '')
ENVIRONMENT = env.str('ENVIRONMENT', default='development')
