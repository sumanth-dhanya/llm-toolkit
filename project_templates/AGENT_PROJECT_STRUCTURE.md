
# 🧠 Agent Project Template

This project template helps scaffold a modular, production-grade AI Agent architecture with a comprehensive folder structure and essential files.

---

## 📁 Structure Overview

The template creates a complete project structure including:

- **Application Layer**: Conversation, agent management, and evaluation services
- **Core Components**: Agent logic, prompts, tools, and utilities
- **Infrastructure**: Vector databases, monitoring, LLM clients, and APIs
- **Development Tools**: Jupyter notebooks, CLI scripts, and testing framework
- **DevOps**: CI/CD workflows, Docker configuration, and environment setup

---

## 🧩 Components Explained

| Folder/File                           | Purpose                                      |
|---------------------------------------|----------------------------------------------|
| `.github/workflows/`                  | CI/CD pipeline using GitHub Actions         |
| `data/`                              | Stores input/output data                     |
| `notebooks/`                         | Interactive development and experimentation |
| `├── 01_prompt_engineering_playground.ipynb` | Prompt design and testing            |
| `├── 02_short_term_memory.ipynb`     | Short-term memory implementation             |
| `├── 03_long_term_memory.ipynb`      | Long-term memory and persistence             |
| `└── 04_tool_calling_playground.ipynb` | Tool integration and testing              |
| `src/agent_project/application/`     | High-level application services              |
| `src/agent_project/core/`            | Core agent logic and components              |
| `src/agent_project/infrastructure/`  | External integrations and infrastructure     |
| `tools/`                             | CLI scripts and utilities                    |
| `├── populate_long_term_memory.py`   | Memory population script                     |
| `├── delete_long_term_memory.py`     | Memory cleanup script                        |
| `├── evaluate_agent.py`              | Agent evaluation script                      |
| `├── generate_evaluation_dataset.py` | Dataset generation for evaluation            |
| `├── finetune_agent_llm.py`          | Model fine-tuning script                     |
| `└── run_agent.py`                   | Main agent execution script                  |
| `tests/`                             | Test coverage for core components            |
| `static/`                            | Static assets and resources                  |
| Configuration files                   | Environment, Docker, and project setup      |

---

## 🚀 Getting Started

### Create a New Agent Project

```bash
# Create a project named "my-agent"
python agent_project_template.py my-agent

# Create a project in a specific directory
python agent_project_template.py my-agent --base-path /path/to/projects

# Or using the short form
python agent_project_template.py my-agent -p /path/to/projects

```