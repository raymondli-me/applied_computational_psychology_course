# Module 5 Flashcards: Embeddings

**Total Cards:** 22
**Format:** Anki-compatible (Front/Back)

---

## Definitions (6 cards)

### Card 1
**Front:** What is an embedding?
**Back:** A numerical vector (list of numbers) representing the semantic meaning of text. Computers can only do math on numbers, so embeddings convert meaning into calculable form.
**Tags:** M5, definition, embeddings

### Card 2
**Front:** What is a vector?
**Back:** An ordered list of numbers. A 768-dimensional embedding is a vector of 768 numbers: [0.23, -0.45, 0.12, ...]. Each dimension captures some aspect of meaning.
**Tags:** M5, definition, embeddings

### Card 3
**Front:** What is cosine similarity?
**Back:** Measures the angle between two vectors. 1 = same direction (identical meaning), 0 = perpendicular (unrelated), -1 = opposite direction (opposite meaning).
**Tags:** M5, definition, similarity

### Card 4
**Front:** What is semantic similarity?
**Back:** How similar two texts are in MEANING, not just words. "I love dogs" and "Canines are my favorite" have high semantic similarity despite different words.
**Tags:** M5, definition, similarity

### Card 5
**Front:** What is a pre-trained model?
**Back:** A model already trained on massive data (billions of texts). We use its learned knowledge rather than training from scratch - faster, cheaper, often better.
**Tags:** M5, definition, models

### Card 6
**Front:** What are BERT embeddings?
**Back:** 768-dimensional vectors from the BERT model. Industry standard for semantic representation. Captures context (same word = different embedding based on surrounding text).
**Tags:** M5, definition, models

---

## Concepts (6 cards)

### Card 7
**Front:** Why can't we just compare words directly?
**Back:** Word matching misses meaning. "I love canines" and "I adore dogs" share 0 words but same meaning. Embeddings capture meaning, not surface form.
**Tags:** M5, concept, embeddings

### Card 8
**Front:** What does "768 dimensions" mean for text embeddings?
**Back:** Each text is represented by 768 numbers. Each dimension captures some aspect of meaning (topics, style, sentiment). Collectively they encode the text's semantic content.
**Tags:** M5, concept, embeddings

### Card 9
**Front:** Why use pre-trained models instead of training your own?
**Back:** Training requires: 1) Billions of text examples, 2) Specialized hardware (GPUs), 3) Weeks of compute time. Pre-trained models already learned language understanding. Just use them.
**Tags:** M5, concept, models

### Card 10
**Front:** What can you do with embeddings?
**Back:** 1) Find similar texts (cosine similarity), 2) Cluster texts by meaning, 3) Semantic search ("find posts like this"), 4) Predict outcomes from meaning, 5) Visualize (with UMAP).
**Tags:** M5, concept, applications

### Card 11
**Front:** Why might two AI headlines be similar despite different details?
**Back:** Embeddings capture SEMANTIC meaning, not surface details. "AI startup raises $50M" and "Tech company secures $45M for AI" share: topic (AI funding), structure (company + money), meaning (investment).
**Tags:** M5, concept, similarity

### Card 12
**Front:** Why might same-topic texts be DISSIMILAR in embedding space?
**Back:** Different framing/context. "AI cures disease" vs "AI threatens jobs" both mention AI but: different domains (health vs labor), tone (positive vs negative), actors (researchers vs workers).
**Tags:** M5, concept, similarity

---

## Code Patterns (5 cards)

### Card 13
**Front:** How to load pre-computed embeddings:
**Back:**
```python
df = load_dataset("clara_bert_embeddings")
# Embedding columns are Dim_1 through Dim_768
embedding_cols = [c for c in df.columns if c.startswith('Dim_')]
embeddings = df[embedding_cols].values
```
**Tags:** M5, code, loading

### Card 14
**Front:** How to compute cosine similarity between texts:
**Back:**
```python
from sklearn.metrics.pairwise import cosine_similarity
sim_matrix = cosine_similarity(embeddings)
# sim_matrix[i,j] = similarity between text i and j
```
**Tags:** M5, code, similarity

### Card 15
**Front:** How to find the most similar pair:
**Back:**
```python
import numpy as np
np.fill_diagonal(sim_matrix, 0)  # Ignore self-similarity
i, j = np.unravel_index(sim_matrix.argmax(), sim_matrix.shape)
print(f"Most similar: {i} and {j}, sim={sim_matrix[i,j]:.3f}")
```
**Tags:** M5, code, similarity

### Card 16
**Front:** How to generate your own embeddings:
**Back:**
```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(df['text'].tolist())
```
**Tags:** M5, code, generation

### Card 17
**Front:** How to do semantic search:
**Back:**
```python
query_emb = model.encode(["find posts about this topic"])
sims = cosine_similarity(query_emb, all_embeddings)[0]
top_idx = sims.argsort()[-5:][::-1]  # Top 5
```
**Tags:** M5, code, search

---

## Interpretation (3 cards)

### Card 18
**Front:** Cosine similarity = 0.95 between two texts. Interpret.
**Back:** Extremely similar meaning. Nearly identical semantic content. Could be: paraphrases, near-duplicates, or discussing exactly the same topic with same framing.
**Tags:** M5, interpretation, similarity

### Card 19
**Front:** Cosine similarity = 0.40 between two texts. Interpret.
**Back:** Moderate similarity. Some shared semantic content (maybe same broad domain) but different specific topics or framing. Not closely related, not completely unrelated.
**Tags:** M5, interpretation, similarity

### Card 20
**Front:** Cosine similarity = -0.10 between two texts. Interpret.
**Back:** Essentially unrelated. Slight negative values are often noise - treat as "no relationship." The texts discuss completely different topics or have opposing frames.
**Tags:** M5, interpretation, similarity

---

## Common Mistakes (2 cards)

### Card 21
**Front:** What's wrong with: "Texts with similarity 0.8 are 80% the same"?
**Back:** Cosine similarity isn't a percentage. 0.8 means vectors point in similar directions, not that texts share 80% of content. Interpretation is relative: 0.8 is "high" but exact meaning depends on context.
**Tags:** M5, mistake, interpretation

### Card 22
**Front:** Why shouldn't you interpret individual embedding dimensions?
**Back:** Dimensions don't have clear meanings like "topic" or "sentiment." They're learned statistical patterns, collectively encoding meaning. Don't try to interpret dim_47 alone - interpret the vector as a whole.
**Tags:** M5, mistake, interpretation

---

*Module 5 Flashcards | Applied Psychological Data Science*
