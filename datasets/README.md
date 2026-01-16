# Course Datasets

This course uses **504 real datasets** collected by students, hosted on Google Cloud Storage.

## Accessing Datasets

All datasets are loaded through the `load_dataset()` function in the course notebook:

```python
# Load a dataset
df = load_dataset("andrea_reddit_results_andrea_2025_03_13")

# Load only first N rows (for large datasets)
df = load_dataset("andrea_reddit_results_andrea_2025_03_13", nrows=5000)

# List all available datasets
list_datasets()

# Filter by contributor
list_datasets(contributor="Andrea")

# Search by keyword
list_datasets(search="reddit")
```

## Dataset Hosting

Datasets are hosted on Google Cloud Storage:
- **Bucket:** `variable-resolution-applied-computational-psychology-course`
- **Format:** CSV files
- **Access:** Public (read-only)

The catalog (`manifest.json`) contains metadata for all 504 datasets including:
- Row counts
- Column information
- Contributor attribution
- Quality tier ratings

## Recommended Datasets by Module

| Module | Dataset | Rows | Description |
|--------|---------|------|-------------|
| M1 | `andrea_reddit_results_andrea_2025_03_13` | 871K | Reddit posts about weddings |
| M2 | `agatha_ballet_dancemoms_agatha` | 2.5K | Dance community posts |
| M3 | `yashita_yashita_data` | 2.1K | YouTube video metadata |
| M3 | `kaitlyn_merged_data_overview_kaitlyn_master` | 809K | Mental health comments with ratings |
| M5 | `clara_bert_embeddings` | 12.9K | Political texts with 768D embeddings |
| M6 | `raymond_umap_dbscan_results_20250223_154628` | 82K | Pre-computed UMAP coordinates |

## Data Contributors

| Tier | Contributors | Description |
|------|--------------|-------------|
| 1 | Andrea, Peter, Kaitlyn, Lauren, Emily, Agatha, Raymond | Large, exemplary datasets |
| 2 | Leighton, Nash, Elle, Winnie, Clara | Medium-sized datasets |
| 3 | Malina, Melana, Ernest, Yashita | Smaller practice datasets |

## Adding New Datasets

Instructors can add datasets using the ingestion scripts in the `dataset_system/` folder (not included in this repo). Contact the course administrator for access.
