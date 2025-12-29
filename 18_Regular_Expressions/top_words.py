import re
from collections import Counter


def get_top_words(text, top_n=3, stop_words=None):
    """
    Extract the top N most frequent meaningful words from a text.

    Parameters:
    - text: str → input string
    - top_n: int → number of top words to return
    - stop_words: set → optional set of words to ignore

    Returns:
    - List of tuples: [(word, count), ...] sorted by frequency
    """
    if stop_words is None:
        stop_words = {'i', 'a', 'as', 'to', 'be', 'the', 'and', 'is',
                      'there', 'any', 'this', 'you', 'of', 'in', 'for', 'on', 'at'}

    # Step 1: Clean unwanted characters but keep letters, numbers, punctuation, apostrophes
    cleaned = re.sub(r"[^a-zA-Z0-9\s.,!?']", "", text)

    # Step 2: Convert to lowercase
    cleaned = cleaned.lower()

    # Step 3: Extract words including contractions like "I'm"
    words = re.findall(r"\b\w+(?:'\w+)?\b", cleaned)

    # Step 4: Remove stop words
    filtered_words = [word for word in words if word not in stop_words]

    # Step 5: Count word frequencies
    counts = Counter(filtered_words)

    # Step 6: Return top N words
    return counts.most_common(top_n)
