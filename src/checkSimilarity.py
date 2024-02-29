from itertools import combinations
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(content1, content2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([content1, content2])
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return similarity_matrix[0, 1]

# Example articles (replace with your actual articles)
articles = [
    "This is the content of article 1.",
    "Here is the content of article 2, which is similar to article 1.",
    "Content of article 3.",
    "Article 4 has some unique content.",
    "This is the content of the fifth article."
]

# Generate pairs of articles
article_pairs = list(combinations(articles, 2))

# Check similarity for each pair
for pair in article_pairs:
    article1, article2 = pair
    similarity_score = calculate_similarity(article1, article2)
    print(f"Similarity Score between Article 1 and Article 2: {similarity_score}")


# Assuming similarity_score is the result of your similarity calculation
threshold = 0.7

if similarity_score >= threshold:
    print("The articles are similar.")
else:
    print("The articles are not similar.")
