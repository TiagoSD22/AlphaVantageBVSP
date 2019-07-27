# Alpha Vantage Wrapper (Desafio PontoTel)

Este projeto foi criado para a participação no processo seletivo da Empresa PontoTel. O desafio consistia em desenvolver uma aplicação em Python 3.7 que consumisse a API da [Alpha Vantage](https://www.alphavantage.co/) a fim de se calcular os dados do Ibovespa e cotações das 10 maiores empresas brasileiras. Preferivelmente, a API deveria ser consumida de forma assíncrona e, como bônus, deveria-se ,utilizando PostgreSQL, modelar em banco de dados tabelas de empresas e cotações e fornecer para o usuário operações de acesso e manipulação desses dados por meio de uma página HTML. 

---

# Estrutura do projeto

O projeto está dividido em uma arquitetura cliente-servidor. O lado do servidor foi feito em Python 3.7 e consome, assíncronamente, as API's fornecidas pela [Alpha Vantage](https://www.alphavantage.co/) para fornecer os dados da aplicação.
O lado do cliente foi desenvolvido com Angular 7 e componentes do Material Design. Existe também uma camada de banco de dados desenvolvida com PostgreSQL para persistência de dados sobre empresas e suas cotações recebidas durante a execução da aplicação.

---

# Endpoints da API

```
/bvsp-intraday/<timeInterval> Recebe um valor numérico(timeInterval) para calcular o Ibovespa do dia, em que o timeInterval representa o intervalo de tempo entre os pontos.
```
```
/get-top-10  Retorna a lista das 10 maiores empresas brasileiras salvas no banco de dados
```
```
/get-company-stock/<companySymbol> Recebe uma string que representa o código de uma empresa e retorna a cotação atual desta
```

```
/update-company-stock/ Recebe um JSON contendo a cotação de uma empresa e persiste essa informação no banco de dados
```
Para ver a documentação completa da API acesse o [Swagger Editor](https://editor.swagger.io/) e importe o arquivo [documentacaoAPI.yaml](https://github.com/TiagoSD22/AlphaVantageBVSP/blob/master/documentacaoAPI.yaml) na opção File -> Importe file, localizada na parte superior esquerda do menu de navegação do site.

---

## Dependências utilizadas

Para a aplicação em Python foram usadas, principalmente, as dependências:

+ [Python 3.7](https://www.python.org/)
  - Uma das versões mais recentes desta linguagem.
+ [Sanic](https://sanic.readthedocs.io/en/latest/index.html)
  - Um framework web para Python3.6+ com suporte a requisições assíncronas.
+ [Marshmallow](https://marshmallow.readthedocs.io/en/3.0/api_reference.html)
  - Biblioteca ORM/ODM útil para validação e desserialização de dados.
+ [Asyncpg](https://magicstack.github.io/asyncpg/current/index.html)
  - Biblioteca Python para interface com banco de dados postgreSQL por meio de funções assíncronas.
+ [Asyncio](https://docs.python.org/3/library/asyncio.html)
  - Biblioteca Python para escrever funções assíncronas em código concorrente usando a sintaxe async/await.
+ [Pytest](https://docs.pytest.org/en/latest/)
  - Framework para escrever testes em Python.
+ [Requests](https://requests.readthedocs.io/pt_BR/latest/user/quickstart.html)
  - Biblioteca HTTP para Python.

Para a aplicação em Angular foram usadas, principalmente, as dependências:
+ [Angular 7](https://angular.io/)
  - Uma das versões mais recentes do Framework Angular para desenvolvimento WEB.
+ [Angular-CLI](https://cli.angular.io/)
  - Ferramenta de linha de comando para gerenciamento de projetos Angular.
+ [NPM](https://www.npmjs.com/)
  - Gerenciador de pacotes NodeJs
+ [Angular Material](https://material.angular.io/)
  - Biblioteca com implementações estilo Material Design para Angular.
+ [Ngx-datatable](https://github.com/swimlane/ngx-datatable)
  - Componente para criação de tabelas utilizando TypeScript, HTML e CSS.
+ [Highcharts](https://www.highcharts.com/blog/post/highcharts-and-angular-7/)
  - Componente para exibição de dados em formato gráfico.
+ [NGINX](https://www.nginx.com/)
  - Servidor HTTP usado para o deploy da aplicação.

Para a camada de banco de dados foi utilizada a seguinte dependência:
+ [PostgreSQL 10](https://www.postgresql.org/)
  - SGBD relacional em uma de suas versões mais atuais.
---

## Execução da aplicação

O projeto foi configurado para execução com Docker Compose. Contudo, é possível fazer a execução manualmente.

### 1 Execução via Docker Compose

Para executar utilizando o Docker Compose, primeiramente, é necessário fazer a instalação do [Docker](https://docs.docker.com/), siga as instruções da documentação para instalar a versão mais apropriada da sua distro. Instalado o Docker, precisamos instalar o [Docker Compose](https://docs.docker.com/compose/install/) para gerenciar os 3 containers da aplicação. Após instalá-lo, basta executar o comando docker-compose up --build (**pode precisar de permissão de super usuário**) na pasta fonte do projeto, onde está localizado o arquivo docker-compose.yml e o processo de download/instalação de dependências se dará de forma automática. O processo de build total da aplicação pode levar em torno de 10 a 15 minutos, dependendo da máquina e conexão com a internet. Quando o Docker Compose completar o processo,a aplicação poderá ser acessada a partir de um navegador WEB acessando o endereço **http://localhost:4200**. Observação: certifique-se antes de executar o build da aplicação de que não há nenhuma processo rodando em uma das seguintes portas: **4200,5432,5000**, pois se houver, o comando docker-compose falhará. Dica: caso o endereço do postgreSQL esteja em execução, pare-o com o comando sudo service postgresql restart, caso aconteça o erro de 'endereço 0.0.0.0:5432 already in use' procure o **pid** do processo ouvindo essa porta com o comando sudo ss -nlp | grep 5432 e execute sudo kill -9 <**pid**>

### 2 Execução manual

+ 2.1 Configurando o PostgreSQL
  - Instale o PostgreSQL, caso ainda não o tenha na sua máquina. Tendo-o instalado, precisamos criar o database e role da aplicação. Para isso, execute o comando sudo -u postgres psql, isto abrirá o console psql no terminal, depois, execute os comandos:
    ```
    CREATE ROLE desafiopontotel WITH SUPERUSER CREATEDB CREATEROLE LOGIN ENCRYPTED PASSWORD 'alphavantage';
    CREATE DATABASE alphavantage OWNER desafiopontotel; 
    ```
    Isso criará o database da aplicação com o login/senha configurados de acordo com o arquivo config.ini que controla parâmetros de configuração da aplicação. Após criar o database, altere no arquivo config.ini a linha:
    ```
    location = database:5432 
    ```
    para:
    ```
    location = localhost 
    ```
    Observação: o valor **database:5432**(valor padrão para o endereço do serviço PostgreSQL da aplicação) deve ser usado caso a aplicação seja executada com o Docker Compose, para execução manual esse valor tem de ser substitúido para **localhost**. 

+ 2.2 Configurando o Python
  - Para executar manualmente a aplicação em Python, primeiramente faça a instalação do Python 3.7 e do gerenciador de pacotes pip. Após instalados, vá para a pasta /Back-end na pasta fonte do projeto e execute o comando python3.7 -m pip install requirements.txt. Instaladas todas as dependências, podemos executar a aplicação com o comando python3.7 application.py, contudo, a aplicação precisa se comunicar com o PostgreSQL para rodar, portanto, certifique-se de que o passo 2.1 foi concluído com sucesso.

+ 2.3 Configurando o Angular
  - Primeiro faça o download e instalação do [Angular-CLI](https://cli.angular.io/), caso ainda não o tenha instalado em sua máquina. Depois instale o [Node.js](https://nodejs.org/en/). Vá para a pasta /Front-end e execute o comando **npm-install**, que fará o download/instalação das dependências necessárias para subir a aplicação Angular. Execute então **ng serve** ainda na pasta /Front-end, assim a aplicação client será executada na porta 4200(porta padrão do Angular).
  
Feitos os 3 passos anteriores, a aplicação poderá ser acessada pelo endereço http://localhost:4200, em que estará rodando a aplicação Angular que por sua vez se comunica com o Python + PostgreSQL.

---

## Testes

Dentro da pasta /tests localizada em /Back-end/modules existe um arquivo feito com pytest para teste unitário de alguns casos dos endpoints da API. Para executar esse script basta usar o comando pytest estando dentro da pasta com o arquivo de teste. O pytest cuida de fazer o processo automaticamente.

---

## Conhecimentos adquiridos e dificuldades encontradas

* Aprender a consumir uma API de forma assíncrona em Python.
* Criar uma interface assíncrona para comunicação do Python com o PostgreSQL.
* Configurar a aplicação para ser executada com Docker.
* Interligar as 3 partes da aplicação em containers distintos.

---

#### Screenshots da aplicação

![Tela de exibição do Ibovespa](https://i.imgur.com/2B9WbdS.png)
  *Tela de exibição do Ibovespa do dia*

---  
  
![Tela de cotações de empresas](https://i.imgur.com/l82q7wI.png)
  *Tela de cotações das 10 maiores empresas brasileiras. Na coluna de **Ações**, o botão à esquerda obtém a cotação atual da empresa selecionada e o botão à direita envia esses dados para serem persistidos em banco.*
  
###### Considerações finais

+ Todos os dados acerca das cotações de empresas, bem como o valor do Ibovespa são fornecidos em tempo real pelas API's do [Alpha Vantage](https://www.alphavantage.co/)
+ A lista das 10 maiores empresas brasileiras de 2019 foi retirada da **Forbes Global 2000** disponível no endereço: <https://forbes.uol.com.br/listas/2019/05/global-2000-20-maiores-empresas-brasileiras-de-capital-aberto-de-2019/#foto11> .
