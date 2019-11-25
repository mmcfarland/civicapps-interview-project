# Interactive coding exercise

## Overview

This repository contains the beginnings of a key/value database server. During the interview, you will pair with another engineer to extend the server's functionality. This server is available in both Python and JavaScript variants.

For more information on the web frameworks used, please refer to the [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [Restify](http://restify.com/docs/home/) documentation. Also, many thanks to [The Recurse Center](https://www.recurse.com/pairing-tasks) for providing the inspiration for this exercise.

## Getting started

### Dependencies

The runtimes and libraries required to run each server are encapsulated within container images. The instructions used to create those container images are contained within this repository. To run the servers, you must have the following dependencies installed:

- Docker 19.03+
- Docker Compose 1.24+

### Running the server

To run either server, navigate to the appropriate directory and bring the service up with Docker Compose.

```shell
$ cd python
$ docker-compose up

. . .

$ cd javascript
$ docker-compose up
```

After this, the server will be running at <http://localhost:8080>.

## Enhancement ideas

- Add ability to sort key listing lexicographically in ascending or descending order.
- Add ability to filter keys by some prefix query.
- Add ability to delete keys.
