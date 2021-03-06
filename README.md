# Healthcare-Platform
Platform used to monitor paitents at home or in the hospital. Paitents and medical practitioners will be able to access a database with user information and monitor the status of medical devices. 

## Dependencies
pip install django
<br>
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
![image](https://user-images.githubusercontent.com/55994268/158830069-e2ccaed3-35f9-4b04-8e81-75e217ee2762.png)

### Roles
Each user selects from a bank of predefined roles. They are defined as RID (integers mapped to roles)
![image](https://user-images.githubusercontent.com/55994268/158822023-e5bb9745-f28d-45de-b96b-7adc8129ce8e.png)

## Chatting Function
Users are able to chat within the application. By naviagting to the /chat url, a user can choose the chat room they want to enter and then begin communicating. This application uses Redis to store messages. When two or more windows of the same chat room are open, users can send messages back and forth that populate on both chat boxes.
