# Blog
## Author
Sandra Kinoti

# Description
This  is a flask application that allows writers to post blogs, edit and delete blogs. It also allows users who have signed up to comment on the blogs posted by other writers. It also allows a person to subscribe and receive email notifications everytime a new blog is posted by a writer in my platform.

## User Story

* A user can view the most recent posts.
* View and comment the blog posts on the site.
* A user gets an email alert when a new post is made by joining a subscription.
* Register to be allowed to log in to the application
* A user sees random quotes on the site
* A writer can create a blog from the application and update or delete blogs they have created.

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all blogs, Select between signup and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with blogs that have been posted by writers and be able to subscribe to the blog|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments template with your comment and other comments|
|Subscription | **Email Address**| Flash message "Succesfully subsbribed to Blog"|

## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  https://github.com/sandrakinoti16/blog
  ```
2. Move to the folder and install requirements
  ```bash
  cd Blog
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  python manage.py server
  ```
5. Testing the application
  ```bash
  python manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* [Python3.8](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at [sandrakinya6@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2022 **sandra kinoti**