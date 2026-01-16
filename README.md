# Applied Psychological Data Science

**A hands-on course teaching data science through real psychological research datasets.**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/raymondli-me/applied_computational_psychology_course/blob/main/course_notebook.ipynb)

> **Click the badge above to open the course notebook in Google Colab!**

---

## Quick Start

1. **Click the "Open in Colab" badge** above
2. **Save a copy** to your Google Drive (File → Save a copy in Drive)
3. **Run the first cell** to connect to the course datasets
4. **Follow the lab instructions** for each module below

---

## Course Overview

This course teaches psychological data science using real datasets collected by students. You'll learn to:

- Clean and structure data for analysis
- Run and interpret linear regression
- Use LLMs (GPT-4, Claude) as research assistants
- Collect data from APIs (YouTube, Reddit, News)
- Create text embeddings and measure semantic similarity
- Visualize high-dimensional data with PCA and UMAP

---

## Modules

| Module | Topic | Key Dataset |
|--------|-------|-------------|
| [Module 1](module_1_data_foundations/) | Data Foundations | Andrea's Reddit (871K posts) |
| [Module 2](module_2_linear_regression/) | Linear Regression | Agatha's Dance Community |
| [Module 3](module_3_llms_as_raters/) | LLMs as Raters | Kaitlyn's Mental Health Data |
| [Module 4](module_4_apis/) | APIs & Data Collection | Elle, Peter, Andrea exemplars |
| [Module 5](module_5_embeddings/) | Text Embeddings | Clara's BERT Embeddings |
| [Module 6](module_6_pca_umap/) | PCA & UMAP | Raymond's UMAP Clusters |

---

## Course Materials (Each Module Contains)

- **lecture_notes.md** - Concepts and explanations
- **lab_instructions.md** - Hands-on coding exercises
- **assessment.md** - Test your understanding
- **answer_key.md** - Model answers (for self-checking)
- **flashcards.md** - Study cards for key terms

---

## Datasets

This course uses **504 real datasets** collected by students, hosted on Google Cloud Storage.

All datasets are accessible through the `load_dataset()` function in the course notebook:

```python
# Load Andrea's Reddit data
df = load_dataset("andrea_reddit_results_andrea_2025_03_13", nrows=5000)

# List all available datasets
list_datasets()

# Filter by contributor
list_datasets(contributor="Andrea")
```

See [datasets/README.md](datasets/README.md) for the full catalog.

---

## Requirements

- **Google Account** (for Colab)
- **No installation required** - everything runs in the browser
- **Optional**: OpenAI API key for Module 3 (LLM rating)

---

## For Instructors

### Updating Content

- Edit the markdown files in each module folder
- Changes are tracked with git
- The `course_notebook.ipynb` rarely needs updating (only if the data loader changes)

### Repository Structure

```
├── README.md                    # This file
├── SYLLABUS.md                  # Full syllabus
├── course_notebook.ipynb        # Student workspace (Colab)
├── setup/
│   └── data_loader.py           # Standalone loader script
├── module_1_data_foundations/
│   ├── lecture_notes.md
│   ├── lab_instructions.md
│   ├── assessment.md
│   ├── answer_key.md
│   └── flashcards.md
├── module_2_linear_regression/
│   └── ...
└── datasets/
    └── README.md                # Dataset catalog info
```

---

## License

[Add your license here]

---

## Acknowledgments

Course datasets contributed by: Andrea, Peter, Kaitlyn, Lauren, Emily, Agatha, Raymond, Elle, Leighton, Nash, Winnie, Clara, Malina, Melana, Ernest, and Yashita.

---

**Questions?** Open an issue on this repository.
