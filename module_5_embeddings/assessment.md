# Module 5 Assessment: Embeddings

**Recommended Dataset:** `clara_bert_embeddings` (12,915 texts with 768D BERT embeddings)
**Alternate Datasets:** Andrea's wedding embeddings, Agatha's dance embeddings
**See:** DATASETS_FOR_M5.md for all pre-computed embedding options

---

## Part A: Concept Check (35 points)

### Question 1 (7 points)
What is an embedding, and why is it useful for computational text analysis?

**Model Answer:** An embedding is a numerical vector (list of numbers) that represents the semantic meaning of text. It's useful because computers can only do math on numbers, not words. By converting text to vectors, we can compute similarity, find clusters, and perform other mathematical operations on meaning. Texts with similar meanings will have similar embedding vectors.

---

### Question 2 (7 points)
Explain what cosine similarity measures and what values of 0, 1, and -1 would indicate.

**Model Answer:** Cosine similarity measures the angle between two vectors, indicating how "aligned" their directions are:
- 1 = vectors point in the same direction = texts have identical/very similar meaning
- 0 = vectors are perpendicular = texts are unrelated/orthogonal in meaning
- -1 = vectors point in opposite directions = texts have opposite meanings

---

### Question 3 (7 points)
Your embedding model produces 384-dimensional vectors. What does this mean in practical terms?

- A) Each text is represented by 384 separate words
- B) Each text is represented by 384 numbers, collectively encoding its meaning
- C) The model can only understand 384 different words
- D) The text must be exactly 384 characters long

**Correct Answer:** B

---

### Question 4 (7 points)
Why do we use "pre-trained" embedding models instead of training our own?

**Model Answer:** Training embedding models requires enormous amounts of data (billions of text examples) and significant computational resources (specialized hardware, weeks of training time). Pre-trained models have already learned from this massive data and capture general language understanding. For most research purposes, using a pre-trained model is faster, cheaper, and often more effective than training from scratch.

---

### Question 5 (7 points)
Two headlines have cosine similarity of 0.92. Another pair has similarity of 0.45. What can you conclude about each pair?

**Model Answer:** The first pair (0.92) is highly semantically similar—they likely discuss very similar topics, use similar language, or convey similar meanings. The second pair (0.45) has moderate similarity—they may share some semantic content (perhaps same general domain) but discuss different specific aspects or have different framing. They're neither very similar nor completely unrelated.

---

## Part B: Interpretation (30 points)

### Scenario
You embedded 100 headlines about "artificial intelligence" and found these results:

**Most similar pair (similarity = 0.97):**
- "AI startup raises $50 million in Series B funding"
- "Tech company secures $45 million for AI development"

**Most different pair (similarity = 0.12):**
- "Researchers develop new AI algorithm for medical diagnosis"
- "Hollywood actors strike over AI concerns in contracts"

---

### Question 6 (10 points)
Why might the model identify the first pair as highly similar, even though they're about different companies and different funding amounts?

**Model Answer:** The model captures semantic meaning, not surface details. Both headlines share:
- Topic: AI companies receiving investment
- Structure: Company + raises/secures + dollar amount + purpose
- Key concepts: AI, funding, development, business growth

The specific company names and exact dollar amounts are less important to the semantic embedding than the overall meaning: "AI company gets significant funding."

---

### Question 7 (10 points)
Why is the second pair identified as very different despite both being about AI?

**Model Answer:** Despite sharing "AI" as a topic, these headlines are semantically different in:
- Domain: healthcare/research vs. entertainment/labor
- Actors: researchers vs. actors
- Framing: technological advancement vs. labor dispute
- Tone: neutral/positive vs. conflictual

The embedding captures more than just keywords—it captures the overall semantic context, and these contexts are very different.

---

### Question 8 (10 points)
If you wanted to find all headlines similar to "AI threatens jobs," how would you use embeddings to do this? Describe the process.

**Model Answer:**
1. Generate an embedding for the query "AI threatens jobs"
2. Calculate cosine similarity between this query embedding and all 100 headline embeddings
3. Sort headlines by similarity score (highest to lowest)
4. Return the top N headlines (e.g., top 10) as the most relevant matches
5. Optionally, set a similarity threshold (e.g., > 0.7) to filter only truly relevant headlines

---

## Part C: Lab Results (35 points)

### Task 1: Embedding Generation (10 points)

Report your embedding results:

| Metric | Your Value |
|--------|------------|
| Number of documents embedded | |
| Embedding dimensions | |
| Total numbers generated (docs × dims) | |

Include a screenshot showing the embedding shape.

---

### Task 2: Similar Pair Analysis (15 points)

**Most similar pair found:**

Text 1: _______________

Text 2: _______________

Similarity score: _______________

**Analysis (3-4 sentences):**
Why do you think the model identified these as most similar? What semantic features do they share? Does this match your intuition?

---

### Task 3: Different Pair Analysis (10 points)

**Most different pair found:**

Text 1: _______________

Text 2: _______________

Similarity score: _______________

**Brief interpretation (2-3 sentences):**
Why are these texts semantically different despite being in the same dataset?

---

## Grading Summary

| Component | Points |
|-----------|--------|
| Part A: Concept Check | 35 |
| Part B: Interpretation | 30 |
| Part C: Lab Results | 35 |
| **Total** | **100** |

---

## Submission Instructions

1. Complete all written answers in a single document
2. Include required screenshots
3. Include screenshot showing embedding shape and similarity output
4. Submit via [Course Platform] by [Deadline]

---

## Bonus Question (5 extra points)

The famous "King - Man + Woman = Queen" example suggests that semantic relationships can be represented as directions in embedding space. Give another example of a relationship that might work this way, and explain why.

**Model Answer:**
Example: "Doctor - Hospital + Courtroom = Lawyer" or "Paris - France + Japan = Tokyo"

These work because embeddings capture analogical relationships. The vector from "Man" to "Woman" represents a gender transformation. The vector from "France" to "Paris" represents a "country to capital" relationship. By adding this direction to "Japan," we should get close to "Tokyo."

This works because pre-trained models see these patterns repeatedly in training data and learn to encode such relationships as consistent directions in the vector space.
