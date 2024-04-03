<h1>Simple Ecommerce website built using Django 5.0.3, Python 3.10.0</h1>

<h2>Features: </h2>
   <ul>
    <li>Home page that shows all the products (/index)</li>
    <li>Home page has Pagination that only shows 4 products per page</li>
    <li>Search functionality to search any products</li>
    <li>Add to cart functinality to add products you liked</li>
    <li>Checkout page to do the payment and place your order</li>
   </ul> 

<h2>Screenshot:</h2>

<h3>Home Page</h3>

![indexpage](https://github.com/Dinesh294/ecommercesite/assets/84972612/a708f7b7-d6e5-4c18-9ba3-5d09d1fa5a7d)

<h3>Cart</h3>

![cartpage](https://github.com/Dinesh294/ecommercesite/assets/84972612/764a9e7b-e017-4b91-bd8e-c1623e8b8525)

<h3>Checkout Page</h3>

![checkoutpage](https://github.com/Dinesh294/ecommercesite/assets/84972612/aa532f80-042e-4481-ad94-e3248e83c6f3)

<h2>Steps:</h2>
    <ul>
    <li>clone the project and install the requirements <br>
        &emsp; python -m pip install -r requirements.txt </li>
    <li>do the migrations to migate the models <br>
        &emsp; python manage.py makemigrations <br>
        &emsp; python manage.py migrate </li>
    <li>to run the django server <br>
        &emsp; python manage.py runserver </li>
    <li>access ecommerce website in  http://127.0.0.1:8000/index </li>
    </ul>
