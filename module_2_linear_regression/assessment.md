# Module 2 Assessment: Linear Regression

**Recommended Dataset:** `agatha_ballet_dancemoms_agatha` (Agatha's Dance Data - 30,511 posts with scores)
**Alternate Datasets:** See DATASETS_FOR_M2.md (Agatha's complete dataset, Peter's news data)

---

## Part A: Concept Check (30 points)

### Question 1 (6 points)
What does a β (beta) coefficient of -0.35 tell you?

**Model Answer:** A negative relationship where for every 1 standard deviation increase in the predictor (X), the outcome (Y) decreases by 0.35 standard deviations. The relationship is moderate in strength.

---

### Question 2 (6 points)
A researcher finds p = 0.08 for their predictor. Should they claim the effect is significant? Why or why not?

- A) Yes, because 0.08 is close to 0.05
- B) No, because p must be below 0.05 to claim significance
- C) Yes, because any p < 0.10 is acceptable
- D) No, because we should use p < 0.01 instead

**Correct Answer:** B

---

### Question 3 (6 points)
If R² = 0.45, what does this mean in plain language?

**Model Answer:** The predictor variable(s) explain 45% of the variance in the outcome variable. The remaining 55% is due to other factors not included in the model.

---

### Question 4 (6 points)
Why would a researcher "control for" view count when examining whether word count predicts likes?

**Model Answer:** To isolate the unique effect of word count on likes. Without controlling for views, the relationship might be confounded—videos with more views naturally get more likes, so any correlation between word count and likes might actually be due to view count. Controlling allows us to ask: "Among videos with similar view counts, does word count still matter?"

---

### Question 5 (6 points)
What's the difference between correlation and causation in the context of regression?

**Model Answer:** Regression shows correlation (association/relationship) but not causation. Just because word count predicts likes doesn't mean typing more words *causes* more likes. The relationship could be reverse (engaging content → more words AND more likes) or due to a third variable. Causation requires experimental manipulation.

---

## Part B: Output Interpretation (35 points)

### Scenario
You run a regression predicting `comment_count` from `video_length_minutes` and `subscriber_count`. Here is a simplified output:

```
                        coef    std err     P>|t|
---------------------------------------------------------
Intercept             15.23      4.21     0.000
video_length_min       0.89      0.32     0.006
subscriber_count       0.00012   0.00003  0.000

R-squared: 0.287
```

Standardized coefficients (β):
- video_length_min: β = 0.18
- subscriber_count: β = 0.42

---

### Question 6 (10 points)
Which predictor has the stronger relationship with comment_count? How do you know?

**Model Answer:** Subscriber count has the stronger relationship (β = 0.42 vs. β = 0.18). We compare standardized coefficients (β) because they're on the same scale, allowing direct comparison. The unstandardized coefficient for subscriber_count (0.00012) looks tiny, but that's because subscriber counts are large numbers—standardizing reveals its true relative impact.

---

### Question 7 (10 points)
Is the effect of video_length_minutes statistically significant? How do you know?

**Model Answer:** Yes, it is statistically significant because p = 0.006, which is less than the threshold of p = 0.05. This means there's only a 0.6% chance we would observe this relationship if there were truly no effect.

---

### Question 8 (15 points)
Write a complete APA-style paragraph reporting these results. Include:
- Type of analysis
- What predicted what
- β values
- p-values
- R² value
- A plain-language interpretation

**Model Answer:**
"A multiple linear regression was conducted to predict comment count from video length (minutes) and subscriber count. Both predictors significantly predicted comment count. Subscriber count was the stronger predictor, β = 0.42, p < .001, while video length also showed a significant positive relationship, β = 0.18, p = .006. The model explained 28.7% of the variance in comment count (R² = .287). These results suggest that channels with more subscribers and longer videos tend to receive more comments, with audience size being the more influential factor."

---

## Part C: Lab Submission (35 points)

### Task 1: Screenshot (10 points)
Submit a screenshot of your regression output from the Colab notebook showing:
- [ ] The coefficient table
- [ ] R-squared value visible

---

### Task 2: Results Table (10 points)

Using Agatha's dance data (`agatha_ballet_dancemoms_agatha`), complete this table:

| Metric | Simple Regression (text_length only) | Multiple Regression (+ Comment_Score) |
|--------|-------------------------------------|-------------------------------------|
| β for text_length | | |
| p-value for text_length | | |
| R² | | |

*Note: Create `text_length` from `Post Title` string length. Rename columns for statsmodels compatibility.*

What changed when you added the control variable?

---

### Task 3: APA Write-Up (15 points)

Write 3-4 sentences reporting your multiple regression results in APA format.

**Grading Rubric:**
- Correctly identifies analysis type (2 points)
- Reports β with correct value (3 points)
- Reports p-value correctly (3 points)
- Reports R² correctly (3 points)
- Mentions controlling for view_count (2 points)
- Grammar and clarity (2 points)

---

## Grading Summary

| Component | Points |
|-----------|--------|
| Part A: Concept Check | 30 |
| Part B: Output Interpretation | 35 |
| Part C: Lab Submission | 35 |
| **Total** | **100** |

---

## Submission Instructions

1. Complete all questions in a single document
2. Include clearly labeled screenshots
3. Double-check your β and p-value decimal places
4. Submit via [Course Platform] by [Deadline]
