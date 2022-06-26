import time
import requests
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    try:
        time.sleep(1)
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news_links = selector.css('.entry-title a::attr(href)').getall()
    return news_links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css('a.next::attr(href)').get()
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    link = selector.css('link[rel="canonical"]::attr(href)').get()
    title = selector.css("h1.entry-title::text").get()
    date = selector.css("li.meta-date::text").get()
    author = selector.css("span.author a::text").get()
    comments_count = selector.css("#comments .title-block::text").re(r"\d")
    category = selector.css("span.label::text").get()
    summary = selector.css(".entry-content > p:first-of-type *::text").getall()
    tags = selector.css('.post-tags a[rel="tag"]::text').getall()

    news_info = {
        "url": link,
        "title": title,
        "timestamp": date,
        "writer": author,
        "comments_count": int(comments_count or 0),
        "summary": ''.join(summary),
        "tags": tags,
        "category": category,
    }

    return news_info


# Requisito 5
def get_tech_news(amount):
    html_content = fetch("https://blog.betrybe.com/")
    news_links = scrape_novidades(html_content)
    next_page_link = scrape_next_page_link(html_content)

    while len(news_links) < amount and next_page_link:
        next_page_content = fetch(next_page_link)
        more_news_links = scrape_novidades(next_page_content)
        news_links.extend(more_news_links)
        next_page_link = scrape_next_page_link(html_content)

    if len(news_links) > amount:
        news_links = news_links[:amount]

    news_dict_list = []
    for link in news_links:
        news_html_content = fetch(link)
        news_dict = scrape_noticia(news_html_content)
        news_dict_list.append(news_dict)

    create_news(news_dict_list)

    return news_dict_list
