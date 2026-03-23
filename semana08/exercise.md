# Week 8 Exercise: Building with AI -- Hands-On Setup and First Skills

## Overview

- **Format:** In-class, professor-led + independent work
- **Format:** Follow along with the professor. Everyone does each step together.
- **Prerequisites:** Laptop with Node.js 18+ installed, internet connection
- **Outcome:** Working AI CLI environment + your first custom skill + understanding of MCP servers

---

## Part 1: Setup Your Environment

### Step 1: Install Your CLI Tool

You have four options. Pick one based on what you have access to. If you are unsure, the professor will recommend one.

| Tool | Install Command | Best For |
|------|----------------|----------|
| **OpenCode** | `npm install -g @anthropics/opencode` | Flexibility, connects to any LLM |
| **Gemini CLI** | `npm install -g @anthropic/gemini-cli` | Free Google Gemini access |
| **Claude Code** | `npm install -g @anthropic-ai/claude-code` | Anthropic Claude models |
| **Codex CLI** | `npm install -g @openai/codex` | OpenAI GPT models |

Open your terminal and run the install command for your chosen tool.

Verify the installation:

```bash
# Replace with your tool's command
opencode --version
# or: gemini --version
# or: claude --version
# or: codex --version
```

**Checkpoint:** Everyone run the version command. You should see a version number. Raise your hand if you see an error.

**Troubleshooting:**

| Problem | Solution |
|---------|----------|
| "command not found" | Your Node.js bin is not in PATH. Try: `npx <package-name> --version` |
| Permission error on Mac | Run: `sudo npm install -g <package-name>` |
| Node.js not installed | Download from [nodejs.org](https://nodejs.org) (LTS version) |

---

### Step 2: Connect to an LLM

Each tool connects to its LLM differently:

**OpenCode (multiple options):**

```bash
opencode
/connect
# Select "Google" for Gemini (free, Google OAuth)
# Or configure DeepSeek, OpenRouter, etc.
```

**Gemini CLI:**

```bash
gemini
# Authenticates via your Google account automatically
# Free: 60 requests/minute, 1M token context
```

**Claude Code:**

```bash
claude
# Follow the authentication prompts
# Uses your Anthropic account or API key
```

**Codex CLI:**

```bash
codex
# Follow the authentication prompts
# Uses your OpenAI account or API key
```

**Checkpoint:** Your tool is connected and responding. If you see an error, share your screen with the professor.

---

### Step 3: First Test -- Everyone Together

Professor says the prompt. Everyone types it at the same time:

```
Explain what data analytics is in one sentence.
```

Wait for your response.

**Checkpoint:** Everyone got a response? Read yours out loud. Notice how each response is slightly different -- that is the non-deterministic nature of LLMs. Same prompt, different outputs.

---

### Step 4: Second Test -- Code Generation

Now try generating code. Type this prompt:

```
Generate a Python function using pandas that takes a DataFrame and returns a summary of missing values per column, including count and percentage. Just the code, no explanation.
```

**Checkpoint:** You should see Python code with `pd.DataFrame` and some kind of missing value analysis. If you see an error or something unexpected, share your screen.

---

## Part 2: Create Your First Skill

A skill is a SKILL.md file that gives the AI specialized instructions for a specific task. Think of it as a recipe card: the AI follows the recipe instead of improvising.

We are going to create one together, step by step.

### Step 1: Create the skill folder

In your terminal (not inside your AI tool), run:

```bash
# For OpenCode:
mkdir -p .opencode/skills/data-quality-report

# For Claude Code:
mkdir -p .claude/skills/data-quality-report

# For Gemini CLI:
mkdir -p .gemini/skills/data-quality-report

# For Codex CLI:
mkdir -p .codex/skills/data-quality-report
```

Use the command that matches your tool. This creates a folder for your skill.

---

### Step 2: Create the SKILL.md file

Open your text editor (VS Code, nano, whatever you prefer) and create a file at this path:

```
.opencode/skills/data-quality-report/SKILL.md
```

(Replace `.opencode` with `.claude`, `.gemini`, or `.codex` depending on your tool.)

Type this content exactly:

```markdown
---
name: Data Quality Report
description: Generates a structured data quality report for a dataset
version: 1.0.0
---

# Data Quality Report

You are a data quality analyst. When given a dataset (CSV file path or DataFrame description), analyze it and generate a comprehensive data quality report.

## Format

### Dataset Overview
- Name: [dataset name]
- Rows: [count]
- Columns: [count]
- File size: [if available]

### Column Analysis
For each column:
- **[Column Name]**
  - Type: [detected type]
  - Missing: [count] ([percentage]%)
  - Unique values: [count]
  - Issues: [list any problems found]

### Quality Score
- Completeness: [X/10] - [justification]
- Consistency: [X/10] - [justification]
- Validity: [X/10] - [justification]
- Overall: [X/10]

### Recommended Actions
1. [First priority action with specific column/issue]
2. [Second priority action]
3. [Third priority action]

## Rules

- Always check for missing values, duplicates, and type mismatches
- Score must be justified with specific evidence from the data
- Recommend concrete actions, not vague suggestions like "clean the data"
- If no issues are found in a category, say so explicitly
- Order recommended actions by impact (most important first)
```

Save the file.

**Checkpoint:** Open your SKILL.md file and verify it has three parts:

1. Frontmatter section (between `---` markers) with name, description, version
2. Instructions telling the AI what to do
3. Rules constraining the output

Compare with your neighbor. Do your files match?

---

### Step 3: Test the skill

In your AI tool, invoke your skill:

**OpenCode:**
```
/skill data-quality-report

Analyze the educacion_estadisticas.csv dataset. It has columns: municipio, ano, cobertura_neta, tasa_desercion, num_estudiantes, num_docentes. About 500 rows, some missing values in cobertura_neta and tasa_desercion.
```

**Claude Code:**
```
Use the data-quality-report skill to analyze the educacion_estadisticas.csv dataset. It has columns: municipio, ano, cobertura_neta, tasa_desercion, num_estudiantes, num_docentes. About 500 rows, some missing values in cobertura_neta and tasa_desercion.
```

(Adapt the command syntax for your tool.)

Wait for the output.

**Checkpoint:** You should see a report with:

- A dataset overview with row/column counts
- Column analysis for each column
- Quality scores with justifications
- Recommended actions ordered by priority

Compare your report with your neighbor's. Are the scores or recommendations different? That is expected.

---

### Step 4: Iterate (2 minutes on your own)

What would you change about your skill? Here are some ideas:

- Add a "Data Type Recommendations" section (suggest better types for columns)
- Add a "Sample Values" section showing first 3 values per column
- Change the scoring scale from /10 to /5
- Make the rules stricter about what counts as a "valid" column

Edit your SKILL.md, save, and test again with the same prompt. See how the output changes.

---

## Part 3: Now You -- Create Your Own Skill

You just built a data-quality-report skill with step-by-step guidance. Now create a **second skill on your own**. Pick a topic, write the SKILL.md, test it.

### Pick one of these (or invent your own):

| Skill Idea | What It Does |
|-----------|-------------|
| **CSV Describer** | Given a CSV file, produce a plain-language description of what each column means and what the data represents |
| **Commit Message Writer** | Given a description of changes, generate a conventional commit message with type, scope, and body |
| **Class Notes Organizer** | Given raw class notes, organize by topics with headings, bullet points, and key takeaways |
| **Assignment Planner** | Given an assignment description and deadline, break it into concrete steps with dates |
| **Paper Summarizer** | Given an academic paper or article, extract key findings, methodology, and conclusions |
| **Bibliography Formatter** | Given a list of sources, format them in APA or IEEE style with all required fields |
| **Exam Prep Generator** | Given a topic, generate practice exam questions with answers and explanations |

### Requirements

Your SKILL.md must have:

- [ ] Frontmatter with name, description, version
- [ ] Clear instructions (what should the AI do?)
- [ ] A defined output format (what structure do you want back?)
- [ ] At least 3 rules or constraints
- [ ] Tested with at least 1 real prompt

### Process

1. Create the folder: `.yourTool/skills/your-skill-name/`
2. Write the SKILL.md (use the data-quality-report as reference, but do NOT copy it)
3. Test it with a real prompt
4. If the output is not what you wanted, improve the instructions and test again

Work individually or in pairs.

**Checkpoint:** Show your neighbor your skill and its output. Can they understand what it does just by reading the SKILL.md?

---

## Part 3.5: Understanding MCP Servers

MCP (Model Context Protocol) servers let your AI agent connect to external tools and data in real-time. Instead of copy-pasting information into prompts, you give the agent a live connection.

### Professor Demo

The professor shows an MCP server in action. Watch the screen.

**What you are seeing:**

1. The agent connects to an MCP server (e.g., a filesystem or GitHub server)
2. The agent can now browse, read, and interact with that external system
3. No copy-pasting needed -- the agent has direct access

### When Would You Use This?

| Scenario | Without MCP | With MCP |
|----------|------------|----------|
| Check your GitHub issues | Copy-paste issue text into prompt | Agent reads issues directly |
| Query a database schema | Export schema, paste into chat | Agent queries the database live |
| Analyze a large CSV | Describe columns manually | Agent reads the file itself |

### Key Concept

Think of it this way:
- A **skill** tells the agent HOW to do a task (recipe)
- An **MCP server** gives the agent ACCESS to external tools (kitchen appliance)
- An **agent** orchestrates both to complete complex work

**Checkpoint:** Can you think of one MCP server that would be useful for your data analytics project? Discuss with your neighbor for 30 seconds.

---

## Part 4: Download and Use an Existing Skill

### Step 1: Browse skills

Professor opens the skills source on screen. Everyone looks at the available skills.

Notice the structure: each skill is a folder with a SKILL.md file. Same format you just wrote.

---

### Step 2: Pick one together

As a class, we pick one skill relevant to our work. Professor reads through it out loud.

---

### Step 3: Security review

Before installing ANY skill, answer these questions:

- [ ] Does the SKILL.md try to read sensitive files? (passwords, .env, credentials)
- [ ] Does it instruct the agent to make network calls? (sending your data somewhere)
- [ ] Does it ask for API keys or tokens?
- [ ] Is the description clear about what it does?

**If any of the first three are YES: do NOT install.**

This is the same logic as reviewing a browser extension before installing. A skill gets access to your project files. Read what it does before you grant that access.

**Remember:** 13.4% of community skills have critical security issues. Over a third have at least one flaw. Only install from sources your instructor has reviewed.

---

### Step 4: Install and test

Copy the skill folder into your skills directory. Run it with a real prompt.

**Checkpoint:** The skill ran and produced useful output. Thumbs up if it worked.

---

## Part 5: Group Challenge

Now you work with your project team. Each group creates a custom skill for one of these deliverable types:

| # | Skill Type | What It Does |
|---|-----------|-------------|
| 1 | **Data Quality Reporter** | Given a dataset description, generate a structured quality assessment |
| 2 | **EDA Summary Generator** | Given analysis results, produce a structured EDA narrative |
| 3 | **README Generator** | Given a project folder, create a complete README.md |
| 4 | **Code Review Helper** | Given a code snippet, review for quality, readability, and bugs |

Coordinate with other groups so we cover all four types.

### Instructions

1. Pick one deliverable type from the table above.
2. Create a new skill folder: `.opencode/skills/your-skill-name/` (or your tool's equivalent)
3. Write the SKILL.md file with:
   - Clear frontmatter (name, description, version)
   - Specific instructions for the task
   - A defined output format
   - At least 3 rules or constraints
4. Test your skill with a real prompt. Iterate at least twice.
5. Prepare a 2-minute presentation:
   - What does your skill do?
   - What prompt did you test with?
   - Show the output.
   - What would you improve if you had more time?

### Presentations

Each group presents. After each presentation, the class gives one piece of feedback:

```
Strength: [One thing the skill does well]
Suggestion: [One improvement]
```

The best skill gets shared with the whole class.

---

## Deliverables

By end of class, you should have:

- [ ] Working AI CLI tool setup (connected and responding)
- [ ] One data-quality-report skill you built in Part 2 (guided)
- [ ] One skill you created on your own in Part 3 (independent)
- [ ] One downloaded skill installed and tested from Part 4
- [ ] One group-created skill from Part 5
- [ ] Understanding of what MCP servers do and when to use them (from Part 3.5)

---

## What Happens Next

From this week onward, you can use your AI CLI tool and skills for every exercise and workshop in this course. Every analysis, every visualization, every report.

The **workshop** (take-home) will guide you through building your full skills ecosystem: planning what skills you need for the rest of the semester and creating at least two more.

---

## Troubleshooting Reference

| Problem | Solution |
|---------|----------|
| "command not found" after install | Close and reopen your terminal, or use `npx <package-name>` |
| Gemini OAuth fails | Check your Google account has no restrictions. Try an incognito browser window. |
| API key errors | Regenerate the key on your provider's dashboard. Make sure no extra spaces were copied. |
| "Rate limit exceeded" | Wait 1 minute, or check your credit balance with your provider. |
| Skill not found | Check folder structure: `.toolname/skills/skill-name/SKILL.md` (exact path matters). |
| Skill output is bad | Improve your SKILL.md instructions. Be more specific about the format and constraints you want. |
| Tool hangs or freezes | Press Ctrl+C to cancel, then restart your tool. |
| "No provider configured" | Follow the authentication steps for your tool again. |
