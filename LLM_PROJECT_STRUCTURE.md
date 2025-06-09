# 🧠 Generative AI Project Structure

> By **Sumanth Dhanya**

A structured template for building robust and scalable Generative AI applications, following best practices for maintainability and modular design.

---

## 📁 Project Directory Structure
```
generative_ai_project/
│
├── config/ # Configuration files
│ ├── init.py
│ ├── model_config.yaml
│ ├── prompt_templates.yaml
│ └── logging_config.yaml
│
├── src/ # Core source code
│ ├── llm/
│ │ ├── init.py
│ │ ├── base.py
│ │ ├── claude_client.py
│ │ ├── gpt_client.py
│ │ └── utils.py
│ ├── prompt_engineering/
│ │ ├── init.py
│ │ ├── templates.py
│ │ ├── few_shot.py
│ │ └── chainer.py
│ ├── utils/
│ │ ├── init.py
│ │ ├── rate_limiter.py
│ │ ├── token_counter.py
│ │ ├── cache.py
│ │ └── logger.py
│ └── handlers/
│ ├── init.py
│ └── error_handler.py
│
├── data/ # Organized data storage
│ ├── cache/
│ ├── prompts/
│ ├── outputs/
│ └── embeddings/
│
├── examples/ # Reference implementations
│ ├── basic_completion.py
│ ├── chat_session.py
│ └── chain_prompts.py
│
├── notebooks/ # Experimentation notebooks
│ ├── prompt_testing.ipynb
│ ├── response_analysis.ipynb
│ └── model_experimentation.ipynb
│
├── requirements.txt # Package dependencies
├── setup.py # Installation script
├── README.md # Project overview
└── Dockerfile # Container setup
```


---

## 🚀 Project Overview

This project provides a well-structured template to build generative AI applications using large language models. It emphasizes:

- Maintainability
- Scalability
- Modular design
- Clear separation of concerns

---

## 🧩 Key Components

| Component       | Description                                  |
|----------------|----------------------------------------------|
| `config/`       | YAML config files separated from code        |
| `src/`          | Modular and organized source code            |
| `data/`         | Organized storage for various data types     |
| `examples/`     | Sample implementation and test cases         |
| `notebooks/`    | Jupyter notebooks for experiments and analysis |

---

## ✅ Best Practices

1. Use YAML for configuration files
2. Implement proper error handling
3. Apply API rate limiting
4. Keep model clients modular
5. Cache results effectively
6. Maintain clean documentation
7. Use notebooks for iterative development

---

## 🛠 Getting Started

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd generative_ai_project
   ```
2. Install dependencies:

```bash
pip install -r requirements.txt
```
3. Configure your model and logging in config/

4. Review example code in examples/

5. Start exploring via notebooks/
---
💡 Development Tips

* Follow modular design principles
 
* Write tests for components
 
* Use version control (e.g., Git)
 
* Keep documentation updated
 
* Monitor model/API usage for limits
---
📦 Core Files

| Files            | Purpose                                 |
|------------------|-----------------------------------------|
| requirements.txt | Lists all dependencies                  |
| README.md        | Provides project documantation          |
| Docker File      | Containerization for deployment/testing |


🧪 License
This template is open for use and modification. Attribution appreciated. 🚀

