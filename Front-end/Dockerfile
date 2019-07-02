# Descrição:
# Dockerfile para build da imagem do cliente em Angular da API
# @Maintainer: Tiago Siqueira Dionizio <tiagosdionizio@gmail.com>

### STAGE 1: Build ###

# Imagem para Docker do cliente Angular
FROM node:10-alpine as builder

# Copiando o arquivo com as dependências do projeto localizadas nos arquivos package.json e package-lock.json
COPY package.json package-lock.json ./

## Armazenar a pasta node modules em outro lugar evitará chamadas desnecessárias do npm install a cada build da imagem

RUN npm ci && mkdir /ng-app && mv ./node_modules ./ng-app

WORKDIR /ng-app

COPY . .

## Build do cliente Angular em modo de produção

RUN npm run ng build -- --prod --output-path=dist


### STAGE 2: Setup ###

FROM nginx:1.14.1-alpine

## Copiando o arquivo de configuração default do nginx
COPY nginx/default.conf /etc/nginx/conf.d/

## Removendo o arquivo que direciona para a página do nginx, pois este é desnecessário para a aplicação (Ps: obrigado Nginx)
RUN rm -rf /usr/share/nginx/html/*

## Copiando os artefatos gerados durante o build do Angular para a pasta pública padrão do Nginx
COPY --from=builder /ng-app/dist /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
