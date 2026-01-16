# Module 3: Lecture Script
## "Teaching AI to Read: LLMs as Research Assistants"

**Total Runtime:** ~38 minutes
**Video Production Ready:** Yes

---

### INTRO [0:00-2:00]
*[INSTRUCTOR NOTE: The scale numbers (809,000) should hook students—this is the "why" for the module]*

**[SLIDE: Kaitlyn's Mental Health Data - 809,000 Comments]**

*"Kaitlyn's team analyzed 809,000 YouTube comments about mental health. Each comment got a rating for emotional support, self-disclosure, and stigma. Who do you think read all 809,000 comments?"*

**[PAUSE]**

*"Well, some of them—Kaitlyn's team of 6 human raters coded a sample to validate. But the scale of 809,000? That's where AI comes in. Today, you learn how."*

---

### SECTION 1: THE PROBLEM WITH SCALE [2:00-8:00]
*[INSTRUCTOR NOTE: Make the "50 hours" calculation interactive—have students think before revealing]*

**[SLIDE: 6,000 comments scrolling]**

*"Let's do some math. If you spend 30 seconds reading and rating each comment, 6,000 comments takes..."*

**[CLICK: Calculator showing 50 hours]**

*"Fifty hours. That's more than a full work week of doing nothing but reading comments."*

*"And that's just ONE study. What if you want to analyze 100,000 news headlines? Or a million tweets? Human coding doesn't scale."*

**[SLIDE: Traditional solution - multiple coders]**

*"The traditional approach: Hire multiple research assistants. Train them on a codebook. Have them rate overlapping samples to check reliability. It works, but it's slow, expensive, and still limited in scale."*

**[SLIDE: The new solution - LLMs]**

*"The modern approach: Treat an LLM—GPT-4, Claude, Llama—as a tireless research assistant. One that can rate thousands of items in minutes. One that never gets tired, never gets hungry, and costs a fraction of human labor."*

*"But—and this is crucial—one that needs very clear instructions to do the job right."*

---

### SECTION 2: PROMPT ENGINEERING IS SURVEY DESIGN [8:00-18:00]
*[INSTRUCTOR NOTE: This is the core insight—prompt engineering = survey design. Spend extra time here]*

**[SLIDE: Bad survey question example]**

*"Think back to your methods courses. What makes a bad survey question?"*

*"'Do you think the video was good?' That's terrible. Good how? Entertaining? Informative? Morally good? What scale? Yes/no? 1-10?"*

**[SLIDE: Good survey question example]**

*"'On a scale of 1 (not at all) to 7 (extremely), how entertaining did you find this video?' Better. Specific construct. Clear scale. Defined anchors."*

*"Here's the insight: When you prompt an LLM, you're essentially writing a survey question for the AI. All the same rules apply."*

**[SLIDE: Prompt template breakdown]**

*"Let me show you the template we'll use:"*

```
You are a research assistant helping code YouTube comments for psychological research.

TASK: Rate the following comment on SUPPORTIVENESS.

DEFINITION: Supportiveness refers to expressions of empathy, encouragement,
validation, or emotional support toward the video creator or other commenters.

SCALE:
1 = No support (neutral or negative)
4 = Moderate support (some encouraging words)
7 = High support (strong emotional validation, empathy, encouragement)

COMMENT TO RATE:
"This video really helped me. Thank you for sharing your story."

Provide ONLY a single number (1-7) as your response.
```

**[HIGHLIGHT each section as you discuss]**

*"Role statement—tells the AI what kind of task this is."*
*"Construct definition—critical! The AI needs to know what 'supportiveness' means to YOU."*
*"Scale anchors—without these, the AI has to guess what 1 vs. 7 means."*
*"Output format—'provide only a number' prevents the AI from rambling."*

---

### SECTION 3: THE TEMPERATURE DIAL [18:00-23:00]
*[PAUSE: Check understanding of prompt structure before introducing temperature]*

**[SLIDE: Temperature visualization - dial from 0 to 1]**

*"There's one technical setting you need to know about: Temperature."*

*"Temperature controls how 'creative' or 'random' the AI is."*

**[SLIDE: Temperature = 1]**

*"Temperature = 1: The AI is playful. If you ask it to write a poem, it might give you something surprising each time. Great for creative writing. Terrible for research."*

**[SLIDE: Temperature = 0]**

*"Temperature = 0: The AI is deterministic. Given the same input, it gives the same output every time. This is what we want for rating."*

*"Why? Because if you ask the AI to rate the same comment twice and it gives you different answers, that's noise. That's unreliable. For research, we want consistency."*

*"In your lab today, you'll set Temperature = 0. Always."*

---

### SECTION 4: VALIDATION—THE HUMAN-AI CHECK [23:00-31:00]
*[INSTRUCTOR NOTE: Emphasize that validation is non-negotiable—this is what separates rigorous from sloppy research]*

**[SLIDE: Correlation visualization - scatter plot of human vs. AI ratings]**

*"Here's the million-dollar question: How do you know the AI is rating things correctly?"*

*"You can't just trust it. You need to validate."*

**[SLIDE: Validation protocol]**

*"The protocol:"*

1. *"YOU rate a subset of items yourself (say, 50 items)"*
2. *"The AI rates the same 50 items"*
3. *"Calculate the correlation between your ratings and the AI's ratings"*
4. *"If correlation is high (r > 0.70), you can trust the AI to rate the rest"*

**[SLIDE: What different correlations mean]**

*"Interpretation guide:"*

| Correlation | Interpretation |
|-------------|----------------|
| r > 0.80 | Excellent agreement - AI closely matches your judgment |
| r = 0.60-0.80 | Good agreement - AI captures the construct reasonably well |
| r = 0.40-0.60 | Moderate - Consider refining your prompt |
| r < 0.40 | Poor - Major revisions needed or construct may be too subjective |

*"If your correlation is low, don't blame the AI. Look at your prompt. Is your definition clear? Are your anchors specific? Are YOU even consistent in your own ratings?"*

---

### SECTION 5: WHAT CAN GO WRONG [31:00-36:00]
*[INSTRUCTOR NOTE: These are the debugging tips that will save students hours of frustration]*

**[SLIDE: Common pitfalls]**

*"Let me save you some debugging time."*

**Pitfall 1: Vague Constructs**

*"If you ask the AI to rate 'toxicity' without defining it, the AI has to guess. Its definition might not match yours."*

**Pitfall 2: Missing Anchors**

*"Without anchor descriptions, the AI doesn't know what '1' vs. '4' means. It might use the full scale differently than you."*

**Pitfall 3: Asking for Explanations**

*"If your prompt says 'rate and explain,' the AI might give you '4 - because the commenter seems somewhat supportive...' Now you have to parse that text. Just ask for the number."*

**Pitfall 4: Forgetting Temperature**

*"If temperature isn't 0, ratings will vary randomly. Your reliability will tank."*

---

### WRAP-UP [36:00-38:00]

**[SLIDE: Today's Takeaways]**

*"Key points:"*

1. *"LLMs are scalable research assistants, not magic—they need good instructions"*
2. *"Prompt engineering = survey design: define constructs, anchor scales"*
3. *"Set Temperature = 0 for consistent ratings"*
4. *"ALWAYS validate: calculate human-AI correlation"*
5. *"Low agreement = revise the prompt, not the AI"*

*"In lab, you'll write your first rating prompt, compare your ratings to the AI's, and iterate until you achieve good agreement. This is real computational psychology."*

*"Let's go."*

---

### SECTION 6: WORKING WITH COURSE DATASETS [38:00-41:00]
*[LIVE CODING: Share screen and demonstrate with students following along]*

**[LIVE DEMO: Loading data for LLM rating]**

```python
# Load Kaitlyn's data - already has human ratings for validation
df = load_dataset("kaitlyn_merged_data_overview_kaitlyn_master")
print(f"Loaded {len(df):,} comments with human ratings")

# Or use Peter's GPT-analyzed news for studying existing AI outputs
df_news = load_dataset("peter_fox_msnbc_100video_gpt_data_to_analyze_mar9_2025")
print(f"Loaded {len(df_news):,} headlines with GPT ratings")
```

*"In your lab, you'll practice prompt engineering on real data. You can use Yashita's small dataset (4,689 comments) to experiment without API costs, then scale up to the larger datasets when your prompts are refined."*

---

### LECTURE MATERIALS CHECKLIST
- [ ] Kaitlyn's mental health data loaded in Colab demo
- [ ] Prompt template slide
- [ ] Temperature visualization
- [ ] Correlation interpretation table
- [ ] Example good/bad prompts for comparison
- [ ] DATASETS_FOR_M3.md reference card
