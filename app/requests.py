from app import app
from .models import Articles, News
import requests

# Getting api key
api_key = app.config["NEWS_API_KEY"]

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

#Getting the articles base url
article_base_url = app.config["ARTICLE_API_BASE_URL"]

def get_sources():
    '''
    Function that gets the json response to our url request
    '''

    get_news_url = base_url + api_key

    get_news_response = requests.get(get_news_url).json()

    if get_news_response['sources']:
        news_results_list = get_news_response['sources']
        news_results = process_results(news_results_list)

        return news_results