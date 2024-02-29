from src.summarise import summa
from src.getArticles import get_articles
from utils.discordWebhook import send_discord_notification
import time

def monitor_websites(websites):
    old_articles = {}
    while True:
        for website, url in websites.items():
            print(f"Checking {website}...")
            new_articles = get_articles(url)
            

            if new_articles != old_articles:
                old_articles = new_articles
                print(f"New articles from {website}:")
                for article in new_articles:                    
                    obj = summa(article['link'])
                    send_discord_notification(obj['title'], obj['summary'], article['link'])
                print("\n")
            else:
                print('Same article detected!')
                
        time.sleep(300)


if __name__ == "__main__":
    websites_to_monitor = {
        'Hindistan Times': 'https://www.hindustantimes.com/latest-news'
    }
    monitor_websites(websites_to_monitor)