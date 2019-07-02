# Create image based on the official Node 10 image from dockerhub
FROM node:10

#RUN apt-get update -qq && apt-get install -y build-essential libpq-dev vim

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

#RUN npm audit fix

# Get all the code needed to run the app
COPY . /app/

#RUN npm rebuild node-sass --force

# Expose the port the app runs in
EXPOSE 4200 49153

# Serve the app
CMD ["npm", "start"]

