
# 🏋️ Pose Analysis Project 📸

Um **projeto inovador** para análise de poses de fisiculturismo utilizando **Python**, **Docker**, **Machine Learning** e **Inteligência Artificial**. O objetivo principal é analisar poses de fisiculturismo, identificar landmarks corporais, calcular ângulos e reconhecer poses com base nos critérios do **IFBB Pro**.

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
1. **Instalar Docker e Docker Compose**:
   - [Docker](https://www.docker.com/)
   - [Docker Compose](https://docs.docker.com/compose/install/)

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
1. **Construa as imagens Docker**:
   ```bash
   make build
   ```

2. **Inicie os containers**:
   ```bash
   make up
   ```

3. **Acesse a aplicação**:
   - **Frontend:** [http://localhost:3000](http://localhost:3000)
   - **Backend:** [http://localhost:8000/docs](http://localhost:8000/docs)

4. **Realize o upload de uma imagem de pose**:
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

## 🌟 **Imagens de Demonstração**
### **Frontend**
![Frontend Example](https://via.placeholder.com/800x400.png?text=Frontend+Example)

### **Imagem Anotada**
![Annotated Image](https://via.placeholder.com/800x400.png?text=Annotated+Image)

---

> Desenvolvido com 💪 e ☕ para aprender, crescer e explorar o mundo de Machine Learning, IA e Python!
