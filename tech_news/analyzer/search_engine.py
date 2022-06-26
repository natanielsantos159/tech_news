# Requisito 6
from tech_news.database import search_news
import re
import datetime


def search_by_title(title):
    regex = re.compile(title, re.IGNORECASE)
    results = search_news({"title": regex})
    response = [(news["title"], news["url"]) for news in results]
    return response


# Source: https://stackoverflow.com/a/16870699/17502226
def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 7
def search_by_date(date):
    validate_date(date)

    month_list = [
        "janeiro",
        "fevereiro",
        "março",
        "abril",
        "maio",
        "junho",
        "julho",
        "agosto",
        "setembro",
        "outubro",
        "novembro",
        "dezembro",
    ]

    year, month, day = re.findall(r"\d+", date)

    date_str = f"{int(day)} de {month_list[int(month) - 1]} de {year}"
    results = search_news({"timestamp": date_str})

    response = [(news["title"], news["url"]) for news in results]
    return response


# Requisito 8
def search_by_tag(tag):
    regex = re.compile(tag, re.IGNORECASE)
    results = search_news({"tags": regex})
    response = [(news["title"], news["url"]) for news in results]
    return response


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
