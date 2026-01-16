# Module 5: Lecture Script
## "The Geometry of Meaning: How Computers Understand Text"

**Total Runtime:** ~37 minutes
**Video Production Ready:** Yes

---

### INTRO [0:00-2:00]
*[INSTRUCTOR NOTE: The "768 numbers" revelation should spark curiosity—this is the conceptual leap]*

**[SLIDE: Clara's 12,915 Political Texts as Vectors]**

*"Clara analyzed 12,915 political texts. Each text became 768 numbers. Andrea embedded 13,000 wedding posts. Agatha converted 314,000 dance comments into vectors."*

*"How do you compare thousands of texts to each other? You turn them into geometry."*

*"Today, we learn how to turn words into numbers—numbers that preserve meaning. And you can use the embeddings Clara, Andrea, and Agatha already computed, or generate your own."*

---

### SECTION 1: THE PROBLEM [2:00-7:00]
*[INSTRUCTOR NOTE: The "dog/canine" example establishes why simple string matching fails]*

**[SLIDE: Computer looking confused at text]**

*"Here's the fundamental problem: Computers don't read. They compute. They do math on numbers."*

*"If I give a computer two sentences:"*
- *"The dog chased the cat"*
- *"The canine pursued the feline"*

*"To a computer, these are just different strings of characters. Totally unrelated. But WE know they mean the same thing."*

**[SLIDE: Old approach - bag of words]**

*"Old approach: Count words. 'Dog' appears once, 'cat' appears once. But this misses:"*
- *Synonyms (dog ≠ canine to a word counter)*
- *Context (bank = river bank or money bank?)*
- *Meaning (word order doesn't matter in counting)*

**[SLIDE: New approach - embeddings]**

*"Modern approach: Embeddings. Instead of counting words, we convert entire sentences into VECTORS—lists of numbers that capture MEANING."*

---

### SECTION 2: WHAT IS AN EMBEDDING? [7:00-15:00]
*[INSTRUCTOR NOTE: Build intuition step-by-step—1D to 2D to many dimensions. Don't rush this]*

**[SLIDE: Single number line]**

*"Let's build intuition. Imagine a number line from -1 to +1."*

*"We could place words on it by sentiment:"*
- *"Terrible" at -0.9*
- *"Okay" at 0*
- *"Amazing" at +0.9*

*"Now we have numbers representing meaning. 'Terrible' and 'Amazing' are far apart. 'Okay' is in the middle."*

**[SLIDE: Two dimensions]**

*"One dimension isn't enough. Let's add another: formality."*

*"Now we have a 2D map:"*
- *"Yo" = (casual, neutral) = (-0.8, 0)*
- *"Greetings" = (formal, neutral) = (+0.8, 0)*
- *"This is terrible, sir" = (formal, negative) = (+0.7, -0.8)*

*"The MORE dimensions we have, the MORE aspects of meaning we can capture."*

**[SLIDE: 384 dimensions]**

*"Real embedding models use 384 to 4096 dimensions. Each dimension captures some subtle aspect of meaning. We can't visualize 384 dimensions, but math still works."*

*"The key insight: SIMILAR MEANINGS cluster together. If two texts mean similar things, their vectors will point in similar directions."*

---

### SECTION 3: THE FAMOUS EXAMPLE [15:00-20:00]
*[PAUSE: Check understanding of dimensions before the King-Queen example]*

**[SLIDE: King - Man + Woman = ?]**

*"Here's the most famous example of embedding magic."*

*"If you take the embedding for 'King', subtract the embedding for 'Man', and add the embedding for 'Woman'..."*

**[CLICK: = Queen]**

*"...you get something very close to the embedding for 'Queen'!"*

*"This works because embeddings encode RELATIONSHIPS:"*
- *King is to Man as Queen is to Woman*
- *The gender relationship is captured as a direction in the space*

*"This is wild. Mathematical operations on word vectors produce meaningful results."*

**[Caveat slide]**

*"Now, this example is famous but simplified. It doesn't always work this cleanly. But it demonstrates the core idea: meaning is captured geometrically."*

---

### SECTION 4: MEASURING SIMILARITY [20:00-27:00]
*[INSTRUCTOR NOTE: Cosine similarity is the practical tool—focus on interpretation, not formula]*

**[SLIDE: Two arrows]**

*"How do we measure if two embeddings are similar?"*

*"We use COSINE SIMILARITY. It measures the angle between two vectors."*

**[SLIDE: Cosine similarity visual]**

*"If two vectors point in the same direction: cosine similarity = 1 (identical meaning)"*

*"If they're perpendicular: cosine similarity = 0 (unrelated meaning)"*

*"If they point opposite: cosine similarity = -1 (opposite meaning)"*

**[SLIDE: Formula]**

```
cosine_similarity = dot(A, B) / (|A| * |B|)
```

*"Don't worry about the formula—the code does this for you. Just understand the concept: we're measuring how 'aligned' two meanings are."*

**[SLIDE: Example]**

*"Let's say we have three headlines:"*
1. *"Scientists discover new treatment for depression"*
2. *"Researchers find promising therapy for mental illness"*
3. *"Stock market crashes amid recession fears"*

*"Headlines 1 and 2 would have high cosine similarity (both about mental health research)."*

*"Headlines 1 and 3 would have low cosine similarity (totally different topics)."*

---

### SECTION 5: HOW THE MODEL WORKS (SIMPLIFIED) [27:00-32:00]
*[INSTRUCTOR NOTE: "Black box" framing relieves anxiety—students don't need to understand internals]*

**[SLIDE: Black box transformer]**

*"Where do these magical numbers come from? From a pre-trained model."*

*"Think of it as a black box. Text goes in, vector comes out."*

**[SLIDE: Training process]**

*"How was it trained? On BILLIONS of text examples. The model learned patterns:"*
- *'Cat' appears near 'pet', 'meow', 'fur'*
- *'King' appears near 'queen', 'throne', 'royal'*

*"By seeing these patterns billions of times, the model learned to place similar words/sentences close together in vector space."*

**[SLIDE: We don't train, we use]**

*"The good news: We don't train this model. That would take massive resources. We just USE a pre-trained model. Like borrowing a calculator instead of building one."*

*"In lab, you'll use a model called MiniLM. It's small, fast, and already trained. You just feed it text and get vectors."*

---

### WRAP-UP [32:00-34:00]

**[SLIDE: Today's Takeaways]**

*"Key points:"*

1. *"Embeddings convert text to vectors (lists of numbers)"*
2. *"Similar meanings = similar vectors = close in high-dimensional space"*
3. *"Cosine similarity measures how aligned two vectors are"*
4. *"We use pre-trained models—no need to understand the internals"*
5. *"This is how modern NLP makes text computable"*

*"In lab, you'll turn your own collected headlines into embeddings. You'll find which ones are most similar, and start to see the 'shape' of your data. This is the foundation for the visualizations you'll create in Module 6."*

*"Let's make some vectors."*

---

### SECTION 6: USING COURSE EMBEDDINGS [34:00-37:00]
*[LIVE CODING: Load Clara's embeddings and show the shape—students follow along]*

**[LIVE DEMO: Pre-computed embeddings]**

```python
# Load Clara's pre-computed BERT embeddings
df = load_dataset("clara_bert_embeddings")
print(f"Loaded {len(df):,} texts with 768-dimensional embeddings")

# The embeddings are already computed - just analyze!
from sklearn.metrics.pairwise import cosine_similarity
embedding_cols = [c for c in df.columns if c.startswith('dim_')]
embeddings = df[embedding_cols].values
print(f"Shape: {embeddings.shape}")  # (12915, 768)
```

*"Clara, Andrea, and Agatha each spent hours computing these embeddings on Google Colab. You can use their pre-computed vectors and skip straight to the analysis. Or use Yashita's small dataset (4,689 rows) to practice generating embeddings yourself."*

---

### LECTURE MATERIALS CHECKLIST
- [ ] Pre-computed embedding demo (Clara's data)
- [ ] Number line visualization
- [ ] 2D and 3D space animations
- [ ] King/Queen example graphic
- [ ] Cosine similarity diagram
- [ ] Transformer black box visual
- [ ] DATASETS_FOR_M5.md reference card
