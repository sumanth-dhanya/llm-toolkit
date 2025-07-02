import os
import argparse

# Directory structure
project_structure = {
    "agent-project": {
        ".github": {
            "workflows": ["ci.yml"],
            "__files__": ["ISSUE_TEMPLATE.md"]
        },
        "data": {},
        "notebooks": [
            "01_prompt_engineering_playground.ipynb",
            "02_short_term_memory.ipynb",
            "03_long_term_memory.ipynb",
            "04_tool_calling_playground.ipynb"
        ],
        "src": {
            "agent_project": {
                "application": {
                    "conversation_service": {},
                    "add_new_agent_service": {},
                    "add_new_tool_service": {},
                    "evaluation_service": {},
                },
                "core": {
                    "agent": {},
                    "prompts": {},
                    "tools": {},
                    "utils": {},
                },
                "infrastructure": {
                    "vector_database": {},
                    "monitoring": {},
                    "llm_clients": {},
                    "api": {},
                },
                "__files__": ["config.py"]
            }
        },
        "tools": [
            "populate_long_term_memory.py",
            "delete_long_term_memory.py",
            "evaluate_agent.py",
            "generate_evaluation_dataset.py",
            "finetune_agent_llm.py",
            "run_agent.py"
        ],
        "tests": [
            "test_memory.py",
            "test_agent.py"
        ],
        "__files__": [
            ".env.example",
            ".python-version",
            "Dockerfile",
            "Makefile",
            "pyproject.toml"
        ],
        "static": {}
    }
}


def create_structure(base_path, structure):
    for name, content in structure.items():
        if name == "__files__":
            for file in content:
                file_path = os.path.join(base_path, file)
                with open(file_path, 'w') as f:
                    f.write(f"# {file}")
        elif isinstance(content, dict):
            dir_path = os.path.join(base_path, name)
            os.makedirs(dir_path, exist_ok=True)
            create_structure(dir_path, content)
        elif isinstance(content, list):
            os.makedirs(os.path.join(base_path, name), exist_ok=True)
            for file in content:
                file_path = os.path.join(base_path, name, file)
                with open(file_path, 'w') as f:
                    f.write(f"# {file}")


def main():
    parser = argparse.ArgumentParser(description='Create an agent project template')
    parser.add_argument('project_name',
                        help='Name of the project to create')
    parser.add_argument('--base-path', '-p',
                        default='.',
                        help='Base path where the project should be created (default: current directory)')

    args = parser.parse_args()

    # Update the project structure with the provided project name
    updated_structure = {args.project_name: project_structure["agent-project"]}

    create_structure(args.base_path, updated_structure)
    print(f"✅ Agent project template '{args.project_name}' created successfully.")


if __name__ == "__main__":
    main()