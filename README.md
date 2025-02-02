# Nunjucks tutorial

Repository containing example code to set up a web application using ons-design-system Nunjucks components.




## Setup
To set up the project, follow these steps:

0. **Clone the repository**:
    ```bash
    git clone https://github.com/aebel-shajan/ons-design-system-example.git
    cd ons-design-system-example
    ```

### Python-Flask-Jinja setup
<details>
<summary>Python-Flask-Jinja setup</summary>

1. **CD into python-jinja2**
    ```bash
    cd python-jinja2
    ```

2. **Setup virtual environment**:
    ```bash
    python3 -m venv .venv
    ```
    On MacOs/Linux:
    ```bash
    source venv/bin/activate
    ```
    On Windows:
    ```bash
    .\venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install and unzip ons-design-system components & layout templates**
    ```bash
    python download_ons_design_system.py
    ```

5. **Run the Flask application**:
    ```bash
    flask run
    ```

6. **Open your browser** and navigate to `http://0.0.0.0:8080` to see the application running.

7. **Make changes** to the code and see them reflected in real-time, thanks to the Flask development server.

#### PIP packages used
Library | Description
-|-
flask | A lightweight WSGI web application framework in Python.
jinja2 | A full-featured template engine for Python.

</details>


### NodeJS-Express-Nunjucks setup
<details>
<summary>NodeJS-Express-Nunjucks setup</summary>

1. **Install node**:
    https://nodejs.org/en

2. **CD into js-nunjucks**
    ```bash
    cd js-nunjucks
    ```

3. **Install dependencies**:
    ```bash
    npm install
    ```

4. **Run the development server**:
    ```bash
    npm run dev
    ```

5. **Open your browser** and navigate to `http://localhost:3000` to see the application running.

6. **Make changes** to the code and see them reflected in real-time, thanks to `nodemon`.

#### NPM packages used:
Library | Description
-|-
node | A JavaScript runtime built on Chrome's V8 JavaScript engine.
express | A minimal and flexible Node.js web application framework that provides a robust set of features for web apps.
nunjucks | A rich and powerful templating engine for JavaScript.
ons-design-system | Contains nunjucks components and layouts to import and use.
nodemon | A utility that monitors for any changes in your source and automatically restarts your server.

</details>


## Links

| Name | Link |
|------|------|
| ONS Design System | https://service-manual.ons.gov.uk/design-system |
| Flask Quickstart | https://flask.palletsprojects.com/en/stable/quickstart/#rendering-templates |
| Jinja Basics | https://jinja.palletsprojects.com/en/stable/api/#basics |
| Express Hello World | https://expressjs.com/en/starter/hello-world.html |
| Nunjucks Templating | https://mozilla.github.io/nunjucks/templating.html |