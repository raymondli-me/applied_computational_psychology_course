# Module 6: PCA & UMAP Visualization

**Mapping the Mind**

## Learning Objectives

By the end of this module, you will be able to:
- Understand why we need dimensionality reduction
- Compare PCA (global structure) vs UMAP (local neighborhoods)
- Create and interpret UMAP visualizations
- Identify and describe clusters in your data

## Key Dataset

**Raymond's UMAP Results** - 82,127 comments with pre-computed UMAP coordinates

```python
df = load_dataset("raymond_umap_dbscan_results_20250223_154628", nrows=10000)
# Columns: comment_id, umap_x, umap_y, cluster, auto_cluster_label
```

## Materials

| File | Description |
|------|-------------|
| [lecture_notes.md](lecture_notes.md) | Lecture content (~41 min) |
| [lab_instructions.md](lab_instructions.md) | Hands-on exercises (60 min) |
| [assessment.md](assessment.md) | Test your understanding |
| [answer_key.md](answer_key.md) | Model answers |
| [flashcards.md](flashcards.md) | 22 study cards |

## Estimated Time

~2 hours total
