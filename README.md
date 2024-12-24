Django & React E-commerce Website.

Cloning the repository
--> Clone the repository using the command below :

git clone 
https://github.com/MariaL2000/Econmerce_store-D-R.git
--> Move into the directory where we have the project files :

cd django-ecommerce
--> Create a virtual environment :

# Create our virtual environment
python -m venv venv
--> Activate the virtual environment :

windows

venv\scripts\activate
linux

source venv/bin/activate
--> Install the requirements :

pip install -r requirements.txt
--> Migrate Database

python manage.py migrate
--> Create Super User

python manage.py createsuperuser
Running the App
--> To run the App, we use :

python manage.py runserver
