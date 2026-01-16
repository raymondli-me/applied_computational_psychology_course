# Module 2 Flashcards: Linear Regression

**Total Cards:** 24
**Format:** Anki-compatible (Front/Back)

---

## Definitions (7 cards)

### Card 1
**Front:** What is a regression coefficient (b)?
**Back:** The unstandardized coefficient showing the change in Y for each 1-unit change in X. Example: b = 2.5 means Y increases by 2.5 for every 1-unit increase in X.
**Tags:** M2, definition, regression

### Card 2
**Front:** What is beta (β)?
**Back:** The standardized coefficient showing how many standard deviations Y changes for each 1 SD change in X. Allows comparing effects across different variables.
**Tags:** M2, definition, regression

### Card 3
**Front:** What is R² (R-squared)?
**Back:** The proportion of variance in Y explained by the predictor(s). R² = 0.30 means the model explains 30% of the variance; 70% is due to other factors.
**Tags:** M2, definition, regression

### Card 4
**Front:** What is a p-value?
**Back:** The probability of observing this result (or more extreme) if there were truly no effect. p < 0.05 is typically considered statistically significant.
**Tags:** M2, definition, statistics

### Card 5
**Front:** What is statistical significance?
**Back:** When p < 0.05 (typically), meaning there's less than 5% chance the observed relationship is due to random chance. The effect is "real" enough to not be a fluke.
**Tags:** M2, definition, statistics

### Card 6
**Front:** What is a control variable?
**Back:** A variable included in the model to "hold constant" its effects. Allows examining the unique effect of your IV on DV, removing the influence of the control.
**Tags:** M2, definition, regression

### Card 7
**Front:** What is multiple regression?
**Back:** Regression with more than one predictor variable. Allows controlling for confounds and examining unique effects of each predictor.
**Tags:** M2, definition, regression

---

## Concepts (7 cards)

### Card 8
**Front:** Why use standardized beta (β) instead of unstandardized (b)?
**Back:** β allows comparing effects across variables with different scales. "Likes" (0-1000) vs. "word count" (0-500) have different b values even if equally important. β puts them on the same scale.
**Tags:** M2, concept, regression

### Card 9
**Front:** What does "controlling for view_count" mean?
**Back:** Asking: "Among videos with similar view counts, does word count still predict likes?" Removes the confounding effect of views to isolate word count's unique contribution.
**Tags:** M2, concept, regression

### Card 10
**Front:** Why might R² = 0.05 still be meaningful?
**Back:** In psychology, human behavior is messy. 5% explained variance can be theoretically important and practically useful. Small effects are real effects. Report honestly, don't chase large R².
**Tags:** M2, concept, interpretation

### Card 11
**Front:** What happens to β when you add control variables?
**Back:** It can: 1) Decrease (the original effect was partly due to the control), 2) Stay same (independent effects), or 3) Increase (suppression - rare). Changes reveal what's driving the relationship.
**Tags:** M2, concept, regression

### Card 12
**Front:** What's the formula syntax for regression in statsmodels?
**Back:** `'DV ~ IV'` for simple regression. `'DV ~ IV1 + IV2'` for multiple regression. The ~ means "predicted by." Example: `'likes ~ word_count + views'`
**Tags:** M2, concept, code

### Card 13
**Front:** Why does statsmodels need columns without spaces?
**Back:** The formula syntax `'Y ~ X'` can't parse column names with spaces. Rename `'Post Score'` to `'Post_Score'` or use `Q('Post Score')` syntax.
**Tags:** M2, concept, code

### Card 14
**Front:** What does "variance explained" mean intuitively?
**Back:** How well your predictor(s) predict the outcome. R² = 0.40 means knowing X gives you 40% of the information needed to perfectly predict Y. The rest is noise/other factors.
**Tags:** M2, concept, interpretation

---

## Code Patterns (5 cards)

### Card 15
**Front:** How do you run a simple regression in Python?
**Back:**
```python
import statsmodels.formula.api as smf
model = smf.ols('DV ~ IV', data=df).fit()
print(model.summary())
```
**Tags:** M2, code, regression

### Card 16
**Front:** How do you run multiple regression with controls?
**Back:**
```python
model = smf.ols('likes ~ word_count + view_count', data=df).fit()
print(model.summary())
```
**Tags:** M2, code, regression

### Card 17
**Front:** How do you get standardized beta coefficients?
**Back:**
```python
from scipy import stats
df['x_z'] = stats.zscore(df['x'])
df['y_z'] = stats.zscore(df['y'])
model = smf.ols('y_z ~ x_z', data=df).fit()
```
**Tags:** M2, code, regression

### Card 18
**Front:** How do you prepare column names for statsmodels?
**Back:**
```python
df = df.rename(columns={'Post Score': 'Post_Score'})
# Or use all underscores
df.columns = df.columns.str.replace(' ', '_')
```
**Tags:** M2, code, data_prep

### Card 19
**Front:** How do you handle NaN before regression?
**Back:**
```python
df_clean = df.dropna(subset=['DV', 'IV1', 'IV2'])
# Or in the model call:
model = smf.ols('y ~ x', data=df.dropna()).fit()
```
**Tags:** M2, code, data_cleaning

---

## Interpretation (3 cards)

### Card 20
**Front:** β = -0.25, p = 0.03. Interpret this.
**Back:** Significant negative relationship. For each 1 SD increase in X, Y decreases by 0.25 SD. The effect is unlikely due to chance (p < 0.05). Moderate effect size.
**Tags:** M2, interpretation, regression

### Card 21
**Front:** β = 0.15, p = 0.08. Interpret this.
**Back:** NOT statistically significant (p > 0.05). We cannot claim a relationship exists. Report as "did not significantly predict" with the exact p-value. Do NOT say "almost significant."
**Tags:** M2, interpretation, regression

### Card 22
**Front:** R² went from 0.15 to 0.22 after adding a control. What happened?
**Back:** The control variable helped explain additional variance. The original predictor still contributes, but together they explain more (22% vs 15%). The improvement is 7 percentage points.
**Tags:** M2, interpretation, regression

---

## Common Mistakes (2 cards)

### Card 23
**Front:** What's wrong with "p = 0.06 is almost significant"?
**Back:** "Almost significant" is not valid. Either p < 0.05 or it isn't. Report honestly: "did not significantly predict, p = .06." Don't torture the data to get significance.
**Tags:** M2, mistake, statistics

### Card 24
**Front:** What's wrong with claiming causation from regression?
**Back:** Regression shows correlation, not causation. "Word count predicts likes" doesn't mean more words CAUSE more likes. Could be reverse causation or a third variable. Need experiments for causation.
**Tags:** M2, mistake, interpretation

---

*Module 2 Flashcards | Applied Psychological Data Science*
