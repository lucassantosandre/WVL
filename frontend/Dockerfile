FROM node:16

WORKDIR /app

COPY package.json yarn.lock ./
RUN yarn install --network-timeout=300000

COPY . .

EXPOSE 3000

CMD ["yarn", "start"]
