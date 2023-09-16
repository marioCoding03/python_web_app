# python_web_app
This is my first ever github repository which is a small web application in python that let's you login or register as a user. Nothing fancy at all, but this is what got me started in programming. 
Thank you for reading! :)

Step 1:

    Set Up your Linux(Ubuntu) Server

Step 2 - Setup Apache2:

    sudo -s
    apt update
    apt install apache2 -y
    apt install git -y
    apt-get install libapache2-mod-wsgi-py3 -y
    ufw allow 'Apache'
    rm -r /var/www/html
    git clone https://github.com/BigBrainer007/WebPage.git /var/www/WebPage
    chmod +x /var/www/WebPage/SSL-gen.sh
    mv /var/www/WebPage/basic-app.conf /etc/apache2/sites-available
    a2dissite 000-default.conf
    a2ensite basic-app.conf
    a2enmod ssl
    a2enmod wsgi

Step 3 - Setup the Virtual Enviroment:

    sudo -s(if not already in super-user)
    sudo apt update
    sudo apt install pip -y
    apt install pipenv -y
    exit(super-user)
    cd /var/www/WebPage
    pipenv install Pipfile

Step 4 - Setup the Database:

    python3
    from app import db
    db.create_all()
    exit()
