FROM node:latest

# 🔧 Solución para el error de OpenSSL
ENV NODE_OPTIONS=--openssl-legacy-provider

WORKDIR /frontreact
COPY . .

RUN npm install --silent
RUN npm install react-scripts@3.0.1 -g --silent



EXPOSE 3000

#RUN npm run build
CMD npm start