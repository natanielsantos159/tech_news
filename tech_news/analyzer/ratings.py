# Requisito 10
from tech_news.database import find_news
import functools


def compare_popularity(news1, news2):
    if news1["comments_count"] < news2["comments_count"]:
        return 1
    elif news1["comments_count"] > news2["comments_count"]:
        return -1
    elif news1["title"] > news2["title"]:
        return -1
    elif news1["title"] < news2["title"]:
        return 1
    else:
        return 0


def top_5_news():
    news_list = find_news()
    news_list.sort(key=functools.cmp_to_key(compare_popularity))
    response = [(news["title"], news["url"]) for news in news_list[:5]]
    return response


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
