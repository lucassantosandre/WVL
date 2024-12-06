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


# 🏋️ Pose Analysis Project 📸

Um **projeto focado no aprendizado e desenvolvimento de tecnologias** para análise de poses corporais. Utilizando **Python**, **Docker**, **Machine Learning** e **Inteligência Artificial**, o objetivo é detectar landmarks corporais, calcular ângulos e identificar poses clássicas, alinhando-se aos critérios estabelecidos pelo **IFBB Pro**.

> ⚠️ **Nota:** Este projeto está em desenvolvimento contínuo e tem como foco o **aprendizado** de tecnologias como Python, Docker, Machine Learning e IA. Ainda há diversos pontos a melhorar, mas ele está sendo aprimorado regularmente!

---

## ✨ **Objetivos do Projeto**
- 📏 **Análise de Poses:** Detectar landmarks corporais e calcular ângulos para avaliação precisa.
- 🏋️ **Reconhecimento de Poses:** Identificar poses clássicas como "Duplo Bíceps de Frente".
- 🤖 **Evolução em IA:** Criar um pipeline para aprendizado de máquina, capaz de identificar poses automaticamente.
- 🔧 **Foco em aprendizado:** Utilizar ferramentas como **Docker**, **Machine Learning** e **Python** de forma prática.

---

## 🛠️ **Tecnologias Utilizadas**
- **Python 3.9**
- **FastAPI** para criação da API
- **Mediapipe** para detecção de landmarks
- **OpenCV** para processamento de imagens
- **Docker** para gerenciamento de containers
- **React** para o frontend
- **Node.js** para o ambiente do frontend

---

## ⚙️ **Como Configurar o Projeto**

### **Pré-requisitos**
1. **Instalar Python 3.11**:
   - [Baixar Python 3.11](https://www.python.org/downloads/release/python-3110/)

2. **Instalar Docker e Docker Compose**:
   - [Docker](https://www.docker.com/)
   - [Docker Compose](https://docs.docker.com/compose/install/)

3. **Instalar Make**:
   - [Linux/MacOS: Já disponível na maioria das distribuições.](https://www.gnu.org/software/make/)
   - [Windows: Baixar Make para Windows](http://gnuwin32.sourceforge.net/packages/make.htm)


2. **Clone o repositório**:
   ```bash
   git clone <seu-repo-url>
   cd <nome-do-repo>
   ```

---

### **Utilizando o Makefile**
O projeto utiliza um **Makefile** para simplificar os comandos com Docker. Aqui estão os comandos disponíveis:

| Comando                 | Descrição                                      |
|-------------------------|-----------------------------------------------|
| `make build`            | Constrói as imagens Docker                   |
| `make up`               | Inicia os containers Docker                  |
| `make down`             | Para e remove os containers                  |
| `make logs`             | Exibe os logs de todos os serviços           |
| `make backend-bash`     | Acessa o shell do container do backend        |
| `make frontend-bash`    | Acessa o shell do container do frontend       |
| `make restart`          | Reinicia os containers                       |

---

### **Passo a Passo para Uso**
1. **Builda e Subir a aplicação**:
   ```bash
   make up
   ```
2. **Acesse a aplicação**:
   - **Frontend:** [http://localhost:3000](http://localhost:3000)
   - **Backend:** [http://localhost:8000/docs](http://localhost:8000/docs)

3. **Realize o upload de uma imagem de pose**:
   - Utilize o botão de upload no frontend.
   - Verifique os resultados no painel de resposta e visualize a imagem anotada.

---

## 📚 **Como Funciona o Projeto**
1. O **Frontend** permite o upload de imagens e exibe os resultados da análise.
2. O **Backend** processa as imagens utilizando o **Mediapipe** para detecção de landmarks e cálculo de ângulos.
3. O sistema tenta identificar a pose e gera feedbacks com base nos critérios definidos.
4. Uma imagem anotada é gerada, destacando os landmarks detectados.

---

## 🚧 **Pontos a Melhorar**
- **Reconhecimento Avançado de Poses:** Melhorar o reconhecimento automático de poses como "Duplo Bíceps de Frente".
- **Feedbacks Detalhados:** Implementar análises mais completas e detalhadas baseadas em critérios de simetria e alinhamento.
- **Detecção Facial Avançada:** Refinar o uso de MediaPipe para validar a presença e o alinhamento do rosto.
- **Suporte a Novas Poses:** Adicionar mais poses clássicas ao sistema.
- **Integração com Machine Learning:** Treinar um modelo personalizado para identificação de poses específicas.

---

## 🧪 **Contribuindo**
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para discutir melhorias ou adicionar funcionalidades.

---

## 📄 **Licença**
Este projeto é de código aberto e licenciado sob os termos da **MIT License**.

---

> Desenvolvido com 💪 e ☕ para aprender, crescer e explorar o mundo de Machine Learning, IA e Python!
