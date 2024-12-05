import os

# Estrutura de diretórios e arquivos
structure = {
    "project": {
        "backend": {
            "app": {
                "api": ["poses.py"],
                "services": ["pose_analysis.py"],
                "utils": ["helpers.py"],
                "__init__.py": ""
            },
            "main.py": "",
            "Dockerfile": "",
            "requirements.txt": ""
        },
        "frontend": {
            "public": [],
            "src": {
                "components": ["Upload.js"],
                "pages": ["Home.js"],
                "App.js": ""
            },
            "Dockerfile": "",
            "package.json": "",
            "yarn.lock": ""
        },
        "database": {
            "init.sql": "",
            "Dockerfile": ""
        },
        "docker-compose.yml": "",
        "Makefile": "",
        "README.md": ""
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        elif isinstance(content, list):
            os.makedirs(path, exist_ok=True)
            for file in content:
                open(os.path.join(path, file), 'a').close()
        else:
            open(path, 'a').close()

# Cria a estrutura de diretórios e arquivos
create_structure(".", structure)