# -*- coding: utf-8 -*-
"""data_collection.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IOwrjuxe21cWKvvdjEVl5h5c_Bf_8AlU
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

class WebScraper:

    @staticmethod
    def build_url(page_number, sort_by='votes&page='):
        base_url = "https://stackoverflow.com/questions?tab="
        return f'{base_url}{sort_by}{page_number}'

    @staticmethod
    def fetch_page(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return BeautifulSoup(response.content, "html.parser")
        except requests.RequestException as e:
            print(f"Error fetching the page: {e}")
            return None

    @staticmethod
    def extract_questions(soup):
        if not soup:
            return []

        classes_needed = ['.s-post-summary--stats-item-number', '.s-post-summary--content-title', '.s-post-summary--content-excerpt', '.post-tag']
        key_names = ['votes', 'summary', 'question', 'tags']
        question_classes = soup.select('.s-post-summary')
        datas = []

        for question in question_classes:
            question_data = {}
            for i, _class in enumerate(classes_needed):
                sub_element = question.select_one(_class)
                keyname = key_names[i]
                question_data[keyname] = sub_element.text.strip() if sub_element else None
            datas.append(question_data)

        return datas

    @staticmethod
    def scrape_stack_overflow(start_page=1, end_page=50):
        all_data = []
        for page_number in range(start_page, end_page + 1):
            print(f"Scraping page {page_number}...")
            url = WebScraper.build_url(page_number)
            soup = WebScraper.fetch_page(url)
            data = WebScraper.extract_questions(soup)
            all_data.extend(data)
        return pd.DataFrame(all_data)

if __name__ == "__main__":
    start_page = 1
    end_page = 10
    scraper = WebScraper()
    questions_df = scraper.scrape_stack_overflow(start_page=start_page, end_page=end_page)
    print(questions_df)