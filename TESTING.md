# [Chocify](https://chocify-milestone-four.herokuapp.com/) Testing


This is the testing write up for the main [README.md](README.md) file for the [Chocify](https://chocify-milestone-four.herokuapp.com/).

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