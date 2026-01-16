# Applied Psychological Data Science
## Detailed Syllabus

---

## Course Information

**Course Title:** Applied Psychological Data Science: The Li Lab Bootcamp
**Credits:** Micro-credential (equivalent to 2 credit hours)
**Duration:** 12 weeks
**Time Commitment:** 2 hours per week
**Format:** Asynchronous with optional synchronous office hours

---

## Instructor Information

**Instructor:** [Name]
**Email:** [Email]
**Office Hours:** [Times]
**Office:** [Location/Zoom link]

---

## Course Description

This micro-credential provides hands-on training in computational methods for psychological research. Students will learn to collect, clean, and analyze text data using modern tools including large language models (LLMs), embeddings, and dimensionality reduction techniques. The course culminates in an independent project replicating the methodology of published research.

---

## Learning Objectives

By the end of this course, students will be able to:

1. **Data Management**
   - Clean and structure raw data for analysis
   - Distinguish between structured and unstructured data
   - Formulate testable hypotheses

2. **Statistical Analysis**
   - Conduct and interpret linear regression
   - Report results in APA format
   - Understand controlling for confounding variables

3. **AI-Assisted Research**
   - Design effective prompts for LLM rating tasks
   - Validate AI-generated ratings against human judgment
   - Apply ethical considerations in AI-assisted research

4. **Data Collection**
   - Collect data from web APIs
   - Design effective search queries
   - Assess and improve data quality

5. **High-Dimensional Analysis**
   - Generate and interpret text embeddings
   - Apply dimensionality reduction (PCA, UMAP)
   - Visualize and interpret semantic clusters

6. **Research Communication**
   - Write a research brief following publication standards
   - Create informative data visualizations
   - Present findings to diverse audiences

---

## Required Materials

### Technology (Free)
- Google Account (for Google Colab)
- Internet connection
- Web browser (Chrome recommended)

### Provided by Course
- All code notebooks
- **825 research datasets** (105M+ rows) from past RAs
- API access keys (shared for educational use)

---

## Course Dataset Bank

This course includes access to a comprehensive dataset bank created by 16 students who completed this program before you.

**Total Resources:**
- 825 datasets | 105+ million rows | 10+ GB of data
- 7 research domains | All publicly accessible

**Key Contributors & Their Research:**
| Student | Domain | Scale | Best For |
|---------|--------|-------|----------|
| Andrea | Wedding Reddit | 871K posts | M1, M4, M7 |
| Peter | Political News | 1.5M articles | M1, M3, M6 |
| Kaitlyn | Mental Health | 809K comments | M2, M3 |
| Agatha | Dance/Body Image | 314K comments | M2, M5, M6 |
| Elle | YouTube Influencers | 59 channels | M4 |
| Clara | Political Text | 25K texts | M5, M6 |
| Winnie | YouTube Comments | 26M comments | M6 |

**How to Access:**
```python
# Copy the data loader boilerplate into any Colab notebook
# Then use these commands:

list_datasets()                    # See all 825 datasets
list_datasets(tier=1)              # See best exemplars
list_datasets(module="M4")         # Filter by module
df = load_dataset("dataset_name")  # Load any dataset
```

**The Philosophy:** Every dataset was created by a real research assistant. Their work trains you. Your capstone may train future students.

### Recommended (Not Required)
- OpenAI API account ($5-10 credit recommended for extended work)

---

## Weekly Schedule

### Week 1-2: Module 1 - The Dataset & The Question
**Topics:**
- Tidy data principles
- Rows, columns, observations, variables
- Formulating hypotheses

**Featured Dataset: Andrea's Wedding Reddit Study**
```python
df = load_dataset("andrea_reddit_results_andrea_2025_03_13")
# 871,775 Reddit posts about wedding conflicts
```
*Andrea collected this data for her capstone studying interpersonal dynamics in wedding-related advice seeking.*

**Deliverables:**
- Cleaned dataset (screenshot)
- One-sentence hypothesis

**Readings:**
- RA Manuscript Abstract and Introduction
- See: `DATASETS_FOR_M1.md` for all recommended datasets

---

### Week 3-4: Module 2 - The General Linear Model
**Topics:**
- Simple and multiple regression
- Beta coefficients, p-values, R-squared
- APA reporting format

**Featured Dataset: Agatha's Dance Ratings**
```python
df = load_dataset("agatha_ballet_1_100_ratings")
# 4,985 comments with human ratings from 6 raters
```
*Agatha's team manually coded body image discourse in dance communities - perfect for inter-rater reliability practice.*

**Deliverables:**
- Regression output
- APA-style results paragraph

**Readings:**
- RA Manuscript Table 2 and Results section
- See: `DATASETS_FOR_M2.md` for all recommended datasets

---

### Week 5-6: Module 3 - LLMs as Raters
**Topics:**
- Prompt engineering principles
- Temperature and consistency
- Human-AI reliability

**Featured Dataset: Kaitlyn's Mental Health Ratings**
```python
df = load_dataset("kaitlyn_merged_data_overview_kaitlyn_master")
# 809,098 YouTube comments with human ratings across 23 conditions
```
*Kaitlyn's 6-rater team achieved κ > 0.80 reliability - use as ground truth for validating your LLM prompts.*

**Deliverables:**
- Rating prompt
- Correlation with human ratings

**Readings:**
- RA Manuscript Methods (Rating section)
- See: `DATASETS_FOR_M3.md` for all recommended datasets

---

### Week 7-8: Module 4 - Getting Real Data
**Topics:**
- API fundamentals
- Keyword strategy
- Data quality assessment

**Featured Dataset: Elle's YouTube Channel Collection**
```python
list_datasets(contributor="Elle")  # 59 datasets from 55 channels
df = load_dataset("elle_morgan_ashley_absher_30_videos_ucvuw0xt38ho7qyumbgbzxqa")
```
*Elle systematically collected from 55 YouTube influencer channels - study her methodology as a collection exemplar.*

**Deliverables:**
- Collected dataset (100+ items)
- Data collection log

**Readings:**
- News Analysis Code documentation
- See: `DATASETS_FOR_M4.md` for all recommended datasets

---

### Week 9-10: Module 5 - Embeddings
**Topics:**
- Text representation
- Cosine similarity
- Semantic search

**Featured Dataset: Clara's BERT Embeddings**
```python
df = load_dataset("clara_bert_embeddings")
# 12,915 texts with 768-dimensional BERT embeddings pre-computed
```
*Clara's embeddings are ready for cosine similarity and clustering - skip the computation, focus on interpretation.*

**Deliverables:**
- Generated embeddings
- Most similar pair analysis

**Readings:**
- Thesis: Text Representation Methods section
- See: `DATASETS_FOR_M5.md` for all recommended datasets

---

### Week 11: Module 6 - PCA & UMAP
**Topics:**
- Dimensionality reduction concepts
- UMAP visualization
- Cluster interpretation

**Featured Dataset: Winnie's UMAP Clusters**
```python
df = load_dataset("winnie_umap_dbscan_results_20250223_154628")
# 82,127 YouTube comments with UMAP coordinates and cluster labels
```
*Winnie processed over 26 million comments through UMAP - explore her clusters and interpretation methods.*

**Deliverables:**
- UMAP visualization
- Cluster identification and interpretation

**Readings:**
- Thesis: UMAP figures and discussion
- See: `DATASETS_FOR_M6.md` for all recommended datasets

---

### Week 12: Module 7 - Capstone Project
**Topics:**
- Project synthesis
- Research communication
- Peer feedback (optional)

**Exemplar Capstone: Andrea, Agatha, Raymond**
```python
# Andrea's complete pipeline (raw → embeddings → PCA)
# Agatha's body image study (human ratings + LLM validation)
# Raymond's ML pipeline (XGBoost → SHAP → DML)
# See DATASETS_FOR_M7.md for full exemplar details
```
*Choose a course dataset or collect your own. Apply the full pipeline you've learned.*

**Deliverables:**
- 1-page research brief
- Code notebook
- Presentation (optional/bonus)

**See:** `DATASETS_FOR_M7.md` for capstone exemplars and dataset recommendations

---

## Grading

### Assessment Breakdown

| Component | Weight | Description |
|-----------|--------|-------------|
| Module 1 Assessment | 10% | Data cleaning + hypothesis |
| Module 2 Assessment | 10% | Regression analysis |
| Module 3 Assessment | 10% | LLM rating + validation |
| Module 4 Assessment | 10% | Data collection |
| Module 5 Assessment | 10% | Embeddings |
| Module 6 Assessment | 10% | Visualization |
| Capstone Project | 30% | Research brief |
| Participation | 10% | Engagement, questions |

### Grading Scale

| Grade | Percentage |
|-------|------------|
| A | 93-100% |
| A- | 90-92% |
| B+ | 87-89% |
| B | 83-86% |
| B- | 80-82% |
| C+ | 77-79% |
| C | 73-76% |
| C- | 70-72% |
| D | 60-69% |
| F | Below 60% |

### Late Policy
- Assignments due by 11:59 PM on the specified date
- 10% penalty per day late (up to 3 days)
- After 3 days, assignments not accepted without prior arrangement

---

## Course Policies

### Academic Integrity
- All work must be your own
- Collaboration encouraged on concepts; individual submissions required
- AI assistance (like ChatGPT) is permitted for debugging and explanation
- AI-generated analysis or writing must be disclosed and validated

### Attendance
- Asynchronous format: no required synchronous attendance
- Office hours are recommended but optional
- Discussion board participation counts toward participation grade

### Accessibility
- All materials available in text format
- Video content includes transcripts
- Contact instructor for accommodations

### Communication
- Email responses within 48 hours (business days)
- Use discussion board for questions others might benefit from
- Office hours for individual guidance

---

## Technical Support

### Google Colab Issues
- Ensure you're signed into Google account
- Try refreshing the page
- Check [Colab FAQ](https://research.google.com/colaboratory/faq.html)

### API Issues
- Verify API key is entered correctly
- Check for rate limiting (add delays)
- Contact instructor if shared key issues

### General Computing
- [University IT Support Link]
- [Colab Community Forums]

---

## Course Calendar Summary

| Week | Module | Key Deliverable |
|------|--------|-----------------|
| 1-2 | Data & Question | Cleaned data + hypothesis |
| 3-4 | Linear Models | Regression results |
| 5-6 | LLMs as Raters | Validated ratings |
| 7-8 | APIs & Data | Collected dataset |
| 9-10 | Embeddings | Similarity analysis |
| 11 | PCA & UMAP | Visualization |
| 12 | Capstone | Research brief |

---

## Additional Resources

### Statistics Refresher
- [Khan Academy: Statistics](https://www.khanacademy.org/math/statistics-probability)
- [Crash Course Statistics](https://www.youtube.com/playlist?list=PL8dPuuaLjXtNM_Y-bUAhblSAdWRnmGUcr)

### Python Basics (Optional)
- [Python for Everybody](https://www.py4e.com/)
- [Colab Introduction Notebook](https://colab.research.google.com/notebooks/intro.ipynb)

### Writing Help
- APA Style Guide (7th edition)
- [Purdue OWL: APA Formatting](https://owl.purdue.edu/owl/research_and_citation/apa_style/)

---

## Instructor's Note

This course is designed to be achievable for students with no prior programming experience. The code is provided—your job is to understand what it does and apply it to your own questions.

The golden rule: **"Don't invent a new method. Clone the RA Manuscript but change the Dataset and the Variable."**

Success comes from mastering the fundamentals and applying them thoughtfully, not from methodological complexity.

Welcome to computational psychology!

---

*Last Updated: [Date]*
*Version: 1.0*
