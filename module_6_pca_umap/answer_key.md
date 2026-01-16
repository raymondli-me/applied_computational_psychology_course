# Module 6 Answer Key: PCA & UMAP Visualization
## INSTRUCTOR USE ONLY

**Assessment:** Module 6 Assessment
**Dataset:** `raymond_umap_dbscan_results_20250223_154628` (82,127 rows with UMAP + clusters)
**Total Points:** 100

---

## Part A: Concept Check (30 points)

### Question 1 (6 points)
**Question:** Why do we need dimensionality reduction when working with embeddings?

**Model Answer:**
> Embeddings have hundreds of dimensions (e.g., 384), which humans cannot visualize or directly interpret. Dimensionality reduction compresses this to 2-3 dimensions, allowing us to create scatter plots, identify clusters, and visually explore the structure of our data.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 6 | Mentions high dimensions + human limitation + visualization benefit |
| 4 | Correct purpose but incomplete explanation |
| 2 | Vague understanding |
| 0 | Incorrect |

---

### Question 2 (6 points)
**Question:** In simple terms, what does PCA do?

**Model Answer:**
> PCA finds the directions (axes) in which the data varies most and projects all data points onto those directions. The first principal component captures the most variance, the second captures the next most (perpendicular to the first). By keeping only 2-3 components, we reduce dimensions while preserving main patterns.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 6 | Mentions variance, directions/axes, dimensionality reduction |
| 4 | General idea correct but missing key terms |
| 2 | Vague |
| 0 | Incorrect |

**Key Concepts:**
- Variance maximization
- Principal components (ordered by variance)
- Linear transformation

---

### Question 3 (6 points)
**Question:** In simple terms, what does UMAP do?

**Model Answer:**
> UMAP preserves local neighborhood structure when reducing dimensions. It builds a graph of nearest neighbors in high dimensions, then finds a low-dimensional arrangement where points that were neighbors stay close together. This reveals clusters and groupings.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 6 | Mentions neighbors, local structure preservation, clustering |
| 4 | General idea but missing key terms |
| 2 | Vague |
| 0 | Incorrect |

**Key Concepts:**
- Local structure preservation
- Nearest neighbors
- Non-linear (vs. PCA's linear)

---

### Question 4 (6 points)
**Question:** When should you use UMAP over PCA?

**Correct Answer:** B) When you want to find clusters and groupings

**Rubric:**
| Score | Criteria |
|-------|----------|
| 6 | Selects B |
| 0 | Any other answer |

**Why Other Options Are Wrong:**
- A: PCA is actually faster than UMAP
- C: UMAP involves randomness; PCA is deterministic
- D: Neither preserves exact distances

---

### Question 5 (6 points)
**Question:** What are two important cautions when interpreting UMAP plots?

**Model Answer:**
> 1. **Distances between clusters aren't meaningful** - While points close together within a cluster are similar, distance between different clusters doesn't have consistent interpretation.
> 2. **UMAP involves randomness** - Running twice can produce different-looking plots. Always set random seed for reproducibility.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 6 | Both cautions correct with explanation |
| 4 | One caution correct |
| 2 | Vague understanding of limitations |
| 0 | Incorrect or no cautions |

**Other Acceptable Cautions:**
- Cluster size doesn't indicate frequency
- Hyperparameters affect appearance
- Visual inspection is subjective

---

## Part B: Interpretation (35 points)

### Question 6 (10 points)
**Question:** What does the color pattern suggest about semantic content and optimism?

**Given:** Cluster A (negative), Cluster B (mixed), Cluster C (positive)

**Model Answer:**
> The color pattern suggests semantic content correlates with optimism ratings. Headlines with similar topics cluster together in UMAP, and these semantic clusters also have similar sentiment. Certain topics (layoffs, breaches) are discussed pessimistically, while others (breakthroughs, innovation) are discussed optimistically. AI rating and semantic embedding capture related but distinct information.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 10 | Notes correlation + explains topic-sentiment relationship + appropriate nuance |
| 7 | Sees pattern but explanation incomplete |
| 4 | Notes pattern without interpretation |
| 0 | Incorrect |

---

### Question 7 (10 points)
**Question:** Cluster B has "mixed colors." What does this suggest?

**Model Answer:**
> Mixed colors suggest headlines with neutral or varied sentiment—neither consistently optimistic nor pessimistic. These might be factual, objective news items (earnings reports, announcements) that can be framed positively or negatively. Semantic similarity (routine tech news) doesn't determine sentiment like other clusters.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 10 | Notes neutral/varied + gives examples + explains semantic similarity doesn't predict sentiment |
| 7 | Identifies mixed as neutral but limited explanation |
| 4 | Notes "mixed" without interpretation |
| 0 | Incorrect |

---

### Question 8 (15 points)
**Question:** Is the claim "UMAP proves negative tech news is semantically different from positive" justified?

**Model Answer:**
> The claim is partially justified but overstated:
>
> **What UMAP DOES show:** Headlines with similar semantic content cluster together, and these correlate with sentiment.
>
> **What UMAP DOESN'T prove:**
> 1. Not causation—we can't say sentiment causes semantic difference
> 2. Clustering based on embeddings, not sentiment
> 3. Some negative/positive headlines may be semantically similar
> 4. UMAP positions are approximations
>
> Better statement: "UMAP suggests positive and negative tech headlines often discuss different sub-topics."

**Rubric:**
| Score | Criteria |
|-------|----------|
| 15 | Acknowledges partial truth + lists limitations + provides better phrasing |
| 11 | Sees nuance but incomplete limitations |
| 7 | Either accepts or rejects without nuance |
| 4 | Some relevant points |
| 0 | Incorrect |

**Key Points to Award Credit:**
- Recognizes correlation vs. causation
- Notes UMAP limitations
- Provides nuanced interpretation

---

## Part C: Lab Results (35 points)

### Task 1: UMAP Visualization (15 points)

**Checklist:**
| Requirement | Points | Criteria |
|-------------|--------|----------|
| Colored by variable | 5 | Meaningful variable (cluster, rating, etc.) |
| Axis labels | 3 | "UMAP 1" and "UMAP 2" or similar |
| Legend/colorbar | 3 | Shows what colors mean |
| Title | 2 | Descriptive |
| Resolution | 2 | Clear, readable |

**Using raymond_umap_dbscan_results:**
- Available color variables: `cluster`, `auto_cluster_label`
- X/Y coordinates: `umap_x`, `umap_y`

---

### Task 2: Cluster Identification (10 points)

**Expected Format:**
| Cluster | Location | Sample Titles | Theme |
|---------|----------|---------------|-------|
| 1 | Upper left | [examples] | [description] |
| 2 | Center | [examples] | [description] |
| 3 | Lower right | [examples] | [description] |

**Rubric:**
| Component | Points |
|-----------|--------|
| 2-3 clusters identified | 3 |
| Locations described | 2 |
| Sample titles relevant | 3 |
| Themes identified | 2 |

---

### Task 3: Interpretation (10 points)

**Required Elements:**
1. What structure UMAP reveals
2. Color pattern (if used)
3. Surprising groupings
4. Research implications

**Rubric:**
| Component | Points |
|-----------|--------|
| Structure described | 3 |
| Pattern noted | 3 |
| Surprises mentioned | 2 |
| Implications drawn | 2 |

---

## Grading Summary

| Component | Points |
|-----------|--------|
| Part A: Q1-Q5 | 30 |
| Part B: Q6 | 10 |
| Part B: Q7 | 10 |
| Part B: Q8 | 15 |
| Part C: Task 1 | 15 |
| Part C: Task 2 | 10 |
| Part C: Task 3 | 10 |
| **TOTAL** | **100** |

---

## Bonus Question (5 extra points)

**Question:** You run UMAP twice with different seeds. Plots look different. Are results wrong?

**Model Answer:**
> No, this is expected. UMAP positions are not absolute; only relative relationships matter:
> 1. Similar items should still cluster together
> 2. Number/composition of clusters should be similar
> 3. Neighborhoods should be preserved
>
> Different runs may rotate/flip/shift clusters, but internal structure should be consistent. Always set random seed for reproducibility.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 5 | States not wrong + explains why + notes seed importance |
| 3 | Correct answer but incomplete explanation |
| 0 | Says results are wrong |

---

## Expected Code Outputs

**Loading Raymond's UMAP data:**
```python
df = load_dataset("raymond_umap_dbscan_results_20250223_154628")
print(df.shape)  # (82127, 6)
print(df.columns.tolist())
# ['comment_id', 'umap_x', 'umap_y', 'cluster', 'auto_cluster_label', 'embedding_text']
```

**Basic UMAP plot:**
```python
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
plt.scatter(df['umap_x'], df['umap_y'], c=df['cluster'], cmap='tab10', alpha=0.5, s=1)
plt.xlabel('UMAP 1')
plt.ylabel('UMAP 2')
plt.title('UMAP Visualization of Text Embeddings')
plt.colorbar(label='Cluster')
plt.savefig('umap_plot.png', dpi=150)
```

**Cluster statistics:**
```python
print(df['cluster'].value_counts())
# Shows distribution across clusters
```

---

## Common Student Errors

1. **Over-interpreting distances**
   - Error: "Cluster A is 'farther' from C so more different"
   - Fix: Between-cluster distances not meaningful

2. **Expecting reproducibility without seed**
   - Error: "My plot looks different than classmate's"
   - Fix: Set random_state parameter

3. **Confusing PCA and UMAP strengths**
   - Error: "UMAP preserves global structure"
   - Fix: UMAP preserves local structure; PCA preserves variance

4. **Missing color variable**
   - Error: Plot with all same color
   - Fix: Color by cluster, rating, or other variable

5. **Claiming causation from visualization**
   - Error: "UMAP proves X causes Y"
   - Fix: Visualization shows association, not causation

---

## PCA vs UMAP Quick Reference

| Feature | PCA | UMAP |
|---------|-----|------|
| Goal | Maximize variance | Preserve local structure |
| Method | Linear projection | Non-linear embedding |
| Speed | Faster | Slower |
| Determinism | Deterministic | Stochastic (set seed!) |
| Best for | Global structure | Clusters, local patterns |
| Distance interpretation | More meaningful | Within-cluster only |

---

*Answer Key Version: 1.0 | Date: 2026-01-15*
