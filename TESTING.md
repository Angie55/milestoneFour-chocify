# [Chocify](https://chocify-milestone-four.herokuapp.com/) Testing


This is the testing write up for the main [README.md](README.md) file for the [Chocify](https://chocify-milestone-four.herokuapp.com/).

1. [Automated testing](#automated-testing)

2. [Travis](#travis)

3. [Manual testing](#manual-testing)
    - [Navbar](#navbar)
    - [Footer](#footer)
    - [Home](#home)
    - [All products](#all-products)
    - [Search results](#search-results)
    - [Product details](#product-details)
    - [Products by category](#products-by-category)
    - [Cart](#cart)
    - [Checkout](#checkout)
    - [Login](#login)
    - [Register](#register)
    - [Reset password](#reset-password)
    - [Profile](#profile)
    - [Contact us](#contact-us)
    - [Other bugs](#other-bugs)

4. [User Story and Journey](#user-story-and-journey)

### Automated testing

The following validation services and linter were used to check the validity of the website code.

- [W3C Markup Validation](https://validator.w3.org/)- used to validate HTML.

- [W3C CSS validation](https://jigsaw.w3.org/css-validator/)- was used to validate CSS.

- [JShint](https://jshint.com/)- was used to validate JavaScript.

- The python code was validated within the [Gitpod IDE](https://www.gitpod.io/).

### Travis

- Travis was used throughout the unit testing of this project to provide continuous integration with the deployed site. You can
find all the info needed to set [Travis](https://docs.travis-ci.com/user/tutorial/) up in the documentation.

### Manual testing

#### Navbar

- The number of products added to the cart displays correctly and the badge only shows when there are items in the cart.

- The correct link display depending on whether the user is logged in or not. Login and Register when the user is not logged in and
Profile and Logout when the user is logged in.

- The logo takes the user to the homepage.

- All links go to the correct pages.

- Smaller screens- The main nav toggles, showing a burger icon that opens the menu when clicked. The nav items display well on this small menu.

- Search- The user can type in the search field and then click enter or the search icon to start the search.

#### Footer

- Links go to the correct pages.

- The address and disclaimer are removed on small screens.

#### Home

- The hero images display well, they slide and the user can click to the next or previous one. The caption is not visible of very small screens.

- All the categories images display well and have the correct hover style and go to the correct category when clicked.

#### All products

- The categories all display with and link to the correct category.

- Products display well with all the correct information showing and clicking the title or image takes you to the product details.

- Products can be added to the cart and the user sees feedback if they do not enter a quantity.

- On small screens the products display well with a hr line to separate each product.

- Pagination
    - The correct number of products displays per page.
    - Pages with fewer than 9 products display well as the products are centered.
    - The number of pages is correct and can be clicked to navigate to other pages. The current page is highlighted.
    - The arrows can only be clicked of there is a next or previous page.

##### Bugs (fixed)-

- I had removed the categories from displaying at all on mobile screens but these are currently the only links to categories. I added just the title
back as it need to be simpler on the small screen. Categories links in the main menu would be good for future development.

##### Bugs (Not fixed)-

- Add to cart
    - Bring you back to the top of the page wherever you are are on the page.
    - If you are on page 3 of the products, you are taken to the top of the first page rather than staying where you were.

#### Search results

- Returns products with word searched for in the title.

- Returns products when partial word typed such as 'fi' which showed fish and 'truf' showed truffles. A single letter can be
used.

- If no products found the user sees a message to confirm this and a link to the all products page.

##### Bugs (fixed)-

- Shop all header was displaying for search results. At first I added separate headers for categories and all products but found the category header
displayed on the search results. There is now just a header for all products and the search results look cleaner.

#### Product details

- All product details display well.

- Thumbnails can be clicked to become the main image.

- Products can be added to the cart and the user sees feedback if they do not enter a quantity.

- The correct choc types connected to the products display.

##### Bugs (fixed)-

- Small screens- Content to narrow on small and medium screens. Margin tops to too large on small screens. Both fixed so the content noe displays well.

##### Bugs (Not fixed)-

- When the add to cart button is clicked, the user is taken to the all products page rather than staying on the individual product page.

#### Products by category

- All the correct products for that category display.

- Products can be added to the cart and the user sees feedback if they do not enter a quantity.

##### Bugs (Not fixed)-

- When the add to cart button is clicked, the user is taken to the all products page rather than staying on the category page.

#### Cart

- If the cart is empty the correct text shows with button links to Shop or Home.
- Correct number items display in the cart that were added.
- The products information such as image, title, quantity and price display. 
- Product title can be clicked to view the products details if I want to check anything before I buy it.
- The quantity of each product can be amended with the up and down arrows or by typing a number in.
- Changing the quantity to 0 removes the product from the cart.
- Total displays under items.
- Link to the checkout works if I’m logged in. If I’m not logged in I am taken to the login page.

#### Checkout

- The correct products with the correct quantities display.
- The correct total displays.
- The forms display.
- The forms feedback when a required field is not filled.
- The form displays feedback if the card number or security code is incorrect. 
- Feedback displays if the expiry date is not valid.
- I am redirected to the homepage an see an alert message that the payment was successful and my order will be processed shortly.
- The order is visible on the admin page.

##### Bugs (Not fixed)-

- If the payment is unsuccessful or declined, the feedback will display poorly as the mssages where styles around the home page hero
carousel. The needs to be a message alert styles for this page. It is still readable but will have a large gap above it.

#### Login

- I get feedback if I do not fill both fields.
- I get feedback if the username or password in incorrect.
- I get feedback if I use an email that is not on an account (although it does not yet specifically say that, it just says the username
or password are incorrect).
- When my details are correct I am logged in, redirected to the homepage and see an alert message that I have successfully logged in.
- Once logged on I can no longer access the login page until I log out and iI now have access to my Profile page.
- I can clearly see where I can click to reset my password or register an account.
- I can use either my username or email to login. 

##### Bugs (fixed)-
- When I try to log in with incorrect details, not only do I get feedback that the details are incorrect within the form but he “You have
successfully logged" in alert also pops up at the top of the page login page. This was because I had the message code in the wrong place 
in the accounts view and amending that fixed the issue.
 
#### Register 

- I receive feedback if I use a username that already exists.
- I receive feedback if the passwords do not match.
- I receive feedback if not all the fields are filled, as all are required.
- I receive feedback if my password is too short and how many characters it should have.
- I receive feedback if the password is too similar to the username.
- I can clearly see a link to login if I already have an account.

##### Bugs (not fixed)
- Lets me use the same email address as another account.

##### Bugs (fixed)
- Alert displayed badly and the page does not go home. This has been resolved as on registering the user is taken to the
home page where the alert displays well.
- Alert does not say I’m logged in. This has been fixed by amending the message to tell the user they have registered and are logged in.

#### Reset password

- Email can be entered on password reset page.
- Email is clear and contains a link.
- If the link is vaild the user goes to the page to set their new password.
- If the link is invalid the user is informed and given a link to the password reset page.
- The new passwords entered need to match or the user receives feedback.
- The users sees confirmation the password has been changes and a link to login.
- The login is successful with the new password.

#### Profile

- My username and email address are correctly displayed at the top of the page and in the form for me to edit them.
- I can edit either my username or password and I can also amend both.
- I receive feedback if the email address is not valid.
- I receive feedback if one field does not contain content.
- I can't use a username that already exists.
- My Profile is immediately updated and I see the changes in the profile page.

##### Bugs (fixed)
- Alert message that the profile had been updated displayed poorly as it was styled to work around the hero carousel on the homepage.
It now redirects the user to the homepage, this is not ideal but the message displays well. Potentially there could be no 
feedback when the details are updated as you can see the changes in front of you but I think the feedback is required so the user gets
clear feedback. They can easily go into the Profile again if they want to check.

##### Bugs (not fixed)
- If the user tries to change the username to one that already exist, it will not work and the there is feedback within the form however
the display at the top of the page changes to the new user name. The users new username will not be saved and they will need the old one
to login but may think it has changed. If they come out of and go back into the profile page, they will see the old
username. To resolve this the username at the top of the page should only update if the update is successful or a clear pop up message
should let the user know that this username will not be saved and they should try another. 
 
#### Contact us

- I am able to type in all fields.
- If I do not put anything in the fields I receive feedback as they are all required.
- The email filed must contain and valid email address, I receive feedback if it is not.
- I receive feedback if the email has sent or if there is an issue. This feedback pop up disappears with enough to read the feedback.
- The form is cleared after pressing send.
- The form and the feedback look good on all screen sizes.
- An email is received in the connected inbox.
- Image of filled contact form and email received:

<div align="center">
    <img src="https://i.ibb.co/cyhHbJN/contact-email.jpg" alt="contact-email" border="0">
</div>

#### Other bugs

Other bugs and issues not yet resolved:

##### Add to cart

Although the input to add an item to the cart has been set to give the user feedback if they try to submit without entering anything
or a number larger than 0, i have found at times that sometimes the user sees an error page that the value must be larger than 0. It
usually happens when the page has just been reached and often won’t happen a second time if you go back to the page. This will need
further investigation and testing to ensure that the user never sees this error page.

#### Error page

An error page is required that would be the default for the user to see on any occasion where something goes wrong. Even with defensive
coding in place this would be good to set up as a back up.

#### Product title

For longer product titles, as the text wraps, it pushes the add to cart form down and is out of line with other products with shorter titles.
This occurs on screen sizes from 768px to approx 1024px.


### User Story and Journey

"**_A visitor/user to the Chocify website I want_** ____"

- To see a professional looking site as soon as I land in the site. √
- To quickly and easily know what the brand is about with links to information where I would expect them. √
- Predictable navigation with all the links working and going where expected. √
- It to be easy to hop back and forth between products, categories and the cart as I explore what is available. √
- To be able to view the site with the same level of quality and experience whatever the size the device I am using is. √
- To be able to view a range of products that are displayed is manageable chunks. √
- To be able to clearly see the price and be able to add an item to cart without viewing the details if I choose. √
- See clear images and more than one image for each products so I can see the details of what I am about to purchase. √
- Be able to see a description, ingredients and chocolate types to help me decide and assess suitability for myself or whoever the gift of for. √
- To see how many items I have added to my cart at all times. √
- Search the site to try and find a specific item or see if something I have in mind exists. √
- To be able to make contact easily with a simple form. √
- See a clear list of items and prices in my cart and on the checkout page with totals before I pay. √
- To be able to update my username or email address. √
- To be able to reset my password if I forget.
- To see clear feedback on actions taken whether they are successful or incorrect. √