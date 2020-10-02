# T2A3 - Anime & Manga Recommendation Tool
![alt-text](https://github.com/DarrenTrafford/T2A3/blob/Master/img/header1.jpg)

## Description
Welcome to my latest terminal app project! 

This is a simple app that will provide you recommendations based on what anime or manga you enter.
This is utilising the Jikan's API, which can be found at https://jikan.docs.apiary.io.

This API has a lot of features, however I have thus far only implemented a basic Search and Save function for Manga and Anime.

I have included some basic menu's with plans on adding to this in the future, so be sure to keep an eye on this if you are an Anime or Manga fan!

![alt-text](https://github.com/DarrenTrafford/T2A3/blob/Master/img/mainmenu.PNG) 

A screengrab of what you can expect to see

## Workflow

Current workflow is setup to push through GitHub Actions CI/CD pipeline to and Amazon EC2 instance for deployment. The pipeline looks like this:

Development Machine -> Flake8/Mypy -> GitHub -> Automated testing -> Push to master -> Deploy & run on EC2

## Installation
### Requirements

[Requirements](requirements.txt)

### Setup
Clone this repository

`git clone https://github.com/DarrenTrafford/T2A3.git`

Initialise whichever method of pythons virtual environment, activate your environment and run the following:

`pip install -r requirements.txt`

### Running
To run this application you will simply execute main.py as follows:

`python src/main.py`

## What to Expect
The first time you run this program for either Anime or Manga, it will create a file where it will store your recommendations.
It requires to do this for both, but don't worry as it will create the file and add your first search at the same time.

![alt-text](https://github.com/DarrenTrafford/T2A3/blob/Master/img/listcreation.PNG)

Example of the message you will see

## Release History

- 0.1.0  
  - Working Menus, Save & Search Feature
  
## Future Plans
- Implementing more of Jikans API features
- Working on a GUI
- Linking to MyAnimeList account
- Images
- Random Anime Search
- Displaying top rated User Reviews
- Deleting objects from lists & preventing duplicate entries

## Usage
Please feel free to fork this and/or report bugs to me! I created this for an assignment but I am intending to continue to work on this
Open to any suggestions! Enjoy this basic tool if you happen to use it. 
Please note, this API does have limits to how many searches it can make per second and day. I have not needed to change the values 
my app uses as it is well under this, be mindful if you change any of the code. The link mentioned in the start of this Readme
has information if you're looking to do bulk requests or make your own database.

## Code Contributers
https://github.com/eric-chew - Keep an eye on this guy, he is amazing.

## FAQ
-Coming Soon.

## Flow Chart Logic

![alt-text](https://github.com/DarrenTrafford/T2A3/blob/Master/img/t2a3flowchart.png)

This is what I based my code structure off

![alt-text](https://github.com/DarrenTrafford/T2A3/blob/Master/img/header2.jpg)

- I hold no rights to any Studio Ghibli Images