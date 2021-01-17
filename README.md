# shopify-backend-challenge
Photo gallery for Shopify backend internship challenge

## Intro
Hello Shopify team! Thank you for taking the time to review my submission for the backend developer intern role. I'm very excited for you to evaluate my work! In response to the challenge prompt "create a photo repository", I've developed and deployed a simple Django web app (deployed on Heroku) that models a photo store for buying and selling images. 

## Run app remotely
If you want to access the photo store directly, you can access it [here](https://paulhinta-shopify-backend-2021.herokuapp.com/). The rest of the usage instructions will also be pasted in the [about](https://paulhinta-shopify-backend-2021.herokuapp.com/about/) page.

## Run app locally:
You can also install the repo onto your computer and run the program locally. There is already a virtual environment created, so you can activate it using:
```bash
cd shopify-backend-challenge
```
Then activate venv:
### Windows:
```bash
venv\Scripts\activate
```
### Mac:
```bash
source venv\bin\activate
```
Then run the app using:
```bash
cd src

python manage.py runserver
```
Now, the web app should be running on [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## App explanation & basic instructions:
To get started, you can create a username and password (email is required). Then, you can navigate to the home page, where you will see displayed in a 3x10 grid all of the photos on the site, in reverse chronological order. At any point, you can click the photo name to view details of the photo, or click the username of the user who uploaded the photo to view all photos that that user has uploaded.

Each upload is an instance of the django model "Photo", which can be found under "src/store/models.py". You'll notice that a Photo will have many attributes: </br>
                - Title </br>
                - Author (which is the user who uploaded the photo) </br>
                - Pic (which contains the photo data of the object) </br>
                - Price </br>
                - Description </br>
                - Available (which indicates whether or not the Photo is currently listed for purchase) </br>
                - Featured (which indicates whether the site has decided to feature the Photo on the featured page. In a complete version, the site would construct an algorithm which allows certain photos to be featured; for instance, this algorithm could sort them by what's trending at the moment.) </br>
                - Date Posted </br>
                - Thumbnail (which contains a lower resolution rendering of the Pic attribute, as well as the words 'This is a sample photo' written in the bottom-right corner) </br>                
The Photos are stored in an AWS S3 bucket. However, in order to be able to display the photos on the website (for buying-selling purposes), the bucket's content must be accessible from outside sources (i.e. the Heroku app must be able to access the photos and display them in the browser); this means that the bucket itself is not publically accessible, but the photos inside it are (at least this is my understanding of it, this was my first time trying out AWS!).</br>

To give an example of this, if you try to access the [bucket itself](https://s3.console.aws.amazon.com/s3/buckets/paulhinta-shopify-backend-2021), you will be redirected to sign into your AWS account (and you won't have access to it, since you aren't authorized to see the bucket), but you can access a [photo item's 'pic' attribute](https://paulhinta-shopify-backend-2021.s3.ca-central-1.amazonaws.com/Room_25.jpg) from this bucket without being authenticated.</br>

This brings up a challenge: if anyone can access any photo on the web app, then what's to stop them from downloading the picture without purchasing it first? To solve this, each Photo object is in a one-to-one relationship with another model called 'Owners'. This allows us to track which Photo(s) has been purchased by which User(s). Then, if a user is not authenticated, or a certain Photo object is not owned by that user, the html template automatically returns the [photo item's 'thumbnail' attribute](https://paulhinta-shopify-backend-2021.s3.ca-central-1.amazonaws.com/thumbnail/Room_25.jpg) instead.</br>

Overall there are five objects in this web app demo: User, Profile (user's profile picture), Photo, Owners, and Cart. If at any time you want to check out the database to get a better understanding of how these objects interact with each other, I've created a user with admin rights for you to check it out! </br>

### Shopify login with admin rights:
You can access this page [here](https://paulhinta-shopify-backend-2021.herokuapp.com/admin/) and log in with the following credentials: </br>
User = "Shopify"
Pass = "Shopify123"

A user may also look at their profile and update their information (including a profile picture; a default picture (Pikachu) is always provided). A user may also make updates to any Photo that they have listed, including de-listing it, changing the price, the name, the description, or removing the Photo altogether. </br>

Finally, when a user is done shopping, they make check out by using the navigation to the cart page (using the nav bar at the top of the page) and then clicking "check out". (Note that in this demo, there is no function implemented for actually purchasing the Photo(s) in the user's cart. Checking out will just return the user's cart total and then clear the cart.) Then, all photos purchased by them will be available for viewing on the side navigation bar (under 'Photos you have purchased'). </br>

And that's it! Hopefully you enjoy this app as much as I enjoyed developing it. </br>

One last thing: I understand that based on my resume and experiences, I'm not the most qualified person for this position! However, I would still really, really appreciate any feedback on my work :) I understand that it might be hard for y'all to give me detailed feedback since I'd imagine you are all quite busy, but anything is appreciated. </br>

Thank you very much and I look forward to hearing from you!</br>
-Paul
