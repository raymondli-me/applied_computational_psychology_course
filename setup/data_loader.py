"""
Applied Psychological Data Science - Data Loader

This module provides functions to load course datasets from Google Cloud Storage.
Use this in Google Colab or any Python environment.

Usage:
    from data_loader import load_dataset, list_datasets

    df = load_dataset("andrea_reddit_results_andrea_2025_03_13")
    list_datasets(contributor="Andrea")
"""

import pandas as pd
import json
import urllib.request

# Course dataset configuration
GCS_BUCKET = "variable-resolution-applied-computational-psychology-course"
GCS_BASE_URL = f"https://storage.googleapis.com/{GCS_BUCKET}"
CATALOG_URL = f"{GCS_BASE_URL}/manifest.json"

# Load the catalog on import
_CATALOG = None

def _get_catalog():
    """Load the dataset catalog (cached)."""
    global _CATALOG
    if _CATALOG is None:
        with urllib.request.urlopen(CATALOG_URL) as response:
            _CATALOG = json.loads(response.read().decode())
        print(f"Connected to course dataset system: {len(_CATALOG['datasets'])} datasets available")
    return _CATALOG


def load_dataset(name: str, nrows: int = None) -> pd.DataFrame:
    """
    Load a course dataset by name.

    Parameters
    ----------
    name : str
        The dataset name (e.g., "andrea_reddit_results_andrea_2025_03_13")
    nrows : int, optional
        Number of rows to load (useful for large datasets)

    Returns
    -------
    pandas.DataFrame
        The loaded dataset

    Examples
    --------
    >>> df = load_dataset("andrea_reddit_results_andrea_2025_03_13")
    >>> df = load_dataset("clara_bert_embeddings", nrows=1000)
    """
    catalog = _get_catalog()

    for ds in catalog['datasets']:
        if ds['canonical_name'] == name:
            url = ds['access']['public_url']
            df = pd.read_csv(url, nrows=nrows)
            print(f"Loaded {len(df):,} rows from '{name}'")
            return df

    # Dataset not found - show similar names
    similar = [ds['canonical_name'] for ds in catalog['datasets']
               if name.lower() in ds['canonical_name'].lower()][:5]
    raise ValueError(f"Dataset '{name}' not found. Similar names: {similar}")


def list_datasets(contributor: str = None, search: str = None, limit: int = 20):
    """
    List available datasets.

    Parameters
    ----------
    contributor : str, optional
        Filter by contributor name (e.g., "Andrea", "Peter")
    search : str, optional
        Search in dataset names
    limit : int, default 20
        Maximum number of results to display

    Examples
    --------
    >>> list_datasets()
    >>> list_datasets(contributor="Andrea")
    >>> list_datasets(search="reddit")
    """
    catalog = _get_catalog()

    results = []
    for ds in catalog['datasets']:
        name = ds['canonical_name']
        if contributor and contributor.lower() not in name.lower():
            continue
        if search and search.lower() not in name.lower():
            continue
        rows = ds.get('stats', {}).get('rows', 'unknown')
        if isinstance(rows, int):
            results.append(f"{name} ({rows:,} rows)")
        else:
            results.append(name)

    print(f"Found {len(results)} datasets:")
    for r in results[:limit]:
        print(f"  - {r}")
    if len(results) > limit:
        print(f"  ... and {len(results) - limit} more")


def get_dataset_info(name: str) -> dict:
    """
    Get metadata for a specific dataset.

    Parameters
    ----------
    name : str
        The dataset name

    Returns
    -------
    dict
        Dataset metadata including rows, columns, contributor info
    """
    catalog = _get_catalog()

    for ds in catalog['datasets']:
        if ds['canonical_name'] == name:
            return ds

    raise ValueError(f"Dataset '{name}' not found")


# Convenience: load catalog on import
if __name__ != "__main__":
    try:
        _get_catalog()
    except Exception as e:
        print(f"Warning: Could not connect to dataset catalog: {e}")
