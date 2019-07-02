# Descrição:
# Dockerfile para build da imagem do servidor em Python da API
# @Maintainer: Tiago Siqueira Dionizio <tiagosdionizio@gmail.com>

# Imagem base do container
FROM python:3.7.3

# Endereço do projeto
ENV APP=/usr/src/app

# Pasta padrão para a aplicação
RUN mkdir -p $APP

# Copiando todos os arquivos para dentro da pasta padrão
COPY . $APP

# Diretório base da aplicação
WORKDIR $APP

# Instalando dependências
RUN python3.7 -m pip install -r requirements.txt

# Porta para subir a API com o Sanic
EXPOSE 5000

# Executando a aplicação
CMD python3.7 application.py
