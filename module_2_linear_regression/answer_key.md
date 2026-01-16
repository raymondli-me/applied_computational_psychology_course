# Module 2 Answer Key: Linear Regression
## INSTRUCTOR USE ONLY

**Assessment:** Module 2 Assessment
**Dataset:** `agatha_ballet_dancemoms_agatha`
**Total Points:** 100

---

## Part A: Concept Check (30 points)

### Question 1 (6 points)
**Question:** What does a β (beta) coefficient of -0.35 tell you?

**Model Answer:**
> A negative relationship where for every 1 standard deviation increase in the predictor (X), the outcome (Y) decreases by 0.35 standard deviations. The relationship is moderate in strength.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 6 | Mentions: negative relationship, standardized interpretation, approximate strength |
| 4 | Correct direction and standardized interpretation but missing strength |
| 2 | Identifies negative relationship only |
| 0 | Incorrect or no response |

**Key Points Expected:**
- Negative relationship
- 1 SD change in X → 0.35 SD change in Y
- "Moderate" strength (between 0.2-0.5 is moderate)

---

### Question 2 (6 points)
**Question:** A researcher finds p = 0.08 for their predictor. Should they claim the effect is significant?

**Correct Answer:** B) No, because p must be below 0.05 to claim significance

**Rubric:**
| Score | Criteria |
|-------|----------|
| 6 | Selects B |
| 0 | Any other answer |

**Instructor Note:** Common error is selecting A ("close to 0.05"). Emphasize that "almost significant" is not a valid claim in quantitative research.

---

### Question 3 (6 points)
**Question:** If R² = 0.45, what does this mean in plain language?

**Model Answer:**
> The predictor variable(s) explain 45% of the variance in the outcome variable. The remaining 55% is due to other factors not included in the model.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 6 | Full credit: Explains variance explained + remaining variance |
| 4 | Correct interpretation but missing "remaining variance" component |
| 2 | Mentions 45% but explanation unclear |
| 0 | Incorrect interpretation |

**Common Errors:**
- "R² = 0.45 means 45% correlation" (incorrect - R² is variance explained)
- "The model is 45% accurate" (imprecise language)

---

### Question 4 (6 points)
**Question:** Why would a researcher "control for" view count when examining whether word count predicts likes?

**Model Answer:**
> To isolate the unique effect of word count on likes. Without controlling for views, the relationship might be confounded—videos with more views naturally get more likes, so any correlation between word count and likes might actually be due to view count. Controlling allows us to ask: "Among videos with similar view counts, does word count still matter?"

**Rubric:**
| Score | Criteria |
|-------|----------|
| 6 | Full credit: Mentions isolation of effect + confounding + "holding constant" logic |
| 4 | Correct general idea but missing confounding explanation |
| 2 | Vague mention of "removing effect" without clear reasoning |
| 0 | Incorrect or no response |

**Key Terms Expected:**
- Isolate, unique effect, hold constant
- Confound, spurious relationship
- "Among similar X levels"

---

### Question 5 (6 points)
**Question:** What's the difference between correlation and causation in the context of regression?

**Model Answer:**
> Regression shows correlation (association/relationship) but not causation. Just because word count predicts likes doesn't mean typing more words *causes* more likes. The relationship could be reverse (engaging content → more words AND more likes) or due to a third variable. Causation requires experimental manipulation.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 6 | Distinguishes correlation from causation + explains why regression ≠ causation + mentions alternative explanations |
| 4 | Correct distinction but missing alternative explanations |
| 2 | States "correlation ≠ causation" without elaboration |
| 0 | Incorrect or no response |

**Key Points:**
- Regression = association, not causation
- Alternative explanations (reverse causality, third variable)
- Experimental design needed for causation

---

## Part B: Output Interpretation (35 points)

### Scenario (Given in Assessment)
```
                        coef    std err     P>|t|
---------------------------------------------------------
Intercept             15.23      4.21     0.000
video_length_min       0.89      0.32     0.006
subscriber_count       0.00012   0.00003  0.000

R-squared: 0.287

Standardized coefficients (β):
- video_length_min: β = 0.18
- subscriber_count: β = 0.42
```

---

### Question 6 (10 points)
**Question:** Which predictor has the stronger relationship with comment_count?

**Model Answer:**
> Subscriber count has the stronger relationship (β = 0.42 vs. β = 0.18). We compare standardized coefficients (β) because they're on the same scale, allowing direct comparison. The unstandardized coefficient for subscriber_count (0.00012) looks tiny, but that's because subscriber counts are large numbers—standardizing reveals its true relative impact.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 10 | Correct answer + correct reasoning using β + explains why not raw coefficients |
| 7 | Correct answer + mentions β but reasoning incomplete |
| 5 | Correct answer but uses wrong reasoning |
| 2 | Incorrect answer with some correct reasoning |
| 0 | Incorrect answer and reasoning |

**Common Errors:**
- Comparing raw coefficients (0.89 vs 0.00012) → wrong answer
- Saying "video length" is stronger because 0.89 > 0.00012

---

### Question 7 (10 points)
**Question:** Is the effect of video_length_minutes statistically significant?

**Model Answer:**
> Yes, it is statistically significant because p = 0.006, which is less than the threshold of p = 0.05. This means there's only a 0.6% chance we would observe this relationship if there were truly no effect.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 10 | Correct (yes) + cites p < 0.05 + correct interpretation of p-value |
| 7 | Correct answer + cites p-value but interpretation imprecise |
| 5 | Correct answer but no explanation |
| 0 | Incorrect answer |

**Key Points:**
- p = 0.006 < 0.05 → significant
- Probability interpretation (0.6% chance if null true)

---

### Question 8 (15 points)
**Question:** Write a complete APA-style paragraph reporting these results.

**Model Answer:**
> "A multiple linear regression was conducted to predict comment count from video length (minutes) and subscriber count. Both predictors significantly predicted comment count. Subscriber count was the stronger predictor, β = 0.42, p < .001, while video length also showed a significant positive relationship, β = 0.18, p = .006. The model explained 28.7% of the variance in comment count (R² = .287). These results suggest that channels with more subscribers and longer videos tend to receive more comments, with audience size being the more influential factor."

**Rubric:**
| Component | Points | Criteria |
|-----------|--------|----------|
| Analysis type | 2 | "multiple linear regression" or equivalent |
| β values | 3 | Both β values reported correctly |
| p-values | 3 | Both p-values reported correctly |
| R² value | 3 | R² = .287 or 28.7% |
| Plain language | 2 | Clear interpretation of findings |
| Grammar/APA style | 2 | Proper format, no major errors |

**Acceptable Variations:**
- "β = .42" or "β = 0.42" (both OK)
- "p < .001" or "p = .000" (prefer < .001)
- Decimal places: 2-3 acceptable

---

## Part C: Lab Submission (35 points)

### Task 1: Screenshot (10 points)

**Required Elements:**
| Element | Points |
|---------|--------|
| Coefficient table visible | 5 |
| R-squared value visible | 5 |

**Expected Output Preview:**
```
                            OLS Regression Results
==============================================================================
Dep. Variable:             Post Score   R-squared:          0.XXX
Model:                            OLS   ...
```

---

### Task 2: Results Table (10 points)

**Using Agatha's Dance Data:**
```python
df = load_dataset("agatha_ballet_dancemoms_agatha")
df['text_length'] = df['Post Title'].str.len()
```

**Expected Values (approximate):**

| Metric | Simple Regression | Multiple Regression |
|--------|-------------------|---------------------|
| β for text_length | ~ -0.03 | ~ -0.01 to 0.02 |
| p-value for text_length | ~ 0.15-0.30 | ~ 0.50-0.80 |
| R² | ~ 0.001 | ~ 0.01-0.05 |

**Instructor Note:** The actual correlation between text_length and Post Score is weak (r = -0.028), so students should find a non-significant relationship. This is a valuable learning moment about null results.

**Grading:**
- Values in reasonable range: 6 points
- Correct observation about control variable effect: 4 points

---

### Task 3: APA Write-Up (15 points)

**Rubric:**
| Component | Points | Criteria |
|-----------|--------|----------|
| Analysis type | 2 | Names regression type |
| β value | 3 | Reports standardized coefficient |
| p-value | 3 | Reports significance correctly |
| R² value | 3 | Reports model fit |
| Control variable | 2 | Mentions what was controlled |
| Clarity | 2 | Readable, professional |

**Example Student Answer:**
> "A multiple linear regression was conducted predicting Post Score from text_length while controlling for Post Num Comments. Text length did not significantly predict Post Score, β = -0.02, p = .62. The model explained only 2% of variance (R² = .02). Controlling for number of comments did not substantially change the relationship."

---

## Expected Code Outputs

### Data Loading
```python
df = load_dataset("agatha_ballet_dancemoms_agatha", nrows=5000)
print(df.shape)
print(df.columns.tolist())
```

**Output:**
```
(2523, 19)
['text_id', 'Post Title', 'Post URL', 'Post Score', 'Post Author',
'Post Num Comments', 'Post Body', 'Media URL', 'Post Created',
'Comment Body', 'Comment Author', 'Comment Score', 'Comment Created',
'Reply Body', 'Reply Author', 'Reply Score', 'Reply Created',
'Unnamed: 17', 'Unnamed: 18']
```

### Descriptive Statistics
```
Post Score: mean=124, std=140, range=0-631
Post Num Comments: mean=60, std=40, range=2-164
text_length: mean=44, std=25, range=10-128
```

### Correlation Matrix
```
text_length vs Post Score: r = -0.028 (very weak negative)
text_length vs Post Num Comments: r = -0.171 (weak negative)
```

---

## Common Student Errors

1. **Comparing raw coefficients instead of β**
   - Error: "0.89 > 0.00012 so video length is stronger"
   - Correction: Compare standardized coefficients (β)

2. **Misinterpreting p-values**
   - Error: "p = 0.06 is almost significant"
   - Correction: p < 0.05 or not significant, no "almost"

3. **Confusing R² with correlation**
   - Error: "R² = 0.45 means 45% correlation"
   - Correction: R² is proportion of variance explained

4. **Forgetting to mention control variables**
   - Error: "Word count predicts likes"
   - Correction: "Word count predicts likes, controlling for view count"

5. **Claiming causation from regression**
   - Error: "Longer videos cause more comments"
   - Correction: "Longer videos are associated with more comments"

---

## Grading Summary

| Component | Points |
|-----------|--------|
| Part A: Q1-Q5 Concepts | 30 |
| Part B: Q6 Stronger predictor | 10 |
| Part B: Q7 Significance | 10 |
| Part B: Q8 APA write-up | 15 |
| Part C: Task 1 Screenshot | 10 |
| Part C: Task 2 Results table | 10 |
| Part C: Task 3 APA write-up | 15 |
| **TOTAL** | **100** |

---

*Answer Key Version: 1.0 | Date: 2026-01-15*
