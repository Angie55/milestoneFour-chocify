[![Build Status](https://travis-ci.org/Angie55/milestoneFour-chocify.svg?branch=master)](https://travis-ci.org/Angie55/milestoneFour-chocify)

Chocify is an ecommerce store selling novelty chocolate gifts. It was created as a final project of a Code Institute web development diploma
to display skills learnt over the course. The overall aim is to build a custom built Django project composed of multiple apps. Chocify is a 
fictional brand using images and content from 2 real brands. This project was designed to show case the products in an appealing way that 
encourages the customer to browse and make a purchase. The focus is on the user having an effortless experience with a design that feels intuitive.

## Developer goals

- To create a Django full stack project, composed of multiple apps to build a functioning ecommerce store. Considering all the necessary steps 
required in browsing and purchasing products with each app.

- To design an attractive website that looks visually appealing but puts the focus on the products.  

- To make navigation easy and give clear feedback and instructions to the user.

- To create a user authentication mechanism so the user can register and login to make purchases. 

- Designs a relational database schema that is well suited to the online store and products.

- To ensure the user can safely and securely make payments for products on the site.

- To expand on what I have learnt about Django project back ends during the final part of the course and improving skills from previous modules.

---

## Table of Contents

1. [UX](#ux)
    - [Target Audience](#target-audience)
    - [Visitor Goals](#visitor-goals)
    - [Business Goals](#business-goals)
    - [User Story and Journey](#user-story-and-journey)
    - [Design Choices](#design-choices)
        - [Font](#font)
        - [Icons](#icons)
        - [Styling](#styling)
        - [Colours](#colours)
    - [Wireframes](#wireframes)
2. [Features](#features)
    - [Existing features](#existing-features)
        - [Navbar](#nav)
        - [Footer](#footer)
        - [Home](#home)
        - [All products](#all-products)
        - [Product details](#product-details)
        - [Products by category](#products-by-category)
        - [Search results](#search-results)
        - [Checkout](#checkout)
        - [Login and Register](#login-and-register)
        - [Profile](#profile)
        - [Reset password](#reset-password)
        - [Contact us](#contact-us)
        - [Cart](#cart)

3. [Information Architecture](#information-architecture)
    - [Databases](#databases)
    - [Data models](#data-models)
    - [User](#user)
    - [Category app model](#category-app-model)
    - [Products app model](#products-app-model)
    - [Order app model](#order-app-model)

4. [Deployment](#deployment)



---

## UX

### Target Audience

- Support small, British brands.
- Likes quirky gifts or knows those who appreciate them.
- Is a chocolate lover or acquaintance of one.
- Both males and females looking for a gift for either sex.
- Someone looking for a specifically themed gift.

### Visitor Goals

"**_As a visitor to the site my goal is to_** ____"

- Find and purchase a unique, quirky gift.
- Find an edible chocolate gift for those that are easy and hard to buy for.
- View a variety of products with clear, detailed pictures that I can click for more details.
- To be able to easily navigate between pages while viewing products, categories and my cart.
- To be able to shop quickly and easily add items to my cart as I go and also easily remove items.
- Easily register, login and pay securely.
- Feel that the site I am using is trustworthy.
- Be able to find out about the brand and where the products are made.
- To be able to make contact and ask questions.

### Business Goals

- To showcase the products in a professional way that not only looks good but gives the user piece of mind that they can trust the site.
- Increase fans and return customers by showing a good range or products that are well organised.
- Make sure each product is well represented through imagery and includes details and ingredients to ensure the customer is well informed.
- Make the checkout and payment easy with minimal steps so the user has a smooth experience.
- Ensure the whole journey from landing and browsing to confirmation on the order/payments to effortless so users are likely to return and recommend.

### User Story and Journey

"**_A visitor/user to the Chocify website I want_** ____"

- Want to see a professional looking site as soon as I land in the site.
- To quickly and easily know what the brand is about with links to information where I would expect them.
- Predictable navigation with all the links working and going where expected.
- It to be easy to hop back and forth between products, categories and the cart as I explore what is available.
- To be able to view the site with the same level of quality and experience whatever the size the device I am using is.
- To be able to view a range of products that are displayed is manageable chunks. 
- To be able to clearly see the price and be able to add an item to cart without viewing the details if I choose.
- See clear images and more than one image for each products so I can see the details of what I am about to purchase.
- Be able to see a description, ingredients and chocolate types to help me decide and assess suitability for myself or whoever the gift of for.
- To see how many items I have added to my cart at all times.
- Search the site to try and find a specific item or see if something I have in mind exists.
- To be able to make contact easily with a simple form.
- See a clear list of items and prices in my cart and on the checkout page with totals before I pay.
- To be able to update my username or email address.
- To be able to reset my password if I forget.
- To see clear feedback on actions taken whether they are successful or incorrect.

### Design Choices

The overall design is clean and boutique like with a few subtle colours. The products have intricate details that can be shown 
of better with clean simple surroundings. The designs are quirky and fun so the design lets them stand out and be the focus 
with subtle, cute colours.

#### Font
After exploring several fonts and looking across several sites that specialise in chocolate I found Poppins looked best on the site. 
I tried some combinations but found Poppins fitted well, slightly heaver as headers and lighter for the main text. It is very easy to 
read but has a friendly and very slight playful feel to the shape of the letter. I feel this complimented the quirky theme without being 
too overly styled. 

#### Icons
All the icons used are from [Fontawesome](https://fontawesome.com/), they are simple and clearly represent what they are used for or help 
add emphasis in some areas. 

#### Styling
- Rounded edges and thin borders are used for a soft, friendly feel. The subtle box shadows bring the images up and way from the background 
so they stand out more.
- A simple colour transition is used when hovering over buttons and links and the feedback is keep the same across the site.
- Horizontal rules are used to separate content or at the end so the eye can easily navigate the content.
- Images are kept large where possible to show the details in the products.
- Pages such a registration, login, profile, resetting password etc. are all kept very simple so the focus is on what the user is on that page for.

#### Colours

The colour pink appeared on a few of the chocolate sites I browsed along with a deep brown. I think that many shades of pink compliment the browns 
used in designs as well as the shades of real chocolates itself. I sampled a few pinks and chose one that worked really well with dark, milk and 
white chocolate as well as the deep brown. 

Pink can be seen as a fun, compassionate colour with gives a friendly feels on the site. 

- ![#f09583](https://placehold.it/15/f09583/f09583) `#f09583` (**Dark Salmon**)

The brown is obvious colour connected to chocolate but also used sparingly to compliment the contents.

- ![#43281e](https://placehold.it/15/43281e/43281e) `#43281e` (**Dark Chesnut**)

The greys work well with the pink and give a gentle, soft touch around the bright, punchy product images.

- ![#baa999](https://placehold.it/15/baa999/baa999) `#baa999` (**Warm Smokey Grey**)
- ![#ddd](https://placehold.it/15/ddd/ddd) `#ddd` (**Light Grey**)

The blue and greens used for buttons are fairly standard to action buttons and the blue was also a good contrast to show the cart count.

- ![#42C0FB](https://placehold.it/15/42C0FB/42C0FB) `#42C0FB` (**Caribbean Blue**)
- ![#66CD00](https://placehold.it/15/66CD00/66CD00) `#66CD00` (**Kelly Green**)

### Wireframes




## Features

### Existing features

#### Navbar

- Logo- links to homepage.

- Search- A word or words can be typed here and products will display if this word or words feature in the products title.

- Links- the links to shop and the cart remain at all times. When the user is not logged they see Login and register. Once logged in they
see Logout and Profile instead so no unnecessary links are shown or unnecessary pages can be accessed.

- Small screens- The main navigation links are replaced with a burger icon to toggle the links when it is clicked. The search bar and cart
are in this toggled menu due to the limited space and the user would expect to find them there.

- Items in cart- A number (badge) will display by the cart icon when there are items in the cart. Only the cart icon will show when it is empty.

#### Footer

- Links- There are links to the about us and information pages and the contact us page.

- Small screens- All footer features on large screens remain until mobile size. At tablet size they become full width then. The address and
disclaimer are removed at mobile size as it would be too cluttered with them.

#### Home

- Displays a carousel of 3 hero images with an arrow for users to slide to the next image. If any area of the hero image is clicked the user
is taken to the shop all products page.

- The categories and their images are displayed, the whole image is a link to that category.

- Alert display- The messages are displayed in an alert that appears above the hero slider and is faded out as the content slides up.

##### Future Devs-

- A carousel of all products that auto slides unto the category displays.

#### All products

- Category display- The image for each category and the title displays. They display from large to tablet size screens and the images are removed on mobile devices.

- Pagination- 9 products are displayed at a time to avoid too much scrolling. The arrows to navigate the pages are disabled as necessary when it is the first or last page.

- Add to cart- Products can be added to the cart from this page.

##### Future Devs-

- Filter Products- By newest to oldest and by price, highest to lowest.

- Choc type display- A small circle with milk, white and dark in chocolate colours the appears in the corner of the image of the products contain that choc type.

#### Product details

- Images- When clicked the thumbnails become the main image. There can be up to 4 images per product and a minimum of 2.

- Add to cart- Products can be added to the cart from this page.

- Choc types- An image for milk, white or dark chocolate will show if it features in that product, some may feature all and some just one. It will be useful for users with particular tastes. Some appear to be milk but may just be dark. Some seem like that could have a milk centre but are all white chocolate.

- Link- A link back to the all products page has been added to avoid use of the back option on the browser.

#### Products by category

- Displays all the products in that category.

- Add to cart- Products can be added to the cart from this page.

#### Search results

- Products can be searched by typing a word, it will display in the results if that word or the correct sequence of letters are in the title.

##### Future Devs-

- Search to include tags that were added for each product as part of the search results.

- When user search it would be good for them to see the text 'Search results for .....' with the word they searched so they can see how they spelt it.
it would be good for this to also show when no products found with 'No results found for ....'.

- Make better use of space on page when no search results found with a carousel of products or and advert.

#### Cart

- Summery- of products added with image, price, quantity and title as link to the details for that product if the user wants to read
more or double check anything.

- Amending cart items- The number of each product to purchase is displayed and can be amended to a different amount.

- Total- displays and changes as cart items are amended.

- Checkout- Link only works of logged in, if they are not they are taken to the login page.

#### Checkout

- Summery- of products added with image, price and quantity. 

- Total- of order displays under summery and just above payment where it can easily be viewed before payment is made.

- Address and payment details- user can fill in their details and pay for their order, which is done securely with Stripe.

- Stripe- used for secure payment of products.

#### Login and Register

- Form to login with links to register or reset password. 

- Form to create an account- If valid once submitted it will create a new account for the user who will see the
details in their profile page.

#### Profile

- Displays current username and email on users account.

- The form can be used to amend username or email or both.

#### Reset password

#### Contact us 

- Form to send a message to the Chocify team using EmailJS, this currently sends an email to one of my email accounts so I could test it.

## Information Architecture

### Databases

Django works with SQL databases and during development I used the standard sqlite3 database installed with Django.
When deployed, the SQL database provided by Heroku is a PostgreSQL database.

### Data models

#### User

For this project I used the standard user model by Django

#### Category app model

    name = models.CharField(max_length=100, default='')   
    image = models.ImageField(upload_to='images', default='')

#### Products app model

    category = models.ForeignKey(Category, null=True)
    title = models.CharField(max_length=150, default='')
    introduction = models.TextField(max_length=400)
    details = models.TextField(default='')
    ingredients = models.TextField(default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    milk_choc = models.BooleanField(default=True)
    white_choc = models.BooleanField(default=False)
    dark_choc = models.BooleanField(default=False)
    tags = models.CharField(max_length=300)
    image1 = models.ImageField(upload_to='images', blank=True)
    image2 = models.ImageField(upload_to='images', blank=True, null=True)
    image3 = models.ImageField(upload_to='images', blank=True, null=True)
    image4 = models.ImageField(upload_to='images', blank=True, null=True)

#### Checkout

    full_name = models.CharField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    street_address1 = models.CharField(max_length=50, blank=False)
    street_address2 = models.CharField(max_length=50, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=40, blank=False)
    date_ordered = models.DateField(default=datetime.date.today, null=True)
    shipped = models.BooleanField(default=False)

#### OrderLineItem app model

    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

## Technologies used

### Tools

- [Photoshop CS6](https://www.adobe.com/Photoshop) - Used for editing images.
- [Gitpod](https://www.gitpod.io/) The IDE used for developing this project.
- [Heroku](https://www.heroku.com) - Used for app hosting.
- [SweetAlert2](https://sweetalert2.github.io/)- A responsive popup box.
- [Python](https://www.python.org/) - Used as the back-end programming language.
- [Django](https://www.djangoproject.com/)- A python web framework for rapid development and clean design.
- [Stripe](https://stripe.com) - As payment platform for secure payments online.
- [Travis](https://travis-ci.org/) - For continuous integration.
- [AWS S3 Bucket](https://aws.amazon.com/) - To store images entered into the database.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - To enable creation, configuration and management of AWS S3.
- [Django Heroku](https://pypi.org/project/django-heroku/) - To improve deployment of django projects on heroku.
- [Django Storages](https://django-storages.readthedocs.io/en/latest/) - A collection of custom storage backends with django to work with boto3 and AWS S3.
- [Gunicorn](https://pypi.org/project/gunicorn/) - To aid in deployment of the Django project to Heroku.
- [Pillow](https://pillow.readthedocs.io/en/stable/) - To aid in processing image files to store in database.
- [Psycopg2](https://pypi.org/project/psycopg2/) - As PostgreSQL database adapter for Python.
- [PIP](https://pip.pypa.io/en/stable/installing/) - For installing the tools needed in this project.
- [git](https://git-scm.com/)- used as a respository.
- [GitHub](https://github.com/) - Used as remote storage of my code online.

### Databases

- [PostgreSQL](https://www.postgresql.org/) - For production database, provided by heroku.
- [SQlite3](https://www.sqlite.org/index.html) - For development database, provided by django.

### Libraries

- [JQuery](https://code.jquery.com/jquery/) - Used as the primary JavaScript functionality in Bootsrap framework.
- [Bootstrap](https://getbootstrap.com/) - Used to help with the layout, navigation and making the site responsive as main design framework.
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) - To provide icons.
- [Google Fonts](https://fonts.google.com/) - To style the website fonts.

## Deployment

### Local deployment

The following will need to be installed on your own system/IDE in order to run this project locally:

- [Python 3](https://www.python.org/downloads/)
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

I used [Gitpod](https://www.gitpod.io/) as my chosen IDE and used this [Code Institute Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)
which hadd all of the tools preinstalled that I needed to get started.

You will need to create free accounts on:
- [Stripe](https://dashboard.stripe.com/register)
- [Emailjs](https://www.emailjs.com/)
- [AWS](https://aws.amazon.com/) and set up an [S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)

Instructions for set up can be found on each site, click the links to create an account or login if you already have one.

- Clone this GitHub repository by either clicking the green 'Clone or download' button and downloading the project as a zip-file (unzip it first),
or by entering the following into the Git CLI terminal:
    - `https://github.com/Angie55/milestoneFour-chocify.git`
- Install all requirements from the requirements.txt file using this command:
    - `pip -r requirements.txt` (if needed upgrade the pip with `pip install --upgrade pip`)

- Set up the following environment variables in your IDE in a new file named env.py:

import os

- os.environ.setdefault("STRIPE_PUBLISHABLE","**Enter key here**")
- os.environ.setdefault("STRIPE_SECRET","**Enter key here**")
- os.environ.setdefault("EMAILJS_USERID","**Enter user id here**")
- os.environ.setdefault("DATABASE_URL", "**Enter url here**")
- os.environ.setdefault("SECRET_KEY", "**Enter key here**")
- os.environ.setdefault("AWS_ACCESS_KEY_ID", "**Enter key here**")
- os.environ.setdefault("AWS_SECRET_ACCESS_KEY","**Enter key here**")

In settings.py remove the hashtag on import env at the top of the file so these keys can be accessed. Comment this
out if you deploy to Heroku.

Migrate the admin panel models to create your database template with the terminal command.
    - `python3 manage.py migrate`

Use the following command to create your superuser to access the django admin panel and database, and then follow the steps
to add your admin username and password:
    - `python3 manage.py createsuperuser`

You will now be able to run the project locally with the following command:
    - `python3 manage.py runserver`

Once running, go to the link provided and type '/admin' at the end of the url. Login as the superuser with the details your used to
create the superuser. You can create categories and add products here as well as view users and orders.

### Heroku deployment

- Sign up for a Heroku account or login if you have one and create a new app.
- Go to 'Resources' to add a database, under 'Add-ons' type postgress, select 'Heroku Pastgress' and choose the 'Hobby Dev' free option.
- Go to 'Settings', click 'Reveal config vars' and copy the DATABASE_URL 'postgress url'.
- Paste the database url in the env.py file,
- Go to the git bash terminal and enter:
    - `pip3 install dj_database_url` and then 
    - `pip3 install psycopg2`

- Make migrations and migrate the admin panel models to create your database template with the terminal command:
    - `python3 manage.py makemigrations` then
    - `python3 manage.py migrate`

- Use the following command to create your superuser to access the admin panel and database, and then follow the steps
to add your admin username and password:
    - `python3 manage.py createsuperuser`

- Create a 'requirements.txt' file using the terminal command:
    - `pip3 freeze > requirements.txt`.
If you already have one, make sure you update it so it has all the requirments before to deploy.

- Install 'gunicorn' with:
    - `pip3 install gunicorn`

- Create a 'Procfile' with the terminal command:
    - `echo web: python app.py > Procfile`
- Open the Procfile and amend it to:
    - `web: gunicorn chocify_ecommerce.wsgi:application`

- Then 'git add' and 'git commit' the new requirements and Procfile and then 'git push' the project to GitHub.

- Go to 'Heroku', 'Settings' and add the following 'Config vars':

    - STRIPE_PUBLISHABLE: "**Enter key here**"
    - STRIPE_SECRET: "**Enter key here**"
    - EMAILJS_USERID: **Enter user id here**"
    - DATABASE_URL: "**Enter url here**"
    - SECRET_KEY: "**Enter key here**"
    - AWS_ACCESS_KEY_ID: "**Enter key here**"
    - AWS_SECRET_ACCESS_KEY: "**Enter key here**"
    - DISABLE_COLLECTSTATIC: "**1**"

- Go to 'Deploy', select 'Github' and search for your repository and 'Connect'.
- You can go to 'Manual deploy' and 'Deploy Branch'. Once it has built you need to add it to
your allowed host in the 'Setting.py' to open it. 
- Open the app and type '/admin' at the end of the url. Login as the superuser with the details your used to
create the superuser. You can create categories and add products here as well as view users and orders.

