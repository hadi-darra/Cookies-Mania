
# [POS Cookies Mania app](https://cookies-mania.herokuapp.com/)

**Author:** Hadi AL DARRA
![](https://github.com/hadi-darra/Cookies-Mania/blob/main/assets/wireframes/responsivedesign.png)

# Project Description
This project is developed as my third portfolio project during my course at Code Institute. It is an command-line application using only Python as programming language.

This app is a POS that can let the cashier of the shop add the sales of the six types of Cookies **(Dark Choco and Pistachio - Salted Dark Choco - White Choco - Caramel Choco Ship - Peanut	Cranberry)** everyday and store them in Google worksheet. Also you can view all stock which is  available inside the shop and  view the sales and view the prices of each item in EURO and reset the sales logs at the end of the day.
# Content
* [Project Description](https://github.com/hadi-darra/Cookies-Mania#project-description)
* [UX](https://github.com/hadi-darra/Cookies-Mania#ux)
  * [User Stories](https://github.com/hadi-darra/Cookies-Mania#user-stories)
  * [Site Owner Goals](https://github.com/hadi-darra/Cookies-Mania#site-owner-goals)
  * [Structure](https://github.com/hadi-darra/Cookies-Mania#structure)
* [Features](https://github.com/hadi-darra/Cookies-Mania#features)
  * [Existing Features](https://github.com/hadi-darra/Cookies-Mania#existing-features)
  * [Features Left To Implement](https://github.com/hadi-darra/Cookies-Mania#features-left-to-implement)
* [Technologies Used](https://github.com/hadi-darra/Cookies-Mania#technologies-used)
  * [Languages](https://github.com/hadi-darra/Cookies-Mania#language)
  * [Other Programmes](https://github.com/hadi-darra/Cookies-Mania#other-programmes)
* [Testing](https://github.com/hadi-darra/Cookies-Mania#testing)
  * [Validator Testing](https://github.com/hadi-darra/Cookies-Mania#validator-testing)
* [Deployment](https://github.com/hadi-darra/Cookies-Mania#deployment)
* [Credits](https://github.com/hadi-darra/Cookies-Mania#credits)

# UX
## User Stories
As a user I want...
* .. the app has a  simple interface easy to interact and use .
* .. to get feedback of what is happening when navigate through the app.
* .. to add sales, be able to see all the enterd sales data and to reset them.
* .. validate the reset choice before take an action.
* .. ways to get back to start or menu easy.

## Site Owner Goals
As a developer of this app, my goals was..
* To build an app allo to store and add information from a user.
* Make user to understand easily how to use it .
* Make functions that add and save user inputs in API Google sheets.
* Create functions like add , view and reset the data. 


## Structure
![](https://github.com/hadi-darra/Cookies-Mania/blob/main/assets/wireframes/flow-chart.jpg)

Structure of this programme is what you can see in the flowchart here. There is six different task from a menu that get the user to the function depending on what the user input. Every function has a way to get back to the menu or quit the programme after the task is done. 
In the flowchart every function has a own colour just to make it easy to follow. 

[Back to Top](https://github.com/hadi-darra/Cookies-Mania)
# Features
## Existing Features
* Start Menu
  - The App starts with this welcome message and a list of choises. The user needs to input the number of what task they want to follow and the app open that function.
![](https://github.com/hadi-darra/Cookies-Mania/blob/main/assets/wireframes/start.png)
* Add new Sales
  * When adding a new sales, the user need to fill in the quantites of each type of Cookies and then the information will be saved in the worksheet gspread.
  * Validation message when the user have correctly enter all the information.
  * Error message if user entered letters.
  * Error message if user entered more than or less than 6 slots.
![](https://github.com/hadi-darra/Cookies-Mania/blob/main/assets/wireframes/add-sales.png)
* View stock
  * This function will return the stock logs which saved in the worksheet .
  * Gives a choice to go back to menu or quit the app from here.
![](https://github.com/hadi-darra/Cookies-Mania/blob/main/assets/wireframes/view-stock.png)
* View sales
  * This function will return the sales logs which enterd by the user and saved in the worksheet .
  * Gives a choice to go back to menu or quit the app from here.
![](https://github.com/hadi-darra/Cookies-Mania/blob/main/assets/wireframes/view-sales.png)
* View prices
  * This function will return the price list which saved in the worksheet.
  * Gives a choice to go back to menu or quit the app from here.
![](https://github.com/hadi-darra/Cookies-Mania/blob/main/assets/wireframes/view-prices.png)
* Reset sales
  * This function will reset the sales logs  which enterd by the user and saved in the worksheet.
  * Gives a choice to go back to menu or quit the app from here.
![](https://github.com/hadi-darra/Cookies-Mania/blob/main/assets/wireframes/reset.png)
* Exit app
  * This feature exit the app and can be reach from some of the other features also.
  * Provide a message with Thanks .
![](https://github.com/hadi-darra/Cookies-Mania/blob/main/assets/wireframes/exit.png)

## Features Left to Implement
This is what I want to implement in future on this app to make it more complete. But that I did not prioritate right now for the short of time.
* Add new type of Cookies
  * This feature i thinks it's important to be found in the app , allow the user to add new type of Cookies in case the shop need to enlarge sales range specially in holydays (Halloween , Christmas .. etc) 

[Back to Top](https://github.com/hadi-darra/Cookies-Mania)

# Technologies Used
## Language
* Python3 - This project is written only with Python as a the programming language.
## Other programmes
* Google sheets - To get my google sheet document (gspread) for store the information the user save, and to reset information.
* Gspread - The API to connect my to my app.
* GitHub - Making my repository and push my commited code.
* Git - Save and commit my workspace.
* Heroku - To deploy my app and get a livelink.
* Am I responsive - For the print screen of my deployed programme for this ReadMe.
* Draw.io - For make my flowchart.
* PEP8 - To validate python code

[Back to Top](https://github.com/hadi-darra/Cookies-Mania)
# Testing
## Validator Testing
When I checked my code for PEP8 requirements it's showed ALL RIGHT
![](https://github.com/hadi-darra/Cookies-Mania/blob/main/assets/wireframes/pep8online.png)

[Back to Top](https://github.com/hadi-darra/Cookies-Mania)

# Deployment
To build this program, I have used the Code Institutes template to be able to deploy it on Heroku and to be able to use the program on a web server. 
Using Gitpod.
In order to save my work I always **git add**, **git commit** with a message and then **git push** it to my Github repository.

## Project Deployment:
For deploy this project in Heroku I followed these steps:

1. Log in to my account at Heroku
2. Select "new" and "Create new app" from the dashboard.
3. Create a unique name for the project
4. Navigate from the deploy tab at the top and select the setting tab.
5. Because I use Code Institute template, I need to add a config var for creating this app. 
(Not necessary if you do not use the template)
6. Select Reveal config vars button. In KEY field, input PORT with capital letters.
In VALUE field, input 8000 and then select add button.
7. Then add buildpacks below the config var section.
8. Select Python as yout first bulid pack in buildpacks window and save that.
9. Add another buildpack and add node.JS and save.
The order of the buildpacks is importent to be Python at the top and node.JS at the bottom.
10. Select the deploy tab again and go to the deployment method section.
11. Select GitHub - connect to GitHub button and follow the steps to connect to your GitHub account.
12. Select your account and enter the name of yout repository and then select search.
13. When Heroku has find your repository select connect to connect the repository to the app within Heroku.
14. Below App connected section, I choose to manual deployments options further down. 
15. When that is done correctly this will provide me the live link for this programe.
16. Then I choose Automatic Deploys button that will automatically rebuild the app everytime you add, commit and push from GitPod.

### Here is the final deployed link:
[Cookies Mania POS App](https://cookies-mania.herokuapp.com/) (Opens in same tab)


[Back to Top](https://github.com/hadi-darra/Cookies-Mania)

# Credits
Credits:
* [Patorjk](https://patorjk.com/software/taag/#p=display&f=Ogre&t=Cookies%20Manaia)
I uesed it for creating ascii art welcome message

[Back to Top](https://github.com/hadi-darra/Cookies-Mania)



