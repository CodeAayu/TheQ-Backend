# The-Q(Backend Server)

## Idea behind this

As we have seen a lot these days that the queues to everything are way much longer than are supposed to be and people have to wait for hours in the queues standing there physically to reach the point of service, even when the people know that their turn will come up hours later because of non-believing nature of us, we stand there. So, to remove this Physical need to stand in the queues, we created this The-Q.
The main idea behind The-Q was very simple yet very fascinating. We tried to digitize the queues where an organiser of any event creates an event and the participant can get into the queue using our application, without explicitally standing there. So, a participant can also track whether his/er turn has come/is near or not on this app only and organiser too can coordinate their events properly by using the data about the number of participants.

## Technologies used(for geeks only :P)

Now to tackle this, we took the support of Django/Python3.6 for our server side(Backend) programming and React native for our client side(frontend). We rested on these two frameworks for this project because of only one main reason. They both let you do things in a secure, fast and effective way and you don't need to reinvent the wheel. Specifically Django was used as it can handle multiple requests and collaborate with database seemlessly with all the RESTful APIs. The routing in Django is pre-defined in the best state possible and using the Object Oriented Programming practices in Python3.6 in Django helped us a lot in speeding up the data transfer from our MySQL server. On the part of React Native, we wanted a mobile app  that we can create and React Native lets us do that in a very effective manner by giving us a lot many pre-built libraries of JavaScript. We chose this over Android Studio because of it's hot reloading feature and cross-platform nature. In just one click, you get both - iOS and Android packages generated.

## How to?

The-Q has two main parts, Backend and Frontend, both of which are required to run individually. 
Both the parts are in seperate directories.  We are using MySQL database where we store all our data about events, credentials, dynamic queues and all that stuffs. To make it up and running, clone the backend directory in a system. 
- Create a database in your SQL server(preferably MySQL). 
- Edit the settings.py (the file in the root directory of Backend directory) as per your need. 
- Change the Databse credentials, `Base URL`(if local host exposes to http/s, like using ngrok) and `static URL` (if you require to save binary files like images in other directories).
- Create a virtual environment of Python3.x where x >=6 and activate it.

```
python3 -m venv name_of_virtualenv
source name_of_virtualenv/bin/activate
```

Now install all the dependencies in the requirements.txt file by

`pip install -r requirements.txt`

Migrate all the models to database using the following commands.

```
python manage.py makemigrations
python manage.py migrate
```

It is advised to create a superuser for your web-app. You can do that using the following.

`python manage.py createsuperuser`

Now you are ready to host the server on the endpoints you like, to run it locally, do the following.

`python manage.py runserver <port_number>`

## Scope and use cases

The scope to this is boundless but as we are still students and we made this first prototype in a 36-hour Hackathon, Hack-A-BIT, so we made this in our best interest, Reality Show Auditions.
As described above we know what all thinsg can be achieved with this product, we wish to reduce the kms of long queues outside reality TV auditions like Indian Idol Jr (our idea generator :D).
But the scope is not limited to this. We can implement this in Corporate Lunches, Govt. offices like DTO, Passport offices, Airport checkins and obviously Reality show auditions. We can (which we will. We didn't because of time constraint) also incorporate several Data driven features in this where one can get an estimated time to get to service counters, webhooks to devices for timed notifications, etc.

## Copyright

All wrongs reserved! Use this code as much as possible and contribute to the project(https://github.com/hackabit18/Geeks_and_Freaks). We are always open to suggestions and Pull requests (preference :P). The project is yet to be completed for the frontend where we require the OSS community's support the most.
On a side note, if you are using this source to create your own version of The-Q, make sure to give proper credits to the original developers of Geeks_and_Freaks from [Cyber Labs](https://www.fb.com/labscyber) (Cyber Society of IIT(ISM)-Dhanbad).

See the file "LICENSE" for information on the history of this software, terms & conditions for usage, and a DISCLAIMER OF ALL WARRANTIES.

###### Note

Special Thanks to POSTMAN which let us test our APIs effectivley so as to design them properly without the frontend up and running.
