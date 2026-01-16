# Module 3 Answer Key: LLMs as Raters
## INSTRUCTOR USE ONLY

**Assessment:** Module 3 Assessment
**Dataset:** `yashita_yashita_data` (testing), `kaitlyn_merged_data_overview_kaitlyn_master` (validation)
**Total Points:** 100

---

## Part A: Concept Check (30 points)

### Question 1 (6 points)
**Question:** Why is prompt engineering similar to survey design?

**Model Answer:**
> Both require crafting clear, unambiguous instructions to get valid measurements. A vague survey question yields inconsistent responses; a vague prompt yields inconsistent AI ratings. Both need defined constructs, clear scales, and specific anchor descriptions to ensure the rater (human or AI) interprets the task consistently.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 6 | Mentions: clarity needed, consistency concern, construct definition, scale/anchors |
| 4 | Makes connection but missing 1-2 key elements |
| 2 | Vague understanding of similarity |
| 0 | Incorrect or no response |

**Key Parallels:**
- Clear instructions → consistent responses
- Defined constructs
- Explicit scales with anchors
- Validity concerns

---

### Question 2 (6 points)
**Question:** What does "Temperature = 0" mean when using an LLM for rating?

**Correct Answer:** B) The AI will give the most deterministic, consistent responses with no randomness

**Rubric:**
| Score | Criteria |
|-------|----------|
| 6 | Selects B |
| 0 | Any other answer |

**Instructor Note:** Temperature controls randomness in LLM outputs. At T=0, the model always picks the highest probability token, ensuring identical outputs for identical inputs. This is crucial for reproducible ratings.

---

### Question 3 (6 points)
**Question:** What is "zero-shot" classification?

**Model Answer:**
> Zero-shot classification means asking an LLM to categorize or rate content without providing any labeled examples in the prompt. The AI relies entirely on its training and the task description to make judgments. This contrasts with "few-shot" classification, where examples are included in the prompt.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 6 | Full definition + contrast with few-shot |
| 4 | Correct definition but no contrast |
| 2 | Partial understanding |
| 0 | Incorrect or no response |

**Key Terms:**
- Zero-shot: no examples provided
- Few-shot: examples included in prompt
- The AI uses only instructions + its training

---

### Question 4 (6 points)
**Question:** Your human-AI correlation is r = 0.35. What should you do?

**Model Answer:**
> Revise the prompt. This low correlation indicates the AI is not interpreting the construct the same way the human rater is. I should: (1) check if my construct definition is clear and specific, (2) add more detailed scale anchors, (3) consider adding examples, and (4) verify my own ratings are consistent. The problem is likely in the prompt design, not inherently in the AI.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 6 | Says revise prompt + gives specific improvement strategies |
| 4 | Says revise but vague on how |
| 2 | Recognizes low correlation is a problem |
| 0 | Says accept the result or blame the AI |

**Wrong Answers:**
- "Accept it and move on" (No - r=0.35 is poor)
- "Use a different AI model" (First improve the prompt)
- "Discard the AI ratings" (Try fixing first)

---

### Question 5 (6 points)
**Question:** Why do we validate AI ratings against human ratings?

**Model Answer:**
> LLMs can have biases, misunderstand constructs, or interpret definitions differently than intended. Validation ensures the AI's understanding matches the researcher's intention. Without validation, we might collect thousands of ratings that measure something different from what we think we're measuring. It's a validity check—just like checking inter-rater reliability with human coders.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 6 | Mentions: bias/misinterpretation + validity check + analogy to human IRR |
| 4 | Mentions validity but incomplete reasoning |
| 2 | Says "to make sure it's correct" (too vague) |
| 0 | Incorrect or no response |

---

## Part B: Prompt Analysis (30 points)

### Question 6 (10 points)
**Question:** Identify THREE problems with this prompt:
```
Rate this comment for negativity. Give a score.
Comment: "[comment text]"
```

**Model Answer:**
1. **No definition of negativity** - Could mean hostility, pessimism, criticism, or sadness
2. **No scale specified** - Is it 1-5? 1-7? 1-10?
3. **No anchor descriptions** - No guidance on what constitutes low vs. high
4. **No role statement** - No context for the task
5. **No output format constraint** - Might return explanation instead of just number

**Rubric:**
| Score | Criteria |
|-------|----------|
| 10 | 3+ valid problems identified with explanation |
| 7 | 3 problems but explanations weak |
| 5 | 2 problems with good explanations |
| 3 | 1-2 problems, weak explanations |
| 0 | No valid problems identified |

**Acceptable Problem Categories:**
- Definition missing
- Scale missing
- Anchors missing
- Format missing
- Context/role missing

---

### Question 7 (20 points)
**Question:** Rewrite the prompt to fix the problems.

**Exemplar Answer:**
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

**Rubric:**
| Component | Points | Required Elements |
|-----------|--------|-------------------|
| Role/Context | 3 | "You are a research assistant..." or similar |
| Construct Definition | 4 | Clear definition of negativity |
| Scale with Numbers | 4 | Explicit 1-7 (or similar) scale |
| Anchor Descriptions | 5 | What each number means |
| Output Instruction | 4 | "Provide only a number" or similar |

**Grading Notes:**
- Scale can be 1-5, 1-7, 1-10 (any reasonable range)
- Anchors should progress logically from low to high
- Output instruction should constrain format

---

## Part C: Lab Results (40 points)

### Task 1: Submit Your Prompt (10 points)

**Checklist:**
| Component | Points | Look For |
|-----------|--------|----------|
| Construct definition | 2 | Clear, operationalized |
| Numeric scale | 2 | Explicit range (1-5, 1-7, etc.) |
| Anchor descriptions | 2 | What each point means |
| Output instruction | 2 | Format constraint |
| Professional formatting | 2 | Readable, organized |

---

### Task 2: Report Your Results (15 points)

**Expected Format:**
1. Construct: [their choice - e.g., negativity, toxicity, sentiment]
2. Correlation: r = [their value]
3. P-value: [their value]
4. N items: [typically 20-50]
5. Interpretation: [based on r value]

**Interpretation Guide:**
| r Value | Category | Points |
|---------|----------|--------|
| r > 0.80 | Excellent | Full credit |
| r = 0.60-0.80 | Good | Full credit |
| r = 0.40-0.60 | Moderate | Full credit |
| r < 0.40 | Poor | Full credit (for honest reporting) |

**Grading:**
- Values reported correctly: 10 points
- Interpretation matches r: 5 points
- NOTE: Do NOT penalize for low correlation—reward honest reporting

---

### Task 3: Disagreement Analysis (15 points)

**Rubric:**
| Component | Points | Criteria |
|-----------|--------|----------|
| Specific example | 3 | Actual item text provided |
| Ratings shown | 3 | Both human and AI ratings |
| Analysis | 6 | Thoughtful explanation of why disagreement occurred |
| Improvement | 3 | Suggests concrete prompt fix |

**Good Analysis Examples:**
- "The AI may have interpreted sarcasm literally"
- "My definition was too vague about what counts as 'criticism'"
- "The comment had mixed signals—praise and complaint together"

**Good Improvement Examples:**
- "I would add: 'Note: sarcasm should be rated based on underlying intent'"
- "I would include an example of a 'mixed' comment in my anchors"

---

## Grading Summary

| Component | Points |
|-----------|--------|
| Part A: Q1-Q5 | 30 |
| Part B: Q6 (3 problems) | 10 |
| Part B: Q7 (rewrite) | 20 |
| Part C: Task 1 (prompt) | 10 |
| Part C: Task 2 (results) | 15 |
| Part C: Task 3 (analysis) | 15 |
| **TOTAL** | **100** |

---

## Bonus Question (5 extra points)

**Question:** When might human raters be more appropriate than AI?

**Model Answer:**
> Human raters are preferable when: (1) the construct is highly subjective or culturally specific and the AI might have training biases, (2) the content requires specialized domain expertise the AI may lack, (3) the consequences of misclassification are high, (4) the research requires understanding of local context, slang, or inside references, or (5) when the research explicitly studies human perception.

**Rubric:**
| Score | Criteria |
|-------|----------|
| 5 | 2+ valid reasons with explanation |
| 3 | 1-2 reasons, limited explanation |
| 0 | No valid reasons |

---

## Common Student Errors

1. **Prompt too vague**
   - Error: "Rate for emotion"
   - Fix: Define which emotions, provide scale

2. **No output format**
   - Error: AI returns paragraph instead of number
   - Fix: "Respond with only a single number"

3. **Misinterpreting correlation**
   - Error: "r = 0.35 is acceptable"
   - Fix: r < 0.40 is poor for rating agreement

4. **Blaming AI for low agreement**
   - Error: "The AI is bad at this task"
   - Fix: Usually the prompt needs improvement

5. **Using few-shot when asked for zero-shot**
   - Error: Including examples in "zero-shot" prompt
   - Fix: Zero-shot means no examples

---

*Answer Key Version: 1.0 | Date: 2026-01-15*
