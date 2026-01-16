# Module 3 Flashcards: LLMs as Raters

**Total Cards:** 23
**Format:** Anki-compatible (Front/Back)

---

## Definitions (6 cards)

### Card 1
**Front:** What is prompt engineering?
**Back:** Designing instructions for an LLM to get consistent, valid outputs. Like writing survey questions - clarity and specificity matter. The prompt is your measurement instrument.
**Tags:** M3, definition, llm

### Card 2
**Front:** What is zero-shot classification?
**Back:** Asking an LLM to classify/rate content WITHOUT providing examples in the prompt. The AI relies only on its training and your task description. Contrast with few-shot (includes examples).
**Tags:** M3, definition, llm

### Card 3
**Front:** What is few-shot classification?
**Back:** Including labeled examples in your prompt to show the AI what you want. "Here are examples of 1=low, 4=medium, 7=high. Now rate this..." Often improves consistency.
**Tags:** M3, definition, llm

### Card 4
**Front:** What is temperature in LLM settings?
**Back:** Controls randomness. Temperature=0 gives deterministic, consistent outputs. Temperature=1 gives varied, creative outputs. For rating tasks, use low temperature (0.1-0.3).
**Tags:** M3, definition, llm

### Card 5
**Front:** What is human-AI validation?
**Back:** Comparing AI ratings to human expert ratings to ensure the AI measures the same construct. Calculate correlation (r) between human and AI scores. High r = valid AI measure.
**Tags:** M3, definition, validation

### Card 6
**Front:** What is inter-rater reliability?
**Back:** Agreement between raters (human or AI) on the same items. High reliability means ratings are consistent. Cohen's Kappa, Pearson r, or Spearman rho measure this.
**Tags:** M3, definition, reliability

---

## Concepts (7 cards)

### Card 7
**Front:** Why is prompt engineering like survey design?
**Back:** Both require: 1) Clear construct definition, 2) Specific scales with anchors, 3) Unambiguous instructions. A vague survey question = inconsistent responses. A vague prompt = inconsistent AI ratings.
**Tags:** M3, concept, prompt

### Card 8
**Front:** What are the 5 components of a good rating prompt?
**Back:** 1) Role statement ("You are a research assistant..."), 2) Construct definition, 3) Scale with numbers, 4) Anchor descriptions for each level, 5) Output format instruction ("Respond with only a number").
**Tags:** M3, concept, prompt

### Card 9
**Front:** Why use Temperature=0 for rating tasks?
**Back:** For research, we want CONSISTENCY - the same input should get the same rating. Temperature=0 minimizes randomness. Use higher temperature only when you want creative variation.
**Tags:** M3, concept, llm

### Card 10
**Front:** What does a low human-AI correlation (r < 0.40) indicate?
**Back:** The AI isn't measuring the same thing as the human. Problem is likely in the prompt - unclear definition, ambiguous anchors, or construct too complex. Revise the prompt, don't blame the AI.
**Tags:** M3, concept, validation

### Card 11
**Front:** When should you use human raters instead of AI?
**Back:** When: 1) Construct is highly subjective/cultural, 2) Content requires domain expertise, 3) Stakes are high (content moderation), 4) Local context/slang matters, 5) Research is about human perception specifically.
**Tags:** M3, concept, design

### Card 12
**Front:** What's the difference between reliability and validity for AI ratings?
**Back:** Reliability = consistency (AI gives same rating to same input). Validity = accuracy (AI rating matches what you're trying to measure). Can be reliable but not valid if consistently measuring wrong thing.
**Tags:** M3, concept, measurement

### Card 13
**Front:** Why validate on a SUBSET before rating everything?
**Back:** If your prompt is flawed, you'll waste API costs and time rating thousands of items incorrectly. Rate 50-100 items, calculate human-AI correlation, fix prompt, THEN scale up.
**Tags:** M3, concept, workflow

---

## Code Patterns (5 cards)

### Card 14
**Front:** Basic OpenAI API call for rating:
**Back:**
```python
import openai
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.1
)
rating = response.choices[0].message.content.strip()
```
**Tags:** M3, code, api

### Card 15
**Front:** How to calculate correlation between human and AI ratings:
**Back:**
```python
from scipy.stats import pearsonr, spearmanr
r, p = pearsonr(df['human_rating'], df['ai_rating'])
print(f"r = {r:.3f}, p = {p:.4f}")
```
**Tags:** M3, code, validation

### Card 16
**Front:** How to structure a rating loop:
**Back:**
```python
ratings = []
for text in df['comment']:
    formatted_prompt = prompt.format(comment=text)
    rating = get_ai_rating(formatted_prompt)
    ratings.append(rating)
df['ai_rating'] = ratings
```
**Tags:** M3, code, workflow

### Card 17
**Front:** How to parse AI responses to numbers:
**Back:**
```python
def parse_rating(response):
    try:
        return int(response.strip())
    except ValueError:
        return None  # Handle non-numeric responses
```
**Tags:** M3, code, processing

### Card 18
**Front:** Good prompt template structure:
**Back:**
```
You are [ROLE].
TASK: Rate [ITEM] for [CONSTRUCT].
DEFINITION: [CONSTRUCT] means...
SCALE: 1=[low anchor], 4=[mid], 7=[high anchor]
[ITEM TO RATE]: "{text}"
Respond with ONLY a number (1-7).
```
**Tags:** M3, code, prompt

---

## Interpretation (3 cards)

### Card 19
**Front:** Human-AI r = 0.75. Is this good?
**Back:** Yes - good agreement. Most studies consider r > 0.70 acceptable for research use. The AI is capturing the same construct as human raters. Proceed with scaling up.
**Tags:** M3, interpretation, validation

### Card 20
**Front:** AI always returns "5" regardless of input. What's wrong?
**Back:** Likely: 1) Prompt too vague - AI can't differentiate, 2) Temperature too high, or 3) Scale anchors unclear. The AI is defaulting to middle. Revise prompt with clearer anchors.
**Tags:** M3, interpretation, troubleshooting

### Card 21
**Front:** Human rates "7" but AI rates "3" on same item. What to do?
**Back:** Examine the item. Possible causes: 1) Construct definition unclear, 2) Cultural/contextual knowledge AI lacks, 3) Human error. Use these disagreements to improve your prompt definition.
**Tags:** M3, interpretation, troubleshooting

---

## Common Mistakes (2 cards)

### Card 22
**Front:** What's wrong with: "Rate this for negativity. Give a score."?
**Back:** Missing: 1) No negativity definition, 2) No scale specified, 3) No anchors, 4) No output format. AI will guess what "score" means. Could return "3/10" or "somewhat negative" or "3".
**Tags:** M3, mistake, prompt

### Card 23
**Front:** Why shouldn't you trust AI ratings without validation?
**Back:** LLMs can: 1) Misunderstand constructs, 2) Have biases, 3) Interpret differently than intended. Without validation, you might collect thousands of ratings measuring something you didn't intend.
**Tags:** M3, mistake, validation

---

*Module 3 Flashcards | Applied Psychological Data Science*
