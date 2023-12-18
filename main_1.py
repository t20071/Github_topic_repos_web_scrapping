# importing the necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


# Getting the url
url = r"https://github.com/topics"

# Making the request
response = requests.get(url)

# Checking the status code
if response.status_code != 200:
    raise Exception(f'Failed to load --->> {url}')

# Parsing the response
soup = BeautifulSoup(response.text, "html.parser")

# Get the topic name 
def get_topic_title(soup):
    topic_title_tag = soup.find_all('p', class_="f3 lh-condensed mb-0 mt-1 Link--primary")
    topics = []
    for tag in topic_title_tag:
        topics.append(tag.text)
    return topics

topics = get_topic_title(soup)

# Get the description of the topics
def get_desc(soup):
    topic_desc_tags = soup.find_all("p", class_="f5 color-fg-muted mb-0 mt-1")
    desc = []
    for tag in topic_desc_tags:
        desc.append(tag.text.strip())
    return desc

description = get_desc(soup)

# getting the url of the topics
def get_url(soup):
    url_tags = soup.find_all("a", "no-underline flex-1 d-flex flex-column")
    base_url = 'https://github.com'
    topic_urls = []
    for url in url_tags:
        topic_urls.append(base_url + url['href'])
    return topic_urls

urls = get_url(soup)

# creat the Dataframe
def scrape_topics():
    topics_dict = {
        'Title': topics,
        'description': description,
        'url': url
    }
    return pd.DataFrame(topics_dict)

df = scrape_topics()
df.to_csv('data/data.csv', index=False)








