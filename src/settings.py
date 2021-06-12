from environs import Env

env = Env()
env.read_env()

# In-memory Caching
# ^^^^^^^^^^^^^^^^^
CACHE_TTL = env.int('CACHE_TTL', default=86_400)  # 24 hours
CACHE_MAXSIZE = env.int('CACHE_MAXSIZE', default=128)

# Database
# ^^^^^^^^
DATABASE_CONNECTION_STRING = '{drivername}://{user}:{password}@{host}:{port}/{db_name}'.format(
    drivername='postgresql',
    user=env.str('PG_USERNAME', default='postgres'),
    password=env.str('PG_PASSWORD', default=''),
    host=env.str('PG_HOST', default='localhost'),
    port=env.int('PG_PORT', default='5432'),
    db_name=env.str('PG_DATABASE', default='burplist'),
)
LAST_N_DAY_DATA = env.int('LAST_N_DAY_DATA', default=7)

# SEO
# ^^^
SEO_TITLE = 'Burplist.me - Free Price Comparison Tool for Craft Beers'
SEO_DESCRIPTION = 'Compare online craft beer prices in Singapore.'

# Misc
CONTACT_EMAIL = env.str('CONTACT_EMAIL', default='hello@burplist.me')

GUMROAD_URL = env.str('GUMROAD_URL', default='https://gumroad.com/l/burplist')

RECONNECT_TIMEOUT = env.int('RECONNECT_TIMEOUT', default=60)

STATIC = '/static/'

ALLOWED_ORIGINS = env.list('ALLOWED_ORIGINS', default=['*://*.burplist.me'])
