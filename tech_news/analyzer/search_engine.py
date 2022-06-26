# Requisito 6
from tech_news.database import search_news
import re


def search_by_title(title):
    regex = re.compile(title, re.IGNORECASE)
    results = search_news({"title": regex})
    response = [(news["title"], news["url"]) for news in results]
    return response


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
