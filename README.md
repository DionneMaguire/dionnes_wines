# Dionne's Wines

## Purpose of this site

This site has been created so that users can buy wine from the store.  Users can also read the wine descriptions to help decide what to buy.  They can also read the blog posts about new wines, vineyards etc.  Users can also add reviews about their shopping experience and also review individual wines that they have bought.  These reviews are available for all users to view.  The store owner/ superuser can add, edit and delete wines available for sale.  The store owner can also add blog posts for all users to view.  All users can buy from the store whether they are logged in or not.  The advantage of logged in users is that their delivery information can be stored and also their order history is displayed in their profile.

![Am I responsive](/documentation/images/amiresp-wine.png)

## User Experience

### User Goals

#### Not signed in user

- find out the purpose of the site and how to use it
- be able to easily navigate throughout the site
- see a list of available wines to buy
- able to click on any wine to get a detailed decription and be able to add to bag
- be able to add, edit and delete items from their bag
- be able to enter their delivery and payment details to complete purchase
- be able to register for an account
- be able to leave feedback on their shopping experience
- be able to review wines

#### logged in users
- can do all that a not signed in user can do +
- save their delivery details to their profile
- delivery information is prepopulated in their checkout process, to speed up the process
- can logout of their account to keep their information safe

#### site owner / superuser
- can add, edit and delete wines form the store
- can add blog posts to the site
- can approve customer reviews and wine reviews from customers ( only approved reviews will be visible on the website)

### User Stories

I used Github issues to record the following user stories:
- account register - As a site user I can easily register for an account so that I can view and edit my profile
- login/logout - As a site user I can login and logout of my account so that I can access my delivery information and order history
- email confirmation on registration - as a site user I can receive an email confirmation so that I can verify account registration has been successful
- personal user profile - As a site user I can have a personalised user profile so that I can view delivery information and order confirmation
- view list of wines - As a site user I can view a list of wines so that I can select some to buy
- view individual wine details - As a site user i can view individual wine details so that I can view the details and add to my bag
- sort wines - as a site user I can sort the list of available wines so that I can easily identify what I want
- search - As a site user I can search for wine by name or description so that I can find a specific wine
- search results - As a site user I can easily see what I have searched for and the number of results so that I can quickly see what is available
- wine category - As a site user I can view a specific category of wine so that I can quickly find the wines that I am interested in
- view total spend - As a site user I can see the total of my purchases so that I avoid overspending
- select quantity - As a site user I can easily select quantity of wine when purchasing so that I don't accidentally select too much
- view bag - as a site user I can view items in my bag so that I can clearly see the items I am going to purchase and the total cost
- adjust quantity - As a site user I can adjust the quantity od individual wines in my bag so that I can easily make changes to my bag before checkout
- payment information - as a site user I can easily enter payment information so that I can checkout quickly and easily
- secure infromation - as a site user I feel my information is safe and secure so that I can confidently provide information to make purchase
- view order confirmation - as a site user I can view an order confirmation after checkout so that I can verify I haven't made a mistake
- receive an email confirmation - as a site user I can receive a email confirmation after checkout so that I have the details for my records
- free delivery - as a site user I can see clearly how much more I have to spend to get free delivery so that I can make decision to buy more
- add a wine - as a store owner I can add a wine so that I can add it to the store
- edit wine - as a store owner I can edit a wine so that I can change prices and details
- delete wine - as astore owner I can delete a wine so that I can remove from store if it is not longer available
- view list of blogs - as a site user I can view a list of blogs so that I can choose whiah to read
- view blog detail - as a site user I can view blog details so that I can learn interesting facts about wine
- add blogs - as a store owner I can add blogs to the website so that I can give users interesting and informative information
- edit blog - as a store owner I can edit a blog so that I can update information
- delete blog - as a store owner I can delete a blog so that I can remove it if it is no longer relevant
- view customer reviews - as a site user I can view customer reviews so I can decide whether or not to but from the site
- add review - as a site user I can add a review so that I can share my experience with the other users
- view wine reviews - as a site user I can view wine reviews so that I can decide what to buy
- add wine review - as a site user I can add a wine review so that I can share information with other users
- approve reviews - as a store owner I can approve customer and wine reviews so that they appear on the website
- email marketing - as a site user I can subscribe for email marketing so that I can receive information on promotions and discounts
- privacy policy - as a site user I can view the privacy policy so that I can see how my information is collected and processed
- About Us - as a site user I can view the about Us page so that I can learn more about Dionne's Wines
- FAQ - as a site user I can view FAQ so that I can easily see more information
- messages - as a user I can get messages after actions to confirm whether the action was successful or not.

### Agile Development Tool

I am using an agile software development tool in the development of this website.  I am using Github Projects, using a basic Kanban Template.  I addded automation so that as each issue is added , it adds it to the 'To Do' list for my project.  as I started working on each issue I move it to the 'In progress' column.  When coding was completed , the issue was then moved to the 'done' column.

![github project](/documentation/images/userstories1.png)
![github project](/documentation/images/userstories2.png)
![github project](/documentation/images/userstories3.png)
![github project](/documentation/images/userstories4.png)
![github project](/documentation/images/userstories5.png)

### Wireframes

I created my wireframes using Balsamiq.

for the home page
![wire home](/documentation/images/wire-home.png)

for the wines page
![wire wines](/documentation/images/wire-wines.png)

for the wines detail page
![wire home](/documentation/images/wire-wine-detail.png)

for the shopping bag page
![wire bag](/documentation/images/wire-bag.png)

for the checkout page
![wire checkout](/documentation/images/wire-check.png)

for the confirmation page
![wire confirmation](/documentation/images/wire-success.png)

for the blog list page
![wire blog](/documentation/images/wire-blog.png)

for the blog detail page
![wire blog detail](/documentation/images/wire-blog-detail.png)

## Existing Features

### Navbar and Footer

#### Navbar

The navbar is plain and simple to make it easy for users to see what is available to them.  On larger screens the navbar is split into a top part and a bottom part. 

![desktop navbar](/documentation/images/desk-navbar.png)

The top part contains the website logo in the top left, a search box in the center and my account option and a shopping bag in the right.  My account gives a dropdown menu for registering or login.  If the user is logged in there is an extra option in the drop down menu from my account for My profile.  If the store owner/superuser is logged in then there is 2 more options available to them : blog management and wine management.

The bottom part of the navbar has 2 drop down menus for users to select different ways of selecting wines. The 'All wines' options gives a dropdown menu where the user can select wine by category, grape, country or price. 
The shop by style dropdown menu allows users to select wines by category ie red,white, rosé or sparkling & champagne. There is also a blog button for users to look at blog posts that the store owner has added. 


In mobile view the logo is removed, some of the navbar items are collapsed into a hamburger menu.

![mobile navbar](/documentation/images/mobile-navbar.png)

The dropdown menu from the hamburger icon gives home, all wines, shop by style and blog.  

![mobile navbar with dropdown](/documentation/images/mobile-nav-drop.png)

The search box is reduced to the word search, but when the user clicks on it the search box appears. The my account and bag are also on the mobile navbar.

#### Footer

On larger screens the footer contains is split into 2 columns, the first is the social media link to Dionne's Wines Facebook page. If the user clicks on the facebook link it will open in a new page.  The second column containes the form from mailchimp for users to enter their email so that they receive direct emails with promotions and discounts.  Under these 2 columns are 3 links to the privacy policy, the 'About Us' page and the FAQ page.

![desk footer](/documentation/images/desk-footer.png)

On mobile the 2 columns stack on top of one another.

![mobile footer](/documentation/images/mobile-footer.png)

### Register page

I have used Allauth for register, login and logout.
When user clicks the register button they will be brought to the register page, where they have to fill in email, username and password.

![signup](/documentation/images/signup.png)

The user has the option of going back to login if they have already signed up or to signup. If the form is filled in correctly and signup button clicked, the user is brought to a page for them to verify their email.  There is also an alert message that confirmation email sent to the users email.

![verify email](/documentation/images/verify-email.png)

The user will get an email with a link to confirm their email.  The link brings them to the page below, to confirm their email. 

![confirm email](/documentation/images/confirm-email.png)

When the user clicks the confirm button, they get a message to say the user has confirmed the email address and they are redirected to the signin page.

![sign in](/documentation/images/sign-in.png)

The user can fill in their username and password and signin or they can return to the home page.  if the user signs in they get a message to say successfully signed in as their username and they are redirected to the home screen.
Now that the user is signed in, the options in My account are now my Profile and logout.
If the user clicks logout, they are brought to a logout page, with the option to either cancel and return to the home page or to sign out.  

![sign out](/documentation/images/sign-out.png)

If they sign out, they get a message to say successfully signed out and returned to the home page.

### Profile page

If a user has signed in they have access to their profile.  Their profile holds their default delivery information and any past orders that they have had.

![profile](/documentation/images/profile.png)

The user can update their delivery information and it is saved to their profile or when they are ordered wine their is an option in the checkout process for them to save their delivery information and it is saved to their profile.

### Home page

The home page can be accessed by clicking the logo 'Dionne's Wines'.  The home page has a hero image of a lady holding a glass of wine, with text 'Buy wine online delivered to your door' and there is an action button for them to shop wines.  At the top of the image there is a banner with 'free delivers on orders over €60'.

![top of home page](/documentation/images/home1.png)

Under the hero image are customer reviews.  There are 4 reviews accross the page.  On mobile the reviews are stacked.

![reviews on home page](/documentation/images/home2.png)

There is a button for users to leave their review.  If they click the leave a review button they are taken to add a review page.

### Add Customer review

![customer review](/documentation/images/cust-review.png)

The user has the option of filling in the review or returning to the home page.  If they fill in the review and submit it they get a message to say successfully added a review.  The store owner has to approve the review before it can be viewed on the site.

### Wine list

When the user shops wines or any other option for wines, they are brought to the wines list page.
This has an image of the bottle, the grape type, the region, the country, price and the category.

![wines](/documentation/images/wines.png)

On larger screens there are 4 bottles accross the screen, going down to 3 accross, then 2 accross, until they are stacked in mobile.  The category tags at the bottom of each bottle of wine also lets the user get all the white wines if they click the white wine tag. If the user clicks the bottle they are taken to the wine detail page.  There is a arrow button to return to the top of the page.

### Wine details

On large screens, there are 2 columns at the top of the page.  The first column holds the image of the bottle.  In the second column holds the details about the wine, with a quantity box. The user can use the + / - buttons or type in the quantity.  There are 2 buttons, one to return shopping and one to add the wine to you bag.

![wine detail](/documentation/images/wine-detail.png)

On mobile the 2 columns are stacked.

If the user adds the wine to their bag, the user gets an alert saying the name of the wine has been added to the bag, and they can see the contents of their bag, the total excluding delivery, how much more they have to spend to get free delivery and a button to go to secure checkout. The user has the option to close the message and continue shopping or to click the go to secure checkout.

![add to bag](/documentation/images/addtobag.png)

At the bottom of the wine detail page is a place for wine reviews.  If wine reviews exist for this wine they are displayed and if not a message is displayed to ask the user to be the first to review the wine.

![wine review](/documentation/images/wine-review.png)

![no wine review](/documentation/images/no-wine-review.png)

### Add wine review page

If the user clicks write a review they are taken to the add wine review page.

![add wine review](/documentation/images/add-wine-review.png)

It has the name of the wine that the user is going to review.  The user fills in the form and clicks add a wine review.  The user gets a message to say successfully added a wine review.  The store owner has to approve the review before it can be viewed on the website.

### Bag page

When the user clicks secure checkout they are brought to the shopping bag page.

![shopping bag](/documentation/images/bag.png)

This page contains the wine information, the price, quantity and subtotal.  At the bottom of the page is the bag total, delivery cost, the grand total.  There is also a message to tell the user how much more they need to spend to get free delivery.  There are 2 buttons at the bottom to either continue shopping or to go to secure checkout.  On the shopping bag page the user can adjust the quantities of each wine and also remove a wine if they want to.  On mobile the information is displayed slightly differently.  The totals are at the top and the wine information is further down the page.  This page can get quite long so I have added a button to return to the top.  If the user clicks go to secure checkout, they are brought to the checkout page.

### Checkout page

The checkout page is split into 2 columns. The first column holds the delivery information for the user and the secong column holds the order summary.  

![checkout](/documentation/images/checkout.png)

If the user is logged in and has saved their delivery details to their profile the form will be filled in with their details.  If it is the users first time to order, they can fill in the checkout page and then select the save these details to my profile, and the next time they will have the form prefilled.  If the user is not signed in they will be given the option to register and login so that they can save their details.

On mobile the 2 columns will be stacked, with the order information first and then the delivery and payment form.

The fields on the form that are required have *. Any error in filling in the form, the page will be reloaded with the error message.
When the complete order button is clicked a spinner is overlayed the whole screen to show the payment is being processed.  If the payment is a success the user gets a succes message with their order number and a message to say that a confirmation email has been sent to the users email.  The user is brought to a confirmation page.

### Confirmation Page

The confirmation page tells the user thanks for the order and that a confirmation email has been sent to the users email.  The order information, delivery information and billing information are all listed.  There is a button at the bottom of the page for the user to continue shopping.

![confirmation page](/documentation/images/confirmation.png)

### blog page

If the user clicks on blog on the navbar, they will be taken to the blog list page.  Each blog has an image, date and a title.  On large scereens there are 3 blogs accross the page, on mobile one blog is stacked on top of the next.

![blog](/documentation/images/blog.png)

If the user wants to read the blog detail they just click on the image and they are taken to the blog detail page.

### Blog detail page

The blog detail page, has the image, title, date and content of the blog.  On large screens it is displayed as 2 columns, with the first column holding the image anf the second column holding the details of the blog.

![blog detail](/documentation/images/blog-detail.png)

On mobile the columns are stacked.

### Store owner / superuser options

For the store owner, they need to be able to add, edit and delete wines.  So if the store owner or superuser is logged in, they have access to wine management from the navbar.  I ahve added security that only superuser can access these pages and even if people try to access them through the urls they will not be able to do so.

![wine mgt](/documentation/images/wine-mgt.png)

If the store owner clicks wine management they are brought to the add wine page.

### Add wine page

![add wine](/documentation/images/add-wine.png)

The fields that are required have an astericks. The store owner can either cancel out of the page or fill in the form and add wine. The category is a drop down box so we can only pick from the categories in the database. When the form is filled in and add wine clicked, the store owner will get a message to say the wine has been successfully added and they are returned to the wine detail page of the wine just added. If an image is not selected then a stock image is added to the wine.

When logged in as store owner /superuser, when they view the wine list page or the wine details page there is an option to edit or delete each wine.  There is added security to ensure that only the store owner can do these operations and people can not access them through the urls.

On the wine list page

![wine list edit delete](/documentation/images/list-edit-del.png)

On the wine detail page

![wine detail edit delete](/documentation/images/detail-edit-del.png)

From either page if the store owner clicks edit they are taken to the edit wine page.  The store owner also gets an alert messgae to say that they are editing and name the wine.

### Edit Wine page

The edit wine page is basically the same as add wine except in edit the details of the wine are populated in the form.

![edit wine](/documentation/images/edit-wine.png)

The store owner can either cancel out of the page or update the fields and then click update wine.  A success message is displayed to say the named wine has been updated and the store owner is brought to the wine detail page for the updated wine.

### Delete wine

If the store owner clicks the delete button for a wine, a message pops up to ask are you sure you want to delete.

![delete confirmation](/documentation/images/del-confirm.png)

If they click ok, then the wine is deleted and they get a message to say the named wine has been deleted.

The store owner can also add, edit and delete blogs.   There is security for this similar to the add wines and to stop people accessing these pages through the urls.The option for Blog management, brings the store user to the add blog page.

### Add blog page

![add blog](/documentation/images/add-blog.png)

The store owner can add title, image and content of the blog.  They can either cancel out of the page or fill in the form and add the blog.  If an image is not selected a stock image is added to the blog.
When the add blog button is clicked, the store owner gets a message to say the blog has been successfully added and they are brought to the blog detail page of the new blog.

When signed in as the store owner or superuser when they are viewing the blog list or blog detail page the edit and delete buttons are visible.

![blog edit del](/documentation/images/blog-edit-del.png)

If the store owner clicks the edit button, they are brought to the edit blog page.

### Edit Blog page

The edit blog page is very similar to the add blog page, except the details of the blog being edited are already pre-filled.

![edit blog](/documentation/images/blog-edit.png)

The store owner can either cancel out of the page or edit the blog and click update blog.
When update blog is clicked, a success message is shown and they are brought back to the blog detail for the edited blog.

### Delete blog

If the store owner clicks delete for a blog, a message pops up to make sure they mean to delete the blog.  If they click yes, the blog is deleted and a message is shown that the blog has been deleted.

### Approve customer and wine reviews

The store owner / superuser has to approve the customer and wine reviews.  When the reviews are added they have a status of 'draft' and the store owner has to change this to 'published'.  At the moment this has to be done through the admin screen.  Only when the review has a status of  published will it appear on the website.

## Future Features

- to actually show the ratings in stars and have no number.
- to have the approval of the customer and wine reviews from the website and not through admin.
- to make the delete process look nicer for delete wines and delete blogs.
- have the customer reviews on a loop that you can see all the review not just the must recent 4.

## Design

The design is kept simple to let the wines take centre stage and also to make it easier for users to navigate through the site.  The buttons throughout are the same to give the user a consistent experience.

### Data Models

#### Blog App - Blog model

##### Blog Model
Blog model contains the title, image and content of the blog. I have a slug field that I use as the url for the blog detail page.

| Key | Name | Type |
|-------|---------|------------|
| | title (unique) | CharField |
| label for url | slug (unique) | SlugField |
| | image | ImageField |
| | image_url | URLField |
| |  date_created | DateTimeField |
| | content | TextField | 

#### Checkout app - Order and OrderLineItem model

##### Order model
Order Model contains the delivery information for the user, date, costs and information from the users bag
| Key | Name | Type |
|-------|---------|------------|
| | order_number (unique) | CharField |
| Foreign key | user_profile | UserProfile model|
| | full_name | CharField |
| | email | EmailField |
| | phone_number | CharField |
| | street_address1 | CharField | 
| | street_address2 | CharField | 
| | town_or_city | CharField | 
| | county | CharField | 
| | country | CharField | 
| | postcode | CharField | 
| | date | DateTimeField | 
| | delivery_cost | DecimalField | 
| | order_total | DecimalField | 
| | grand_total | DecimalField | 
| | original_bag | TextField | 
| | stripe_pid | CharField | 

##### OrderLineItem
Order Line item model holds the detail information of what the user had in their shopping bag.

| Key | Name | Type |
|-------|---------|------------|
| Foreign Key | order | Order Model |
| Foreign Key | wine | Wine Model |
|  | quantity | IntegerField |
| | lineitem_total | DecimalField |

#### Home app - CustomerReview model
##### CustomerReview Model
The customer review model is a stand alone model and isn't linked to any other model.
| Key | Name | Type |
|-------|---------|------------|
|  | name | CharField |
|  | rating | IntegerField |
|  | is_customer | BooleanField |
|  | comment | TextField |
|  | date_created | DateTimeField |
|  | status | IntegerField |

#### Profile app - UserProfile model
##### UserProfile model
The userprofile model holds default delivery information similar to what is saved in the order model.
| Key | Name | Type |
|-------|---------|------------|
| | user | User model |
| | default_full_name | CharField |
| | default_email | EmailField |
| | default_phone_number | CharField |
| | default_street_address1 | CharField | 
| | default_street_address2 | CharField | 
| | default_town_or_city | CharField | 
| | default_county | CharField | 
| | default_country | CharField | 
| | default_postcode | CharField | 

#### Wines app - Category, Wine and WineReview Model
##### Category model
The differnet categories in the category model are red, white, rosé and sparkling
| Key | Name | Type |
|-------|---------|------------|
|  | name | CharField |
|  | friendly_name | CharField |

##### Wine Model
The wine model holds all the information about each individual wine
| Key | Name | Type |
|-------|---------|------------|
| Foreign Key | category | Category Model |
|  | name | Charfield |
|  | grape | Charfield |
|  | description | Textfield |
|  | price | Decimalfield |
|  | region | Charfield |
|  | country | Charfield |
|  | vintage | Integerfield |
|  | image_url | URLfield |
|  | image | Imagefield |

##### WineReview Model
The wine review is linked to a particular wine and gives a rating and a review of the wine.
| Key | Name | Type |
|-------|---------|------------|
| Foreign key | wine | Wine Model |
|  | name | CharField |
|  | rating | IntegerField |
|  | is_customer | BooleanField |
|  | review | TextField |
|  | date_created | DateTimeField |
|  | status | IntegerField |

### Typography

The font I have selected for the website is Lato.  I have used Cedarville Cursive for the brand.  They have been selected as they are clear and simple.

### Images /color

I have kept the layout and colours simple, to let the wines take center stage.

## Technologies used

### Languages

- HTML 
- CSS 
- JavaScript
- Python

### Frameworks, libraries & programs

- Django
- Bootstrap
- Google Fonts
- Font awesome for icons
- Github/gitpod
- AWS used to host static files
- Gunicorn as a server for Heroku
- Heroku used for cloud based deployment
- crispy forms
- Heroku Postgres for production database
- Sqlite for local environment database
- Pillow
- Django-countries
- Django-allauth for registration, login & logout
- Stripe payments 
- dj-database
- psycopg2


## Code Validation

### HTML validation
To validate each of my html pages I inspected the page through devtools and viewed the page source and copied and pasted into the W3C markup validation service.

for sign up page
![html sign up](/documentation/validation/html-signup.png)

for login page
![html login](/documentation/validation/html-login.png)

for logout page
![html logout](/documentation/validation/html-logout.png)

for home page
![html home](/documentation/validation/html-home.png)

for add customer review page
![html add customer review](/documentation/validation/html-cust-review.png)

for wines page
![html wine list](/documentation/validation/html-wines.png)

for wine detail page
![html wine detail](/documentation/validation/html-wine-detail.png)

for add wine review
![html wine review](/documentation/validation/html-wine-review.png)

for add wine page
![html wine add](/documentation/validation/html-wine-add.png)

for edit wine page
![html wine edit](/documentation/validation/html-wine-edit.png)

for bag page
![html bag](/documentation/validation/html-bag.png)

for checkout page
![html checkout](/documentation/validation/html-check.png)

for confirmation page
![html checkout-success](/documentation/validation/html-check-success.png)

for profile page
![html profile](/documentation/validation/html-profile.png)

for blog
![html blog list](/documentation/validation/html-blog.png)

for blog detail
![html blog detail](/documentation/validation/html-blog-detail.png)

for blog add
![html blog add](/documentation/validation/html-blog-add.png)

for blog edit
![html blog edit](/documentation/validation/html-blog-edit.png)

for privacy page
![html privacy](/documentation/validation/html-privacy.png)

for about us page
![html about us](/documentation/validation/html-about.png)

for FAQ page
![html faq](/documentation/validation/html-faq.png)

### CSS validation

for base.css

![css base](/documentation/validation/css-base.png)

for blog.css

![css blog](/documentation/validation/css-blog.png)

for checkout.css

![css checkout](/documentation/validation/css-checkout.png)

for profile.css

![css profile](/documentation/validation/css-profile.png)

### pep8 validation

I copied and pasted my python files into the PEP8CI validator.

for bag>apps
![pep8 bag-apps](/documentation/validation/pep8-bag-apps.png)

for bag>contexts
![pep8 bag-context](/documentation/validation/pep8-bag-context.png)

for bag>urls
![pep8 bag-urls](/documentation/validation/pep8-bag-urls.png)

for bag>views
![pep8 bag-views](/documentation/validation/pep8-bag-views.png)

for bag>bag-tools
![pep8 bag-tools](/documentation/validation/pep8-bag-bagtools.png)

for blog>admin
![pep8 blog-admin](/documentation/validation/pep8-blog-admin.png)

for blog>apps
![pep8 blog-apps](/documentation/validation/pep8-blog-apps.png)

for blog>forms
![pep8 blog-forms](/documentation/validation/pep8-blog-forms.png)

for blog>models
![pep8 blog-models](/documentation/validation/pep8-blog-models.png)

for blog>urls
![pep8 blog-urls](/documentation/validation/pep8-blog-urls.png)

for blog>views
![pep8 blog-views](/documentation/validation/pep8-blog-views.png)

for checkout>admin
![pep8 checkout-admin](/documentation/validation/pep8-check-admin.png)

for checkout>apps
![pep8 checkout-apps](/documentation/validation/pep8-check-apps.png)

for checkout>forms
![pep8 checkout-forms](/documentation/validation/pep8-check-forms.png)

for checkout>models
![pep8 checkout-models](/documentation/validation/pep8-check-models.png)

for checkout>signals
![pep8 checkout-signals](/documentation/validation/pep8-check-signals.png)

for checkout>urls
![pep8 checkout-urls](/documentation/validation/pep8-check-urls.png)

for checkout>webhook_handler
![pep8 checkout-webhook-handler](/documentation/validation/pep8-check-webhook-handler.png)
I have 2 lines that are too long but I couldn't find a way of splitting the line with the same functionality

for checkout>webhooks
![pep8 checkout-webhooks](/documentation/validation/pep8-check-webhooks.png)
I have 1 line too long, that I couldn't split.

for dionnes>settings
![pep8 dionnes-settings](/documentation/validation/pep8-dionnes-settings.png)

for dionnes>urls
![pep8 dionnes-urls](/documentation/validation/pep8-dionnes-urls.png)

for dionnes>views
![pep8 dionnes-views](/documentation/validation/pep8-dionnes-views.png)

for home>admin
![pep8 home-admin](/documentation/validation/pep8-home-admin.png)

for home>apps
![pep8 home-apps](/documentation/validation/pep8-home-apps.png)

for home>forms
![pep8 home-forms](/documentation/validation/pep8-home-forms.png)

for home>models
![pep8 home-models](/documentation/validation/pep8-home-models.png)

for home>urls
![pep8 home-urls](/documentation/validation/pep8-home-urls.png)

for home>views
![pep8 home-views](/documentation/validation/pep8-home-views.png)

for profile>apps
![pep8 profile-apps](/documentation/validation/pep8-prof-apps.png)

for profile>forms
![pep8 profile-forms](/documentation/validation/pep8-prof-forms.png)

for profile>models
![pep8 profile-models](/documentation/validation/pep8-prof-models.png)

for profile>urls
![pep8 profile-urls](/documentation/validation/pep8-prof-urls.png)

for profile>views
![pep8 profile-views](/documentation/validation/pep8-prof-views.png)

for wines>admin
![pep8 wines-admin](/documentation/validation/pep8-wines-admin.png)

for wines>apps
![pep8 wines-apps](/documentation/validation/pep8-wines-apps.png)

for wines>forms
![pep8 wines-forms](/documentation/validation/pep8-wines-forms.png)

for wines>models
![pep8 wines-models](/documentation/validation/pep8-wines-models.png)

for wines>urls
![pep8 wines-urls](/documentation/validation/pep8-wines-urls.png)

for wines>views
![pep8 wines-views](/documentation/validation/pep8-wines-views.png)
I have 1 line that is too long and I couldn't find a way to split it.

for wines>widgets
![pep8 wines-widgets](/documentation/validation/pep8-wines-widgets.png)

### JS validation
I pasted js code into JS validator
for js at the bottom of bag.html
![js bag.html](/documentation/validation/js-bag.png)

for blog.js file
![js blog.js](/documentation/validation/js-blog.png)

for stripe_element.js file
![js stripe](/documentation/validation/js-stripe.png)

for wines.js file
![js wines.js](/documentation/validation/js-wines.png)

for quantity_input_script.html
![js quantity script](/documentation/validation/js-quantity-script.png)

for add-wine.html
![js add-wine](/documentation/validation/js-add-wine.png)

for wine-detail.html file
![js wine-detail](/documentation/validation/js-wine-detail.png)

## Testing

### Manual Testing

I checked each page to make sure everything looked ok at all screen sizes.  I also got family and friends to test my site on their different devices.

I am going to use my user stories as the structure for my manual testing.  The testing was carried out on my development website and the fully deployed site on heruko.

Firstly I am going to check the navbar and footer as these elements do not fall clearly into any of the user stories.

Desktop navbar  

When the logo is clicked brings you to the home page - yes  
I get an error when I don't enter a search criteria but click the search button - yes  
When not logged in the My account dropdown gives register and login - yes  
When I click the shopping bag it brings me to the shopping bag page. -yes  

Mobile navbar  

The hamburger icon drops down to give home because the logo is hidden in mobile as there isn't enough room.  Also has the all wines, shop by style and blog -yes  
Clicking search opens the search box - yes  
If not logged in the my account drops down register and login - yes  
Clicking shopping bag brings you to shopping bag page - yes  

Desktop/Mobile footer  

Link to facebook page - opens dionne's wines facebook page on a new tab - yes  
Mailchimp adding email, gets success message and checked email is added to mailchimp account -yes  
About us, privacy and FAQ pages all open to correct pages - yes  

#1 easily register for account / #3 email confirmation

On the signup page, you have to enter correct data in all the fields, the email must be a proper email address, the username must be at least 4 characters you must enter the same password twice or you get a warning message - yes  

![test signup](/documentation/testing/test-signup.png)

When the form is filled in correctly, user is redirected to a verify your email address and a message to say an email has been sent to the email entered to confirm.  There is also an alert message to tell the user the email has been sent to and gives the email address.
When you go to the link in the email it brings you to this page.

![test email](/documentation/testing/test-confirm.png)

When you click the confirm button you are brought to the login page.  There is also a message to say the user has been confirmed.

![test email confirm message](/documentation/testing/test-email-mess.png)

#2 easily login and logout

The login form has to be filled in, or get error message, user and password have to match. When click login, you get a success message - you have successfully logged in as username.
When logged in the options in my account dropdown change to profile and logout - yes  
When I click logout, I am brought to a logout page to check I resally want to logout, if click sigout, I get a message to say you have logged out.

#4 view a list of wines

I can view the list of wines, and the back to top button works - yes

#5 view wine details

When you click on the bottle of wine it takes you to the detail on this wine -yes

#6 sort list of wines

Check the all wines dropdown menu works and retrieves the correct wine in the correct order - yes  
Check that the sort by box works and again shows the correct wines in the correct order - yes

#7 search for wines / #8 easily see what searched for

Check that the search word is present in the returned wines -yes  
The search word/s is clearly visible and the search result - yes

![test search result](/documentation/testing/test-search.png)

#9 view categories of wines

Categories of wine can be searched by the dropdown menu - shop by style.  
Checked that for example all red wines are returned when search for red - yes  
Each wine also has a tag with the category that they are in, if this tag is clicked it returns all wines in this category - yes

#11 select quantity

The - button is disabled so can't go below 1 - yes  
If you type 0 you get a warning message to say quantity must be greater than 0 - yes  
The arrows won't let me go below 1 - yes  
Can't go above 99 with + or arrows - yes  

#12 view items in bag

When user clicks add to bag, a success message shows that the particular wine has been added to the bag.  The contents of the bag are shown, with the cost excluding delivery and also how much more the user has to spend to get free delivery.

![test add to bag](/documentation/testing/test-add-to-bag.png)

If the user clicks the go to secure checkout button, they are brought to the shopping bag page.  The user can also get to this page by clicking on the bag in the navbar - yes  
The shopping bag page shows the name of the wine, a small image, the price, quantity and subtotal - yes

#13 adjust quantity in bag

If the user adjusts the quantity on the shopping bag page, they get a message to say updated the name of the wine to new quantity.  The sub total, delivery and grand total are all updated - yes  
The bag total in the navbar is also updated correctly - yes  
When items are removed from the bag again everything is updated as before, the user gets a message to say the name of the wine has been removed - yes  
If everything is removed the user gets the shopping bag page with a message nothing in their shopping bag - yes

#10 view total cost of my purchases

While the user is adding items to their bag, each time they add something or remove something a message pops up to confirm what action they have taken and a small version of their bag with the total excluding delivery and how much more they have to spend to get free delivery.  When they click on either the bag on the navbar or the go to secure checkout, they are brought to the shopping bag page which has each item they have added to their bag, with quantity, price and subtotal, then the bag total, the delivery cost if any and the grand total.

![test total cost](/documentation/testing/test-tot-cost.png)

#15 secure checkout / #16 quick and easy checkout

When the user clicks secure checkout they are brought to the checkout page - yes  

![test checkout](/documentation/testing/test-check.png)

All the required fields have astericks, so if the user does not fill all of these in they get a message to please fill in the field.  The email must be the format of an email.

![test fields](/documentation/testing/test-fields.png)

If the card number isn't filled in correctly or is invalid as message shows up - yes  

![test card](/documentation/testing/test-card.png) 

The card information must all be correct and match.  For testing purposes I have used card number
4242424242424242, date in future, cvc123.

If the user is signed in and have not updated their profile information, in the checkout page their email address will be already in the form.

![test signed in email](/documentation/testing/test-signedin.png)

Signed in users will also have the option to save their delivery information to their profile, which means if they do, when they return to the checkout page for their next purchase the form will be prefilled for them.  
For logged in user checkout form is prefilled - yes  

![test option to save info](/documentation/testing/test-opt-save.png)

Users that are not logged in are given the option to login or register instead of the option to save their information. 

To test I am completing an order for €19.80 using the card details below - yes

![test pay](/documentation/testing/test-pay.png)

The user is brought to the confirmation page with the order number and details -yes 

![test pay confirmation](/documentation/testing/test-confirm-pay.png)

Checked in stripe to make sure the payment was successful -yes  

![test stripe](/documentation/testing/test-stripe.png)

Also check the webhook was successful

![test stripe webhook](/documentation/testing/test-webhook.png)

And finally check in the database to make sure the order has been added -yes

![test order in db](/documentation/testing/test-order-admin.png)

If for some reason the user clicks out of the browser when their payment is being processed, the webhook checks if the order has been written to the database and if not the webhook handler writes the order to database.  I can produce this situation by commenting out my form.submit in stripe_element.js.  
payment successful stripe - yess  
webhook successful - yes
order in database - yes

#17 order confirmation

When payment has been processed the user is brought to confirmation page and an email is sent to the user with the order details

![test order email](/documentation/testing/test-email-confirm.png)

#14 User profile

When a user registers, a user profile is set up for them. It is empty appart from their email address that they used to register with. The user has 2 options they can go into my profile from the navbar and save their details or through the checkout process documented above they have the option of saving their delivery details so that the next time through the checkout process their details will be prefilled in the checkout form.

Also on the profile page is the users past orders that they can click on the individual orders and see the details.  

The profile form fields can be updated by the user and then they can click the update button to save these changes.

![test profile](/documentation/testing/test-profile.png)

I have security in place so that a non logged in user cannot access this page and if they try to from the url they get taken to the login page - yes  

#18 free delivery threshold

Check that they free threshold is working correctly.  
if the user has spent more than €60, they have free delivery - yes  
if the user has spent less than €60, there is a message to say how much more they have to spend to get free delivery - yes  

#19 add a wine

This is only available to the store owner, if a not logged in user tries to get to the add wine page they are redirected to the sign in page - yes 
If a logged in user not the store owner tries to access the add wine page they get an error message - yes  

![test user not store owner](/documentation/testing/test-err.png)

The store owner has the option from the navbar for wine management -yes  

![test wine management](/documentation/testing/test-wine-man.png)

When they click wine management they are brought to the add wine page - yes  

![test add wine](/documentation/testing/test-add-wine.png)

The required fields have astericks and need to be filled or the user gets an error - yes  
The category field is a dropdown box.  If the store owner needs to add another category they will have to go to admin to add it and then the new category will be available here - yes 
If the price has too many digits - max is 6 you get error - yes 
Also get an error message failed to add wine - yes   

![test error add wine](/documentation/testing/test-err-add-wine.png)

if wine is successfully added you get a success message to say the name of the wine has been added and the user gets brought to the wine detail page for the new wine - yes  
If an image is not selected then a stock image is used - yes  

#20 edit a wine

Again there is security in place to only allow the store owner - yes  

The store owner has access to edit and delete any wine from the store - yes  

![test edit button](/documentation/testing/test-edit-but.png)

When the store owner clicks edit, they are brought ot the edit wine page - yes 
They also get a message that they are editing the name of the wine - yes   
the edit wine page is very similar to the add wine page and the same field validation is in place so the price can't be greater than 6 digits etc -yes  

![test edit wine](/documentation/testing/test-edit-wine.png)

When update wine button is clicked, the store owner gets a message that the wine name has been updated and they are brought to the wine detail page for this wine - yes  

#21 delete a wine

Again the security is in place that only the store owner can delete wines - yes  

When the delete button is clicked, a message to make sure they want to delete the wine is displayed and they have to click ok for the deletion to go ahead - yes  

![test delete wine](/documentation/testing/test-delete.png)

A message to say the name of the wine has been deleted - yes  
They are redirected back to the wines page - yes  

#22 view blog list

All users can access the blogs.  When a user clicks blog on the navbar they are taken to the blog page. This contains an image and a title for each blog - yes  

![test blog](/documentation/testing/test-blog.png)

#23 view blog details

By clicking on the image of the blog brings the user to the blog detail page for that blog - yes  

![test blog detail](/documentation/testing/test-blog-detail.png)

At the bottom of the page there is a return to blogs and this brings them back to blog page - yes  

#24 add blog

Only the store owner can add blogs, there is security in place so if another users tries to access the add blog page they are redirected to the login page - yes  
The store owner can access add blog page by going to their account on navbar and clicking blog management - yes  

![test add blog](/documentation/testing/test-add-blog.png)

The store owner must add a title and content for the blog, if either of these fields are left blank they get an error message - yes  
If the store owner does not add an image a stock image will be added - yes
When add blog button is clicked, they are brought to the blog detail page for the new blog and there is a success message successfully added blog - yes  

#25 edit blog

When the store owner is logged in, edit and delete buttons are available to them- yes 
If a user that is not logged in tries to access the edit blog screen through the urls will be redirected to the login page - yes    
Other signed in users trying to access the edit blog page will get a message to say only store owners are allowed to edit - yes  

![test edit blog button](/documentation/testing/test-edit-blog-but.png)

When edit button is clicked it brings the store owner to the edit blog page - yes  

![test edit blog](/documentation/testing/test-edit-blog.png)

The store owner gets a message to say they are editing the name of the blog - yes  
Similar to the add blog the title and content fields must have something in them - yes  
Again if an image is not selected a stock image will be used.

When the update blog button is clicked, they are redirected to the blog detail page for the edited blog and they get a message to say successfully edited blog - yes  
 
#26 delete blog

Again the security is in place that only the store owner can delete blogs - yes  

When the delete button is clicked, a message to make sure they want to delete the blog is displayed and they have to click ok for the deletion to go ahead - yes  

![test delete blog](/documentation/testing/test-delete-blog.png)

A message to say the name of the blog has been deleted - yes  
They are redirected back to the blogs page - yes  

#27 view customer reviews

Customer reviews are displayed under the hero image on the home screen - yes  
The reviews are in order with the most recently added first - yes  

![test customer reviews](/documentation/testing/test-cust-review.png)

#28 add customer review 

Any user whether they are logged in or not can leave a customer review.
When the add a review button is clicked it brings the user to add a review page

![test add customer review](/documentation/testing/test-add-cust-review.png)

The user does not have to fill in their name, but must give a rating and a comment, if not they get an error - yes  
When they click add a review, they are redirected back to the home page and also get a message to say successfully added a review - yes  
The store owner has to approve or publish the review before they can be seen on the website.
If the reviewer is a logged in user, the review should have verified customer - yes  

![test approve review](/documentation/testing/test-approved-cust-review.png)

When store owner approves a review it is then visible - yes 

#29 view wine review

Wine reviews are listed under the wine in the wine detail page.

![test wine reviews](/documentation/testing/test-wine-review.png)

If no review exists for this wine a message is displayed - be the first to leave a review of name of wine.    
Any user whether they are logged in or not can leave a review - yes  

![test no wine reviews](/documentation/testing/test-no-wine-review.png)

#30 add wine review

Any user whether they are logged in or not can leave a wine review.
When the write a review button is clicked it brings the user to add a wine review page - yes  

![test no wine reviews](/documentation/testing/test-no-wine-review.png)

The user does not have to fill in their name, but must give a rating and a review, if not they get an error - yes  
When they click add a wine review, they are redirected back to the wine detail page and also get a message to say successfully added a wine review - yes  
The store owner has to approve or publish the review before they can be seen on the website.
When the store owner approves/publishes a wine review it is then visible - yes  
If the reviewer is a logged in user, the review should have verified customer - yes  

#31 publish reviews

The store owner has to go into admin panel to change the reviews from draft to published so that they can be visible on the website - yes  

#32 email marketing - mailchimp

***  need to do in deployed site

#33 privacy policy

When the privacy button on the footer is clicked, the user is taken to the privacy policy page - yes  

![test privacy](/documentation/testing/test-privacy.png)

#34 about us

When the About Us button on the footer is clicked, the user is taken to the About Us page - yes  

![test about us](/documentation/testing/test-about.png)

#35 faq

When the FAQ button on the footer is clicked, the user is taken to the FAQ page - yes  

![test FAQ](/documentation/testing/test-faq.png)

#36 messages

I have mentioned the messages that appear due to users actions throughout the testing above.  

test for 404 - page not found

When you check for a page that does not exist, the user gets a 404 page - yes  



### Lighthouse

## Deployment, forking and making a clone

I have included a env.sample file to show what keys etc are required for this project.

## Web Marketing

Dionne's Wines is a business to customer business, where we want to reach as many customers as possible, to sell as many bottles of wine as possible.  We want to do this in a way to attract new customers but also retain our existing customers.

### Search Engine Optimisation (SEO)

Keywords for search engine optimisation: buying wine, wine delivery, wines delivered to your door, wines online Ireland, online wine delivery Ireland, wines delivered, buy wine online, buy wine, wines online.
I improved my search engine optimization by using semantic html and using strong tags to emphasize relevant words. I revisited my anchor tags and checked the text to make sure I was using keywords where appropriate.  I have included the meta tags in the head of my base.html to include my keywords.

### Content Marketing

Dionne's Wines has included meaningful content to attract new customers and retain customers, with the description of each wine. Also including other customers feedback on their buying experience with Dionne's Wines, which will hopefully evoke an emotional response to build trust and loyalty. Sharing customers reviews of the individual wines gives new and existing customers more information to help them make decisions on what to buy. Finally their are blog posts to give customers information on new wines and vineyards that the wines are from.  This shows off Dionne's Wines expertise and positions them as a reliable, trustworthy source of information.  Content marketing must work closely with SEO and social media.  Dionne's wines will have to add interesting and relevant blog posts on a regular basis to keep their customers engaged and informed.  It also needs to be organised and consistent in order to build up their reputation.

### Social Media Marketing

Social media allows you to share content that attracts relevant customers and keep in touch with how customers feel about your brand. Dionne's Wines can do this through their facbook page.  This extends their reach to new potiential customers. Dionne's Wines will have to post regularly to their facebook page with interesting articles, new wines available and special offers, to remind their followers of what they are offering, this pairs very nicely with content marketing.  As Dionne's Wines is a small growing business this will be done organically first, as this is free.  This will build Dionne's Wines identity and become recognisable to customers.  There is a risk that there could be negative feedback about Dionne's Wines, which would abviously be bad for business.

### Email marketing

Email marketing is an area that all e-commerce businesses can benefit from, costs are low and you don't need to invest much time, to gain new customers and retain existing customers.  The problem is spam, so they have to try and give the user content that is useful - like discount codes or promotions. Email markeing must be GDPR compliant, users must opt in.  Dionne's Wines have a mailchimp sign up form on the footer of their website so users can sign up.

Dionne's Wines users are online users searching for wines to be delivered to their home. Lots of my potiential customers would have social media accounts.  They may need information on wines, what wines to drink on certain occasions, what wines to drink with certain foods. This is were my blog post with interesting blogs on different wines, maybe new wines, what wines are most popular.  Also giving users themselves the opportunity to rate/review wines that they have tried that other users can read and decide whether to try.
Also users being able to rate/review the buying process from my website to build trust and encourage others to buy and if a user has a bad experience then try and fix it to improve the overall offering by my website.
The goals of my business is to sell as much wine as possible but to also encourage new customers to buy while also retaining existing customers.
As we are a small business email marketing which is relatively cheap to communicate with potiential customers to tell them about special offers and discounts, or new wines that are available.  Also have a presence on social media platforms like facebook, promoting special offers and also sharing content that is useful and of benefit to potential customers.

I created sitemap.xml file from www.xml-sitemaps.com
I created robots.txt file to acknowledge that search engines are allowed on this site and that they can have free access to it.

Dionne's Wines Facebook page
![facebook](/documentation/images/facebook.png)

## Credits

- images and descriptions of wines taken from winesdirect.com
- about us page based on winesdirect.ie and O'briens wines
- content of blogs from winesdirect.ie
- basic structure of store from Boutique Ado

## Acknowledgements
- I would not have completed this project without the support and understanding of my family and friends.
- Wonderful help and support from my cohort and facilitator Kasia.
- Help and support from my mentor Celestine Okoro.
