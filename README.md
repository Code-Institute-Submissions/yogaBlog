# A Cup of Yoga blog CMS - Wayne Pegg Milestone 3 submission - Code Institute/Full Stack Web Developer

A Cup of Yoga is my submission for the third assessment of four projects for the above mentioned course.

This site is currently published on the following link:

[A Cup of Yoga](http://peggy535.pythonanywhere.com/)(github repo: https://github.com/Peggy535/yogaBlog)

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

All apart from '''json {_id and time_of_blog}


## Technologies used

The project has made use of the following technologies;

HTML5, CSS3, Bootstrap 4, Javascript, Python, Flask, MongoDB.

## Testing

Testing for this project was conducted in the 'shoes' of an actual user. That is, all possible options and scenario's were completed as detailed below:

1) Landing page

- Ensured the image, font size and sign-in/sign out buttons were rendered correctly for all responsive device types and orientations


## Deployment

This project was saved the following repository on [Github Peggy535/Cryptograph](https://github.com/Peggy535/Cryptograph).

There were not differences within configuration files nor any branches constructed. 

The projects site was deployed to the following site address, [click here](https://peggy535.github.io/Cryptograph/).

## Credits

Content

- Thanks and acknowledgment is given to [Cryptodatadownload.com](http://www.cryptodatadownload.com/) for their excellent `.csv` data files used in this project.
- dc.js, d3.js and crossfilter communities for the content and API documentation references on Github.

Acknowledgements

- A huge thanks for the supportive, encouring and positive input my tutor, Spencer, has had into this project. He has been a great help and really inspired my efforts. Sincere thanks Spencer.