import os

# Define the project structure as a dictionary
project_structure = {
    "generative_ai_project": {
        "config": [
            "__init__.py",
            "model_config.yaml",
            "prompt_templates.yaml",
            "logging_config.yaml"
        ],
        "src": {
            "llm": [
                "__init__.py",
                "base.py",
                "claude_client.py",
                "gpt_client.py",
                "utils.py"
            ],
            "prompt_engineering": [
                "__init__.py",
                "templates.py",
                "few_shot.py",
                "chainer.py"
            ],
            "utils": [
                "__init__.py",
                "rate_limiter.py",
                "token_counter.py",
                "cache.py",
                "logger.py"
            ],
            "handlers": [
                "__init__.py",
                "error_handler.py"
            ]
        },
        "data": [
            "cache/",
            "prompts/",
            "outputs/",
            "embeddings/"
        ],
        "examples": [
            "basic_completion.py",
            "chat_session.py",
            "chain_prompts.py"
        ],
        "notebooks": [
            "prompt_testing.ipynb",
            "response_analysis.ipynb",
            "model_experimentation.ipynb"
        ],
        "requirements.txt": "",
        "setup.py": "",
        "README.md": "",
        "Dockerfile": ""
    }
}

def create_structure(base_path, structure):
    for key, value in structure.items():
        current_path = os.path.join(base_path, key)
        if isinstance(value, dict):
            os.makedirs(current_path, exist_ok=True)
            create_structure(current_path, value)
        elif isinstance(value, list):
            os.makedirs(current_path, exist_ok=True)
            for item in value:
                if item.endswith("/"):
                    os.makedirs(os.path.join(current_path, item.strip("/")), exist_ok=True)
                else:
                    open(os.path.join(current_path, item), 'a').close()
        elif isinstance(value, str):
            open(os.path.join(base_path, key), 'a').close()

# Run the script to create the directory structure
create_structure(".", project_structure)
print("Project structure created successfully.")
