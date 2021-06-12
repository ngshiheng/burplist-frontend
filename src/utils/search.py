import logging
import secrets
from datetime import datetime, timedelta
from typing import List

from cachetools import TTLCache, cached
from sqlalchemy import and_, or_
from sqlalchemy.orm import sessionmaker
from src.settings import CACHE_MAXSIZE, CACHE_TTL, LAST_N_DAY_DATA
from src.utils.constants import POPULAR_BEER_BRANDS, POPULAR_BEER_STYLES, POPULAR_BEERS
from src.utils.models import Product, db_connect

logger = logging.getLogger(__name__)

engine = db_connect()
session = sessionmaker(bind=engine)()


@cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_TTL))
def get_product_based_on_query(search: str) -> List[Product]:
    logger.info(f'Searching database with user query: "{search}".')
    try:
        return session.query(Product) \
            .filter(
            or_(
                Product.brand.match(f"'{search}'"),
                Product.style.match(f"'{search}'"),
                Product.name.match(f"'{search}'"),
            ),
            and_(Product.updated_on >= datetime.utcnow() - timedelta(days=LAST_N_DAY_DATA)))  \
            .order_by(Product.price_per_quantity) \
            .limit(50) \
            .all()

    except Exception as exception:
        logger.exception(exception)

    finally:
        session.close()


def get_random_beer_style() -> str:
    return secrets.choice(POPULAR_BEER_STYLES)


def get_random_beer_brand() -> str:
    return secrets.choice(POPULAR_BEER_BRANDS)


def get_random_beer() -> str:
    return secrets.choice(POPULAR_BEERS)
