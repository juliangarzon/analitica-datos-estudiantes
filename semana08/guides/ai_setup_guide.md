# AI Development Environment Setup Guide

Set up the AI CLI tools you will use for the rest of this course (Weeks 9-16): exercises, workshops, and milestones.

**Estimated Time:** 15-20 minutes
**Required for:** Week 8 in-class exercise

---

## Prerequisites

| Software | Minimum Version | Check Command |
|----------|----------------|---------------|
| Node.js | 18.0.0 | `node --version` |
| npm | 9.0.0 | `npm --version` |

### Installing Node.js (if needed)

**macOS:**
```bash
brew install node
```

**Windows:**
```bash
winget install OpenJS.NodeJS.LTS
```

**Linux (Ubuntu/Debian):**
```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
```

Or download directly from https://nodejs.org (LTS version).

---

## Choose Your CLI Tool

You need ONE working tool. All four options support the SKILL.md standard. Pick whichever is easiest for you.

| | OpenCode | Gemini CLI | Claude Code | Codex CLI |
|---|---|---|---|---|
| **Provider** | Open source (multi-LLM) | Google | Anthropic | OpenAI |
| **Install** | `npm i -g @anthropics/opencode` | `npm i -g @anthropic/gemini-cli` | `npm i -g @anthropic-ai/claude-code` | `npm i -g @openai/codex` |
| **Free tier** | Depends on LLM | 60 RPM, 1M tokens | Limited free | Limited free |
| **Auth method** | Varies by LLM | Google OAuth | API key or account | API key or account |
| **Context window** | Varies by LLM | 1M tokens | Varies by plan | Varies by plan |
| **Best for** | Flexibility | Free, no config | Claude models | GPT models |

**Professor's recommendation:** If you are unsure, start with **Gemini CLI** (free, simple Google OAuth) or **OpenCode + Gemini** (free, more flexible). You can always switch later.

---

## Option A: OpenCode (Multi-LLM)

### Install

```bash
npm install -g @anthropics/opencode
```

Verify:
```bash
opencode --version
```

### Connect to an LLM

```bash
opencode
/connect
```

Select a provider:

**Google Gemini (recommended for free tier):**
1. Select "Google" from the provider list
2. Complete OAuth in your browser (sign in with Google)
3. You should see a confirmation message

**DeepSeek (recommended for heavy use):**
1. Go to https://platform.deepseek.com
2. Create account and get an API key
3. Set environment variable:
```bash
export DEEPSEEK_API_KEY="sk-your-key-here"
```
4. Restart OpenCode

**Troubleshooting:**
- OAuth popup blocked: try an incognito browser window
- "Quota exceeded": you hit the daily limit. Wait until tomorrow or switch provider.
- "command not found": use `npx @anthropics/opencode` instead

---

## Option B: Gemini CLI

### Install

```bash
npm install -g @anthropic/gemini-cli
```

Verify:
```bash
gemini --version
```

### Connect

```bash
gemini
```

It will open your browser for Google OAuth. Sign in with your Google account. Done.

**What you get:** 60 requests/minute, 1M token context window, free.

**Troubleshooting:**
- OAuth fails: check your Google account allows third-party apps
- "Rate limit": wait 1 minute. The limit is per minute, not per day.

---

## Option C: Claude Code

### Install

```bash
npm install -g @anthropic-ai/claude-code
```

Verify:
```bash
claude --version
```

### Connect

```bash
claude
```

Follow the authentication prompts. You need either:
- An Anthropic account with free credits, OR
- An API key from https://console.anthropic.com

**Troubleshooting:**
- "Invalid API key": regenerate on console.anthropic.com
- No free credits: check your Anthropic account billing page

---

## Option D: Codex CLI

### Install

```bash
npm install -g @openai/codex
```

Verify:
```bash
codex --version
```

### Connect

```bash
codex
```

Follow the authentication prompts. You need either:
- An OpenAI account, OR
- An API key from https://platform.openai.com

**Troubleshooting:**
- "Invalid API key": regenerate on platform.openai.com
- "Insufficient quota": add credits to your OpenAI account

---

## Verify Everything Works

Run these 3 test prompts in your chosen tool:

1. **Basic:** "Explain what data analytics is in one sentence."
2. **Code:** "Generate a Python pandas function that calculates missing value percentages per column."
3. **Format:** "Write a bullet-point summary of what EDA means and its 3 main steps."

If all 3 produce reasonable output, you are ready.

---

## Skills Setup

After your tool is working, create your first skill folder:

```bash
# OpenCode
mkdir -p .opencode/skills/

# Gemini CLI
mkdir -p .gemini/skills/

# Claude Code
mkdir -p .claude/skills/

# Codex CLI
mkdir -p .codex/skills/
```

Skills go in subfolders within your tool's skills directory. Example:

```
.opencode/skills/
    data-quality-report/
        SKILL.md
    eda-summary/
        SKILL.md
```

---

## Quick Reference

### OpenCode
| Command | What it does |
|---------|-------------|
| `opencode` | Start OpenCode |
| `/connect` | Connect to an LLM provider |
| `/skill skill-name` | Use a skill |
| `/help` | Show available commands |
| `exit` | Exit |

### Gemini CLI
| Command | What it does |
|---------|-------------|
| `gemini` | Start Gemini CLI |
| Type naturally | Chat with Gemini |
| `exit` or Ctrl+C | Exit |

### Claude Code
| Command | What it does |
|---------|-------------|
| `claude` | Start Claude Code |
| Type naturally | Chat with Claude |
| `/help` | Show available commands |
| `exit` or Ctrl+C | Exit |

### Codex CLI
| Command | What it does |
|---------|-------------|
| `codex` | Start Codex CLI |
| Type naturally | Chat with GPT |
| `exit` or Ctrl+C | Exit |

---

## Security Reminders

- Do NOT share your API keys with anyone
- Do NOT commit API keys to git repositories
- Do NOT post keys in forums or chat
- If a key is compromised, regenerate immediately on your provider's dashboard
- Add `.env` to your `.gitignore` file

---

## Getting Help

1. Check this guide's troubleshooting sections
2. Ask in the class group chat
3. Ask the professor during office hours
4. Search: "[your tool name] [your error message]"
