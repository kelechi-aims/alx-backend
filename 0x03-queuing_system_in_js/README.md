# Queuing System in JavaScript with Redis and Node.js
**By**: Johann Kerbrat, Engineering Manager at Uber Works

**Weight**: 1

##Overview
This project demonstrates how to build a queuing system in JavaScript using Redis and Node.js. It covers various aspects including running a Redis server, performing basic operations with the Redis client, using Redis with Node.js for basic operations, storing hash values in Redis, dealing with async operations, and using Kue as a queue system. Additionally, it shows how to build a basic Express app that interacts with a Redis server and a queue.

## Resources
**Read or watch**:

- [Redis quick start](https://intranet.alxswe.com/rltoken/8xeApIhnxgFZkgn54BiIeA)
- [Redis client interface](https://intranet.alxswe.com/rltoken/1rq3ral-3C5O1t67dbGcWg)
- [Redis client for Node JS](https://intranet.alxswe.com/rltoken/mRftfl67BrNvl-RM5JQfUA)
- [Kue](https://intranet.alxswe.com/rltoken/yTC3Ci2IV2US24xJsBfMgQ) deprecated but still use in the industry

## Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://intranet.alxswe.com/rltoken/7yh7c3Zyy1RyUsdwlfsyDg), **without the help of Google**:

- How to run a Redis server on your machine
- How to run simple operations with the Redis client
- How to use a Redis client with Node JS for basic operations
- How to store hash values in Redis
- How to deal with async operations with Redis
- How to use Kue as a queue system
- How to build a basic Express app interacting with a Redis server
- How to the build a basic Express app interacting with a Redis server and queue

## Requirements
- All of your code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
- All of your files should end with a new line
- A ```README.md``` file, at the root of the folder of the project, is mandatory
- Your code should use the ```js``` extension

## Required Files for the Project

```package.json```
<details>
<summary>Click to show/hide file contents</summary>
```bash

{
    "name": "queuing_system_in_js",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
      "lint": "./node_modules/.bin/eslint",
      "check-lint": "lint [0-9]*.js",
      "test": "./node_modules/.bin/mocha --require @babel/register --exit",
      "dev": "nodemon --exec babel-node --presets @babel/preset-env"
    },
    "author": "",
    "license": "ISC",
    "dependencies": {
      "chai-http": "^4.3.0",
      "express": "^4.17.1",
      "kue": "^0.11.6",
      "redis": "^2.8.0"
    },
    "devDependencies": {
      "@babel/cli": "^7.8.0",
      "@babel/core": "^7.8.0",
      "@babel/node": "^7.8.0",
      "@babel/preset-env": "^7.8.2",
      "@babel/register": "^7.8.0",
      "eslint": "^6.4.0",
      "eslint-config-airbnb-base": "^14.0.0",
      "eslint-plugin-import": "^2.18.2",
      "eslint-plugin-jest": "^22.17.0",
      "nodemon": "^2.0.2",
      "chai": "^4.2.0",
      "mocha": "^6.2.2",
      "request": "^2.88.0",
      "sinon": "^7.5.0"
    }
  }

```
</details>

```.babelrc```
<details>
<summary>Click to show/hide file contents</summary>
```bash
 
{
  "presets": [
    "@babel/preset-env"
  ]
}

```
</details>

### and…
Don’t forget to run ```$ npm install``` when you have the ```package.json```
