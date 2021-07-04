import logging
import secrets
from datetime import datetime, timedelta
from typing import Optional

from cachetools import TTLCache, cached
from sqlalchemy import and_, func, or_
from sqlalchemy.orm import query, sessionmaker
from src.database.models import Price, Product, db_connect
from src.settings import CACHE_MAXSIZE, CACHE_TTL, LAST_N_DAY_DATA
from src.utils.constants import POPULAR_BEER_BRANDS, POPULAR_BEER_STYLES, POPULAR_BEERS, RESULTS_NOT_FOUND_GIFS

logger = logging.getLogger(__name__)

engine = db_connect()
session = sessionmaker(bind=engine)()

ONE_YEAR_IN_DAYS = 365


@cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_TTL))
def get_product_price_history(product_id: int) -> Optional[query.Query]:
    logger.info(f'Getting price history for product_id: "{product_id}".')

    try:
        return session.query(Price) \
            .filter(Price.product_id == product_id) \
            .order_by(Price.updated_on) \
            .limit(ONE_YEAR_IN_DAYS)

    except Exception as exception:
        logger.exception(exception)

    finally:
        session.close()


@cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_TTL))
def get_product_based_on_query(search_string: str) -> Optional[list[Product]]:
    """
    Reference: https://github.com/sqlalchemy/sqlalchemy/issues/3160#issuecomment-441925498

    # TODO: Implement FTS: https://stackoverflow.com/questions/42388956/create-a-full-text-search-index-with-sqlalchemy-on-postgresql/53217555
    """
    logger.info(f'Searching database with user query: "{search_string}".')

    try:
        tq = func.plainto_tsquery('english', search_string)

        return session.query(Product) \
            .filter(
            or_(
                Product.brand.op('@@')(tq),
                Product.style.op('@@')(tq),
                Product.name.op('@@')(tq),
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


def get_random_results_not_found_gif() -> str:
    gif = secrets.choice(RESULTS_NOT_FOUND_GIFS)
    return f"""
        <p align="center">
            <img alt="No Results Found GIF" class="img" width="50%" height="50%" src="{gif}">
        </p>
    """
