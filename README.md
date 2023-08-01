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