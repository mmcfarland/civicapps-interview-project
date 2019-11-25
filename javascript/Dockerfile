FROM node:lts-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN yarn add --tilde \
    restify@8.4.0 \
    nodemon@1.19.4 

ENTRYPOINT [ "npx" ]
CMD [ "nodemon", "main.js" ]
