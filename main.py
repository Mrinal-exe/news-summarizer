import time
from src.summarise import summarize_article
from src.getArticles import get_hindustan_articles, get_toi_articles, get_ndtv_articles, get_india_today_articles
from utils.discordWebhook import send_discord_notification


def fetch_articles():
    hindustan_articles = get_hindustan_articles()
    toi_articles = get_toi_articles()
    ndtv_articles = get_ndtv_articles()
    it_articles = get_india_today_articles()

    articles_dict = {
        'Hindustan Times': hindustan_articles,
        'Times of India': toi_articles,
        'NDTV' : ndtv_articles,
        'India Today' : it_articles
    }

    return articles_dict

def monitor_websites():
    old_articles = {}

    while True:
        websites_articles = fetch_articles()

        for website, articles in websites_articles.items():
            try:
                if articles != old_articles.get(website):
                    old_articles[website] = articles
                    print(f"New articles from {website}:")
                    for article in articles:
                        obj = summarize_article(article['link'])
                        send_discord_notification(obj['title'], obj['summary'], article['link'])
                    print("\n")
                else:
                    print(f'No new articles detected on {website}')
            except Exception as e:
                print(f"Error processing {website}: {e}")

        time.sleep(300)

if __name__ == "__main__":
    monitor_websites()
