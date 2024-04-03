Simple Ecommerce website built using Django 5.0.3, Python 3.10.0

Features:
    1.Home page that shows all the products (/index)
    2.Home page has Pagination that only shows 4 products per page
    3.Search functionality to search any products
    4.Add to cart functinality to add products you liked
    5.Checkout page to do the payment and place your order

Screenshot:


Steps:
    1.clone the project and install the requirements 
        python -m pip install -r requirements.txt
    2.do the migrations to migate the models 
        python manage.py makemigrations
        python manage.py migrate
    3.to run the django server
        python manage.py runserver
    4.access ecommerce website in  http://127.0.0.1:8000/index
