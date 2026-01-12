import spacy
from textblob import TextBlob

# Load spaCy model once
nlp = spacy.load("en_core_web_sm")

def analyze_text(text: str):
    """Analyze message quality using NLP models."""

    doc = nlp(text)

    # Sentiment using TextBlob (simple but effective for demo)
    sentiment = TextBlob(text).sentiment.polarity

    # Detect entities (names, dates, orgs)
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    # Basic readability score (simple heuristic)
    word_count = len(text.split())
    sentence_count = max(1, text.count("."))
    readability = round(word_count / sentence_count, 2)

    return {
        "sentiment": sentiment,
        "entities": entities,
        "word_count": word_count,
        "readability": readability
    }
