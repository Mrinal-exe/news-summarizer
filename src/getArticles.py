import requests
from bs4 import BeautifulSoup


headers = {
    'Dnt' : '1',
    'Referer' : 'https://www.hindustantimes.com/india-news',
    'Sec-Ch-Ua' :'"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122",',
    'Sec-Ch-Ua-Mobile' : '?0',
    'Sec-Ch-Ua-Platform' : 'Windows',
    'Upgrade-Insecure-Requests' : '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'

    }

def get_articles(url):
    
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


