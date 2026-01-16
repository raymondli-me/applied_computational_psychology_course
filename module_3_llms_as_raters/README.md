# Module 3: LLMs as Raters

**Teaching AI to Read**

## Learning Objectives

By the end of this module, you will be able to:
- Design effective prompts for content rating
- Set appropriate temperature for consistent outputs
- Validate AI ratings against human judgments
- Troubleshoot low human-AI agreement

## Key Datasets

**Yashita's Data** (for testing) - 2,101 YouTube videos
**Kaitlyn's Data** (for validation) - 809,000 mental health comments with human ratings

```python
df_test = load_dataset("yashita_yashita_data")
df_validate = load_dataset("kaitlyn_merged_data_overview_kaitlyn_master", nrows=1000)
```

## Requirements

- OpenAI API key (get one at platform.openai.com)

## Materials

| File | Description |
|------|-------------|
| [lecture_notes.md](lecture_notes.md) | Lecture content (~38 min) |
| [lab_instructions.md](lab_instructions.md) | Hands-on exercises (90 min) |
| [assessment.md](assessment.md) | Test your understanding |
| [answer_key.md](answer_key.md) | Model answers |
| [flashcards.md](flashcards.md) | 23 study cards |

## Estimated Time

~2.5 hours total
