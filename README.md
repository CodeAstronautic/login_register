# login_register
Let’s start with the prerequisites for this tutorial. In order to follow the tutorial step by step, you’ll need a few requirements, such as:

Basic knowledge of Python,
Working knowledge of Django (django-admin.py and manage.py),
A recent version of Python 3 installed on your system (the latest version is 3.7)
We will be using pip and venv which are bundled as modules in recent versions of Python so you don't actually need to install them unless you are working with old versions.

If you are ready, lets go started!

Creating a Virtual Environment
A virtual environment allows you to isolate your current project dependencies from the rest of packages installed globally on your system or in the other virtual environments. You can either use virtualenv which needs to be installed on your system or the venv module available as a module in recent versions of Python 3.

Go to your command terminal and run:

$ python -m venv env
Next, activate the virtual environment using:

$ source env/bin/activate
Note: please note that on Windows, you need to use source env/Scripts/activate in order to activate your virtual environment.
After activating the environment, you need to proceed by installing Django using pip:

$ pip install django
If the framework is successfully installed, you can now use the Django management commands to create and work with your project.

Creating a Django Project
Let’s now create the project using django-admin.py. In your terminal, run the following command:

$ django-admin.py startproject demoproject
Django has an ORM that abstracts dircet database operations and supports SQLite which is configured by default in the project so we’ll be using a SQLite database for this tutorial.

If you need to use PostgreSQL, MySQL or any other database management system, you’ll have to install it first then open the settings.py of your project and add the database address and credentials inside the DATABASES object.
