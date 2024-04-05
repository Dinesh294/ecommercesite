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
<h3>This ecommerce django app is deployed in AWS EC2 instance and steps are below. </h3>

<h3>Home Page</h3>

![home_page](https://github.com/Dinesh294/ecommercesite/assets/84972612/f0aabe94-884e-4b8e-b117-393996e01429)


<h3>Cart</h3>

![cart_page](https://github.com/Dinesh294/ecommercesite/assets/84972612/d8c10af8-c6cd-49e9-ba29-ab32f0322846)


<h3>Checkout Page</h3>

![checkout_page](https://github.com/Dinesh294/ecommercesite/assets/84972612/08105c6a-18a4-49d0-afc4-741885a69801)


<h3>Admin Page</h3>

![admin_page](https://github.com/Dinesh294/ecommercesite/assets/84972612/ee5ff147-7e54-4e46-89a3-9fd5b7187379)


<h2>Deploy ecommercesite in EC2 instance:</h2>
      <h3>Create EC2 instance with Linux AMI and Security Group to allow SSH and custom TCP at port 8000 from anywhere and connect to EC2 instace and follow the below steps</h3>
      <h4>Install Python3 and Git:</h4>
      <ol>
      <li>sudo yum update</li>
      <li>sudo yum install python3</li>
      <li>sudo yum install python3-pip</li>
      <li>sudo yum install git</li>
      </ol>
      <h4>Clone the repo from git and create virtualenv:</h4>
      <ol>
      <li>git clone https://github.com/Dinesh294/ecommercesite.git</li>
      <li>cd ecommercesite</li>
      <li>python3 -m pip install virtualenv</li>
      <li>python3 -m venv django-venv</li>
      <li>source django-venv/bin/activate</li>
      </ol>
      <h4>Install requirements and django runserver:</h4>
      <ol>
      <li>python3 -m pip install -r requirements.txt</li>
      <li>python3 -m django --version</li>
      <li>python3 -m manage runserver 0.0.0.0:8000</li>
      </ol>  
      <h3>Access Django ecommerce site:</h3>
      <ol>
      <li>ec2-public-ip:8000/index</li>
      </ol>
   

<h2>Steps to clone and run the django app locally:</h2>
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
