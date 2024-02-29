from newspaper import Article, Config
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


config = Config()
config.memoize_articles = False


def summa(url):
    try:
        article = Article(url, config=config)
        article.download()
        article.parse()

        title = article.title
        content = article.text

        parser = PlaintextParser.from_string(content, Tokenizer('english'))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, 3)

        finalSummary = ''
        print(f"Title: {title}")
        print("Summary:")
        for sentence in summary:
            finalSummary = finalSummary+str(sentence)
            print(sentence)


        summaryObject = {'title' : title, 'summary' : finalSummary}
        return summaryObject

    except Exception as e:
        print(f"Error processing {url}: {e}")

