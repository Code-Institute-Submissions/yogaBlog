# A Cup of Yoga blog CMS - Wayne Pegg Milestone 3 submission - Code Institute/Full Stack Web Developer

A Cup of Yoga is my submission for the third assessment of four projects for the above mentioned course.

This site is currently published on the following link:

[A Cup of Yoga](http://peggy535.pythonanywhere.com/) (github repo: https://github.com/Peggy535/yogaBlog)

This imitation Content Management System for a blog site has been built to be responsive to, and for any device type. Please also note, for this project no user authentication has been added. The focus of this project has been to perform CRUD operations using the Flask framework with MongoDB Atlas.

## Conception

The web page shown is that of an immitation Content Management System for the site owner. It is assumed the user has logged in sucessfully.

The CMS area allows the logged in user to create, read, update and delete either a new or existing blog post's. The landing page shows the same layout that the blog site would take apart from the fact that it has the following extra functionality;

1. A welcome message to the site owner and a button that allows the user to write a new blog

2. A listing showing all previous and published blog articles written by the user.

## UX Design

The main emphasise for this was to ensure simplicity for the user whilst allowing the functionality neccesary to maintain a personal blog website.

The dashboard is the presented. The landing page image and title would be that of the actual site.

Below this is a personalised welcome message to the user. A clear and identifiable button provides the user a chance to 'Write a new blog'. Once clicked, this takes the user to a new page with the relevant form fields to be populated. These form fields relate directly to the MongoDB-schema that have been devised.

Once the user submits the blog, they are returned to the CMS landing page. The most recent blog article is presented at the top of the list with all other blogs being displayed in descending time order.

## Features of the MongoDB schema

MongoDB Atlas was used for this project. The following details relate to the schema devised for this:

Cluster name: YogaCluster
Collections: blogEntries
Fields for blogEntries: _id, title, article_text, tag_name, author_name, time_of_blog

All apart from _id and time_of_blog, are inputted by the user of the blog CMS.

'_id' is the specific and unique primary key created by MongoDb, 'time_of_blog' is a time stamp that is created when the user submits a new blog article. It is this DB field value that is used to predicate and sort the blog articles into descending order for the user.

The connection string that is used to connect to the MongoDB Cluster is stored within a '.env' file that has been included in the sites .gitignore file.

Connection from the Flask project to the MongoDB database is made using PyMongo importing the 'MONGO_URI' connection string as detailed above.

## Technologies used

The project has made use of the following technologies;

HTML5, CSS3, Bootstrap 4, Javascript, Python, Flask, MongoDB.

To host this Flask/MongoDB project use was made of [Python Anywhere](www.pythonanywhere.com).

## Testing

Testing for this project was conducted in the 'shoes' of an actual user. That is, all possible options and scenario's were completed as detailed below:

1. Landing page

- Ensured the image, font size and sign-in/sign out buttons were rendered correctly for all responsive device types and orientations
- Ensured each blog entry that should be presented is presented in the correct date/time order and with the correct 'Edit' & 'Delete' buttons.
- Ensured that the specific 'Edit' and 'Delete' button assigned to a specific blog edits and deletes the correct blog article.
- When the Flask app is run, connection to the MongoDB Atlas Cluster is established for read/write purposes.

2. Writing a blog article

-Ensured the form fields were displayed correctly.
-Ensured values typed into fields are written to the specific MongoDB blogEntries fields values correctly.
-Ensured sent values were saved into the correct fields on the MongoDB blogEntries collection.
-Ensured once submitted the user is returned to the original cms landing page with the most recent blog article positioned at the top of the list and descending in date/time order
-Ensured if user selects the cancel button, nothing is written to the MongoDB collection blogEntries
-Ensured if user selects cancel, user returns to main cms landing page.

3. Editing a blog article

- Ensured all blog articles listed are presented to the user with the Edit button option.
- Ensured that when the Edit button for a specific blog article is selected, the correct text and format are supplied to the user in the corrrect form fields.
- When a change has occured to one or many of each specific fields and the user selects 'Submit' that the changes are made to the relevant blog article.
- When the aboves changes have been made and saved correctly to the MongoDB blogEntries collections, these are reflected and saved correctly in the correctly field value and displayed to the user with the corrections made on the main landing page.

4. Deleting a blog article

- Ensured that each specific blog article has presented a 'Delete' button option for the user.
- Ensured that when selected, the article that should be deleted from the MongoDB blogEntries collection is deleted and nothing else.
- Ensured when the 'Delete' button has been selected, the user is returned to the main landing CMS page with the deleted blog not appearing in the current list of blog articles.

## Deployment

This project was saved the following repository on [Github: Peggy535/yogaBlog](https://github.com/Peggy535/yogaBlog).

There were not differences within configuration files nor any branches constructed. Several git commands were used thoroughly and throughout the project lifecycle. the commands used for this were:

git add ./git commit -m "Meaningful message to reflect the commit"/git push -u origin master.

The projects site was deployed to the following site address, [click here](http://peggy535.pythonanywhere.com/).

In order to set up this Flask project, I registered as a new user of Python Anywhere. Once I had established this I then created and deployed a virtual environment and installed Flask and other dependencies such as PyMongo and dotenv. Once this was done I simply uploaded my project file/folder structure and configured the associated WSGI.py file that is associated with this project and virtual environment.

## Credits

Content

- Thanks and acknowledgment is given to Real Python, Front End Masters & MongoDB University.

Acknowledgements

- A huge thanks for the supportive, encouring and positive input my tutor, Spencer, has had into this project. He has been a great help and really inspired my efforts. Sincere thanks Spencer.