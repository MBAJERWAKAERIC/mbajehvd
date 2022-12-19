const express = require('express');

const app = express();

app.get('/', (request, response) => response.send("Node test and npm"));

app.listen(8080);