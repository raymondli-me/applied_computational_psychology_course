# Module 2: Lecture Script
## "The Line That Predicts: Understanding Regression"

**Total Runtime:** ~41 minutes
**Video Production Ready:** Yes

---

### INTRO [0:00-2:00]
*[INSTRUCTOR NOTE: The "β = .31" reveal should hook students]*

**[SLIDE: Agatha's Dance Research - Human Ratings]**

*"Last semester, Agatha led a team of 6 research assistants. They spent weeks rating dance videos—5,000 ratings for ballet, another 5,000 for K-pop, 4,000 for Zumba. Each video got a score for body image content."*

*"But how do we know those ratings MEAN something? How do we know body image scores relate to viewer engagement? That's where regression comes in."*

*"See this number? β = .31. That's the entire result of a regression analysis, compressed into one number. By the end of today, you'll know exactly what it means—and you'll calculate your own using Agatha's real data."*

---

### SECTION 1: THE BIG IDEA [2:00-10:00]
*[INSTRUCTOR NOTE: The scatterplot-to-line transition is the "aha" moment]*

**[SLIDE: Scatterplot with points, no line]**

*"Let's start with a question. Say you have data on 300 YouTube videos. For each video, you know its word count and its like count. Here's what that looks like as a scatterplot."*

*"Each dot is a video. The x-axis is word count. The y-axis is likes. What do you notice?"*

**[PAUSE for response]**

*"There seems to be a pattern, right? Videos with more words tend to get more likes. But it's messy—lots of scatter."*

**[CLICK: Add line of best fit]**

*"THIS is what regression does. It finds the best line through this chaos. Not a perfect line—there's no such thing with real data—but the BEST line. The one that minimizes the total distance between itself and all the points."*

*"That's called Ordinary Least Squares, or OLS. It finds the line that makes the squared distances as small as possible."*

---

### SECTION 2: INTERPRETING THE OUTPUT [10:00-20:00]
*[INSTRUCTOR NOTE: This is the core—spend time here, check understanding frequently]*

**[SLIDE: Regression output screenshot]**

*"When you run regression in Python—which you'll do in lab—you get output that looks like this. Let's decode it."*

**[HIGHLIGHT: Coefficient]**

*"This is the BETA coefficient, β. In our example, let's say β = 0.42 for word count predicting likes."*

*"What does 0.42 mean? It means: For every 1 standard deviation increase in word count, likes increase by 0.42 standard deviations."*

*"Positive β = positive relationship. Negative β = negative relationship. The closer to 1 (or -1), the stronger the relationship."*

**[HIGHLIGHT: p-value]**

*"This is the p-value. In our example, p = .003."*

*"What does p = .003 mean? It means: If there were NO real relationship between word count and likes—if the true β were zero—there's only a 0.3% chance we'd see a pattern this strong by random chance alone."*

*"Our threshold is p < .05. If p is below .05, we call it 'statistically significant.' We're confident the pattern is real, not noise."*

**[HIGHLIGHT: R-squared]**

*"This is R-squared. Let's say R² = .18."*

*"What does R² = .18 mean? Word count explains 18% of the variance in likes. The remaining 82% is explained by other things we didn't measure—video quality, topic, thumbnail, luck."*

*"In psychology, R² values of .10 to .30 are pretty common. We're studying messy human behavior, not physics."*

---

### SECTION 3: CONTROLLING FOR VARIABLES [20:00-28:00]
*[PAUSE: Ensure students understand β interpretation before introducing multiple regression]*

**[SLIDE: Multiple regression concept diagram]**

*"Here's where it gets powerful. What if you want to know: Does word count predict likes EVEN AFTER accounting for view count?"*

*"This is called 'controlling for' a variable. Or 'holding constant.' Or 'adjusting for.'"*

*"Why would we do this? Because view count is a confound. Videos with more views naturally have more likes. If we don't control for views, we might wrongly conclude that word count matters when really it's just that longer videos happen to get more exposure."*

**[SLIDE: Regression with two predictors]**

*"In multiple regression, we add both variables as predictors:"*

```
Likes ~ Word Count + View Count
```

*"Now the β for word count tells us: The effect of word count on likes, HOLDING VIEW COUNT CONSTANT. It's like asking: Among videos with the same number of views, does word count still matter?"*

*"Look back at Table 2 in the RA Manuscript. Notice how they control for multiple variables? They're isolating the unique effect of each predictor."*

---

### SECTION 4: FROM NUMBERS TO WORDS (APA STYLE) [28:00-33:00]

**[SLIDE: APA reporting template]**

*"Research isn't just running code. You need to COMMUNICATE what you found. Here's the template:"*

> *"A [simple/multiple] linear regression was conducted to predict [DV] from [IV(s)]. Results indicated that [IV] significantly predicted [DV], β = [value], p [</.001/= .XXX]. The model explained [X]% of the variance in [DV] (R² = [value])."*

*"Example from our data:"*

> *"A multiple linear regression was conducted to predict like count from word count and view count. Results indicated that word count significantly predicted likes even after controlling for views, β = .28, p < .001. The full model explained 34% of the variance in likes (R² = .34)."*

*"Notice: I said 'even after controlling for views.' That's the key insight—word count matters above and beyond exposure."*

---

### SECTION 5: CAUTION—CORRELATION ≠ CAUSATION [33:00-36:00]
*[INSTRUCTOR NOTE: This caveat is crucial—emphasize it]*

**[SLIDE: Warning symbol]**

*"One massive caveat. Regression tells you about RELATIONSHIPS, not CAUSES."*

*"When we say 'word count predicts likes,' we're NOT saying that typing more words CAUSES people to like the video. Maybe it's the reverse—maybe engaging topics inspire both longer writing AND more likes."*

*"In science, we say 'predicts' or 'is associated with' rather than 'causes' unless we have an experiment."*

*"Keep this in mind as you write up your results. Say 'predicted,' not 'caused.'"*

---

### WRAP-UP [36:00-38:00]

**[SLIDE: Key Takeaways]**

*"Today's essentials:"*

1. *"Regression finds the best-fit line through your data"*
2. *"β tells you direction and strength; p tells you if it's real; R² tells you how much variance is explained"*
3. *"Control for confounds using multiple regression"*
4. *"Report results in APA style"*
5. *"Remember: Prediction ≠ Causation"*

*"In lab, you'll run your first regression. You'll go from raw data to a publication-ready sentence. Let's do it."*

---

### SECTION 6: WORKING WITH AGATHA'S DATA [38:00-41:00]
*[LIVE CODING: Share screen and run with students]*

**[LIVE DEMO: Loading the data]**

```python
# Load Agatha's dance community data
df = load_dataset("agatha_ballet_dancemoms_agatha", nrows=5000)
print(f"Loaded {len(df):,} posts from dance communities")
print(f"Columns: {list(df.columns)}")

# Create a variable for text length
df['text_length'] = df['Post Title'].str.len()

# Run a regression: Does text length predict post score?
import statsmodels.formula.api as smf
model = smf.ols('Post_Score ~ text_length', data=df.rename(columns={'Post Score': 'Post_Score'})).fit()
print(model.summary())
```

*"That's it. One command, thousands of data points, a full regression analysis. In your lab, you'll explore what predicts engagement in dance communities."*

---

### LECTURE MATERIALS CHECKLIST
- [ ] Agatha's dance ratings loaded in Colab demo
- [ ] Scatterplot visuals (with and without regression line)
- [ ] Regression output example (statsmodels format)
- [ ] APA template slide
- [ ] DATASETS_FOR_M2.md reference card
