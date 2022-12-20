const express = require('express');

const app = express();

app.get('/', (request, response) => response.sendFile(__dirname + "/index.html"));

app.listen(8080);