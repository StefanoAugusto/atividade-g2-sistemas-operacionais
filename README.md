# Trabalho G2 — Docker na Prática

## Descrição do Projeto

Este projeto consiste no desenvolvimento de uma aplicação web simples para gerenciamento de tarefas (CRUD), containerizada utilizando Docker.
Este trabalho foi desenvolvido para a disciplina de Sistemas Operacionais, com o objetivo de demonstrar o uso de containers, comunicação entre serviços, persistência de dados e justificativas técnicas das decisões adotadas, temas que foram abordados na sala de aula.

## Como executar

### 1. Build da imagem
Execute o comando abaixo na raiz do projeto:
```bash
docker build -t meu-app .
```
### 2. Subir os containers
```bash
docker compose up
```
### 3. Acessar a aplicação
Abra no navegador: http://localhost:5000/

## Estrutura do Projeto

```
atividade-g2-sistemas-operacionais/
├── evidencias/               # Prints das evidências
├── app.py                    # Aplicação Flask (API + frontend)
├── diario.md                 # Diário de desenvolvimento com erros e soluções
├── docker-compose.yml        # Orquestração dos serviços (app + redis)
├── Dockerfile                # Imagem docker
├── requirements.txt          # Dependências do projeto
└── Trabalho G2 - Sistemas Operacionais.pdf  # Documento do trabalho
```

## Tecnologias utilizadas

- Python (flask)
- Redis
- Docker
- Docker Compose

## Alunos
- Rhayra Rodrigues Fiorentin - 1135147
- Stefano Augusto Mossi - 1131685
