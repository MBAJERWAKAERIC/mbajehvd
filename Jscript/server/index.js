const express = require('express');

const app = express();

app.get('/', (request, response) => response.sendFile("./index.html"));

app.listen(8080);