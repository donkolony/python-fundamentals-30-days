"""
Two METHODS to check for similarity 1. Jaccard Similarity (Easy) 2. Cosine Similarity (Professional)

**Jaccard Similarity**

What it checks:
How many words do the texts share?

Formula:
similarity = (common words) / (all uniques words)

Example:
Text A words: {freedom, people, nation}
Text B words: {freedom, nation, unity}

Common = {freedom, nation} → 2
Total unique = {freedom, people, nation, unity} → 4

Similarity = 2 / 4 = 0.5 → 50% similar

**Cosine Similarity (Professional)**
**What it checks:**
“Do the texts use the same words with similar importance?”

It compares word frequency vectors. - Same words - Similar frequency → high similarity - Different words → low similarity

**Used by:**

- search engines
- plagiarism tools
- document clustering
  """
