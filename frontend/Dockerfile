# ETAPA 1: Construcción (Build)
FROM node:18-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# ETAPA 2: Producción (Nginx)
FROM nginx:alpine
# Copiamos los archivos compilados de la etapa anterior
COPY --from=build /app/dist /usr/share/nginx/html
# Copiamos nuestra config de Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /etc/nginx/certs
COPY certs/nginx.crt /etc/nginx/certs/
COPY certs/nginx.key /etc/nginx/certs/

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]