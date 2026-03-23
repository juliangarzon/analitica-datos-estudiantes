# Guide: Agent Skills, MCP Servers, and Building Your Own

## What is the Agent Skills Standard?

The Agent Skills open standard (agentskills.io) defines a universal format for extending AI tools with specialized capabilities. A single SKILL.md file works across 20+ tools: OpenCode, Claude Code, Gemini CLI, Codex CLI, Cursor, VS Code Copilot, and others.

Think of a skill as a recipe card for an AI. Without a recipe, a chef can cook something decent. With a recipe, the chef produces exactly what you want, every time.

---

## SKILL.md Anatomy

```markdown
---
name: Skill Name
description: What this skill does (one sentence)
version: 1.0.0
---

# Skill Name

[Main instructions for the AI. Be specific about:]
- What the AI should do
- What format to use for output
- What constraints to follow

## Format

[Define the exact output format you want]

## Rules

- [Rule 1: specific constraint]
- [Rule 2: another constraint]
- [Rule 3: etc.]

## Examples (optional)

[Show input/output examples if helpful]
```

---

## Key Sections

### Frontmatter (required)

The YAML block at the top. Three fields:

- `name`: human-readable name (e.g., "Data Quality Report")
- `description`: one sentence explaining purpose
- `version`: semantic versioning (start with 1.0.0)

### Instructions (the body)

This is where you tell the AI what to do. The quality of your instructions determines the quality of the output.

**Bad:** "Analyze the data"
**Good:** "Analyze the provided dataset and generate a data quality report with completeness scores per column, type detection, missing value counts with percentages, and prioritized action items for cleaning."

### Format Section

Define the exact output structure you want. If you skip this, the AI will guess, and its guess will vary every time.

### Rules Section

Constraints that override default behavior:

- Things the AI tends to get wrong without explicit guidance
- Boundaries on scope ("do not generate visualizations unless asked")
- Style preferences ("use Python 3.10+ syntax with type hints")

---

## Creating Skills for Data Analytics

### Example 1: Data Quality Report

Key elements that make this skill work:

- Clear format with sections (Overview, Column Analysis, Quality Score, Actions)
- Rule: scores must be justified with evidence (AI tends to give high scores by default)
- Rule: recommend concrete actions, not vague suggestions
- Explicit section ordering with priorities

```markdown
---
name: Data Quality Report
description: Generates a structured data quality report for a dataset
version: 1.0.0
---

# Data Quality Report

Analyze the provided dataset and generate a comprehensive data quality report.

## Format

### Dataset Overview
- Name: [dataset name]
- Rows: [count]
- Columns: [count]

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

### Example 2: EDA Summary Generator

```markdown
---
name: EDA Summary Generator
description: Generates a structured EDA summary from dataset analysis
version: 1.0.0
---

# EDA Summary Generator

Given a dataset or analysis results, produce a structured Exploratory Data Analysis summary suitable for a report or presentation.

## Format

### Dataset Profile
- Name and source
- Dimensions (rows x columns)
- Time period covered (if applicable)

### Distribution Analysis
For each numerical column:
- Central tendency (mean, median)
- Spread (std, IQR)
- Shape (skewness direction)
- Notable patterns

### Correlations Found
- Top 3 strongest correlations with values
- Interpretation of each

### Outliers Detected
- Which columns have outliers
- Method used to identify them
- Recommended treatment

### Key Insights (Top 5)
1. [Most important finding]
2. [Second finding]
3. [Third finding]
4. [Fourth finding]
5. [Fifth finding]

### Suggested Next Steps
- [What analysis to do next]
- [What questions remain unanswered]

## Rules
- Use actual column names from the dataset
- Include specific numbers, not vague descriptions ("mean = 45.2" not "average is moderate")
- Prioritize actionable insights over obvious observations
- Flag data quality issues before analysis findings
- If the dataset has fewer than 5 insights worth reporting, report fewer rather than padding
```

### Example 3: README Generator

```markdown
---
name: README Generator
description: Creates a project README from codebase analysis
version: 1.0.0
---

# README Generator

Analyze the project and generate a README.md suitable for a data analytics or software project.

## Format

# [Project Name]

[One-line description of what this project does]

## Overview

[2-3 sentences explaining the project's purpose and scope]

## Dataset

- **Source:** [where the data comes from]
- **Size:** [rows x columns]
- **Key columns:** [list the most important columns]
- **Time period:** [if applicable]

## Installation

```bash
[Actual installation commands]
```

## Usage

```python
[Actual usage example with real file names]
```

## Project Structure

```
[Directory tree of the project]
```

## Results / Findings

[Brief summary of key findings, if applicable]

## Contributing

[Guidelines for contributing]

## Rules
- Read package.json, setup.py, requirements.txt, or similar for project metadata
- Include actual commands and file names, not placeholders
- Keep it under 200 lines
- If the project has a data/ folder, describe the datasets
- Use the project's actual language and framework in examples
```

---

## MCP Servers: Connecting Agents to External Tools

### What Is MCP?

MCP (Model Context Protocol) is an open standard that lets AI agents connect to external data sources and tools in real-time. Instead of pasting information into your prompts, you give the agent a live connection to the systems it needs.

Think of it as a USB port for your AI: plug in the right adapter, and your agent can talk to any external system.

### How MCP Works

```
Your Agent <---> MCP Server <---> External System
   (AI)         (bridge)       (GitHub, DB, API, etc.)
```

The MCP server acts as a bridge:
1. Your agent makes a request ("list open issues")
2. The MCP server translates it into an API call to the external system
3. The external system responds
4. The MCP server delivers the result back to your agent

### Common MCP Server Types

| MCP Server | What It Connects To | Use Case |
|-----------|---------------------|----------|
| Filesystem | Local files and directories | Navigate and read your codebase |
| GitHub | Repositories, issues, PRs | Manage code without leaving the agent |
| Database | PostgreSQL, MySQL, SQLite | Query schemas and data live |
| Browser | Web pages | Interact with web applications |
| Fetch | HTTP APIs | Call any REST API endpoint |

### When to Use MCP vs Copy-Paste

**Use MCP when:**
- You need live, up-to-date data (database queries, current GitHub issues)
- The data is large or complex (entire codebases, long API responses)
- You want the agent to take actions (create a PR, update a record)
- You are doing repeated queries against the same source

**Use copy-paste when:**
- It is a one-time, small piece of context (a single error message)
- The data does not change (a design decision, a specification)
- You do not have an MCP server set up for that source

### MCP and Data Analytics

MCP servers are particularly useful for data analytics workflows:

- **Database MCP server:** Query your data source directly instead of exporting CSVs
- **Filesystem MCP server:** Let the agent read your notebooks and scripts
- **GitHub MCP server:** Manage your project repository from within the agent
- **Fetch MCP server:** Pull data from APIs (datos.gov.co, public datasets)

---

## Security Guidelines

Before installing ANY community skill, review it carefully.

### Red Flags

- Skill instructions ask the AI to read `.env`, credentials, or SSH keys
- Skill makes network calls to external URLs
- Skill asks for API tokens or passwords
- Description is vague about what it does
- Source is an unknown author with no history

### Approved Sources

1. **Official tool repos:** GitHub repos maintained by Anthropic, Google, OpenAI
2. **Instructor-reviewed skills:** shared in the class repository
3. **Your own skills:** you wrote it, you trust it

### Rule of Thumb

Installing a skill is like installing a browser extension. You would not install one from an unknown source without reading what it does. Same principle applies here.

**To review a community skill:**
1. Read the entire SKILL.md file
2. Check: does it ask for access to sensitive files?
3. Check: does it instruct the AI to send data anywhere?
4. If anything looks suspicious, do not use it. Ask the professor.

---

## Tips for Good Skills

1. **Be specific.** "Analyze the data" is vague. "Generate a data quality report with completeness scores, type detection, and prioritized cleaning actions" is specific.
2. **Include format.** Show the exact output structure you want. The AI cannot read your mind about formatting.
3. **Add constraints.** Tell the AI what NOT to do. It tends to over-generate unless you set boundaries.
4. **Test and iterate.** Run the skill 3-5 times, see where it fails, improve the instructions. The first version is never the best.
5. **Keep it focused.** One skill = one task. A skill that tries to do everything will do nothing well.
6. **Use examples sparingly.** One good input/output example is worth more than three paragraphs of instructions.

---

## Skill Folder Locations by Tool

| Tool | Skill Folder Path |
|------|------------------|
| OpenCode | `.opencode/skills/skill-name/SKILL.md` |
| Claude Code | `.claude/skills/skill-name/SKILL.md` |
| Gemini CLI | `.gemini/skills/skill-name/SKILL.md` |
| Codex CLI | `.codex/skills/skill-name/SKILL.md` |

All four tools use the same SKILL.md format. If you switch tools, you only need to move the files to the new folder path.
