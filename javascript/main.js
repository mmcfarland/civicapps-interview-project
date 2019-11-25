var restify = require("restify");

var server = restify.createServer();
server.use(restify.plugins.queryParser());

var DATA_STORE = {};

/**
 *  Serve up a welcome page at the root url
 */
server.get("/", function(req, res, next) {
  res.send("Hello, world. Looks like everything is working. You got this!", {
    "content-type": "text/plain"
  });
  next();
});

/**
 * Save key and value pairs from the query string.
 *
 * Try: http://localhost:8080/set?key=value
 */
server.get("/set/", function(req, res, next) {
  // Loop through each key in the query string and add it to our dictionary
  Object.entries(req.query).forEach(([key, value]) => {
    DATA_STORE[key] = value;

    // Log the values to the debug console
    console.log(`recieved ${key} with value of ${value}`);
  });

  // Let the client know the operation was successful
  res.send(`saved ${Object.keys(req.query).length} value(s)`, {
    "content-type": "text/plain"
  });

  next();
});

/**
 * Return all saved keys to the client.
 *
 * Try: http://localhost:8080/keys/
 */
server.get("/keys/", function(req, res, next) {
  if (Object.keys(DATA_STORE).length > 0) {
    const allValues = Object.entries(DATA_STORE).map(
      ([key, value]) => `${key}=${value}`
    );
    res.send(allValues.join("\n"), { "content-type": "text/plain" });
  } else {
    res.send("No keys have been set.", { "content-type": "text/plain" });
  }

  next();
});

server.listen(8080, function() {
  console.log("%s listening at %s", server.name, server.url);
});
