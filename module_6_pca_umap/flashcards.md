# Module 6 Flashcards: PCA & UMAP Visualization

**Total Cards:** 22
**Format:** Anki-compatible (Front/Back)

---

## Definitions (6 cards)

### Card 1
**Front:** What is dimensionality reduction?
**Back:** Compressing high-dimensional data (e.g., 768D embeddings) to lower dimensions (2D or 3D) while preserving important structure. Enables visualization and simplifies analysis.
**Tags:** M6, definition, dim_reduction

### Card 2
**Front:** What is PCA?
**Back:** Principal Component Analysis - finds directions of maximum variance in data and projects points onto those directions. Linear method. PC1 captures most variance, PC2 next most, etc.
**Tags:** M6, definition, pca

### Card 3
**Front:** What is UMAP?
**Back:** Uniform Manifold Approximation and Projection - preserves local neighborhood structure when reducing dimensions. Non-linear. Points that are neighbors stay close together.
**Tags:** M6, definition, umap

### Card 4
**Front:** What is a principal component (PC)?
**Back:** A new axis in your data that captures maximum variance. PC1 is the direction of greatest spread. Think of it as rotating your view to see the most informative angle.
**Tags:** M6, definition, pca

### Card 5
**Front:** What is explained variance?
**Back:** The proportion of total data variation captured by each PC. If PC1 explains 40% variance, it captures 40% of the information; 60% remains in other components.
**Tags:** M6, definition, pca

### Card 6
**Front:** What is a cluster in UMAP visualization?
**Back:** A group of points close together in the plot - texts with similar semantic content. UMAP reveals these natural groupings that are invisible in high dimensions.
**Tags:** M6, definition, umap

---

## Concepts (6 cards)

### Card 7
**Front:** Why can't we visualize 768 dimensions directly?
**Back:** Humans can only perceive 2-3 spatial dimensions. 768D data is impossible to plot or intuit. Dimensionality reduction compresses to 2D while preserving key patterns.
**Tags:** M6, concept, motivation

### Card 8
**Front:** When should you use PCA vs UMAP?
**Back:** PCA: interpretable dimensions, variance explained, feature importance. UMAP: finding clusters, visualization, revealing natural groupings. PCA is linear; UMAP captures non-linear structure.
**Tags:** M6, concept, choice

### Card 9
**Front:** Why do UMAP plots look different with different random seeds?
**Back:** UMAP involves randomness in initialization. Different runs produce different layouts (rotated, flipped). The INTERNAL structure (which points cluster together) stays consistent.
**Tags:** M6, concept, umap

### Card 10
**Front:** Can you interpret distances BETWEEN clusters in UMAP?
**Back:** NO. UMAP preserves LOCAL structure (neighbors), not global distances. Two clusters far apart on screen might not be "more different" than close clusters. Only interpret within-cluster proximity.
**Tags:** M6, concept, interpretation

### Card 11
**Front:** What does coloring UMAP by a variable reveal?
**Back:** Whether semantic clusters correlate with your variable. If cluster A is all red (high scores) and cluster B all blue (low scores), semantic content relates to that variable.
**Tags:** M6, concept, visualization

### Card 12
**Front:** What does "mixed colors" in a UMAP cluster mean?
**Back:** That cluster's semantic content doesn't determine your coloring variable. The texts are similar in meaning but vary in the colored attribute (e.g., sentiment is unrelated to topic).
**Tags:** M6, concept, interpretation

---

## Code Patterns (5 cards)

### Card 13
**Front:** How to load pre-computed UMAP results:
**Back:**
```python
df = load_dataset("raymond_umap_dbscan_results_20250223_154628")
# Columns: umap_x, umap_y, cluster, embedding_text
```
**Tags:** M6, code, loading

### Card 14
**Front:** How to create a UMAP scatter plot:
**Back:**
```python
import matplotlib.pyplot as plt
plt.scatter(df['umap_x'], df['umap_y'],
            c=df['cluster'], cmap='tab20', alpha=0.5, s=1)
plt.xlabel('UMAP 1')
plt.ylabel('UMAP 2')
plt.colorbar(label='Cluster')
```
**Tags:** M6, code, visualization

### Card 15
**Front:** How to examine cluster contents:
**Back:**
```python
for cluster_id in df['cluster'].unique()[:5]:
    texts = df[df['cluster'] == cluster_id]['embedding_text'].head(3)
    print(f"=== Cluster {cluster_id} ===")
    for t in texts:
        print(f"  {str(t)[:80]}...")
```
**Tags:** M6, code, exploration

### Card 16
**Front:** How to load PCA results:
**Back:**
```python
df_pca = load_dataset("clara_pca_results")
df_loadings = load_dataset("clara_pca_component_loadings")
# Plot PC1 vs PC2
plt.scatter(df_pca['PC1'], df_pca['PC2'])
```
**Tags:** M6, code, pca

### Card 17
**Front:** How to set random seed for reproducible UMAP:
**Back:**
```python
import umap
reducer = umap.UMAP(random_state=42)
embedding_2d = reducer.fit_transform(embeddings)
```
**Tags:** M6, code, reproducibility

---

## Interpretation (3 cards)

### Card 18
**Front:** UMAP shows 3 clear clusters. What does this mean?
**Back:** Your data contains 3 distinct semantic groups - texts within each cluster are similar in meaning, different from other clusters. Examine samples from each to understand what defines them.
**Tags:** M6, interpretation, umap

### Card 19
**Front:** UMAP shows no clear clusters - just a blob. What does this mean?
**Back:** Data is relatively homogeneous in semantic space OR differences exist in dimensions UMAP didn't preserve. Could also mean: too much noise, or clustering structure at different scales.
**Tags:** M6, interpretation, umap

### Card 20
**Front:** PC1 explains 60% variance, PC2 explains 15%. Interpret.
**Back:** One dominant pattern in your data (captured by PC1). Secondary pattern captures much less. First 2 PCs explain 75% total - a good 2D summary, but 25% of variation still lost.
**Tags:** M6, interpretation, pca

---

## Common Mistakes (2 cards)

### Card 21
**Front:** What's wrong with: "Clusters A and B are far apart, so they're very different"?
**Back:** UMAP doesn't preserve global distances. Cluster positions are somewhat arbitrary. Only within-cluster structure is reliable. Compare cluster CONTENTS, not screen positions.
**Tags:** M6, mistake, interpretation

### Card 22
**Front:** What's wrong with running UMAP without setting random_state?
**Back:** Results won't be reproducible. Each run gives different positions. For research, always `random_state=42` (or any fixed number) so others can replicate your exact visualization.
**Tags:** M6, mistake, reproducibility

---

*Module 6 Flashcards | Applied Psychological Data Science*
