import requests
from bs4 import BeautifulSoup



def get_hindustan_articles():
    url = 'https://www.hindustantimes.com/latest-news'
    headers = {
        'Dnt' : '1',
        'Referer' : 'https://www.hindustantimes.com/india-news',
        'Sec-Ch-Ua' :'"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122",',
        'Sec-Ch-Ua-Mobile' : '?0',
        'Sec-Ch-Ua-Platform' : 'Windows',
        'Upgrade-Insecure-Requests' : '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'

        }
    
    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            articles = []
            h3 = soup.find_all('h3', class_='hdg3')

            for i, article in enumerate(h3):
                if i>=5:
                    break
                title = article.text.strip()
                link = article.a.get('href', '')
                articles.append({'title': title, 'link': f'https://www.hindustantimes.com{link}'})


            return articles

    except Exception as e:
        print(f"Error fetching articles from {url}: {e}")
        return []


def get_toi_articles():
    url = 'https://timesofindia.indiatimes.com/'
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            articles = []
            divs = soup.find_all('div', class_='col_l_6')

            for i, article in enumerate(divs):
                if i>=5:
                    break
                title = article.text.strip()
                link = article.a.get('href', '')
                articles.append({'title': title, 'link': link})


            return articles

    except Exception as e:
        print(f"Error fetching articles from {url}: {e}")
        return []
    

def get_ndtv_articles():
    url = 'https://www.ndtv.com/latest#pfrom=home-ndtv_mainnavgation'
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            articles = []
            divs = soup.find_all('div', class_='news_Itm')

            for i, article in enumerate(divs):
                if i >= 6:
                    break
                title_tag = article.find('h2', class_='newsHdng')
                if title_tag:
                    title = title_tag.a.text.strip() if title_tag.a else title_tag.text.strip()
                    link = title_tag.a.get('href') if title_tag.a else None
                    articles.append({'title': title, 'link': link})

            return articles

    except Exception as e:
        print(f"Error fetching articles from {url}: {e}")
        return []
    

def get_india_today_articles():
    url = 'https://www.indiatoday.in/'
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            articles = []
            divs = soup.find_all('article')

            for i, article in enumerate(divs):
                if i>=5:
                    break
                title = article.find('h2').text.strip()
                link = article.a.get('href', '')
                articles.append({'title': title, 'link': f'https://www.indiatoday.in{link}'})

            return articles

    except Exception as e:
        print(f"Error fetching articles from {url}: {e}")
        return []