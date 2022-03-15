# Healthcare-Platform
Platform used to monitor paitents at home or in the hospital. Paitents and medical practitioners will be able to access a database with user information and monitor the status of medical devices. 

## Dependencies
pip install django
pip install djangorestframework

## Running the Django Server
python manage.py runserver
<br>
On ec2 instance:
<br>
python3 manage.py runserver 172.31.85.185:8000 
<br>
Reach the server using http://{public IP}:8000
<br>
## Relational Database Schema
Django relational database with a user's UID as the primary key that links a majority of the tables
![image](https://user-images.githubusercontent.com/55994268/155548655-1ab4a1ee-7a20-4b61-bb7a-e80aef9e9078.png)
