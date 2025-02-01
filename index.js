const express = require('express');
const nunjucks = require('nunjucks');

const app = express();
const port = 3000;

nunjucks.configure(
    "views",
    {
        autoescape: true,
        express: app,
        watch: true
    }
)

app.get('/', function(req, response) {
    response.render('index.njk', {Name: "Aebel"});
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});