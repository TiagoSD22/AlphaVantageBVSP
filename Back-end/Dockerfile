FROM python:3.7.3
# Informação dessa docker image
LABEL version="0.1" description="API criada para o Desafio da Empresa Ponto Tel" maintainer="Tiago Siqueira Dionizio" email="tiagosdionizio@gmail.com"

# Endereço da API
ENV APP=/usr/src/app

# Criando para a aplicação
RUN mkdir -p $APP

# Copiando todos os arquivos para dentro do container
COPY . $APP

# Diretório base da aplicação
WORKDIR $APP

# Instalando dependências
RUN python3.7 -m pip install -r requirements.txt

# Porta para subir a API com o Sanic
EXPOSE 5000

# Executando a aplicação
CMD python3.7 application.py
