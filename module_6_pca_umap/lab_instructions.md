# Module 6 Lab: Visualizing Your Data with UMAP

## Lab Overview
**Duration:** 60 minutes
**Tools Required:** Google Colab, umap-learn, matplotlib
**Input:** Pre-computed PCA/UMAP from course dataset bank (see below)
**Notebook:** Continue in your course notebook from previous modules

---

## Dataset Options for This Lab

### Recommended: Pre-computed UMAP Clusters (Ready to Visualize)

```python
# If you haven't run the setup cell yet:
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

# Raymond's UMAP results - pre-computed with cluster labels
# Ready to visualize immediately!
df = load_dataset("raymond_umap_dbscan_results_20250223_154628", nrows=10000)
print(f"Columns: {list(df.columns)}")
```

*These UMAP results were computed from YouTube comments and include cluster labels for visualization.*

### Alternative: PCA Component Analysis

```python
# Clara's PCA results with interpretable loadings
df_loadings = load_dataset("clara_pca_component_loadings")  # What each PC means
df_pca = load_dataset("clara_pca_results")  # Texts in PCA space
```

**See:** `DATASETS_FOR_M6.md` for all PCA/UMAP datasets.

---

## Learning Goals
By the end of this lab, you will:
- Apply PCA to reduce dimensionality
- Apply UMAP to create 2D visualizations
- Color plots by meaningful variables
- Identify and interpret clusters
- Create publication-ready visualizations

---

## Setup Instructions

### Step 1: Open the Course Notebook
1. Open your course notebook in Colab
2. Make sure you've run the setup cell with `load_dataset()`
3. Load pre-computed UMAP data from the course dataset bank:

```python
# Raymond's pre-computed UMAP results - ready to visualize!
df = load_dataset("raymond_umap_dbscan_results_20250223_154628", nrows=10000)
print(f"Columns: {list(df.columns)}")
```

### Step 2: Verify Data Has UMAP Coordinates
Your data should have columns like `umap_x`, `umap_y`, and optionally `cluster`.

---

## Part 1: Setup and Data Loading (10 minutes)

### Cell 1: Install Libraries

```python
# ============================================
# SETUP - Install required libraries
# ============================================
!pip install umap-learn matplotlib pandas numpy scikit-learn -q

print("Libraries installed!")
```

### Cell 2: Import Libraries

```python
# ============================================
# IMPORTS
# ============================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import umap

# For reproducibility
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

print("Ready to visualize!")
```

### Cell 3: Load Your Data

```python
# ============================================
# LOAD DATA
# ============================================

# Load embeddings from Module 5
embeddings = np.load('embeddings.npy')
print(f"Embeddings shape: {embeddings.shape}")

# Load metadata
df = pd.read_csv('data_with_embedding_index.csv')
print(f"Metadata rows: {len(df)}")
print(f"Columns: {list(df.columns)}")

# Preview
print(f"\nFirst 3 titles:")
for t in df['title'].head(3):
    print(f"  - {t[:60]}...")
```

---

## Part 2: PCA Visualization (15 minutes)

### Cell 4: Run PCA

```python
# ============================================
# PCA - Principal Component Analysis
# ============================================

print("Running PCA...")

# Reduce from 384D to 2D
pca = PCA(n_components=2, random_state=RANDOM_SEED)
embeddings_pca = pca.fit_transform(embeddings)

print(f"Original shape: {embeddings.shape}")
print(f"PCA shape: {embeddings_pca.shape}")
print(f"\nVariance explained by PC1: {pca.explained_variance_ratio_[0]:.2%}")
print(f"Variance explained by PC2: {pca.explained_variance_ratio_[1]:.2%}")
print(f"Total variance explained: {sum(pca.explained_variance_ratio_):.2%}")
```

### Cell 5: Plot PCA

```python
# ============================================
# PCA SCATTER PLOT
# ============================================

plt.figure(figsize=(10, 8))

plt.scatter(
    embeddings_pca[:, 0],
    embeddings_pca[:, 1],
    alpha=0.6,
    s=50
)

plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.1%} variance)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.1%} variance)')
plt.title('PCA Visualization of Text Embeddings')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('pca_plot.png', dpi=150)
plt.show()

print("PCA plot saved to: pca_plot.png")
```

**Question:** What do you notice about the shape of the data? Are there any obvious clusters?

---

## Part 3: UMAP Visualization (20 minutes)

### Cell 6: Run UMAP

```python
# ============================================
# UMAP - Uniform Manifold Approximation
# ============================================

print("Running UMAP... (this may take 1-2 minutes)")

# Create UMAP reducer
reducer = umap.UMAP(
    n_neighbors=15,        # How many neighbors to consider
    min_dist=0.1,          # How tightly to pack points
    n_components=2,        # Output dimensions
    random_state=RANDOM_SEED,
    metric='cosine'        # Use cosine distance (matches our similarity measure)
)

# Fit and transform
embeddings_umap = reducer.fit_transform(embeddings)

print(f"UMAP shape: {embeddings_umap.shape}")
print("UMAP complete!")
```

### Cell 7: Basic UMAP Plot

```python
# ============================================
# UMAP SCATTER PLOT (BASIC)
# ============================================

plt.figure(figsize=(10, 8))

plt.scatter(
    embeddings_umap[:, 0],
    embeddings_umap[:, 1],
    alpha=0.6,
    s=50
)

plt.xlabel('UMAP Dimension 1')
plt.ylabel('UMAP Dimension 2')
plt.title('UMAP Visualization of Text Embeddings')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('umap_basic.png', dpi=150)
plt.show()
```

**Question:** Compare to PCA. Does UMAP reveal more distinct clusters?

### Cell 8: UMAP Colored by Variable

```python
# ============================================
# UMAP COLORED BY A VARIABLE
# ============================================

# Option 1: If you have AI ratings from Module 3
# COLOR_COLUMN = 'ai_rating'  # Change to your column name

# Option 2: Use source as color
COLOR_COLUMN = 'source'  # Or 'category', 'date', etc.

# Check if column exists
if COLOR_COLUMN in df.columns:
    plt.figure(figsize=(12, 8))

    # For categorical variables
    if df[COLOR_COLUMN].dtype == 'object':
        categories = df[COLOR_COLUMN].unique()
        colors = plt.cm.tab10(np.linspace(0, 1, len(categories)))

        for cat, color in zip(categories, colors):
            mask = df[COLOR_COLUMN] == cat
            plt.scatter(
                embeddings_umap[mask, 0],
                embeddings_umap[mask, 1],
                c=[color],
                label=cat[:20],  # Truncate long names
                alpha=0.6,
                s=50
            )
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    # For numerical variables
    else:
        scatter = plt.scatter(
            embeddings_umap[:, 0],
            embeddings_umap[:, 1],
            c=df[COLOR_COLUMN],
            cmap='RdYlGn',  # Red-Yellow-Green gradient
            alpha=0.6,
            s=50
        )
        plt.colorbar(scatter, label=COLOR_COLUMN)

    plt.xlabel('UMAP Dimension 1')
    plt.ylabel('UMAP Dimension 2')
    plt.title(f'UMAP Colored by {COLOR_COLUMN}')
    plt.tight_layout()
    plt.savefig(f'umap_by_{COLOR_COLUMN}.png', dpi=150, bbox_inches='tight')
    plt.show()

else:
    print(f"Column '{COLOR_COLUMN}' not found!")
    print(f"Available columns: {list(df.columns)}")
```

---

## Part 4: Identify Clusters (10 minutes)

### Cell 9: Interactive Cluster Exploration

```python
# ============================================
# EXPLORE CLUSTERS
# ============================================

# Add UMAP coordinates to dataframe
df['umap_x'] = embeddings_umap[:, 0]
df['umap_y'] = embeddings_umap[:, 1]

# Function to find texts in a region
def get_texts_in_region(df, x_min, x_max, y_min, y_max, text_col='title'):
    """Find texts within a rectangular region of the UMAP plot."""
    mask = (
        (df['umap_x'] >= x_min) & (df['umap_x'] <= x_max) &
        (df['umap_y'] >= y_min) & (df['umap_y'] <= y_max)
    )
    return df[mask][text_col].tolist()

# Example: Look at texts in different regions
# Modify these coordinates based on YOUR plot!
print("To explore clusters, look at your plot and identify regions.")
print("Then modify the coordinates below:\n")

# Example region (modify based on your plot)
REGION_X_MIN, REGION_X_MAX = -5, 0
REGION_Y_MIN, REGION_Y_MAX = 0, 5

texts_in_region = get_texts_in_region(
    df, REGION_X_MIN, REGION_X_MAX, REGION_Y_MIN, REGION_Y_MAX
)

print(f"Texts in region ({REGION_X_MIN} to {REGION_X_MAX}, {REGION_Y_MIN} to {REGION_Y_MAX}):")
for t in texts_in_region[:10]:
    print(f"  - {t[:60]}...")
```

### Cell 10: Automatic Cluster Labels (Optional)

```python
# ============================================
# AUTOMATIC CLUSTERING (Optional)
# ============================================
from sklearn.cluster import KMeans

# Choose number of clusters (adjust based on your plot)
N_CLUSTERS = 5

# Run K-means on UMAP coordinates
kmeans = KMeans(n_clusters=N_CLUSTERS, random_state=RANDOM_SEED)
df['cluster'] = kmeans.fit_predict(embeddings_umap)

# Plot with cluster colors
plt.figure(figsize=(12, 8))

for cluster_id in range(N_CLUSTERS):
    mask = df['cluster'] == cluster_id
    plt.scatter(
        embeddings_umap[mask, 0],
        embeddings_umap[mask, 1],
        label=f'Cluster {cluster_id}',
        alpha=0.6,
        s=50
    )

plt.xlabel('UMAP Dimension 1')
plt.ylabel('UMAP Dimension 2')
plt.title('UMAP with K-Means Clusters')
plt.legend()
plt.tight_layout()
plt.savefig('umap_clusters.png', dpi=150)
plt.show()

# Print sample texts from each cluster
print("\nSAMPLE TEXTS FROM EACH CLUSTER:")
print("=" * 60)
for cluster_id in range(N_CLUSTERS):
    cluster_texts = df[df['cluster'] == cluster_id]['title'].head(3)
    print(f"\nCluster {cluster_id}:")
    for t in cluster_texts:
        print(f"  - {t[:60]}...")
```

---

## Part 5: Save and Export (5 minutes)

### Cell 11: Save All Results

```python
# ============================================
# SAVE RESULTS
# ============================================

# Save dataframe with coordinates
df.to_csv('data_with_umap_coords.csv', index=False)
print("Saved: data_with_umap_coords.csv")

# Save UMAP coordinates
np.save('umap_coordinates.npy', embeddings_umap)
print("Saved: umap_coordinates.npy")

# Files are saved in Colab's /content/ folder
# Right-click files in the left panel to download if needed

print("\nVisualization complete! Check the left panel for saved files.")
```

---

## Submission Checklist

### Required Deliverables:

1. **UMAP Plot Image:** Your colored UMAP visualization

2. **Cluster Identification:** List 2-3 clusters you can identify
   | Cluster | Approximate Location | Common Theme |
   |---------|---------------------|--------------|
   | 1 | | |
   | 2 | | |
   | 3 | | |

3. **Interpretation (3-4 sentences):**
   What does your visualization reveal about the structure of your data? Are there surprising groupings?

4. **Saved Files:** Confirm plots are visible in your notebook output

---

## Troubleshooting

**"UMAP is very slow"**
- Reduce sample size for testing: `embeddings[:500]`
- Use lower `n_neighbors` (e.g., 10 instead of 15)

**"My plot has no clusters"**
- Your data might be homogeneous—all similar topic
- Try different UMAP parameters: `min_dist=0.3`
- This is okay—not all data has clear clusters

**"Points are too packed together"**
- Increase `min_dist` (e.g., 0.3 or 0.5)
- This spreads points apart

**"Every run gives different results"**
- Set `random_state` consistently
- UMAP has inherent randomness; this is normal

---

## Challenge Extension (Optional)

1. **3D UMAP:**
```python
reducer_3d = umap.UMAP(n_components=3, random_state=42)
embeddings_3d = reducer_3d.fit_transform(embeddings)
# Requires plotly for interactive 3D visualization
```

2. **Parameter Exploration:**
   Try different `n_neighbors` (5, 15, 50) and `min_dist` (0.0, 0.1, 0.5). How do they affect the visualization?

3. **Word Cloud by Cluster:**
   Generate word clouds for each cluster to understand themes.
