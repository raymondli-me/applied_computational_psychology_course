# Module 3 Assessment: LLMs as Raters

**Recommended Dataset:** `yashita_yashita_data` (4,689 comments - good for prompt testing)
**Validation Dataset:** `kaitlyn_merged_data_overview_kaitlyn_master` (809K with human ratings)
**See:** DATASETS_FOR_M3.md for all options

---

## Part A: Concept Check (30 points)

### Question 1 (6 points)
Why is prompt engineering similar to survey design?

**Model Answer:** Both require crafting clear, unambiguous instructions to get valid measurements. A vague survey question yields inconsistent responses; a vague prompt yields inconsistent AI ratings. Both need defined constructs, clear scales, and specific anchor descriptions to ensure the rater (human or AI) interprets the task consistently.

---

### Question 2 (6 points)
What does "Temperature = 0" mean when using an LLM for rating, and why is it important?

- A) The AI will give faster responses
- B) The AI will give the most deterministic, consistent responses with no randomness
- C) The AI will use less computing power
- D) The AI will refuse to answer ambiguous prompts

**Correct Answer:** B

---

### Question 3 (6 points)
What is "zero-shot" classification?

**Model Answer:** Zero-shot classification means asking an LLM to categorize or rate content without providing any labeled examples in the prompt. The AI relies entirely on its training and the task description to make judgments. This contrasts with "few-shot" classification, where examples are included in the prompt.

---

### Question 4 (6 points)
Your human-AI correlation is r = 0.35. What should you do?

**Model Answer:** Revise the prompt. This low correlation indicates the AI is not interpreting the construct the same way the human rater is. I should: (1) check if my construct definition is clear and specific, (2) add more detailed scale anchors, (3) consider adding examples, and (4) verify my own ratings are consistent. The problem is likely in the prompt design, not inherently in the AI.

---

### Question 5 (6 points)
Why do we validate AI ratings against human ratings? Why not just trust the AI?

**Model Answer:** LLMs can have biases, misunderstand constructs, or interpret definitions differently than intended. Validation ensures the AI's understanding matches the researcher's intention. Without validation, we might collect thousands of ratings that measure something different from what we think we're measuring. It's a validity check—just like checking inter-rater reliability with human coders.

---

## Part B: Prompt Analysis (30 points)

### Scenario
A student writes the following prompt to rate YouTube comments for "negativity":

```
Rate this comment for negativity. Give a score.

Comment: "[comment text]"
```

### Question 6 (10 points)
Identify THREE problems with this prompt.

**Model Answer:**
1. **No definition of negativity** - "Negativity" could mean hostility, pessimism, criticism, or sadness. The AI has to guess.
2. **No scale specified** - Is it 1-5? 1-7? 1-10? What does each number mean?
3. **No anchor descriptions** - Even if a scale is implied, there's no guidance on what constitutes low vs. high negativity.
4. **No role statement** - Doesn't establish context for the task.
5. **No output format constraint** - AI might return "3 - because the comment seems somewhat negative" instead of just "3".

---

### Question 7 (20 points)
Rewrite the prompt to fix the problems. Include all necessary components.

**Model Answer:**
```
You are a research assistant helping code YouTube comments for psychological research.

TASK: Rate the following comment on NEGATIVITY.

DEFINITION: Negativity refers to expressions of hostility, criticism, pessimism,
dismissiveness, or general negative sentiment toward the video, creator, or topic.

SCALE:
1 = No negativity (positive, supportive, or neutral)
2 = Minimal negativity (slight criticism but mostly neutral)
3 = Mild negativity (some negative elements, constructive criticism)
4 = Moderate negativity (clear criticism or pessimism, but not hostile)
5 = Notable negativity (strong criticism, dismissive tone)
6 = High negativity (hostile or very pessimistic)
7 = Extreme negativity (aggressive, attacking, or deeply pessimistic)

COMMENT TO RATE:
"[comment text]"

Provide ONLY a single number (1-7) as your response.
```

---

## Part C: Lab Results (40 points)

### Task 1: Submit Your Prompt (10 points)

Copy and paste your final rating prompt (the version you used for your best correlation).

**Grading Criteria:**
- Includes construct definition (2 points)
- Includes scale with numbers (2 points)
- Includes anchor descriptions (2 points)
- Includes clear output instruction (2 points)
- Professional formatting (2 points)

---

### Task 2: Report Your Results (15 points)

Fill in the following:

1. **Construct you rated for:** _______________

2. **Correlation coefficient (r):** _______________

3. **P-value:** _______________

4. **Number of items rated:** _______________

5. **Interpretation (circle one):**
   - Excellent agreement (r > 0.80)
   - Good agreement (r = 0.60-0.80)
   - Moderate agreement (r = 0.40-0.60)
   - Poor agreement (r < 0.40)

---

### Task 3: Disagreement Analysis (15 points)

Describe ONE item where you and the AI strongly disagreed:

1. **The item (headline/comment):** _______________

2. **Your rating:** _______________

3. **AI rating:** _______________

4. **Why do you think you disagreed?** (3-4 sentences)

**Grading Criteria:**
- Specific example provided (3 points)
- Thoughtful analysis of disagreement (6 points)
- Suggests potential prompt improvement (6 points)

---

## Grading Summary

| Component | Points |
|-----------|--------|
| Part A: Concept Check | 30 |
| Part B: Prompt Analysis | 30 |
| Part C: Lab Results | 40 |
| **Total** | **100** |

---

## Bonus Question (5 extra points)

When might it be more appropriate to use human raters instead of AI raters, even when scale is not a concern?

**Model Answer:** Human raters are preferable when: (1) the construct is highly subjective or culturally specific and the AI might have training biases, (2) the content requires specialized domain expertise the AI may lack, (3) the consequences of misclassification are high (e.g., content moderation for harmful content), (4) the research requires understanding of local context, slang, or inside references, or (5) when the research explicitly studies human perception rather than "objective" qualities.

---

## Submission Instructions

1. Complete all sections in a single document
2. Include your prompt as plain text (not a screenshot)
3. Include a screenshot of your correlation output
4. Submit via [Course Platform] by [Deadline]
