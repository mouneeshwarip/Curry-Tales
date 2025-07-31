# Manual testing

## Additional Testing

### Testing User Stories

* As a Site User | I can enter the page on the 'home' page so that I can see bestsellers and new grocery items immediately
* This user story was implemented a bit differently - on the home page, a user can see a carousel that redirects them to the corresponding grocery

* As a Site User | I can see all products and sort them to my preferences so that I can browse all products to see what is interesting for me
* When clicking the "All Products" link in the main navigation, the user gets to the product page displaying all products

* As a Site User | I can view detailed information about a product so that I can make an informed purchase decision
* When clicking the picture on the "products" page, they will be redirected to the product detail page that shows all information about the product

* As a Site User | I can browse products by categories so that I can find grocery item I'm interested in
* In the main navigation, there is a "Grocery" dropdown menu - when clicking Grocery, all corresponding products assosiated with the Grocery will be displayed

* As a Site User | I can sort by Grocery so that I can search for products which category interests me
* This user story has been modified and basically does the same as the one above. Refer to bug section on why

* As a Site User | I can use a search function so that I can find specific items quickly
* The search function will go through each field from each product and presents anything relevant to the search

* As a Site User | I can access an Grocery page where I can find them category wise
* This page is accessible from the main navigation menu and each category redirects to items belonging to that specific category

* As a Site User | I can see pictures and infos about Grocery items so that I can get a visual idea of how it looks or feels
* As a Site User | I can create an account so that I can make purchases and access personalized features
* A user does not need to have an account to make a purchase, but if they have an account, they can save their delivery info to the profile and access their order history

* As a Site User | I can log in to my account so that I can access my profile
* When a user is logged in, they can access their profile page via the "My Account" menu

* As a Site User | I can view my order history so that I can track the status of my current and past orders
* When a user is logged in, they can access their order history on the profile page via the "My Account" menu; status of current order has not been implemented and would be via email notifications

* As a Site User | I can add grocery items to my shopping cart so that I can purchase multiple items at once
* A user can add as many items in a quantity of a maximum of 99 items each to their shopping bag

* As a Site User | I can edit the contents in the shopping cart so that I do not buy items or quantities I do not want
* A user can modify their shopping bag by changing the amount and pressing "update" or deleting the item by clicking "remove"

* As a Site User | I can proceed through an easy checkout process so that I can complete my purchase without problems
* The shopping bag and checkout page are easy to follow and customized for both mobile and desktop screens for easy accessibility

* As a Site User | I can safely process payments so that my financial information is secure
* This website uses the third party application "Stripe" for processing the payments, also payment information will not be saved in the databank

* As a Site User | I can enter and save my delivery information in my profile so that I can use it for future purchases
* When clicking the "Save information to profile" before checking out, the info will be saved to their profile. (Bug present, refer to bugs section)

* As a Site User | I will get an email confirmation after a purchase so that I know the order has been placed and I get additional info about it
* If the user enters their correct email address, after each purchase they will recieve the order information immediately

* As a Site User | I can reset my password so that I am not excluded from the page if I forgot my old password
* If a user has forgotten their password, they can click "Forgot Password?" on the log in page and after providing their email address, a mail gets send to the email address. In this mail is a link on which the user can set a new password

* As a Site User | I can access a contact form so that I can submit questions or feedback to the grocery store
* The contact form works and has validation. The message will be sent to the admin panel - in a future feature I would like to implement a reply function

* As a Site User | I can access the FAQ page so that I get all answers to frequently asked questions
* The webpage has a FAQ page, accessable through the "About Us" menu or on big screens through the footer. The page is populated with questions that each have their answer as a dropdown function

* As a Site User | I can view an 'About Us' page so that I can learn more about the bookstore and its expertise
* The user can get to the About page through the "About Us" menu where the information of the store are present

* As a Site User | I can subscribe to a newsletter so that I can receive updates about new releases and promotions
* The newsletter can be accessed via the "About Us" menu or the footer on bigger screens. Given that the user provides a valid email address, they will get the confirmation that they have subscribed to the Newsletter

* As a Site User | I cannot access an invalid url so that a custom error page will give me the information on what went wrong
* If a user enters an invalid url, thew will be redirected to a custom error 404 page with a button back to the home page

* As a Site User | I can receive a discount and/or free shipping when my purchase exceeds a certain amount so that I am encouraged to place larger orders
* If the user spends more than 100€, the delivery fee falls away. When adding an item to the shopping bag, the notification will inform the user about how much they need to spend more to get the free delivery




* As a Site Admin | I can add new items to the store and remove old ones so that I can keep the catalog up-to-date
* Adding, editing and deleting products has full frontend and admin panel functionality

* As a Site Admin | I can create and manage grocery item categories so that I can keep the store organized
* Adding categories is implemented in the frontend, editing or deleting them has to be done on in the admin panel

* As a Site Admin | I can manage user accounts so that there are no unwanted customers
* In the admin panel, any user can be deleted

* As a Site Admin | I can manage the content of the "About Us" page and other static pages so that I can keep the information current
* The admin has to go through the admin panel, but there the "About us" page can be fully modified

* As a Site Admin | I can change questions and answers for the FAQ page so that I do not have to go through the admin panel
* FAQ functionalities are fully implemented in the frontend




* As Developer | I can implement SEO best practices so that the website ranks higher in search engine results
* Doing the SEO challange helped with this user story; on the desktop version, Lighthouse always gave a score of 100 for SEO, on mobile versions it went down to 91 on some sites

* As Developer | I can implement secure coding practices so that the application is protected against common vulnerabilities
* Every function which needs an authenticated user for is secured in the backend, also differentiating between normal and super users

[Back to top](<#table-of-content>)


### Manual Testing

In addition to tests stated above I have performed a series of manual tests. Below the list of tests that has been conducted can be found. Many of these steps have been documented and can be found in this [folder](readme/assets/images/manual-testing)

| Status | **Main Website - User Logged Out**
|:-------:|:--------|
| &check; | Typing in a incorrect URL on the page loads the 404 error page
| &check; | Entering an url that needs authentication loads the log in page
| &check; | Clicking the sites logo loads the home page
| &check; | Clicking the Home button on the nav bar loads the home page and lists all posts
| &check; | Clicking the Register link loads the Register page
| &check; | Clicking the Log In link loads the Log In page
| &check; | For both log in and register, any missing field will notify the user and will not submit until form is valid
| &check; | Clicking the items image on categories page loads the product page with grocery items from this category
| &check; | Clicking the product image on the products page loads the product detail page
| &check; | Clicking a Grocery from the main navigation dropdown loads the product page with all items with the corresponding Grocery type
| &check; | Using the search bar to get all items related to search
| &check; | Clicking the quantity buttons changes the quantity a user can add to their bag
| &check; | Clicking the add to bag button adds the item in wished quantity to the shopping bag
| &check; | Clicking secure checkout redirects the user to the checkout page
| &check; | On the checkout page the user can complete the order by providing delivery and payment information
| &check; | On the checkout page, any necessary field that has a wrong input will notify the user and will not submit until form is valid
| &check; | Clicking complete order lets the user make a purchase
| &check; | When an order succeeds the minimum free delivery amount, no delivery costs will be applied
| &check; | Clicking the "Contact us" button redirects the user to the form which he can submit a contact request
| &check; | Clicking the "Subscribe to our Newsletter" button redirects the user towards the page and lets them subscribe to the newsletter
| &check; | Clicking the "About Page" button redirects the user to the About page
| &check; | Clicking the "FAQ" button redirects the user to the FAQ page
| &check; | Clicking the Facebook link in the footer area opens Facebook in a new window
| &check; | Clicking the Instagram link in the footer area opens Instagram in a new window
| &check; | Clicking the Linkedin link in the footer area opens LinkedIN in a new window

| Status | **Main Website - User Logged In**
|:-------:|:--------|
| &check; | Typing in a incorrect URL on the page loads the 404 error page
| &check; | Entering an url that needs authentication loads an error informing that this is only allowed for superusers
| &check; | Clicking the sites logo loads the home page
| &check; | Clicking the Home button on the nav bar loads the home page and lists all posts
| &check; | Clicking the Register link loads the Register page
| &check; | Clicking the Log In link loads the Log In page
| &check; | Clicking the item image on the Grocery page loads the product page with items from this grocery category
| &check; | Clicking the product image on the products page loads the product detail page
| &check; | Clicking a category from the main navigation dropdown loads the product page with all books with the corresponding category
| &check; | Using the search bar to get all items related to search
| &check; | Clicking the quantity buttons changes the quantity a user can add to their bag
| &check; | Clicking the add to bag button adds the book in wished quantity to the shopping bag
| &check; | Clicking secure checkout redirects the user to the checkout page
| &check; | On the checkout page the user can complete the order by providing delivery and payment information
| &check; | If the user has made a previous order and clicked "Save info" or filled out the profile form, delivery details are pre populated
| &check; | Clicking complete order lets the user make a purchase
| &check; | When an order succeeds the minimum free delivery amount, no delivery costs will be applied
| &check; | Clicking the "Contact us" button redirects the user to the form which he can submit a contact request
| &check; | Clicking the "Subscribe to our Newsletter" button redirects the user towards the page and lets them subscribe to the newsletter
| &check; | Clicking the "About Page" button redirects the user to the About page
| &check; | Clicking the "FAQ" button redirects the user to the FAQ page
| &check; | Clicking the Facebook link in the footer area opens Facebook in a new window
| &check; | Clicking the Instagram link in the footer area opens Instagram in a new window
| &check; | Clicking the Linkedin link in the footer area opens LinkedIN in a new window

| Status | **Main Website - Admin Logged In**
|:-------:|:--------|
| &check; | Clicking the Admin Panel button in the Product Management page loads the Admin Panel Page
| &check; | The product management button is only visible for admins
| &check; | Deleting a profile works on the Admin Panel
| &check; | Deleting a product works on the Admin Panel
| &check; | Deleting an Grocery works on the Admin Panel
| &check; | Deleting a Grocery category works on the Admin Panel
| &check; | Deleting a FAQ works on the Admin Panel
| &check; | Editing a product works on the Admin Panel
| &check; | Editing an Grocery category works on the Admin Panel
| &check; | Editing a Grocery category works on the Admin Panel
| &check; | Editing a FAQ works on the Admin Panel
| &check; | Adding a product works on the Admin Panel
| &check; | Adding an Grocery category works on the Admin Panel
| &check; | Adding a Grocery category works on the Admin Panel
| &check; | Adding a FAQ works on the Admin Panel
| &check; | Changing an email of any user works in the Admin Panel
| &check; | Changing a password of any user works in the Admin Panel
| &check; | Deleting a Profile will delete their profile but keeps the oders
| &check; | Deleting a product works on the Fontend
| &check; | Deleting an author works on the Fontend
| &check; | Deleting a FAQ works on the Fontend
| &check; | Editing a product works on the Fontend
| &check; | Editing an Grocery works on the Fontend
| &check; | Editing a FAQ works on the Fontend
| &check; | Adding a product works on the Fontend
| &check; | Adding an Grocery works on the Fontend
| &check; | Adding a FAQ works on the Fontend
| &check; | Adding a Grocery works on the Fontend
| &check; | Leaving out any nessesary fields (non nullable in the models) will notify the admin about what is missing

Status | **Create A New User - User Logged Out**
|:-------:|:--------|
| &check; | Username field is required
| &check; | Username field does not accept empty field
| &check; | Email field does not accept an invalid email format
| &check; | Email field is required
| &check; | Password field does not accept empty field
| &check; | Success message is displayed when the user creates a new user
| &check; | Error with corresponding info when wrong input is submitted

Status | **Create A Profile Page - User Logged In**
|:-------:|:--------|
| &check; | The default profile info is seen on the profile page (placeholders)
| &check; | The profile success message is displayed when the user updates the profile form
| &check; | As soon as a user has placed an order, the orer summary will show up on the profile page

[Back to top](<#table-of-content>)

