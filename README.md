# Dionne's Wines

## Purpose of this site

This site has been created so that users can buy wine from the store.  Users can also read the wine descriptions to help decide what to buy.  They can also read the blog posts about new wines, vineyards etc.  Users can also add reviews about their shopping experience and also review individual wines that they have bought.  These reviews are available for all users to view.  The store owner/ superuser can add, edit and delete wines available for sale.  The store owner can also add blog posts for all users to view.  All users can but from the store whwther they are logged in or not.  The advantage of logged in users is that their delivery information can be stored and also their order history is displayed in their profile.

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

### Agile Development Tool

I am using an agile software development tool in the development of this website.  I am using Github Projects, using a basic Kanban Template.  I addded automation so that as each issue is added , it adds it to the 'To Do' list for my project.  as I started working on each issue I move it to the 'In progress' column.  When coding was completed , the issue was then moved to the 'done' column.

![github project](/documentation/images/userstories1.png)
![github project](/documentation/images/userstories2.png)
![github project](/documentation/images/userstories3.png)
![github project](/documentation/images/userstories4.png)
![github project](/documentation/images/userstories5.png)

### Wireframes

## Existing Features

### Navbar and Footer
### Register page
### Profile page
### Home page
### Wine list
### Wine details
### bag page
### checkout page
### blog page

## Design

The design is kept simple to let the wines take centre stage and also to make iteasier for users to navigate through the site.  The buttons throughout are the same to give the user a consistent experience.

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

### Images /color

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
for bag page
for checkout page
![html checkout](/documentation/validation/html-check.png)
for confirmation page
![html checkout-success](/documentation/validation/html-check-success.png)
for profile page
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
### pep8 validation

## Testing

### Manual Testing

### Manual Testing

- remember to test 404 handler - check refactor video part 4

### Lighthouse

## Deployment, forking and making a clone

I have included a env.sample file to show what keys etc are required for this project.

## Web Marketing

Dionne's Wines is a business to customer business, where we want to reach as many customers as possible, to sell as many bottles of wine as possible.  We want to do this in a way to sttract new customers but also retain our existing customers.

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
