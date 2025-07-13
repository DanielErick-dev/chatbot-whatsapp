# ChatBot de WhatsApp com RAG, LangChain e FastAPI

![Status](https://img.shields.io/badge/status-em_desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100-green?logo=fastapi)
![LangChain](https://img.shields.io/badge/LangChain-AI-orange)

Este projeto é um ChatBot de WhatsApp em desenvolvimento, projetado para atuar como um assistente especialista em um tópico específico, utilizando uma arquitetura RAG (Retrieval-Augmented Generation).

---

## 🏛️ Arquitetura da Solução

O projeto foi construído sobre uma arquitetura de microsserviços conteinerizada com Docker, onde cada componente tem uma responsabilidade clara:

- **`FastAPI (Bot)`:** O serviço principal escrito em Python, que contém a lógica do bot, o processamento de linguagem com LangChain e a comunicação com as outras partes do sistema.
- **`Evolution API`:** Atua como um gateway para o WhatsApp, recebendo e enviando mensagens de forma confiável.
- **`PostgreSQL`:** Banco de dados relacional, planejado para armazenar o histórico de conversas e permitir que o bot tenha "memória" de longo prazo.
- **`Redis`:** Utilizado para caching rápido e gerenciamento de filas de tarefas, otimizando a performance.
- **`LangChain`:** A biblioteca central que orquestra a interação com modelos de linguagem (LLMs), a base de conhecimento (Vectorstore) e a lógica de decisão (Chains e Prompts).

---

## 🚧 Estado Atual do Projeto

Atualmente, a infraestrutura base está 100% funcional. O bot já está conectado à Evolution API, sendo capaz de receber mensagens do WhatsApp e enviar respostas básicas. A estrutura para a implementação do RAG (pastas `rag_files` e `vectorstore_data`) está criada.

---

## 📝 Roadmap e Próximos Passos

O foco agora é evoluir a inteligência do bot. Os próximos passos são:

- [ ] **Treinar a IA:** Ingerir documentos na pasta `rag_files` para criar uma base de conhecimento em um Vectorstore e treinar o bot para responder perguntas sobre um assunto específico.
- [ ] **Implementar Memória de Conversa:** Utilizar o PostgreSQL para que o bot se lembre de interações passadas com o usuário.
- [ ] **Refinar os Prompts:** Melhorar as instruções dadas ao modelo de linguagem para obter respostas mais precisas e coerentes.
- [ ] **Criar uma Chain de Decisão:** Desenvolver uma lógica mais complexa com LangChain para que o bot possa executar diferentes ações com base na intenção do usuário.

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
3.  Execute `docker-compose up --build`.
4.  Conecte seu WhatsApp à instância da Evolution API seguindo a documentação oficial.
