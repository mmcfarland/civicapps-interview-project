# Interactive coding exercise

## Overview

This repository contains the beginnings of a key/value database server.
During the interview, the candidate will pair with Azavea engineers to
extend the server's functionality. This server is available in both Python
and JavaScript variants. The goal of this project is to simulate a set of
real-world tasks that will allow candidates to demonstrate the skills and
knowledge required for this role with a project of limited scope.

For more information on the web frameworks used, please refer to the
[Flask](https://flask.palletsprojects.com/en/1.1.x/) and
[Restify](http://restify.com/docs/home/) documentation. Also, many thanks to
[The Recurse Center](https://www.recurse.com/pairing-tasks) for providing the
inspiration for this exercise.

## Getting started

### Dependencies

The runtimes and libraries required to run each server are encapsulated within
container images. The instructions used to create those container images are
contained within this repository. To run the servers, you must have the
following dependencies installed:

- Docker 19.03+
- Docker Compose 1.24+

### Running the server

To run either server, navigate to the appropriate directory and bring the
service up with Docker Compose.

```shell
$ cd python
$ docker-compose up

. . .

$ cd javascript
$ docker-compose up
```

After this, the server will be running at <http://localhost:8080>.

### Setting up the development environment

Create a development environment that is conducive for the candidate to edit
and exercise their code. Ensure that all key components are in working order
before the interview begins.

1. [Visual Studio Code](https://code.visualstudio.com/download) with Python
   and JavaScript syntax highlighting
2. [Postman](https://www.getpostman.com/downloads/) or other graphical HTTP
   request tool
3. Web browser and internet connection
4. Command line terminal
5. Running server, in the language preferred by the candidate

## The interview

### Baseline implementation

The baseline server implementation has 3 endpoints:

- `/`: serves a welcome message and confirms the site is running
- `/set/?{key}={value}`: persists the key and value to an in-memory data structure
- `/keys/`: returns all keys and values persisted, delimited by a newline

The server does not have any known bugs or "gotchas" that are intended to
trip up or confuse the candidate. Instead, it has a few intentional areas
for improvement. Notably:

- The data is stored in-memory and therefore not persisted when auto-reloading the
  server after source files change.
- There is no explicit error handling.
- No ability to fetch individual keys.
- Not all methods restrict the HTTP verb as appropriate (e.g., `/set` uses `GET`).

The interview process should be structured around making incremental
improvements to the server and evaluating the candidate's ability to
understand the codebase and requirements, and perform the actual
implementation. Aim to guide the exercise in a way that gives you insight
into the candidate's skills and behaviors. For example, if the candidate is
getting stuck and is unable to follow your prompts to make progress, note it
and move on to another feature requirement.

The candidate is allowed to use whatever resources would be available to them
during the normal course of a work day. For example, looking up
documentation, making use of Stack Overflow, and asking the interviewer
questions are all acceptable. How they go about doing this will provide
valuable signals for the interview.

### Programming tasks

#### 1. General understanding

Before the first task, ask the candidate to evaluate the code in the main
server source code file. Invite them to ask you questions or otherwise
clarify any confusing elements. Allow them to scan the framework documentation
or explore the `Dockerfile` that creates the server.

##### Evaluation criteria

1. Are they able to familiarize themselves with a foreign codebase effectively?
2. Do they understand the basics of HTTP and map those concepts correctly to
   the framework?
3. Do they structure their questions clearly and specifically?

#### 2. Persist the key/values between process restarts

If the server process crashes or is reloaded after a code change, the
in-memory data structure is reset. Have the candidate persist keys/values in
a way that makes them resilient to server restarts. A common approach is to
write the contents to disk and reload it when the service starts, but allow
the
candidate to suggest possible implementations.

##### Evaluation criteria

Does the candidate:

1. Understand why the in-memory structure works, and why it is empty after a
   restart?
2. Understand basic I/O concepts (e.g., line based I/O vs. entire file, text encoding, etc.)?
3. Discuss tradeoffs between the different options of when to save and load
   data? Depending on their implementation, this could involve:
   - Having two sources of truth: file persisted to disk and an in-memory data structure
   - Performance implications of reading and writing on every request vs. at startup and shutdown
4. Understand the lifecycle of a server: process re/start, request, response and where
   in the framework they can respond to each?
5. Handle boundary cases (e.g., starting with no keys loaded, loading 100MM keys)?
6. Allow duplicate keys? The in-memory dictionary structure updates existing keys.

#### 3. Fetch key by name

Add a new endpoint that returns the value of the provided key.

##### Evaluation criteria

Does the candidate:

1. Understand how to add a new route and function?
2. Use sensible names for the path and the key?
3. Demonstrate understanding of the methods for encoding the query in the
   request? (e.g., query string param vs path argument vs. form encoded `POST`)
4. Handle common boundary cases, like non-existing keys and null keys?
5. Are they concerned about sanitizing user input?

#### 4. Filter keys by prefix

Add or extend an endpoint to return a list of all keys and values that match the
provided prefix. For example, the prefix `na` would match `name` and `nation`.

As an extension, have them sort the returned list in lexicographical key order.

##### Evaluation criteria

1. Does their method of filtering keys balance readability and performance?
2. How would the filter perform on a very large number of keys, are they aware of
   the design decision?
3. How is an empty result set represented?
4. Do they consider case sensitivity?

#### 5. Delete key by name

Delete the entry for a key provided. This will likely be a new endpoint, but allow
the candidate to suggest the implementation.

##### Evaluation criteria

1. This is similar to the fetch endpoint added above, did they retain knowledge
   and improve the speed at which they could add this feature?
2. Did they select an appropriate HTTP verb for this operation?
3. Is the entry deleted from both the in-memory and on disk database representations?

#### Additional tasks

In the unlikely event that the candidate makes it through all the previous tasks in
the alloted time, ask the candidate to suggest other improvements they would make
and engage in conversations about their suggested implementation.

## General evaluation criteria

Here are additional high level considerations, taken from [The Software Engineer's Guide to
Interviewing](https://blog.usejournal.com/the-software-engineers-guide-to-interviewing-software-engineers-980bbfdb4006):

1. Can they write code?
2. Can they make sensible design decisions?
3. Can they work well with other people?

### Common anti-patterns

- **Poor communicator**: It's unclear how they reached their conclusion, or they
  talk at length without answering a direct question.
- **Poor code quality**: Poor implementation choices, poorly organized or
  formatted.
- **Doesn't explore the problem before jumping into a solution**: Doesn't
  validate assumptions or identify edge cases up front.
- **Broad gaps in knowledge**: Large areas of knowledge that are only shallowly
  understood.
- **Not self-motivated**: Needs excessive instruction to move to the next step.
- **Not detail oriented**: Misses obvious edge cases, didn't understand the problem initially.
- **Veers into the weeds**: Suggests endless possible solutions, but
  struggles picking one to implement. Distracted by low priority details.
- **Solutions are overly complicated**: Makes up unnecessary requirements or
  assumptions, over-engineers or does not prioritize readability.
- **Doesn't interact with the interviewer**: Does not engage in a constructive or collaborative manner.
- **Presents a condescending attitude**: Doesn't display desirable engineering qualities like humility and empathy.
- **Unnecessarily dogmatic**: Adheres to unsupported or unjustified opinions.
