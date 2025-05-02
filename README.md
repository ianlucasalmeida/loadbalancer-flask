# Projeto: Escalabilidade de Aplicações Web com Load Balancer

## Descrição

Este projeto demonstra uma arquitetura básica de escalabilidade horizontal utilizando múltiplas instâncias de uma aplicação Flask distribuídas por meio de um balanceador de carga NGINX. O objetivo é visualizar o funcionamento do balanceamento de carga, com cada instância exibindo seu nome, um contador de requisições e uma cor única.

## Estrutura da Solução

A aplicação é composta por:

- Quatro instâncias Flask (App 1 a App 4), cada uma configurada com uma variável de ambiente identificadora.
- Um container NGINX que atua como balanceador de carga (load balancer), distribuindo as requisições entre as quatro instâncias.
- Arquitetura orquestrada com Docker Compose.

Cliente → NGINX (Load Balancer) → App 1
→ App 2
→ App 3
→ App 4

markdown
Copiar
Editar

## Tecnologias Utilizadas

- Python 3 (Flask)
- Docker
- Docker Compose
- NGINX

## Componentes do Projeto

### 1. Aplicação Flask (`app/app.py`)

A aplicação Flask é responsável por retornar uma página HTML com:

- O nome da instância (`App 1`, `App 2`, etc.).
- O ID real do container (hostname).
- Um contador de requisições.
- Um estilo visual com cor de fundo específica por instância.

A identificação da instância é feita por meio de uma variável de ambiente (`APP_NAME`) passada no `docker-compose.yml`.

### 2. Dockerfile (`app/Dockerfile`)

Define a imagem Docker da aplicação:

- Baseada em `python:3.10-slim`.
- Instala o Flask.
- Copia o código e expõe a porta 5000.

### 3. Configuração do NGINX (`nginx/nginx.conf`)

O arquivo configura o NGINX como balanceador de carga:

- Define um grupo de servidores chamado `flask_app`.
- Cada servidor representa uma instância Flask (App 1 a App 4).
- As requisições no caminho `/` são encaminhadas para esse grupo com política padrão (round robin).

### 4. Docker Compose (`docker-compose.yml`)

Responsável por orquestrar todos os containers:

- Define quatro serviços de aplicação (`app1` a `app4`), todos construídos a partir do mesmo código.
- Cada container recebe uma variável de ambiente `APP_NAME` com seu nome correspondente.
- O serviço `nginx` depende das aplicações e encaminha as requisições externas para as instâncias internas.

## Execução

1. Clonar o repositório ou copiar os arquivos para uma pasta local.
2. No terminal, acessar o diretório do projeto e executar:

```bash
docker-compose up --build
Acessar no navegador:

arduino
Copiar
Editar
http://localhost:8080
Recarregar a página várias vezes para observar:

A mudança na cor de fundo.

O nome da instância.

A contagem individual de requisições por instância.

Expansão Futuras
Utilizar orquestradores como Kubernetes para escalar dinamicamente as instâncias.

Integrar monitoramento com Prometheus e Grafana.

Adicionar cache (ex.: Redis) para otimizar desempenho.

Utilizar serviços gerenciados de balanceamento em nuvem (ex.: AWS ELB, GCP Load Balancing).

Organização do Projeto
Copiar
Editar
loadbalancer-flask/
├── app/
│   ├── app.py
│   └── Dockerfile
├── nginx/
│   └── nginx.conf
├── docker-compose.yml
└── README.md
Autoria
Desenvolvido por Ian Lucas de Almeida Silva como parte da atividade avaliativa de Escalabilidade de Aplicações Web.