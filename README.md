# ANUVITI - NGO Recommendation System By Kaavya Saxena

Anuviti is an attempt to bring the concept and features to life of the robust and popular web streamings applications like Netflix and Spotify.

This project was built as a part of the Microsoft Engage Program 2022 where mentees had to take up one of the three challenges/tracks, namely Face Recognition, Data Analysis and Algorithms.

This project was made in an attempt to take on the 3rd challenge of researching and thinking about the algorithms that may be used in a web streaming service such as netflix and spotify to recommend different ngos to the user

**Motivation:** 

While today's world has become fast paced and hectic people who want to help the society by contributing to it migtht find it difficult to do it with the time constraint and not knowing where to even get started.

**Solved Problem:**

This application aims to offer a quick and easy way to connect with different organizations through which you can contribute to a cause you belive in by utilising the power of Web.

**Learnings:**

Through the Microsoft Engage Mentorship Program 2022 under the able guidance of my mentor - Ashik Kuppili sir I was able to go from a person who just knew how to make static web pages to a person who can learn build and deploy a full stack web applications while my exams are going on.

**Watch Demo** : <a href="https://drive.google.com/file/d/19sp7QBBJjXO6nrE7gXq9e-2rnWbZTtX5/view?usp=sharing">Demo</a>




## Table Of Contents
[Features](#features)

[Installation / Getting Started](#installation)

[Tech Stack](#tech-stack)

[Algorithms](#recommender-system-&-algorithms)

[Challenges](#challenges-faced)

[Future Scope](#future-scope)

[Bug Log](#bug-log)

[Demo](#demo)

[Resources](#resources)

[Support & Contact](#support-&-contact)

## Features

- Toggle Navbar
- Responsive Design for Desktops, Ipads, Tablets and Phone
- User Sign Up Page
- User Sign Up through Unique Username
- User Sign Up through Unique Email.
- User Password Hashing to store it in Database
- User Login Page
- User Login Password Check
- Remember Me Feature for Login 
- Account Page
- Updation of details through account page
- Profile Picture Updation through Account Page
- Home Page Recommendations On the Basis of Users Location
- Direct Link to Official Website of Ngos in the form of button
- Search Bar to search for main areas of work NGO's Work towards


## Installation

To use this Project Follow the steps below:-

1. Initialise Your Git Terminal
```bash
  git init
```
2. Clone this Repository
```bash
  git clone <repo link>
```

3. Move into the Directory
```bash
  cd Anuviti
```
4. Open The Repository with your code editor,  it is recommended you use Visual Studio Code.
```bash
  code .
```
5. Activate Virtual Environment

```bash
  ./env/Scripts/activate.ps1
```  
If you face an Execution Policy error in this step please set your devices execution policy to enable you to run scripts

6. Run the following command:

```bash
  python ./run.py
```  

## Tech Stack

In spite of all the smart devices that exist today in the world, one thing that is common is - web and internet browsers. I selected my application to be a web application so that a large number of users are able to use it with ease and connect together

**Client:** HTML, CSS, JavaScript

**Server:** Flask, SQLite

The design of this application is simple yet responsive keeping in mind for it to work on different types of devices to solve a a real life problem 

## Recommender System & Algorithms

The term Recommender system is described as any
organization that provides personalized suggestions as a
result and it effects the user in the individualized way to
favorable items from the large number of opinions.

Recommender systems are usually classified
into two broad categories: Content based and Collaborative
Filtering

**Content-Based Recommendation:** one tries
to recommend items similar to those a given user has liked in
the past

**Collaborative Recommendation:** one
identifies users whose tastes are similar to those of the given user and recommends items they have liked

### Role Of Sorting Algorithms 

Recommender systems are designed in such a way
that they sort through massive amounts of data so as to help
users in finding their preferred items.

The end product of a recommendation algorithm is a top-list of items recommended
for the user which in turn is ordered by an evaluated score
representing the preference of that item for the user.
The interest of a user in an item is assumed to be dependent on
the value of the item being recommended, i.e., highest the
value, more interested the user will be.

#### Most Efficient Sorting Algorithm To Use

The most Efficient Sorting Algorithm for using shall be 
- QuickSort
- MergeSort

Where to Use these Algorithms will depend on the type of problem we are trying to solve

*QuickSort*

It is preferable to use Quicksort in the following scenarios:-

- When we want to sort the elements in a systematic order
- Mark and compare different elements against a single common elements called the pivot
- Data Set size is small
- There is a constraint of space which can be alloted

*MergeSort*

It is preferable to use MergeSort in the following scenarios:-
- When the way the elements are getting sorted does not matter
- Data Set is very large and generalized
- There is no Constraint of space under which the algorithm needs to work

#### As the dataset for my recommendaton system was not already available and I had to create my own database from scratch. My database was, as a result, small and very specific in terms of the data it stored. Therefore, for my scenario, I would Use Quicksort in my recommendation system

### Role of Search Algorithms

Recommendation systems generally look for overlap or co-occurrence to make a recommendation.

In practise, a recommendation engine computes a co-occurrence matrix from a history matrix of events and actions
After the recommendation system has computed the co-occurrence matrix we have to apply statistics to filter out the sufficiently anomalous signals to be interesting as a recommendation.

Most importantly, a good user experience in search and recommendations are almost indistinguishable. Basically, search results are recommendations if we can formulate recommendations as search queries

#### It’s an ideal solution as many websites like Anuviti and businesses already operate search engines in their backends and we can leverage existing infrastructure to build our recommendation system

## Challenges Faced

*"Errors are a stepping stones to develop good applications"*

During the development process I faced the following challenges:-

- Understanding the working of the backend side of my application as I had never worked with web backend before. However, thanks to online communities, stackoverflow, my mentor (Ashik Kuppili) and friends I was able to find resources which helped me in creating this web application.
- Preparing a feature list. In the beginning I wanted to build an app like no other and incorporate many features. But in the interest of time, I had to narrow down the features to the basic functionalities that are available in a video conferencing web application
- Managing Development of my Project as my exams were going on. It was a challenge to jumble myself and my time between my exam preparation and application development, but due to the guidance of my mentor and discussing strategies with my friends I was able to deliver both of them in time.
- Making my own Database as the database I required was not available, I had to make my Own database from Scratching by visiting different websites to gather data about organizations and thier details




## Future Scope
- Adding more information about the NGOs to give Better Recommendations
- Keeping Track of Click Rates and Search Queries of a User to make more relevant Recommendations
- Sorting The Recommendations on the Home Page and Search page not just by the city or state but also the the distance between the user and the NGO's location
- Adding a Contact Service Between a POC of the NGO and the User
- Adding a Verified Feature to Mark the verified NGO's Working
- Sharing Achievement Badges to Users and Orgs
- Forming Community Section where people can Interact with each other
## Bug Log

Following are the known Bugs of Web Application:-

- The API used to find out Location of the user Does not work Properly Sometimes. There,fore the defualt location for now is set to "Delhi"
- After Regitering An organization Jinja may show an error sometimes while rendering index.html
## Demo

Link to Video Demo: <a href="https://drive.google.com/file/d/19sp7QBBJjXO6nrE7gXq9e-2rnWbZTtX5/view?usp=sharing">Demo</a>


## Resources

https://ieeexplore.ieee.org/document/7050693

https://www.kdnuggets.com/2017/08/recommendation-system-algorithms-overview.html

https://pediaa.com/what-is-the-difference-between-quicksort-and-merge-sort/#:~:text=In%20summary%2C%20the%20main%20difference,until%20one%20element%20is%20left. 

https://towardsdatascience.com/how-to-build-a-recommendation-engine-quick-and-simple-aec8c71a823e


## Support and Contact

Email: kaavya1906@gmail.com

