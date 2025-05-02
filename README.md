# Projeto: Escalabilidade de Aplicações Web com Load Balancer

## Descrição

Este projeto tem como objetivo demonstrar uma arquitetura básica de **escalabilidade horizontal** utilizando múltiplas instâncias de uma aplicação web Flask, distribuídas por meio de um **balanceador de carga NGINX**. Cada instância responde com um layout visual único, contendo seu nome, cor específica e um contador de requisições, facilitando a visualização do funcionamento do balanceamento.

## Estrutura da Solução

A aplicação é composta por:

- Quatro instâncias Flask (App 1 a App 4), cada uma com uma identidade visual.
- Um container NGINX atuando como **load balancer**, responsável por distribuir as requisições entre as instâncias.
- Todos os serviços são orquestrados com Docker Compose.

### Diagrama da Arquitetura

                       +------------------+
                       |      Cliente     |
                       +--------+---------+
                                |
                                v
                     +----------+----------+
                     |      NGINX (LB)     |
                     +----------+----------+
                                |
     +-----------+-------------+-------------+-----------+
     |           |             |             |           |
     v           v             v             v           v
 +--------+  +--------+   +--------+   +--------+
 | App 1  |  | App 2  |   | App 3  |   | App 4  |
 +--------+  +--------+   +--------+   +--------+


O balanceador de carga utiliza a política padrão (round robin) para redirecionar requisições entre as instâncias.

## Tecnologias Utilizadas

- Python (Flask)
- Docker
- Docker Compose
- NGINX

## Componentes do Projeto

### 1. Aplicação Flask (`app/app.py`)

Cada instância Flask:

- Exibe seu nome (ex: "App 1") com uma cor única de fundo.
- Mostra o ID real do container (hostname).
- Possui um contador de requisições recebidas.
- Recebe seu nome via variável de ambiente `APP_NAME`.

### 2. Dockerfile da Aplicação (`app/Dockerfile`)

Cria uma imagem leve da aplicação baseada em `python:3.10-slim`, instalando apenas o Flask e expondo a porta 5000.

### 3. Configuração do NGINX (`nginx/nginx.conf`)

Define um bloco `upstream` com os quatro serviços Flask, e um servidor que escuta na porta 80 para redirecionar as requisições HTTP.

### 4. Docker Compose (`docker-compose.yml`)

Define e orquestra todos os serviços:

- `app1`, `app2`, `app3`, `app4`: instâncias da aplicação Flask, com variáveis de ambiente distintas.
- `nginx`: expõe a porta 8080 ao host, servindo como ponto de entrada para a aplicação.

## Como Executar

1. No terminal, execute:

```bash
docker-compose up --build
Acesse a aplicação no navegador:

arduino
Copiar
Editar
http://localhost:8080
Recarregue a página várias vezes. O balanceador de carga alternará entre as instâncias, mostrando:

Uma cor diferente.

O nome da instância.

O número de requisições que ela já recebeu.

Possibilidades de Expansão
Substituir o NGINX por um serviço de nuvem como AWS Elastic Load Balancer.

Escalar automaticamente com Kubernetes e Auto Scaling Groups.

Monitorar desempenho com Prometheus e Grafana.

Aplicar cache com Redis para otimizar o desempenho.

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
Observações
Cada instância funciona de forma independente e compartilha a mesma base de código.

O uso de variáveis de ambiente permite customização visual e identificação de cada container.

O balanceamento pode ser demonstrado visualmente por meio da mudança de cores, nomes e contadores.

Autor
Desenvolvido por Ian Lucas de Almeida Silva para a atividade avaliativa de Escalabilidade de Aplicações Web.

yaml
Copiar
Editar

---

Se quiser, posso gerar esse `README.md` em arquivo pronto para download. Deseja que eu o envie agora?






Você disse:
poderia te um bloco explicando o Docker e outro explicando o nginx 


O ChatGPT disse:
Claro, Ian! Abaixo está o README.md atualizado, agora com dois blocos adicionais explicando Docker e NGINX em linguagem clara e técnica, voltada para um avaliador que busca domínio do conteúdo.

markdown
Copiar
Editar
# Projeto: Escalabilidade de Aplicações Web com Load Balancer

## Descrição

Este projeto tem como objetivo demonstrar uma arquitetura básica de **escalabilidade horizontal** utilizando múltiplas instâncias de uma aplicação web Flask, distribuídas por meio de um **balanceador de carga NGINX**. Cada instância responde com um layout visual único, contendo seu nome, cor específica e um contador de requisições, facilitando a visualização do funcionamento do balanceamento.

## Estrutura da Solução

A aplicação é composta por:

- Quatro instâncias Flask (App 1 a App 4), cada uma com uma identidade visual.
- Um container NGINX atuando como **load balancer**, responsável por distribuir as requisições entre as instâncias.
- Todos os serviços são orquestrados com Docker Compose.

### Diagrama da Arquitetura

lua
Copiar
Editar
                       +------------------+
                       |      Cliente     |
                       +--------+---------+
                                |
                                v
                     +----------+----------+
                     |      NGINX (LB)     |
                     +----------+----------+
                                |
     +-----------+-------------+-------------+-----------+
     |           |             |             |           |
     v           v             v             v           v
 +--------+  +--------+   +--------+   +--------+
 | App 1  |  | App 2  |   | App 3  |   | App 4  |
 +--------+  +--------+   +--------+   +--------+
yaml
Copiar
Editar

O balanceador de carga utiliza a política padrão (round robin) para redirecionar requisições entre as instâncias.

## Tecnologias Utilizadas

- Python (Flask)
- Docker
- Docker Compose
- NGINX

---

## O que é o Docker e como foi utilizado neste projeto

**Docker** é uma plataforma para criação e execução de containers, que são ambientes isolados e portáteis com tudo o que a aplicação precisa para funcionar (código, bibliotecas, dependências).

Neste projeto, o Docker foi utilizado para:

- Criar imagens da aplicação Flask com seu ambiente de execução.
- Subir múltiplas instâncias da aplicação (App 1 a App 4) isoladamente.
- Garantir reprodutibilidade e padronização entre as instâncias.
- Orquestrar os containers com Docker Compose, simplificando o processo de build e execução.

Cada instância Flask é um container que expõe a porta 5000. O Docker Compose gerencia a construção dessas instâncias a partir do mesmo Dockerfile, mas atribuindo uma variável de ambiente (`APP_NAME`) diferente a cada container, garantindo identidade própria para fins de balanceamento visual.

---

## O que é o NGINX e como foi utilizado neste projeto

**NGINX** é um servidor web que também pode atuar como proxy reverso e balanceador de carga. Ele é amplamente utilizado em sistemas escaláveis para distribuir o tráfego entre múltiplas réplicas de uma aplicação.

Neste projeto, o NGINX foi utilizado como **load balancer**:

- Escutando na porta 80 do container.
- Distribuindo requisições HTTP para as quatro instâncias Flask nas portas 5000.
- Utilizando a diretiva `upstream` para definir os servidores de backend (App 1 a App 4).
- Encaminhando o tráfego via `proxy_pass`.

A imagem oficial do NGINX foi utilizada via Docker, e seu comportamento foi configurado com o arquivo `nginx.conf`, mapeado para dentro do container com Docker Compose.

---

## Componentes do Projeto

### 1. Aplicação Flask (`app/app.py`)

Cada instância Flask:

- Exibe seu nome (ex: "App 1") com uma cor única de fundo.
- Mostra o ID real do container (hostname).
- Possui um contador de requisições recebidas.
- Recebe seu nome via variável de ambiente `APP_NAME`.

### 2. Dockerfile da Aplicação (`app/Dockerfile`)

Cria uma imagem leve da aplicação baseada em `python:3.10-slim`, instalando apenas o Flask e expondo a porta 5000.

### 3. Configuração do NGINX (`nginx/nginx.conf`)

Define um bloco `upstream` com os quatro serviços Flask, e um servidor que escuta na porta 80 para redirecionar as requisições HTTP.

### 4. Docker Compose (`docker-compose.yml`)

Define e orquestra todos os serviços:

- `app1`, `app2`, `app3`, `app4`: instâncias da aplicação Flask, com variáveis de ambiente distintas.
- `nginx`: expõe a porta 8080 ao host, servindo como ponto de entrada para a aplicação.

---

## Como Executar

1. No terminal, execute:

```bash
docker-compose up --build
Acesse a aplicação no navegador:

arduino
Copiar
Editar
http://localhost:8080
Recarregue a página várias vezes. O balanceador de carga alternará entre as instâncias, mostrando:

Uma cor diferente.

O nome da instância.

O número de requisições que ela já recebeu.

Possibilidades de Expansão
Substituir o NGINX por um serviço de nuvem como AWS Elastic Load Balancer.

Escalar automaticamente com Kubernetes e Auto Scaling Groups.

Monitorar desempenho com Prometheus e Grafana.

Aplicar cache com Redis para otimizar o desempenho.

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
Observações
Cada instância funciona de forma independente e compartilha a mesma base de código.

O uso de variáveis de ambiente permite customização visual e identificação de cada container.

O balanceamento pode ser demonstrado visualmente por meio da mudança de cores, nomes e contadores.

Autor
Desenvolvido por Ian Lucas de Almeida Silva para a atividade avaliativa de Escalabilidade de Aplicações Web.
