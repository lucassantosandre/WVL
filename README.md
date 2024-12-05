<p align="center">
  <a href="https://www.python.org/" target="blank">
    <img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png" width="200" alt="Python Logo" />
  </a>
</p>

<p align="center">Calculadora de RM e Progressão de Carga: um sistema para registrar treinos e sugerir cargas com base na progressão semanal e princípios científicos de treino.</p>

<p align="center">
<a href="https://www.python.org/" target="_blank"><img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python Version" /></a>
<a href="https://opensource.org/licenses/MIT" target="_blank"><img src="https://img.shields.io/badge/license-MIT-brightgreen.svg" alt="License" /></a>
<a href="https://hub.docker.com/" target="_blank"><img src="https://img.shields.io/badge/docker-compatible-blue" alt="Docker Compatible" /></a>
<a href="https://fastapi.tiangolo.com/" target="_blank"><img src="https://img.shields.io/badge/framework-fastapi-brightgreen" alt="FastAPI Framework" /></a>
</p>

---

## 🚀 **Calculadora de RM e Progressão de Carga**

Esta aplicação permite:
- **Registrar exercícios e treinos**.
- **Calcular o RM (1 Repetition Maximum)** com base em fórmulas científicas (Epley, Brzycki).
- **Sugerir progressões de carga** com foco em intensidade.
- **Acompanhar o progresso dos treinos** através de histórico e métricas.

---

## 🛠️ **Tecnologias Utilizadas**

- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Banco de Dados**: SQLite
- **Containerização**: Docker
- **Linguagem**: Python 3.10+

---

## 📁 **Estrutura do Projeto**

```plaintext
calculadora_rm/
├── app/
│   ├── __init__.py        # Inicialização do módulo
│   ├── main.py            # API principal
│   ├── models.py          # Banco de dados
│   ├── schemas.py         # Validação dos dados
│   ├── services.py        # Lógica de negócio
│   └── utils.py           # Fórmulas de RM e progressão
├── frontend/
│   └── streamlit_app.py   # Interface interativa
├── database/
│   └── db.sqlite          # Banco de dados SQLite
├── requirements.txt       # Dependências do projeto
├── Dockerfile             # Configuração do contêiner Docker
├── docker-compose.yml     # Orquestração do Docker
├── Makefile               # Automatização de comandos
└── README.md              # Documentação do projeto
```

## 🐳 Usando o Docker
