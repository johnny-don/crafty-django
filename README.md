[![Build Status](https://travis-ci.com/johnny-don/crafty-django.svg?branch=master)](https://travis-ci.com/johnny-don/crafty-django)

# CRAFTY

Crafty e-commerce App - milestone project 4

This is a a fictional website where carpenters can post their pieces online for sale and customers can purchase original pieces from them. The app removes the need for the carpenter to have his own personal website or store and the customer is guaranteed an orignal piece of work.


# DEMO

A live demo of this project can be found [here](https://crafty-django.herokuapp.com/). This app is hosted on Heroku using a Postgres database.

# UX

This site is intended for customers and sellers. It provides a meeting place for people who want original pieces of furniture but do not know where to find such pieces. It also gives carpenters a market for their pieces without the hassle of setting up their own personal website or renting a shop front.

I tried to keep the design as minimalist and sleek as possible. I chose a select range of colors and a common body image and header layout for every page. The site is designed to be very simple to use as the seller and customers may not be used to purchasing goods online.

This site is only available to people with an account. This allows for exclusivity and an ability to assure the customer of the validation of the seller. Once you arrive on the homepage you are either brought straight to the Products (if you are already logged in) or you are urged to login or register. Once registered you can both buy and sell products simualtaneously. You can also view your profile, I wasn't able to add the user's posted products to their profile but I hope to implement this in future versions. In the navbar you can also search for products from the product database. The footer is deliberately minimal as to keep with the minimal theme. 

When you have chosen a product to purchase you can then add it to your cart. This affords the customer the opportunity to purchase more items instead of being aken directly to the checkout. When they have finally decided on their order the can then go to the checkout where their order is displayed and the payment form is presented. 

I used [bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/) when styling this app. This allowed me to create a uniform and responsive design. Django bootstrap forms was also used to style the forms and give them a uniform look.

I aimed to create a site that is uniform, minimal and easy to navigate. The font and font colors are uniform and the buttons are also similar.

# TECHNOLOGIES

1.Django 
2.Heroku
3.Postgres Database (mySQL)
4.Stripe Payment
5.JavaScript/jQuery
6.HTML
7.CSS
8.Bootstrap (4)
9.Travis
10.Github

# DEVELOPMENT PROCESS

I started by focusing on the backend. I created a diagram of the navigation that I wanted for the site. I planned my urls, views and models and focused on their functionality. During this process I came across many problems and it took me a lot longer than expected.

Once I got the functionality working I then focused on the design. The CSS is custom and I worked off the bootsrap grid system.

Once I was happy with my app I tested it on Travis, bought a product using Stripe and deployed it to Heroku.

# TESTING

AUTOMATED TESTING

Testing was done by Travis-CL. 

During testing there were numerous problems with the requirements.txt file. I had to go through each entry and delete the ones that were not needed and were creating errors in my testing.


MANUAL TESTING

Manual testing was done on all the functionality of the site. The products were successfully loaded and stored in the database, same with the profile of the user. Products were added to the cart and moved to the checkout successfully and the Stripe payment function has been verified with a test card and all transactions show up on the Stripe dashboard.

I tested the app on Chrome, Firefox and Opera browsers and on a Samsung smartphone. I noticed that sometimes on Firefox the navbar didnt take up the whole width of the screen. Also the hamburger icon on smaller screens doesn't close when pressed. It briefly closes but then reopens again.

# FEATURES

Only registered users can use the site. When they are registered they have the option to buy products or sell products. They have the ability to post a detailed description of the product that they want to sell, they can confirm the origin of their wood and set their own price. 

The customer can navigate through all the products or search for a specific product in the search bar. When they decide to buy the product they can add it to their cart. If they later choose to not buy the product they enter a quantity of 0 and the item is deleted from the cart.

They checkout gives the customer a summary of their order and the total price. They can then purchase the item using Stripe.

FEATURES LEFT TO IMPLEMENT

I would like to add the users purchased or posted products to their user profile. I would also like to add a interactive feature where the customers and the sellers can communicate and the customers can request specific designs from the seller. 

# KNOWN ISSUES

The navabr doesn't stretch the width of the page on some browsers. 
The hamburger icon collapsable menu is automatically opn and only briefly shuts when clicked.
Sometimes the borders of the products were appearing blue.
After trying every method of clearning cache and hard resets I still had a recurring problem with cloud 9, it sometimes didn't render my CSS. 

# CREDITS

CONTENT

All content was written by me.

MEDIA

The background image was taken from [Pexels](https://www.pexels.com/) and the product images were from google images

ACKNOWLEDGEMENTS

The majority of the layout and design was taken from bootstrap. I used slack and tutor support for most of my problems and the majority of the functionality came from the ecommerce mini project from Code Institute.