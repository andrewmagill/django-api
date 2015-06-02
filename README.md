## Django REST framework tutorial

You may want to work through the [tutorial] [tutorial] yourself, or take a look at the actual [code] [code] from the tutorial.

#### Create new [virtualenv] [virtualenv]:

    virtualenv env
    source env/bin/activate

#### Install requirements:

    pip install django
    pip install django-rest-framework
    pip install pygments

#### Clone my repo:

    git clone https://github.com/andrewmagill/django-api.git

#### Create local_setting with SECRET_KEY:

    cd django-api
    touch serialization/local_settings.py
    echo "SECRET_KEY = 'bigsecret'" >> local_settings.py

#### Run:

    ./manage.py runserver

[tutorial]: http://www.django-rest-framework.org/#tutorial
[code]: https://github.com/tomchristie/rest-framework-tutorial
[virtualenv]: https://virtualenv.pypa.io/en/latest/index.html
