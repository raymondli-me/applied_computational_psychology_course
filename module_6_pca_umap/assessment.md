# Module 6 Assessment: Visualization

**Recommended Dataset:** `raymond_umap_dbscan_results_20250223_154628` (82,127 with UMAP + clusters)
**Alternate Datasets:** Clara's PCA results, Andrea's PCA results, Agatha's PCA results
**See:** DATASETS_FOR_M6.md for all pre-computed PCA/UMAP options

---

## Part A: Concept Check (30 points)

### Question 1 (6 points)
Why do we need dimensionality reduction when working with embeddings?

**Model Answer:** Embeddings have hundreds of dimensions (e.g., 384), which humans cannot visualize or directly interpret. Dimensionality reduction compresses this to 2-3 dimensions, allowing us to create scatter plots, identify clusters, and visually explore the structure of our data.

---

### Question 2 (6 points)
In simple terms, what does PCA do?

**Model Answer:** PCA finds the directions (axes) in which the data varies most and projects all data points onto those directions. The first principal component captures the most variance, the second captures the next most (perpendicular to the first), and so on. By keeping only the first 2-3 components, we reduce dimensions while preserving the main patterns of variation.

---

### Question 3 (6 points)
In simple terms, what does UMAP do?

**Model Answer:** UMAP preserves local neighborhood structure when reducing dimensions. It builds a graph of nearest neighbors in high dimensions, then finds a low-dimensional arrangement where points that were neighbors stay close together. This reveals clusters and groupings in the data.

---

### Question 4 (6 points)
When should you use UMAP over PCA?

- A) When you want faster computation
- B) When you want to find clusters and groupings
- C) When you want deterministic results
- D) When you want to preserve exact distances

**Correct Answer:** B

---

### Question 5 (6 points)
What are two important cautions when interpreting UMAP plots?

**Model Answer:**
1. **Distances between clusters aren't meaningful** - While points close together within a cluster are similar, the distance between different clusters doesn't have a consistent interpretation.
2. **UMAP involves randomness** - Running UMAP twice can produce different-looking plots, so always set a random seed for reproducibility and don't over-interpret exact positions.

---

## Part B: Interpretation (35 points)

### Scenario
You created a UMAP visualization of 500 news headlines about "technology." The plot shows three distinct clusters. You colored points by the "optimism" ratings (1-7) from Module 3.

**Observations:**
- Cluster A (upper left): Mostly red/orange points (low optimism, ratings 1-3)
- Cluster B (center): Mixed colors (moderate optimism, ratings 3-5)
- Cluster C (lower right): Mostly green points (high optimism, ratings 6-7)

When you examine headlines in each cluster:
- Cluster A: "Tech layoffs continue...", "Privacy concerns grow...", "Cybersecurity breach..."
- Cluster B: "Apple announces new product...", "Tech earnings report...", "Software update..."
- Cluster C: "Breakthrough in AI research...", "Tech startup revolutionizes...", "Innovation award..."

---

### Question 6 (10 points)
What does the color pattern suggest about the relationship between semantic content and optimism in your data?

**Model Answer:** The color pattern suggests that semantic content (what the headline is about) correlates with optimism ratings. Headlines with similar topics cluster together in UMAP (based on semantic embeddings), and these semantic clusters also tend to have similar sentiment. This indicates that certain topics (layoffs, breaches) are inherently discussed more pessimistically, while others (breakthroughs, innovation) are discussed more optimistically. The AI rating and semantic embedding capture related but distinct information.

---

### Question 7 (10 points)
Cluster B has "mixed colors." What might this tell you about that cluster?

**Model Answer:** Mixed colors in Cluster B suggest that this cluster contains headlines with neutral or varied sentiment—neither consistently optimistic nor pessimistic. These might be factual, objective news items (earnings reports, product announcements) that can be framed positively or negatively depending on the specific content. The semantic similarity (all about routine tech news) doesn't determine sentiment the way topics in other clusters do.

---

### Question 8 (15 points)
A classmate says: "The UMAP proves that negative news about tech is semantically different from positive news." Is this claim justified? Explain why or why not.

**Model Answer:**
The claim is partially justified but somewhat overstated:

**What UMAP DOES show:** Headlines with similar semantic content (topics, language) cluster together, and these clusters happen to correlate with sentiment. This suggests negative and positive tech news often discuss different sub-topics.

**What UMAP DOESN'T prove:**
1. UMAP doesn't establish causation—we can't say sentiment CAUSES semantic difference or vice versa
2. The clustering is based on semantic embeddings, not sentiment—the color overlay is separate
3. Some negative and positive headlines might be semantically similar (same topic, different framing)
4. UMAP positions are approximations, not exact measurements

A more accurate statement: "The UMAP suggests that positive and negative tech headlines often discuss different sub-topics, but this doesn't mean all positive and negative news is semantically distinct."

---

## Part C: Lab Results (35 points)

### Task 1: UMAP Visualization (15 points)

Submit your UMAP plot that is:
- [ ] Colored by a meaningful variable (5 points)
- [ ] Has clear axis labels (3 points)
- [ ] Has a legend or colorbar (3 points)
- [ ] Has a descriptive title (2 points)
- [ ] Is high resolution (2 points)

---

### Task 2: Cluster Identification (10 points)

Identify 2-3 visible clusters in your plot:

| Cluster | Location (approx.) | Sample Titles | Common Theme |
|---------|-------------------|---------------|--------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

---

### Task 3: Interpretation (10 points)

In 4-5 sentences, interpret your visualization:
1. What structure does the UMAP reveal about your data?
2. If you colored by a variable, is there a pattern?
3. Were there any surprising groupings?
4. What might this tell you about your research topic?

---

## Grading Summary

| Component | Points |
|-----------|--------|
| Part A: Concept Check | 30 |
| Part B: Interpretation | 35 |
| Part C: Lab Results | 35 |
| **Total** | **100** |

---

## Submission Instructions

1. Complete all written answers in a single document
2. Include your UMAP plot as a PNG image
3. Ensure plot is high resolution (at least 150 dpi)
4. Submit via [Course Platform] by [Deadline]

---

## Bonus Question (5 extra points)

You run UMAP twice with the same data but different random seeds. The plots look different—clusters are in different positions. Does this mean your results are wrong? Explain.

**Model Answer:**
No, the results aren't wrong—this is expected behavior. UMAP's position assignments are not absolute; only the relative relationships matter. What's important is:
1. Similar items should still cluster together (check this)
2. The number and general composition of clusters should be similar
3. The neighborhood relationships should be preserved

Different runs may place clusters in different screen positions (rotated, flipped, shifted), but the internal structure should be consistent. For reproducibility and consistent reporting, always set a random seed. The differences highlight why we shouldn't over-interpret exact positions—only relative patterns matter.
