# ChatBot de WhatsApp com RAG, LangChain e FastAPI

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100-green?logo=fastapi)
![LangChain](https://img.shields.io/badge/LangChain-AI-orange)

Este projeto é um ChatBot de WhatsApp, projetado para atuar como um assistente especialista em um tópico específico, utilizando uma arquitetura RAG (Retrieval-Augmented Generation).

---

## 🏛️ Arquitetura da Solução

O projeto foi construído sobre uma arquitetura de microsserviços conteinerizada com Docker, onde cada componente tem uma responsabilidade clara:

- **`FastAPI (Bot)`:** O serviço principal escrito em Python, que contém a lógica do bot, o processamento de linguagem com LangChain e a comunicação com as outras partes do sistema.
- **`Evolution API`:** Atua como um gateway para o WhatsApp, recebendo e enviando mensagens de forma confiável.
- **`PostgreSQL`:** Banco de dados relacional, planejado para armazenar o histórico de conversas e permitir que o bot tenha "memória" de longo prazo.
- **`Redis`:** Utilizado para caching rápido e gerenciamento de filas de tarefas, otimizando a performance.
- **`LangChain`:** A biblioteca central que orquestra a interação com modelos de linguagem (LLMs), a base de conhecimento (Vectorstore) e a lógica de decisão (Chains e Prompts).

---

## 🚧 Funcionalidade

Atualmente, a infraestrutura base está 100% funcional. O bot se conecta a instância do evolutionAPI, recebe mensagens do WhatsApp e response baseado em histórico de conversa + documentos inseridos pelo usuário aplicando debounce(tempo de espera) + buffer(armazenamento temporário de informações)

---

## 📝 Roadmap e Próximos Passos
- [ ] **Integrar a IA:** integrar o aprendizado do chatbot com IA em outros projetos

---

## 🛠️ Tecnologias Utilizadas

- Python
- FastAPI
- LangChain
- Evolution API
- Docker & Docker Compose
- PostgreSQL
- Redis

---

## ⚙️ Como Rodar

1.  Clone este repositório.
2.  Crie um arquivo `.env` a partir do `env.example` e preencha suas chaves de API e credenciais.
3.  Crie uma pasta na raiz do projeto chamada: rag_files e insira seus documentos a serem vetorizados
3.  Execute `docker-compose up --build`.
4.  Acesse localhost:8080/manager, insira sua chave de api_key criada no .env para poder acessar
5.  Crie uma instância com mesmo nome da váriavel: **EVOLUTION_INSTANCE_NAME** e selecione opção Balleys
6.  Conecte seu whatsapp a instância do evolutionAPI através da leitura do QRcode
7.  Vá em webhooks, insira: http://bot:8000/webhook na url do webhook, adicione MESSAGE UPSERT como tipo de evento, seleciona a caixa de webhook de eventos, habilite e clique em salvar
8.  Aguarde para que o EvolutionAPI processe todos os contatos/conversas e em seguida o bot começará a responder automaticamente.
