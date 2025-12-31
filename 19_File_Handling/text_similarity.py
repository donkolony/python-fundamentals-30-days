"""
text_similarity.py

A small utility module for comparing the similarity of two text documents.
It supports:
- Text preprocessing using regular expressions
- Stop-word removal
- Jaccard similarity
- Cosine similarity

Author: Don
"""

import re
import math
import collections


def preprocess_text(text):
    """
    Clean and tokenize text.

    Steps:
    - Convert text to lowercase
    - Extract only alphabetic words using regex

    Args:
        text (str): Raw input text

    Returns:
        list[str]: List of cleaned words
    """
    text = text.lower()
    pattern = r'\b[a-z]+\b'
    return re.findall(pattern, text)


def remove_stop_words(words, stop_words):
    """
    Remove stop words from a list of words.

    Args:
        words (list[str]): Tokenized words
        stop_words (set or list): Stop words to exclude

    Returns:
        list[str]: Words with stop words removed
    """
    return [word for word in words if word not in stop_words]


def jaccard_similarity(words_a, words_b):
    """
    Compute Jaccard similarity between two word lists.

    Jaccard similarity = (intersection / union) * 100

    Args:
        words_a (list[str])
        words_b (list[str])

    Returns:
        float: Similarity percentage
    """
    set_a, set_b = set(words_a), set(words_b)

    if not set_a and not set_b:
        return 0.0

    similarity = len(set_a & set_b) / len(set_a | set_b)
    return similarity * 100


def cosine_similarity(words_a, words_b):
    """
    Compute cosine similarity between two word lists.

    Uses word frequency vectors and cosine distance.

    Args:
        words_a (list[str])
        words_b (list[str])

    Returns:
        float: Similarity percentage
    """
    freq_a = collections.Counter(words_a)
    freq_b = collections.Counter(words_b)

    all_words = set(freq_a) | set(freq_b)

    dot_product = sum(freq_a[word] * freq_b[word] for word in all_words)

    magnitude_a = math.sqrt(sum(count ** 2 for count in freq_a.values()))
    magnitude_b = math.sqrt(sum(count ** 2 for count in freq_b.values()))

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    similarity = dot_product / (magnitude_a * magnitude_b)
    return similarity * 100


def read_text_source(source):
    """
    Read input from a text file or return the input string directly.

    Args:
        source (str): File path (.txt) or raw text

    Returns:
        str: Text content
    """
    if source.endswith(".txt"):
        with open(source, encoding="utf-8", errors="ignore") as file:
            return file.read()

    return source
