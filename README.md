# ReleCloud sample

This is a sample Django project used for [Beginner's Series: Django](https://aka.ms/BeginnersSeriesDjango). It's a fictitious company offering tours to space.

## Install and startup steps

1. Clone the repository

    ```bash
    git clone https://github.com/microsoft/beginners-django
    cd beginners-django/demo-code
    ```

1. Install the prerequisites

    ```bash
    # Linux/macOS/BASH
    python3 -m venv venv
    source ./venv/bin/activate
    pip install -r requirements.txt

    # Windows
    python -m venv venv
    .\\venv\\scripts\\activate
    pip install -r requirements.txt
    ```

1. Open the project in Visual Studio Code

    ```bash
    code .
    ```

2. Define your Dependencies in requirements.txt
   Wenn in **Production deployed** wird, ist es wichtig, dass requirements.txt vollständig ist, weil während des deployments alles remote installiert werden muss.

   
   ```
    django
    django-crispy-forms
    crispy-bootstrap4
   ```



## Crispy-Forms und -Bootstrap4

Install this plugin using pip:

    $ pip install crispy-bootstrap4
Usage
You will need to update your project's settings file to add crispy_forms and crispy_bootstrap4 to your projects INSTALLED_APPS. Also set bootstrap4 as and allowed template pack and as the default template pack for your project:

    INSTALLED_APPS = (
        ...
        "crispy_forms",
        "crispy_bootstrap4",
        ...
    )

    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
    CRISPY_TEMPLATE_PACK = "bootstrap4"


## SQLite database

For this sample, the SQLite database is included. Typically this would be ignored in the .gitignore file. To ensure a working site with data was provided, the starting database is included.