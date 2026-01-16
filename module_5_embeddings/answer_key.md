# Module 5 Answer Key: Embeddings
## INSTRUCTOR USE ONLY

**Assessment:** Module 5 Assessment
**Dataset:** `clara_bert_embeddings` (12,915 texts with 768D embeddings)
**Total Points:** 100

---

## Part A: Concept Check (35 points)

### Question 1 (7 points)
**Question:** What is an embedding, and why is it useful?

**Model Answer:**
> An embedding is a numerical vector (list of numbers) that represents the semantic meaning of text. It's useful because computers can only do math on numbers, not words. By converting text to vectors, we can compute similarity, find clusters, and perform other mathematical operations on meaning. Texts with similar meanings will have similar embedding vectors.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 7 | Defines as numerical vector + mentions semantic meaning + explains utility |
| 5 | Correct definition but utility unclear |
| 3 | Partial understanding |
| 0 | Incorrect |

**Key Terms:**
- Vector, numerical representation
- Semantic meaning
- Similarity computation, clustering

---

### Question 2 (7 points)
**Question:** Explain cosine similarity and what 0, 1, -1 indicate.

**Model Answer:**
> Cosine similarity measures the angle between two vectors:
> - 1 = identical/very similar meaning (same direction)
> - 0 = unrelated (perpendicular)
> - -1 = opposite meanings (opposite directions)

**Rubric:**
| Score | Criteria |
|-------|----------|
| 7 | All three values explained correctly with meaning |
| 5 | Two values correct |
| 3 | One value correct |
| 0 | Incorrect |

**Common Error:** Students say -1 means "very different" but it specifically means "opposite" (rare in practice for text).

---

### Question 3 (7 points)
**Question:** 384-dimensional vectors means what?

**Correct Answer:** B) Each text is represented by 384 numbers, collectively encoding its meaning

**Rubric:**
| Score | Criteria |
|-------|----------|
| 7 | Selects B |
| 0 | Any other answer |

**Instructor Note:** Common confusion with A (words) and D (characters). Clarify that dimensions are abstract learned features, not literal words.

---

### Question 4 (7 points)
**Question:** Why use pre-trained embedding models?

**Model Answer:**
> Training embedding models requires enormous amounts of data (billions of examples) and significant computational resources. Pre-trained models have already learned from this massive data. For most research purposes, using pre-trained is faster, cheaper, and often more effective.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 7 | Mentions data requirements + compute + practical benefits |
| 5 | Some practical reasons but incomplete |
| 3 | Vague understanding |
| 0 | Incorrect |

---

### Question 5 (7 points)
**Question:** Pair 1 has similarity 0.92, Pair 2 has 0.45. What can you conclude?

**Model Answer:**
> Pair 1 (0.92) is highly semantically similar—likely similar topics, language, or meaning. Pair 2 (0.45) has moderate similarity—may share some semantic content but discuss different aspects. Neither very similar nor unrelated.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 7 | Correctly interprets both values with appropriate qualifiers |
| 5 | One interpretation correct |
| 3 | General direction correct |
| 0 | Incorrect |

**Similarity Interpretation Guide:**
- 0.9+: Very high similarity
- 0.7-0.9: High similarity
- 0.5-0.7: Moderate similarity
- 0.3-0.5: Low similarity
- <0.3: Unrelated/very different

---

## Part B: Interpretation (30 points)

### Question 6 (10 points)
**Question:** Why is the first pair (funding headlines) identified as highly similar?

**Model Answer:**
> The model captures semantic meaning, not surface details. Both headlines share:
> - Topic: AI companies receiving investment
> - Structure: Company + raises/secures + dollar amount
> - Key concepts: AI, funding, development, business
>
> Specific names and exact amounts matter less than overall meaning: "AI company gets funding."

**Rubric:**
| Score | Criteria |
|-------|----------|
| 10 | Identifies semantic similarity + explains shared features + notes what doesn't matter |
| 7 | Correct general idea but missing specifics |
| 4 | Partial understanding |
| 0 | Incorrect |

---

### Question 7 (10 points)
**Question:** Why is the second pair (research vs. strike) very different despite both being about AI?

**Model Answer:**
> Despite sharing "AI," these are semantically different in:
> - Domain: healthcare/research vs. entertainment/labor
> - Actors: researchers vs. actors
> - Framing: advancement vs. dispute
> - Tone: neutral/positive vs. conflictual
>
> Embeddings capture more than keywords—they capture overall context.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 10 | Identifies multiple dimensions of difference + explains beyond keyword matching |
| 7 | Some differences identified |
| 4 | Mentions "different contexts" vaguely |
| 0 | Incorrect |

---

### Question 8 (10 points)
**Question:** How would you find headlines similar to "AI threatens jobs"?

**Model Answer:**
> 1. Generate embedding for query "AI threatens jobs"
> 2. Calculate cosine similarity with all headline embeddings
> 3. Sort headlines by similarity (highest to lowest)
> 4. Return top N headlines
> 5. Optionally set similarity threshold (e.g., > 0.7)

**Rubric:**
| Score | Criteria |
|-------|----------|
| 10 | All 5 steps in correct order |
| 7 | 3-4 steps correct |
| 4 | General idea but missing specifics |
| 0 | Incorrect |

**Key Steps:**
1. Embed query
2. Calculate similarities
3. Sort
4. Return top results

---

## Part C: Lab Results (35 points)

### Task 1: Embedding Generation (10 points)

**Expected Format:**
| Metric | Example Value |
|--------|---------------|
| Number embedded | 100-1000 |
| Dimensions | 384 or 768 (depends on model) |
| Total numbers | docs × dims |

**Using clara_bert_embeddings:**
- Rows: 12,915
- Dimensions: 768 (Dim_1 through Dim_768)
- Total: 12,915 × 768 = 9,918,720 numbers

**Screenshot Requirements:**
- Shape shown (e.g., `(12915, 768)`)
- Clear that dimensions match expected

**Rubric:**
| Component | Points |
|-----------|--------|
| Correct numbers | 5 |
| Calculation correct | 3 |
| Screenshot included | 2 |

---

### Task 2: Similar Pair Analysis (15 points)

**Rubric:**
| Component | Points |
|-----------|--------|
| Two texts provided | 3 |
| Similarity score | 3 |
| Analysis explains shared features | 5 |
| Intuition check mentioned | 4 |

**Good Analysis Includes:**
- Shared topic identification
- Shared structure/framing
- Whether match intuition
- Specific features noted

---

### Task 3: Different Pair Analysis (10 points)

**Rubric:**
| Component | Points |
|-----------|--------|
| Two texts provided | 3 |
| Similarity score | 3 |
| Brief interpretation | 4 |

**Good Interpretations:**
- Different domains/topics
- Different frames/perspectives
- Explains why in same dataset but different

---

## Grading Summary

| Component | Points |
|-----------|--------|
| Part A: Q1-Q5 | 35 |
| Part B: Q6 | 10 |
| Part B: Q7 | 10 |
| Part B: Q8 | 10 |
| Part C: Task 1 | 10 |
| Part C: Task 2 | 15 |
| Part C: Task 3 | 10 |
| **TOTAL** | **100** |

---

## Bonus Question (5 extra points)

**Question:** King - Man + Woman = Queen. Give another example.

**Model Answer:**
> "Doctor - Hospital + Courtroom = Lawyer" or "Paris - France + Japan = Tokyo"
>
> Works because embeddings capture analogical relationships. The vector from Man to Woman represents gender. Adding this direction to other words transforms them similarly.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 5 | Valid analogy + explanation of why it works |
| 3 | Valid analogy but weak explanation |
| 0 | Invalid or no response |

**Valid Analogy Types:**
- Gender: actor - man + woman = actress
- Country-capital: Berlin - Germany + France = Paris
- Tense: walked - walk + run = ran
- Profession-workplace: nurse - hospital + school = teacher

---

## Expected Code Outputs

**Loading Clara's embeddings:**
```python
df = load_dataset("clara_bert_embeddings")
print(df.shape)  # (12915, 771)
embedding_cols = [c for c in df.columns if c.startswith('Dim_')]
print(len(embedding_cols))  # 768
```

**Cosine similarity calculation:**
```python
from sklearn.metrics.pairwise import cosine_similarity
embeddings = df[embedding_cols].values
sim_matrix = cosine_similarity(embeddings[:100])
# Values range from 0 to 1 for these embeddings
```

---

## Common Student Errors

1. **Confusing dimensions with words**
   - Error: "768 dimensions means 768 words"
   - Fix: Dimensions are abstract learned features

2. **Thinking negative cosine is common**
   - Error: "Similarity is -0.5 so they're opposites"
   - Fix: Negative values rare in text; most are 0-1

3. **Over-interpreting exact values**
   - Error: "0.73 is definitely similar"
   - Fix: Similarity interpretation is relative

4. **Forgetting to normalize**
   - Error: Getting values > 1 or < -1
   - Fix: Use proper cosine similarity function

5. **Wrong column names**
   - Error: Looking for `dim_0` instead of `Dim_1`
   - Fix: Clara's data uses `Dim_1` through `Dim_768`

---

*Answer Key Version: 1.0 | Date: 2026-01-15*
