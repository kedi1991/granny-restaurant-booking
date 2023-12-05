
# Granny's restaurant booking

This application will help the restaurant owner manage clients efficently and provide adequate space to those who have reserved a table for a meal. With this application, the restaurant owner can allocate resources (Human resource, chairs, and security) based on the bookings that have been made. This will in turn allow for better budgeting and customer care for clients.
![Image of the home page](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1686133085/state_1_angjix.jpg)

## Deployment images
Sample images of the different pages on mobile screen (Tested using Samsung S9+)
![Homepage](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1701741695/IMG-20231205-WA0002_cykvbd.jpg)
![My reservations page](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1701741695/IMG-20231205-WA0005_vf85fl.jpg)
![Edit reservation](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1701741695/IMG-20231205-WA0003_jiquur.jpg)


### Project wireframes
![restaurant card](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1701483661/granny_restaurant/resturant_card_lkkl2m.png)
![booking page](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1701483669/granny_restaurant/booking_form_a0jlyu.png)

### Start of the project

![mockup for different screen sizes](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1686133085/state_2_pe8x6c.jpg)
![mockup for different screen sizes](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1686133085/state_3_aqughl.jpg)

### Final stage of the project

![mockup for different screen sizes](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1686133799/resva_q0c2lf.jpg)
![mockup for different screen sizes](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1686133799/resvahhh_t8gih9.jpg)
![mockup for different screen sizes](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1686133085/state_2_pe8x6c.jpg)


## User stories
1. As a site admin , I want to add table configurations so that a client can make a choice.
2. As a site admin, I want to delete a table configuration so that a client can choose only available options
3. As a site user, I want to view all table co figurations so that I can make a choice
4. As an authenticated user, I want to make a reservation so that I can have a meal
5. As an authenticated user, I want to delete a reservation so that the restaurant can offer the same slot to another client
6. As an authenticated user, I want to edit a reservation so that I have a right setup for a group meal

## Code validation
No validations run

## Testing steps
1. Create test classes with naming convention "test_<classname>"
2. Write a fail test case 
3. Run the test case using the command ```python3 manage.py test```
4. Edit the test case until it passes the test.
5. Generate a coverage report using the command ```coverage run --source=<app_name> manage.py test``` to show the extent of testing for the entire application. A sample test case and coverage report is shown below.

#### Sample testcase
![Sample test case run](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1701736917/test_case_result_uoo2cz.png)
#### Sample coverage report

![Sample coverage report](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1701736917/coverage_report_yl9m6q.png)

## Models
1. Booking. 

This is the a representation of the reservation made at the restaurant 

| Attribute | Detail |
|-----------------|-----------------|
| Seat_code (PK)   | Code of the seat (table). This is created by the site admin only   |
| Seat_desc | Brief explanation of the seat/ table configuration    |
| Seat_persons    | Number of occupants for which the table has been reserved  |
| Seat_max  | Maximum number of occupants for the table  |
| Seat_image   | Image representation of the table   |



2. Seat.
This respresents the actual table with a predefined capacity of occupants.


### Seat configurations
1. 2 seater
2. 4 seater
3. 8 seater
4. 16 seater

| Attribute | Detail |
|-----------------|-----------------|
| booking_code (PK)   | Code of the seat (table)  |
| booking_client_name | Name of the online user/ client making the reservation    |
| booking_client_phone    | Phone contact of the client  |
| booking_client_email  | Email of the client  |
| booking_date   | Date on which the client would like to have a meal at the restaurant  |


## Project deployment process
1. Commit all code cnages to github.
2. Create Heroku account using the link https://heroku.com. Heroku will be used to host the application remotely.
3. Install postgres using ```pip3 install psycopg2-binary```
4. Install the webserver - gunicorn using the command ```pip3 install gunicorn```
5. Create an app in the heroku account above and give it a name.
6 On https://elephantsql.com, create a free account and a database instance of type 'Tiny turtle'. Remember to copy the database URL.
7. Head over to the app created in Heroku in step 5, and choose settings, reveal config vars, and add the variable DATABASE_URL. Set it to the database URL in step 6 above.
8. In the Gitpod termincal, install the databse package using the command ```pip3 install dj-database-url```
9. Refreeze the requirements file using the command ```pip3 freeze --local > requirements.txt```
10. In the settings.py file, replace the deafult SQLLite database reference with that of ElephantSQL. this will allow us to persist and retain any data in remote database.
11. Create a Procfile at the root of the project workspace (outside all folders) and add the command ```web: gunicorn django_todo.wsgi:application``` in the file. This will tell Heroku how to run the app.
12. Frome Heroku, run the app. This will display an application error caused by disallowed hostname of the heroku app. To correct this, copy the URL and add it as a new variable ```ALLOWED_HOSTS``` in the Heroku app settings.
13. The application should run without any interruption :)


## Technologies used:
- HTML
- CSS
- JS
- Python (Django framework)
## Libraries
- asgiref 3.6.0
- cloudinary 1.33.0
- dj-database-url 0.5.0
- dj3-cloudinary-storage 0.0.6
- Django 3.2.19
- django-allauth 0.54.0
- django-crispy-forms 1.14.0
- gunicorn 20.1.0
- oauthlib 3.2.2
- psycopg2 2.9.6
- pydantic 1.10.8
- PyJWT 2.7.0
- python3-openid 3.2.0
- pytz 2023.3
- requests-oauthlib 1.3.1
- sqlparse 0.4.4


## Future changes
1. Add notifications (messaging) to the UI
2. Block duplicate bookings on the same day


##  Credits
1. CI mentor: Harry Dhillon for the good guidance (Previous Mentor)
2. Thanks to the strong slack community for the assistance


