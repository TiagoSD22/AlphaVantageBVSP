# Create image based on the official Node 10 image from dockerhub
FROM node:10

# Image informations
LABEL version="0.1" description="API criada para testes do Alpha Vantage como desafio de seleção da empresa PontoTel" maintainer="Tiago Siqueira Dionizio" email="tiagosdionizio@gmail.com"

# Create a directory where our app will be placed
RUN mkdir -p /app

# Change directory so that our commands run inside this new directory
WORKDIR /app

# Copy dependency definitions
COPY package*.json /app/

# Install dependecies
#RUN npm install --save @angular-devkit/build-angular
RUN npm install -g @angular/cli
RUN ng update
RUN npm update

# Get all the code needed to run the app
COPY . /app/

#may be necessary in some cases..
#RUN npm rebuild node-sass --force

# Expose the port the app runs in
EXPOSE 4200 49153

# Serve the app
CMD ["npm", "start"]

