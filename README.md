# SpeedRun - Your Coding Assistant
SpeedRun is an AI coding assistant that uses Large Language Models (LLMs) to
understand code and perform actions through tool calls. In this project,
I built my own Claude Code from scratch by implementing an LLM-powered
coding assistant.

---

## AI Coding Agent — Built from Scratch

A Python-based AI coding agent powered by **Claude (claude-haiku-4.5)** via the OpenRouter API. The agent can autonomously read files, write files, and execute shell commands based on natural language prompts — similar to how tools like Claude Code and Cursor work under the hood.

---

## How It Works

The agent follows an **agentic loop**:

1. Takes a natural language prompt from the user via the terminal
2. Sends it to Claude along with a list of available tools
3. If Claude requests a tool (Read / Write / Bash), the agent executes it
4. The result is fed back to Claude as context
5. This loop continues until Claude produces a final text response
6. The final response is printed to stdout

```
You type prompt
      ↓
Send to Claude
      ↓
Claude requests a tool (e.g. Read file.py)
      ↓
Agent executes the tool
      ↓
Result sent back to Claude
      ↓
Claude gives final answer → printed to terminal
```

---

## Tools Supported

| Tool | What it does |
|------|-------------|
| `Read` | Reads the contents of any file |
| `Write` | Creates or overwrites a file with given content |
| `Bash` | Executes any shell command and returns the output |

---

## Tech Stack

- **Language:** Python
- **LLM:** Claude Haiku 4.5 (Anthropic) via OpenRouter
- **API Standard:** OpenAI-compatible REST API
- **Key Concepts:** LLM Tool Calling, Agentic Loop, Function Calling, Subprocess execution

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/tejastomarbyte/ai-coding-agent.git
cd ai-coding-agent
```

### 2. Set your API key

```bash
export OPENROUTER_API_KEY=your_openrouter_api_key_here
```

### 3. Run the agent

```bash
./your_program.sh -p "Read README.md and summarize it"
```

---

## Example Usage

```bash
# Read a file
./your_program.sh -p "What is the content of app/main.py?"

# Write a file
./your_program.sh -p "Read README.md and create the required file mentioned in it"

# Run shell commands
./your_program.sh -p "Delete the file named README_old.md"
```

---

## Project Structure

```
app/
  main.py         # Core agent logic — agentic loop + tool execution
your_program.sh   # Entry point script
pyproject.toml    # Python dependencies
```

---

## What I Learned

- How LLMs communicate tool usage via structured JSON (Function Calling)
- How to build an agent loop that drives multi-step AI reasoning
- How to integrate Read, Write, and Bash tools into a conversational AI flow
- How OpenAI-compatible APIs work with third-party LLM providers like OpenRouter
