# Module 5 Lab: Creating and Using Embeddings

## Lab Overview
**Duration:** 60 minutes
**Tools Required:** Google Colab, HuggingFace sentence-transformers
**Dataset:** Choose from course dataset bank (see below)
**Notebook:** `04_embeddings_boilerplate.ipynb`

---

## Dataset Options for This Lab

### Option A: Use Pre-Computed Embeddings (Recommended for Learning)

```python
# === DATASET LOADER ===
import pandas as pd, json, urllib.request
GCS_BUCKET = "variable-resolution-applied-computational-psychology-course"
CATALOG_URL = f"https://storage.googleapis.com/{GCS_BUCKET}/manifest.json"
with urllib.request.urlopen(CATALOG_URL) as r:
    CATALOG = json.loads(r.read().decode())

def load_dataset(name, nrows=None):
    for ds in CATALOG['datasets']:
        if ds['canonical_name'] == name:
            return pd.read_csv(ds['access']['public_url'], nrows=nrows)
    raise ValueError(f"Dataset '{name}' not found")

# Clara's BERT embeddings - 12,915 texts with 768 dimensions pre-computed
# Skip the computation, focus on interpretation!
df = load_dataset("clara_bert_embeddings")
print(f"Shape: {df.shape} (rows with 768-dimensional embeddings)")
```

*Clara computed these embeddings for her political text comparison - ready for cosine similarity and clustering.*

### Option B: Generate Your Own Embeddings (More Time)

Use a smaller dataset:
```python
# Yashita's data - small enough to embed in class
df = load_dataset("yashita_yashita_data")  # 4,689 rows
```

**See:** `DATASETS_FOR_M5.md` for all embedding datasets.

---

## Learning Goals
By the end of this lab, you will:
- Generate embeddings for text data using a pre-trained model
- Calculate cosine similarity between texts
- Find the most similar and most different pairs in your data
- Save embeddings for use in Module 6

---

## Setup Instructions

### Step 1: Open the Course Notebook
1. Open your course notebook in Colab
2. Make sure you've run the setup cell with `load_dataset()`
3. Load Clara's pre-computed embeddings (recommended) or your own data

### Step 2: Verify GPU (Optional but Faster)
1. Runtime > Change runtime type
2. Hardware accelerator: GPU (if available)
3. Click Save

---

## Part 1: Setup and Model Loading (10 minutes)

### Cell 1: Install Libraries

```python
# ============================================
# SETUP - Install required libraries
# ============================================
!pip install sentence-transformers pandas numpy scipy -q

print("Libraries installed!")
```

### Cell 2: Import and Load Model

```python
# ============================================
# IMPORT AND LOAD MODEL
# ============================================
from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
from scipy.spatial.distance import cosine

# Load the embedding model
# MiniLM is fast and produces 384-dimensional embeddings
print("Loading model... (this may take a minute)")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("Model loaded!")

# Check model info
print(f"Model: all-MiniLM-L6-v2")
print(f"Embedding dimensions: {model.get_sentence_embedding_dimension()}")
```

### Cell 3: Load Your Data

```python
# ============================================
# LOAD YOUR DATA
# ============================================

# Replace with your filename from Module 4
FILENAME = "your_collected_data.csv"  # <-- CHANGE THIS

df = pd.read_csv(FILENAME)
print(f"Loaded {len(df)} rows")
print(f"Columns: {list(df.columns)}")

# We'll embed the title (or full_text if available)
TEXT_COLUMN = "title"  # <-- CHANGE if using different column

print(f"\nSample texts to embed:")
for text in df[TEXT_COLUMN].head(5):
    print(f"  - {text[:60]}...")
```

---

## Part 2: Generate Embeddings (15 minutes)

### Cell 4: Create Embeddings

```python
# ============================================
# GENERATE EMBEDDINGS
# ============================================

print("Generating embeddings... (this may take 1-2 minutes)")

# Get list of texts
texts = df[TEXT_COLUMN].tolist()

# Generate embeddings for all texts
# The model handles batching automatically
embeddings = model.encode(texts, show_progress_bar=True)

# Convert to numpy array
embeddings = np.array(embeddings)

print(f"\nEmbeddings generated!")
print(f"Shape: {embeddings.shape}")
print(f"  → {embeddings.shape[0]} documents")
print(f"  → {embeddings.shape[1]} dimensions per document")
```

### Cell 5: Examine an Embedding

```python
# ============================================
# EXAMINE A SINGLE EMBEDDING
# ============================================

# Pick the first text
first_text = texts[0]
first_embedding = embeddings[0]

print("First text:")
print(f"  '{first_text}'\n")

print("Its embedding (first 20 numbers):")
print(first_embedding[:20])

print(f"\nEmbedding statistics:")
print(f"  Min: {first_embedding.min():.4f}")
print(f"  Max: {first_embedding.max():.4f}")
print(f"  Mean: {first_embedding.mean():.4f}")
print(f"  Std: {first_embedding.std():.4f}")
```

**Question to Answer:**
What do these numbers represent? (Hint: They don't have individual meanings—together they encode semantic content)

---

## Part 3: Calculate Similarity (20 minutes)

### Cell 6: Cosine Similarity Function

```python
# ============================================
# COSINE SIMILARITY FUNCTION
# ============================================

def cosine_similarity(vec1, vec2):
    """
    Calculate cosine similarity between two vectors.
    Returns value from -1 (opposite) to 1 (identical).
    """
    return 1 - cosine(vec1, vec2)  # scipy.cosine is distance, so 1 - distance = similarity

# Test with first two embeddings
sim = cosine_similarity(embeddings[0], embeddings[1])
print(f"Similarity between text 0 and text 1: {sim:.4f}")
print(f"\nText 0: {texts[0][:60]}...")
print(f"Text 1: {texts[1][:60]}...")
```

### Cell 7: Find Most Similar Pair

```python
# ============================================
# FIND MOST SIMILAR PAIR
# ============================================
from itertools import combinations

print("Finding most similar pair...")
print("(This checks all pairs - may take a moment)\n")

max_similarity = -1
most_similar_pair = (0, 0)

# Compare all pairs
n = len(embeddings)
for i, j in combinations(range(n), 2):
    sim = cosine_similarity(embeddings[i], embeddings[j])
    if sim > max_similarity:
        max_similarity = sim
        most_similar_pair = (i, j)

# Report results
i, j = most_similar_pair
print("=" * 60)
print("MOST SIMILAR PAIR")
print("=" * 60)
print(f"\nSimilarity score: {max_similarity:.4f}")
print(f"\nText {i}:")
print(f"  {texts[i]}")
print(f"\nText {j}:")
print(f"  {texts[j]}")
```

**Question to Answer:**
Do these two texts seem semantically similar to you? Why might the model see them as similar?

### Cell 8: Find Most Different Pair

```python
# ============================================
# FIND MOST DIFFERENT PAIR
# ============================================

print("Finding most different pair...")

min_similarity = 2  # Start high
most_different_pair = (0, 0)

for i, j in combinations(range(n), 2):
    sim = cosine_similarity(embeddings[i], embeddings[j])
    if sim < min_similarity:
        min_similarity = sim
        most_different_pair = (i, j)

# Report results
i, j = most_different_pair
print("=" * 60)
print("MOST DIFFERENT PAIR")
print("=" * 60)
print(f"\nSimilarity score: {min_similarity:.4f}")
print(f"\nText {i}:")
print(f"  {texts[i]}")
print(f"\nText {j}:")
print(f"  {texts[j]}")
```

### Cell 9: Find Similar to a Query

```python
# ============================================
# FIND SIMILAR TO A SPECIFIC QUERY
# ============================================

# Enter your own query text here
QUERY = "mental health and wellbeing"  # <-- CHANGE THIS

# Generate embedding for query
query_embedding = model.encode([QUERY])[0]

# Find most similar in dataset
similarities = []
for i, emb in enumerate(embeddings):
    sim = cosine_similarity(query_embedding, emb)
    similarities.append((i, sim))

# Sort by similarity
similarities.sort(key=lambda x: x[1], reverse=True)

# Show top 5
print(f"TOP 5 MOST SIMILAR TO: '{QUERY}'")
print("=" * 60)
for rank, (idx, sim) in enumerate(similarities[:5], 1):
    print(f"\n{rank}. Similarity: {sim:.4f}")
    print(f"   {texts[idx]}")
```

---

## Part 4: Save for Module 6 (10 minutes)

### Cell 10: Save Embeddings

```python
# ============================================
# SAVE EMBEDDINGS FOR MODULE 6
# ============================================

# Save embeddings as numpy file
np.save('embeddings.npy', embeddings)
print("Embeddings saved to: embeddings.npy")

# Save the texts for reference
df_with_embeddings = df.copy()
df_with_embeddings['embedding_index'] = range(len(df))
df_with_embeddings.to_csv('data_with_embedding_index.csv', index=False)
print("Data index saved to: data_with_embedding_index.csv")

# Files are saved in Colab's /content/ folder
# They persist for the session and can be used in Module 6

print("\nFiles saved! Ready for Module 6 visualization.")
```

### Cell 11: Summary Statistics

```python
# ============================================
# EMBEDDING SUMMARY
# ============================================

print("EMBEDDING SUMMARY")
print("=" * 60)
print(f"Total documents: {len(texts)}")
print(f"Embedding dimensions: {embeddings.shape[1]}")
print(f"Total numbers generated: {embeddings.size:,}")
print(f"\nAverage pairwise similarity: {np.mean([cosine_similarity(embeddings[0], embeddings[i]) for i in range(1, min(100, len(embeddings)))]):.4f}")
print(f"\nReady for dimensionality reduction in Module 6!")
```

---

## Submission Checklist

### Required Deliverables:

1. **Screenshot:** Embedding shape output (showing n_docs × 384)

2. **Most Similar Pair:**
   - Text 1: _______________
   - Text 2: _______________
   - Similarity: _______________

3. **Interpretation (2-3 sentences):**
   Why do you think these two texts were identified as most similar? What semantic features do they share?

4. **Saved Files:** Confirm these exist in your Colab environment:
   - embeddings.npy
   - data_with_embedding_index.csv

---

## Troubleshooting

**"CUDA out of memory"**
- Reduce batch size: `model.encode(texts, batch_size=32)`
- Or switch to CPU runtime

**"Very slow embedding generation"**
- This is normal on CPU; try GPU runtime
- For large datasets, embed in batches

**"All similarities are very high (> 0.9)"**
- Your texts might be very similar (e.g., all about the same narrow topic)
- This is okay—it just means your corpus is focused

**"All similarities are very low (< 0.3)"**
- Your texts might be very diverse
- Or your data has noise/irrelevant content

---

## Challenge Extension (Optional)

1. **Try a different model:**
```python
model2 = SentenceTransformer('all-mpnet-base-v2')  # 768 dimensions
```
Compare: Do the similar pairs change?

2. **Embedding arithmetic:**
```python
# Try: happy - sad + angry = ?
happy = model.encode(["happy"])[0]
sad = model.encode(["sad"])[0]
angry = model.encode(["angry"])[0]

result = happy - sad + angry
# Find closest word to result
```

3. **Cluster analysis preview:**
```python
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=5)
clusters = kmeans.fit_predict(embeddings)
df['cluster'] = clusters
print(df.groupby('cluster')[TEXT_COLUMN].head(2))
```
