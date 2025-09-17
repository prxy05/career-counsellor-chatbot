import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# make sure to run these once in your environment:
# nltk.download('punkt')
# nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def clean_text(text: str) -> str:
    """Tokenize, remove punctuation and stopwords, return cleaned string."""
    tokens = word_tokenize(text.lower())
    tokens = [t for t in tokens if t not in string.punctuation]
    tokens = [t for t in tokens if t not in stop_words]
    return ' '.join(tokens)

if __name__ == '__main__':
    sample = "I like Python, machine learning and building web apps."
    print(clean_text(sample))
