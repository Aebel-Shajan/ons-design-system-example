/**
 * @fileoverview This file sets up an Express server with Nunjucks as the templating engine.
 * It configures Nunjucks to use the "views" directory, enables autoescaping, and watches for changes.
 * The server serves static resources from the "public" folder and renders an index page with a name variable.
 * 
 * @requires express
 * @requires nunjucks
 */
const express = require('express');
const nunjucks = require('nunjucks');

const app = express();
const port = 3000;

// Configure nunjucks to work with express
nunjucks.configure(
    [
        "views",
        "components"
    ],
    {
        autoescape: true,
        express: app,
        watch: true // So we don't have to keep running `node server.js`
    }
)

// Use static resources in public folder
app.use(express.static('public'))

// Renders the index page with a name variable.
app.get('/', function(req, response) {
    response.render('index.njk', {Name: "Aebel"}); // express infers the .njk file extension
});

// Starts the server and listens on the specified port.
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});