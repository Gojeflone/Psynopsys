# Pysnopsys: Psychogical Synopsis System

This system aims to accurately detect signs of depression in people through their social media posting, as well as user input in the form of a text box. Psynopsys uses a machine learning API called "Tone Analyzer" from IBM's Bluemix platform to detect emotions in text, and we expand on those results by putting them together to match signs of depression, and risk of suicide into an accessible way for everyone to use.

## Built Using

*[IBM Bluemix](https://www.ibm.com/cloud-computing/bluemix/) - The Cloud Platform Used

*[Tone Analyzer](https://www.ibm.com/watson/services/tone-analyzer/) - Tone Analyzer

*[Heroku](https://dashboard.heroku.com/apps) - Heroku


## node-js-getting-started

A barebones Node.js app using [Express 4](http://expressjs.com/).

This application supports the [Getting Started with Node on Heroku](https://devcenter.heroku.com/articles/getting-started-with-nodejs) article - check it out.

## Running Locally

Make sure you have [Node.js](http://nodejs.org/) and the [Heroku CLI](https://cli.heroku.com/) installed.

```sh
$ git clone git@github.com:heroku/node-js-getting-started.git # or clone your own fork
$ cd node-js-getting-started
$ npm install
$ npm start
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```
$ heroku create
$ git push heroku master
$ heroku open
```
or

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Documentation

For more information about using Node.js on Heroku, see these Dev Center articles:

- [Getting Started with Node.js on Heroku](https://devcenter.heroku.com/articles/getting-started-with-nodejs)
- [Heroku Node.js Support](https://devcenter.heroku.com/articles/nodejs-support)
- [Node.js on Heroku](https://devcenter.heroku.com/categories/nodejs)
- [Best Practices for Node.js Development](https://devcenter.heroku.com/articles/node-best-practices)
- [Using WebSockets on Heroku with Node.js](https://devcenter.heroku.com/articles/node-websockets)
