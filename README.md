# Cookin
Cookin is a site made for sharing recipes and food inspiration!
A place to find new favourite dishes or a place to spread your own personal favorite recipes with the world!
This project is built in Django using Python, CSS, HTML and Javascript.

## Table of Content

## UX
### The Strategy Plane
<ul>
<li>Cookin is a site for users to easy share their favorite recipes with the rest of the world but also find inspiration and new favorite dishes. </li>
</ul>

#### The Ideal User
<ul>
<li>Food lovers that want to shair there recipes with the rest of the world</li>
<li>Anyone looking for dinner inspiration</li>
<li>Anyone that want to expand their recipe knowledge</li>
</ul>

#### Site Goals
<ul>
<li>Provide a place for people to find new recipes to try</li>
<li>Provide users a place to share their recipes with the world</li>
</ul>

### User Stories
Since I knew I dident have much time to write this project I settled with six User Stories that where all must haves
<ul>
<li>As a site owner I can display recipes so that people can get inspiration on what to cook tonight</li>
<li>As a user I can create an account so I can log in to my profile</li>
<li>As a user I can add recipes so that other people can view them and get inspiration</li>
<li>As a user I can edit my recipes if I made a misstake when I uploaded it</li>
<li>As a user I can add a image to my recipe so that people can get an idea what the dish looks like</li>
<li>As a user I can delete my recipe if I dont want it visible on the site anymore</li>
</ul>

## The Scope Plane
### Features Planned
<ul>
<li>Everybody - View recipes & Create an account</li>
<li>User profile - Create, Read, Update & Delete</li>
<li>Users Recipes - Users can Create, Read, Update and Delete their own recipes</li>
<li>Users Profile - User can log in to their profile, view their own recipes in a seperate list & log out of their account</li>
</ul>

## The Skeleton Plane
### Wireframes

#### Home Page
The main attraction on the home page is the image carusel in the middle looping through recipes in the database.
The images also contains the name of the recipe and a link to see the full recipe.
![Alt text](<images/Cookin Home Page.png>)

#### Recipe Page
The recipe page contains of cards for all the recipes in the database which are all clickable and takes the user to the recipe datails page.
![Alt text](<images/Cookin Recipe Page.png>)

#### Recipe Datails Page
The datails page gives the user a bigger picture of the recipe on the left hand side.
On the right hand side the user gets a full decription of the recipe.
![Alt text](<images/Cookin Recipe Details.png>)

## The Surface Plane
### Design
Like the wireframes show I decided to got with a very simple design for this project making the recipes the star of the show.
Sadly enough I ran out of time so the color and typography choices got overlooked.

### Images
The only images that exist on the page are images uploaded to the recipes since thats all this site is about.
Since I dident have time to take images of alot of food I decided to simply link to images that was already on the web.
In the long run it would probably be better to allow the user the choice to upload their own images or link to someone elses image.

## Features
### Navigation Bar
The top part of all pages consists of the navigation bar which shows different options if your logged in or not.
If your not logged in you get the options Home, Recipes, Log In and Register.
If your logged in the Log In and Register gets swapped out to Add a Recipe, Profile and Log out.
On smaller screens the nav bar changes to a hamburger meny with the same options.

![Alt text](<images/Skärmavbild-2023-08-01-kl.-16.36.43 (1).webp>)

### Home Page
The big star of the home page is the Image Carusel that takes up the full screen.
It displays recipe images from the database, with name and a link to view the full recipe.

### Recipe Cards
The Recipe page contains clickable cards for all the recipes in the database.
The cards show the name of the recipe, what ingredients are used, a image of the recipe and the name of the author

![Alt text](<images/Skärmavbild-2023-08-01-kl.-16.37.26 (1).webp>)

### Recipe Details
The detail page for each recipe has a bigger image of the recipe on the left side of the screen.
On the right side you can see a list of ingredients and a decription on how to make it.
If your the user how created the recipe you get the option to edit or delete the recipe on the bottom of the page.

![Alt text](<images/Skärmavbild-2023-08-01-kl.-16.58.04 (1).webp>)


### User Profile
On your user profile you get a page similar to the Recipe Cards page but it only contains the recipes uploaded by you.

### Create / Edit a Recipe
The page to add or edit a recipe could use alot of work but it contains the most nessesary at the moment.
The user get to add a name to the recipe, a list of ingedients, a description and a link to an image.

![Alt text](<images/Skärmavbild-2023-08-01-kl.-16.37.42 (1).webp>)

## Future Enhancements
There are quite a few things I would like to add/ enhance on this project in the future.
At the moment its just barely up and running with the basics

Enhancements:
<ul>
<li>Most of the design elements on the page 
    <ul>
        <li>Colors and Fonts</li>
    </ul>
        <li>User Profiles  
    <ul>
        <li>Add a picture and personalize your profile more</li>
    </ul>
<li>Creating recipes
    <ul>
        <li>The layout of the form</li>
        <li>Add ingredients as a list instead of a text box</li>
        <li>Choice of uploading or linking an image</li>
    </ul>
</ul>

More Features:
<ul>
    <li>Ratings on recipes</li>
        <ul>
            <li>Making it possible for other users and views to give feedback on recipes</li>
        </ul>
    <li>Viewing other profiles</li>
        <ul>
            <li>If you find a user making recipes you like, you can view all their recipes</li>
        </ul>
    <li>Log in with social network accounts</li>
        <ul>
            <li>Make it possible to login with facebook or google accounts, making it easier for people to sign up</li>
        </ul>
</ul>
    

## Testing

## Deployment

This site was deployed via Heroku and the live link can be found here - https://cookiin.herokuapp.com/

### Project Deployment

To deploy the project through Heroku I followed these steps:
<ul>
<li>Sign up / Log in to Heroku</li>
<li>From the main Heroku Dashboard page select 'New' and then 'Create New App'</li>
<li>Give the project a name - I entered "cookiin" and select a suitable region, then select create app. The name for the app must be unique.</li>
<li>This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, 
navigate to the resources tab.</li>
<li>Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database</li>
<li>Navigate to the setting tab, within the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.</li>
<li>Within the django app repository create a new file called env.py - within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku. The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"</li>
<li>Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"</li>
<li>Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE</li>
<li>In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url</li>
<li>Insert the line if os.path.isfile("env.py"): import env</li>
<li>Remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')</li>
<li>Replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.</li>
<li>In the terminal migrate the models over to the new database connection</li>
<li>Navigate in a browser to cloudinary, log in, or create an account and log in.</li>
<li>From the dashboard - copy the CLOUDINARY_URL to the clipboard</li>
<li>In the env.py file created earlier - add os.environ["CLOUDINARY_URL"] = "paste in the Url copied to the clipboard here"</li>
<li>In Heroku, add the CLOUDINARY_URL and value copied to the clipboard to the config vars</li>
<li>Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars (this key value pair must be removed prior to final deployment)</li>
<li>Add the cloudinary libraries to the list of installed apps, the order they are inserted is important, 'cloudinary_storage' goes above 'django.contrib.staitcfiles' and 'cloudinary' goes below it.</li>
<li>In the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.</li>
<li>Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')</li>
<li>Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]</li>
<li>Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com</li>
<li>In your code editor, create three new top level folders, media, static, templates</li>
<li>Create a new file on the top level directory - Procfile</li>
<li>Within the Procfile add the code - web: guincorn PROJECT_NAME.wsgi</li>
<li>In the terminal, add the changed files, commit and push to GitHub</li>
<li>In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors</li>
<li>Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site</li>
</ul>

### Forking the repository

By forking the GitHub Repository you can make a copy of the original repository to view or change without it effecting the original repository. 

This can be done by:
<ul>
<li>Log into GitHub or create an account</li>
<li>Locate the repository at https://github.com/linusheinsvig/cookin</li> 
<li>At the top of the repository, on the right side of the page, select "Fork" from the buttons available</li>
<li>A copy of the repository should now be created in your own repository</li>
</ul>

### Create a clone of this repository

Creating a clone enables you to make a copy of the repository at that point in time - this lets you run a copy of the project locally

This can be done by:
<ul>
<li>Navigate to https://github.com/linusheinsvig/cookin</li>
<li>Click on the arrow on the green code button at the top of the list of files</li>
<li>Select the clone by https option and copy the URL it provides to the clipboard</li>
<li>Navigate to your code editor of choice and within the terminal change the directory to the location you want to clone the repository to</li>
<li>Type 'git clone' and paste the https link you copied from github</li>
<li>Press enter and git will clone the repository to your local machine</li>