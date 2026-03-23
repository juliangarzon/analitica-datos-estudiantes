# Week 8 Workshop: Build Your AI Skills Ecosystem

## Overview

Expand what you started in class into a complete skills ecosystem for the semester. You will plan which AI skills you need, build two more, test them with real course content, and reflect on the experience.

**Duration:** ~2 hours at home
**Prerequisites:** Completed in-class exercise (working AI CLI tool + at least 1 skill created)
**Due:** Before Week 9 class

---

## Task 1: Ecosystem Plan (20 minutes)

Think about the deliverables you will produce in this course over the next 8 weeks:

- Visualizations (matplotlib, seaborn, Plotly charts)
- Interactive dashboards (Streamlit apps)
- Data storytelling narratives
- Project documentation (READMEs, reports)
- Data cleaning and transformation scripts
- EDA reports and summaries
- Milestone presentations
- Machine learning experiments (if time permits)

Write a short document (~1 page) listing:

1. Which deliverable types you will need skills for
2. Priority order (what will you need first?)
3. For each: a one-sentence description of what the skill should do

### Example

| Priority | Deliverable | Skill Description |
|----------|-------------|-------------------|
| 1 | Data Quality Reports | Generate a structured quality assessment with scores, column analysis, and action items |
| 2 | EDA Summaries | Produce a narrative EDA summary from descriptive statistics and visualizations |
| 3 | Streamlit Scaffolding | Generate a Streamlit app skeleton with sidebar filters and chart sections from a dataset description |
| 4 | Storytelling Outline | Create a data story outline with hook, context, insights, and call to action |
| 5 | README Generator | Build a project README with installation, usage, and data dictionary sections |

---

## Task 2: Create 2 More Skills (40 minutes)

Pick the top 2 from your ecosystem plan. Create them:

- Folder: `.toolname/skills/skill-name/SKILL.md` (use the folder for your chosen tool)
- Each skill must have: clear instructions, format specification, constraints/rules
- Test each with at least 2 different prompts
- Iterate until the output is useful

### Quality Checklist

Before moving on, verify each skill:

- [ ] Frontmatter has name, description, and version
- [ ] Instructions are specific (not "write good output")
- [ ] Output format is defined explicitly
- [ ] At least 2 rules constrain the AI behavior
- [ ] Tested with 2 different prompts and produced useful results

### Skill Ideas by Domain

**Data Analytics:**
- Data cleaning script generator
- Visualization recommender (suggest chart types for your data)
- Statistical test selector (which test for your hypothesis?)
- Outlier analysis reporter

**Software / Documentation:**
- README generator for data projects
- Code comment writer
- Git commit message generator
- Requirements.txt generator from imports

**Communication:**
- Data storytelling outline creator
- Executive summary writer
- Presentation slide planner
- Findings report formatter

---

## Task 3: Test with Real Course Content (30 minutes)

Use your skills (or the ones from class) on actual course content:

1. Use the data-quality-report skill on your Milestone 1 dataset (the one from datos.gov.co)
2. Use another skill to generate a deliverable relevant to your next milestone (Milestone 2: dashboard + storytelling)
3. Save the output and note what worked vs what needed manual editing

### What to Document

For each test, record:

- The prompt you used
- Whether the output was usable as-is, needed minor edits, or needed major rework
- What you would change in the skill instructions to improve the output

---

## Task 4: Reflection (15 minutes)

Write a short reflection (half page):

- What surprised you about using AI tools?
- What was harder than expected?
- What skill would save you the most time for Milestones 2 and 3?
- Any concerns about using AI for course deliverables?

---

## Deliverables

Submit a zip containing:

```
workshop-08/
    ecosystem_plan.md        # Your ecosystem plan from Task 1
    skills/                  # All your SKILL.md files (at least 3 total including class)
        data-quality-report/SKILL.md
        skill-two/SKILL.md
        skill-three/SKILL.md
    outputs/                 # Sample outputs from Task 3
        quality_report_output.md
        other_output.md
    reflection.md            # Your reflection from Task 4
    setup_screenshot.png     # Screenshot of working AI CLI setup
```

---

## Evaluation (100 points)

| Criterion | Points |
|-----------|--------|
| Ecosystem plan is thoughtful and complete | 20 |
| Skills are well-structured (clear instructions, format, rules) | 30 |
| Skills produce useful output (tested with real prompts) | 25 |
| Reflection shows genuine engagement | 15 |
| Setup screenshot included | 10 |

---

## Tips

1. **Start with the ecosystem plan.** It forces you to think about what you actually need before building.
2. **Steal from the class example.** The data-quality-report skill from the exercise is a good template. Copy the structure, change the content.
3. **Iterate on your skills.** Run them, see what comes out, adjust the instructions. The first version is never the best.
4. **Be honest in your reflection.** There are no wrong answers. If you think AI is overhyped, say so and explain why.
5. **Test with YOUR data.** Use the dataset from your Milestone 1 project. The more real the test, the more useful the feedback.
6. **Think about Milestone 2.** You will need dashboards, storytelling narratives, and visualizations. Skills that help with those will pay off immediately.
