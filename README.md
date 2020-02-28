# Oceanographic Dictionary Web-Application 

This web-app is designed to allow the user to manipulate the data Oceanographic Dictionary records stored in MongoDB. The user is able to create, 
locate, display, edit and delete records in line with CRUD functionality. 

The web-app is easy to use and allows the user to input their own words, categories and definitions into the database. The user can search for 
existing words in the database, as well as display existing and new words. Also, the user is able to edit current words and categories, as well as 
delete them. 

The purpose of the web-app is to ultimately build a large database of Oceanographic words, categories and definitions that will allow people to better 
understand the oceanic environment and all of the associated elements.

The link for the app is: 

*https://ocean-dictionary-flask-mongo.herokuapp.com/*

## UX

In order to make the user experience as easy and enjoyable as possible I opted for a simple looking site that is easy to navigate 
using the navigation bar buttons (Home, Browse Words, New Word and Manage Categories). There is also a search bar within the Navbar 
that the user can type in any word to search, as well as individual letters that are themselves links to all words beginning with the 
selected letter. The user is also able to add a new word using the floating green button to the left of the Navbar, as well as utilise 
links provided in the card placed on the right of the homepage (Words, New Word and Categories). Additionally, there are a selection of 
links in the footer that will assist the user to easily navigate the pages. A paragraph in the center of the Homepage explains what the
web-app is about.

Once the user browses a word using any of the available search facilities, they can then see the category to which that word belongs, as 
well view the drop down definition by pressing the button. There are also button options to edit or delete the word. A warning will present 
it's self to the user if they press the delete button.

To add a word the user is taken to the Add Word page where they can select an appropriate category, input the word and input the definition.
the user then presses the Add Word button to submit the information to the database. The operation can also be cancelled using the cancel button.
Either action will return the user to the Browse Words page that is sorted in alphabetical order.

The Manage Categories page allows the user to view all categories in alphabetical order and then either delete or edit an existing category 
using the buttons provided or add a new Category that will be submitted to the database. If editing the category, the user has the option to 
either save their changes or cancel the operation. Again, if the delete button is pressed a warning message will be displayed. 

The original concepts for the web-app pages can be seen in the *supporting_docs folder* under *oceanic_dictionary_database_schema.png*, 
*wireframe1_oceanic_dictionary_home.png*, *wireframe2_ oceanic_dictionary_browse_words.png*, *wireframe3_ oceanic_dictionary_manage_categories.png* 
and unused *wireframe4_ oceanic_dictionary_manage_categories.png*. These were created in Balsamiq. There are numerous changes since these  wireframes, 
mainly due to learning more about the capabilities of Python, Flask and MongoDB. There is also a database scehma showing the original idea 
for the project.

The web-app is aimed at users who share an interest in the ocean and oceanographic words, particularly those who would like to understand 
the spelling or definition of a word, or to which oceanographic category it belongs. 

## Features

### Existing Features

The choice of features, links and buttons available to the user are:

* **Nav Bar –** Contains homepage link in the title of the page that is animated and highlited when the user hovers on it to draw atttention to 
the page title. Below the title is a floating Add Word button which will direct the user to the Add Word page. In the centre of the Navbar is a 
Search bar that the user is able to type any word in to and search the database, this is highlighted by the green search button. The search bar 
will bring up all words related to the specified search that are in the database. The Navbar links that are Home, Browse Words, New Word and Manage 
Categories. Direct the user to these specific pages. The links are hilighted and pulse when they are hovered on to make it clear to the user that 
they are links.

* **Side Nav Bar –** This becomes available on smaller screen types and is present in the form of the hamburger style menu icon in the top left 
corner of the Navbar. Once the icon is clicked the Side Navbar presents itself with all the links that are hidden in smaller view (e.g. Home, 
Browse Words, New Word and Manage Category) that direct the user to the specified page. The links are highlighted and pulse when hovered on  
to make it clear to the user that they are links.

* **Individual Letter Links –** Each letter of the alphabet is represented by it's upper and lower case character. The individual letters are 
highlighted when hovered over to make the user aaware that they are links. Once clicked the user will be directed to a page that shows all words 
beginning with the specified letter listed in alphabetical order. Form there the user can see the associated category and definition and edit or 
delete the words.

* **Wave Picture –** The picture of the wave is the basis for all the colours used in the web-app. All colours utilised are colour picked from 
the wave picture.

* **Homepage Paragraph –** This paragraph informs the user of the web-apps purpose by briefly explaining the many things that can be found in 
our oceans.

* **Basic Card –** The card has a second explanation of the web-app and tells the user what they are able to to do with regards to the functions 
available (e.g. browse, search, edit and delete words. Also, categories can be added, managed and edited). There are three links available to the 
user on the card, which are Words, New Word and Categories.

* **Footer –** The Footer has yet another brief paragraph explainin the web-app and its functionality, as well as links to Home, Browse Words, 
New Word and Manage Categories. These are available in the Footer on every ppage of the web-app.

* **Word Results –** When the user searches for a word using the search bar or the individual letters they are dircted to the Word Results page 
that will show all resultant words. Each word has it's own box and within the box is displayed the word in bold, as well as the associated Category.
then the word again.

* **Definition Button –** The large definition button and dropdown selector to its left in each individual word box will display the words definition 
in the drop-down when selected. This is so that the user can choose if they wish to see certain definitions and not all are displayed on screen at 
once. The button pulses when hovered on.

* **Edit Word Button –** The Edit button in each individual word box takes the user to the Edit Word page. Here the user is shown the existing details 
of the word from the database (e.g. Word Category, Input Word and Input Definition). The user is able to edit any of these details by then pressing 
the Edit Word button. There is also an opportinity to cancel the operation by pressing the Cancel button. Once the user either edits the word or cancels 
the operation, they are taken back to the Browse Words page. 

* **Delete Word Button –** The Delete Button in each individual word box gives the user the opportunity to delete the word and associated category from 
the database completely. Once pressed a message is diplayed asking the user if they are sure they want to delete this word?

* **Add Word –** When the user selects the Add Word green button in te Navbar or New Word from any of the links they will be taken to the Add Word page 
where they are given a blank form to fill in beginning with choosing a word category from the dropdown list, then inputting the word, followed by 
inputting the definition. Once the form is completed the user can submit the word to the database using the Add Word button or cancel the operation 
using the Cancel button. Either button will take the user back to the Browse Words page. If the user inputs a word that already exists in the database 
they will receive an error message stating "This item already exists in the database".

* **Categories –** When the user selects Manage Categories from the Navbar or any of the Categories links, they are taken to the Categories page. This 
page displays all of the existing categories in alphabetical order. 

* **Add Category Button –** This button directs the user to a page with a single line form where they can input the name of a new category. Once the 
form is completed the user can submit the category to the database using the Add Category button or cancel the operation using the Cancel button. 
Either button will take the user back to the Categories page. If the user inputs a category that already exists in the database they will receive an 
error message stating "This item already exists in the database". 

* **Delete Category Button –** The Delete Button to the left of each individual category on the Categories page gives the user the opportunity to delete 
the category from the database completely. Once pressed a message is diplayed asking the user if they are sure they want to delete this category?

* **Edit Category Button –** The Edit button to te far left of each individual category on the Categories page takes the user to the Edit Category page. 
Here the user is shown the existing category from the database. The user is able to edit this detail by then pressing the Edit Category button. There is 
also an opportinity to cancel the operation by pressing the Cancel button. Once the user either edits the category or cancels 
the operation, they are taken back to the Categories page. 

### Features left to implement

* View each category and associated words separately by clicking category name?

* User can curretly input upper and lower case versions of the same word / category?

* Words to be spilt up into there own individual letter and not one continous list of all words in alphabeitical order.

* User LOGIN and REGISTER options.

* Voting on words Page? Thumbs up and down. Difficult without user login credentials.

* Could not create Text Index?

## Technologies Used
The languages, frameworks, libraries and other tools utilised for building this web-app are:

* **Gitpod -** Gitpod is a cloud-based integrated development environment (IDE) that has been used to write, run, and debug the code used for 
the web-app. https://www.gitpod.io/

* **GitHub -** GitHub has been used for version control of the code by using Git functions in the control panel. Github was utilised frequently 
during the development of the web-app.  https://github.com/

* **Heroku -** This is a cloud based application platform that allows deployment of an application to the web and connection to the database. 
https://heroku.com/

* **Mongo DB Atlas -** This is a general purpose, document based, distributed database with scalability and flexability. https://www.mongodb.com/

* **PyMongo -** This is a Python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from 
Python, as an API for MongoDB intergration. https://api.mongodb.com/

### Front-End Technologies

* **HTML 5 -** The web-app uses HTML5 as a fundamental basis for building the web-app. Where possible semantic HTML is used to give the user a 
better understanding.

* **CSS3 -** The web-app uses CSS3 for styling of elements within the website. It is linked from the page to the *style.css* file.

* **Materialize 0.100.2 -** The open-source Materialize framework has been used to implement the layout of the web-app. Materialize is also 
utilised to accommodate the responsive and mobile first design of the web-app. http://archives.materializecss.com/0.100.2/about.html

* **JavaScript -** The web-app uses Javascript to provide dynamic interactivity, as it is a full-fledged versatile programming language.

* **jQuery -** The web-app uses jQuery, as it simplifies a lot of complicated tasks from JavaScript, such as AJAX calls and DOM manipulation. 
https://www.jquery.com/jquery-3.4.1

* **Google Fonts-** The dashboard uses Google fonts to accentuate certain text. https://fonts.google.com/

### Back-End Technologies

* **Python 3.1 -** Python emphasises readability, uses English keywords and is highly extensible. The core language itself is quite small, 
and it is easy to learn for brginners. https://www.python.org/  

* **Flask -** This is a lightweight Web Server Gateway Interface (WSGI) web application framework. There is little boilerplate code for 
getting a simple app up and running.

* **Jinja -** This is a modern and designer-friendly templating language for Python. It is fast, widely used and secure with the optional 
sandboxed template execution environment. 

* **dnspython -** This is a toolkit for Python that supports almost all record types and allows the new style connection string for MongoDB 
Atlas to be utilised.

* **Flask-PyMongo -** This allows Flask to communicate with Mongo. It is optimized to work with Flask.

* **itsdangerous -** This is used to cryptographically sign and customize how the data is serialised.

* **Werkzeug -** This is a comprehensive Web Server Gateway Interface (WSGI) web application library.

## Testing

The main basic functions of the web-app that required rigorous testing in different scenarios are listed below.

*	**Navbar** 
    * All Navbar links and buttons are coded within the Header section of the base.html with associated Python functions set up in app.py. 
    * Check Title link words (Oceanographic and Dictionary) return user to Homepage in every instance by ensuring that the index (/show_words) page is 
      returned to. This is valid for both the words 'Oceanographic' and 'Dictionary', as thay are split across two separate rows. 
    * Green `Add Word` button is configured to redirect the user to the Add Word page. Verified the link and left side positioning in all browsers and 
      screen sizes. 
    * The Search Bar required rigourous testing due to the varoius ways the words in Mongo DB could be accessed and displayed (See Issues List).
    * Green magnifying glass icon `Search` button next to the search bar activates the entry into the Search Bar. This has been tested and affixed in place 
      to maintain its funcionality in all browsers and screen sizes.
    * The Navbar `Home`, `Browse Words`, `New Word` and `Manage Categories` buttons have been extensively tested to rediriect the user to the relevant page.
    * The Side-Nav buttons of `Home`, `Browse Words`, `New Word` and `Manage Categories` have been extensively tested to rediriect the user to the relevant 
      page.

*	**Footer** 
    * The Footer links of `Home`, `Browse Words`, `New Word` and `Manage Categories` have all been extensively tested to redirect the user to the relevant page.
    * the `More Links` button is where links to external pages will be placed (e.g. Facebook, Twitter etc.) (See Issues List).

*	**Main base.html section**    
    * The Individual alphabetical letters are situated below the NavBar, but still appear on every page of the web-app. Each letter has been tested numerous 
      times to ensure that the functionality is correct and brings up all words begininng with the relevant letter, regardless of whether the word stored in the 
      database begins with an upper or lower case character.
    * A flashed message appears `This item aleady exists in the database` when a user inputs a word or category that is already in the database. This has been 
      tested and works provided that spelling and capitalisation of letters matches exactly what is all ready in the database (See Issues List).

*	**Homepage Main Section**    
    * Basic Card Links on the home page of `WORDS`, `NEW WORD` and `CATEGORIES` have been extensively tested to take the user to the relevant page.
    * The Wave image, homepage paragraph and basic card are set-up to maintain a third each of this section on larger screen types and each take up 
      the entire width of the screen on smaller devices.

*	**Browse Words Main Section**  
    * The words on this page are listed in alphabetical order regardless of the case of the initial letter. This functionality required extensive testing in order 
      make the functions work correctly.
    * The `Definition` button and drop down menu required were rigourously tested to ensure that they function correctly and display the correct definition for the 
      associated word direct from the data base.
    * The `Edit` button for each word redirects the user to the Edit Word page.  
    * The `Delete` button brings up the `Are you sure you want to delete this word??` box where the user can choose `Ok` or `Cancel`. The `Ok` button deletes the 
      word and associated definition from the database completely, which functonality has been thoroughly tested. `Cancel` returns the user to the Browse Words page.

*	**New Word Main Section**
    * The user is taken to the Add Word page, where there is a three row form. The `Choose Category` row is a drop down menu selector that shows all categories 
      currently entered in to the database. This drop down has been tested to ensure that it shows the categories in alphabetical order regardless of capitalisation
      of the initial letter.The `Input Word` and `Input Definition` rows have been thoroughly tested so that the functionality works and iputs a new word_id and 
      associated definition in to the database. This required a large amount of testing and with different functions and methods (See Issues List).
    * The `Add Word` button submits the form to the database and has been extensively tested.
    * The `Cancel` button returns the user to the Browse Words page. This has been thoroughly tested.

*	**Edit Word Main Section**
    * The `Edit Word` button directs the user to this page where the user is presented with a three row form. The form is already populated with the existing 
      `Word Category`, `Word Name` and `Word Definition` from the database. The `Word Category` row is a drop down menu selector that shows all categories 
      currently entered in to the database. This drop down has been tested to ensure that it shows the categories in alphabetical order regardless of capitalisation
      of the initial letter.The `Input Word` and `Input Definition` rows have been thoroughly tested so that the functionality works and iputs a new word_id and 
      associated definition in to the database. This required a large amount of testing and with different functions and methods (See Issues List).
    * The `Edit Word` button submits the form to the database and overwrites the existing data. This has been extensively tested.

*	**Manage Categories Main Section**
    * The user is taken to the Categories page. The categories on this page are listed in alphabetical order regardless of the case of the initial letter. This 
      functionality required extensive testing in order make the functions work correctly.
    * The `Edit` button for each category redirects the user to the Edit Category page.  
    * The `Delete` button brings up the `Are you sure you want to delete this category??` box where the user can choose `Ok` or `Cancel`. The `Ok` button deletes the 
      category from the database completely, which functonality has been thoroughly tested. `Cancel` returns the user to the Categories page.  

*	**Edit Category Main Section**
    * The `Edit Category` button presents the user with a single row pre-populated form where the user is able to edit the `Category Name`. This will amend the 
      category_id dierctly in the database when the `Save Changes` button is pressed. This function has been extensively tested.
    * The `Cancel` button returns the user to the Browse Categories page. This has been thoroughly tested.    

*	**Add Category Main Section**
    * by pressing the `Add Category` button in the Manage Categories page the user is taken to the Add Category page, where there is a one row form. The `Category Name` 
      row allows the user to input a new category. This has been thoroughly tested so that the functionality works and iputs a new category_id in to the database. This 
      required a large amount of testing and with different functions and methods (See Issues List).
    * The `Add Category` button submits the form to the database and has been extensively tested.
    * The `Cancel` button returns the user to the Browse Words page. This has been thoroughly tested.

*	**Responsive / Mobile First design** 
    * Each page of the web-app has a **Header**; **Main Section** and **Footer**. These needed to display correctly accross 
      all devices and screen resolutions. primarily checks are required to ensure that the dashboard collapses in to columns in mobile view 
      and that the information is presented in a clear and legible fashion.
    * The header title was is straightened in mobile view in order to resize the Navbar sensibly. This was done to provide a 
      better user experience and clarity of design, as the title animation did not show well in a smaller view. 
    * The Side-Nav burger icon presents itself at the top-left of the NavBar in medium and small view. This has been tested across multiple 
      devices listed in this below.
    * Various methods of testing have been carried out to test the code of the web-app. Continuous testing throughout the development has been 
      implemented to check the quality of the code. The aim is to check the functionality of the code on different devices (mobile, tablet, desktop) 
      with an overall perspective of responsive and mobile first design. The site has been viewed and tested in **Firefox**, **Safari**, **Chrome** 
      **Microsoft Edge** and **Explorer**. The 
      devices used to test the site are **iPhone 5/SE**, **Samsung Galaxy**, **iPad**, **iPad Pro** **iPhone X**, **iPhone 6/7/8**, **Pixel 2**, 
      **Pixel 2 XL** , **Hudle2** and **Samsung / Lenovo / HP laptop**. 

*	**Blank Form Input** 
    *       

*	**Data** 
    * 

*	**.gitignore** 
    * 

*	**W3 Nu Html Checker** 
    *  

*	**W3C CSS Validator** 
    *      

*	**JShint** 
    * 

*	**PEP8 Online** 
    *              
       
The final database schema and desktop wireframes for the web-app can be seen in the *supporting_docs folder* under *oceanic_dictionary_database_schema.png*, 
*wireframe1_oceanic_dictionary_home.png*, *wireframe2_ oceanic_dictionary_browse_words.png*, *wireframe3_ oceanic_dictionary_manage_categories.png* 
and unused *wireframe4_ oceanic_dictionary_manage_categories.png*. These wireframes and database schema were used initially to plan the web-app and build 
around The opinions of numerous people including my mentor, friends, tutors, chat forums and such like, whom were asked during various stages of the project.

## Issue List



  | Issue  |                 Description                     |       Solution                      |  
  | ------ |:-----------------------------------------------:|:-----------------------------------:|
  |   1    |Attempted to connect dashboard directly to API but data proving unmanageable|Downloaded .csv file instead|
  |   2    |Unable to download export whole dataset due to issue with website |downloaded each year separately|
  |   3    |Issues with uniformity of the .csv data (e.g. spellings and capitalisation) |Amended these issues directly in .csv file|
  |   4    |Composite chart , Stacked bar chart and Bar graph not scaling correctly on smaller devices |Used viewbox resize to scale correctly |
  |   5    |Dates on Composite Chart X-axis displaying incorrectly (e.g. 1,985)|Function added to bottom of `show_country_year`  to correct this |
  |   6    |Attempted to use Age Range function that would separate the ages Pie Chart into ranges |This did not connect to other charts. Added Age range column to .csv file |
  |   7    |Queue, Crossfilter and and DC.js showing as ‘Undefined’ in main.js tab | `/*global varname*/` added to remove undefined variable errors |
  |   8    |Header image and title took up too much space in responsive views | Changed display to none in media query below tablet resolution |
  |   9    |”Next” and “Last” buttons did not work on Table |Event listener added to these buttons to globally rectify this |
  |   10   |Explorer displaying the charts which use viewbox resizing too small |Decided to leave this, as browser being phased out and rarely used |
  |   11   |Second intro paragraph did not fit on tablet size and was left in row alone | Removed from tablet view using media query |
  |   12   |Stacked bar chart did not read well when using percentages to diplay types of attacks that were fatal |Opted to use actual count as this was clearer|
  |   13   |Table not scaling correctly on smaller devices |Used media query to remove table from smaller devices |
  |   14   |Needed to validate CSS for debugging purposes | Utilised jigsaw.W3 CSS Validator (zero errors) |
  |   15   |Needed to validate JavaScript for debugging purposes | Utilised jshint.com (no errors) |
  |   16   |Needed to validate HTML for debugging purposes | Utilised W3 Markup Validation Service (1 warning) |
  |   17   |HTML Validation warning "Section lacks heading" | This warning can be ignored as does not affect code |
  |   18   |X-axis titles on Activities bar graph not displaying correctly in horizontal view |Used `text-anchor: end !important` in CSS to angle text |
  |   19   |Data in .csv file was causing more columns in graphs for the same variable (e.g. Body Boarding and Boogie Boarding) | Amended to .cvs variable names to make more uniform |
  |   20   |Header `Refresh Charts` button was not positioning correctly in Windows Edge | Used `float: inherit` in CSS to fix |
  |   21   |Is HTML semantic and self explanatory  | Added further comments to index.html file |
  |   22   |Is main.js self explanatory  | Added further comments to main.js file |

  
## Deployment

The web-app is designed in the Gitpod environment and regularly committed to GitHub after each crucial piece of coding. 
Using this method as a sanity check for the development enabled me to restore the site back to previous stages when it 
functioned correctly or easily find lost pieces of code. 

### To deploy the project to Github the following steps were taken:

  1. created a `master` branch in Github repository 
  2. Used Local AWS Cloud9 and Gitpod environment used to build the site
  3. Committed files to the staging area using bash terminal commands: `git status`; `git add (specify directory)`; `git commit -m"add message"`
  4. Pushed files to the working environment using `git push`, which then updates the repository.
  5. Published site from `master` branch using `settings` tab in the main page of the repository, select `source` as `master branch`, then `save`
  6. The repository can be cloned by clicking `Clone or Download` on the main page of the repository 
  7. In the Clone with HTTPs section, click the clipboard icon to copy the clone URL for the repository
  8. Open Git Bash Terminal
  9. Type `git clone`, and then paste the URL
  10. Press `Enter`. A local clone will be created.

### To set gitignore environment variables the following steps were taken: 

  1. Create a file named env.py in the root directory of your project. This is the file you will use to define your environment variables.
  2. If you don't have one already, create a file named .gitignore  in the root directory of your project.
  3. Next we need to stop git from pushing this file to github, and so keep your environment variables secret. To do this, open your .gitignore  file add the following text: env.py
  4. At the top of your env.py  file, you need to import os so that you can set the environment variables in the operating system. Once you have added the line “import os” 
     underneath you can assign your environment variables using the following syntax:  
     `os.environ["Variable Name Here"] = "Value of Variable Goes Here"`
  5. Then the following code imports this new env.py file where you need to use your environment variables. For example your app.py file for flask project. Add this under your 
     other imports at the top of the file  
     `from os import path`
      `if path.exists("env.py"):`
      `import env` 
  6. Now that your environment variables have been set in your env.py file, and the file has been imported into your project, you can use them as needed using the following syntax:  
     `MONGODB_NAME = os.environ.get('MONGODB_NAME')`

### To deploy the project to Heroku the following steps were taken:

  1. created a Heroku account @ https://signup.heroku.com/
  2. Create `requirements.txt` file in Gitpod workspace for Heroku to understand installation files to run app. From CLI type type 
     `pip3 freeze --local > requirements.txt`.
  3. To install the Heroku command line on Gitpod or AWS Cloud9, use the following command `npm install -g heroku`
  4. Using the `New` buton, Create a new app with apropriate title and server in Heroku. This creates a connection between the Gitpod application and Heroku that would allow us 
     to push our changes using Git to update the application at any given time. 
  5. To login to Heroku from the CLI, use the command `heroku login`
  6. To get the application up and running a `Procfile` is required that istructs Heroku which file is the entry point. Use the following command to create this: 
     `echo web: python app.py`
  7. Code that is prepared to be pushed from Github to Heroku can be executed following the CLI commands:
     `git add .`
     `git commit -m "fist Heroku commit"`
     `git push`
  8. Now that the relevant code is pushed to Github, it can also be pushed to Heroku from the chosen branch (e.g. Master)
  9. To connect an existing repository from Github to Heroku use the following CLI syntax: `heroku git:remote -a [followed by name of Heroku app]`
  10. To push to Heroku Master Branch, then simply use `git push heroku master`
  11. To scale dynos and run the app in Heroku, use the CLI command: `heroku ps:scale web=1`
  12. In order for the server instance on Heroku to know how to run our Flask application, we need to specify IP and Port in Heroku. To do this go to `Settings` 
      tab > `Config Variables` and input: `IP Address: 0.0.0.0`; `Port: 5000`  

## Credits 

### Content

This README.md file is based on the Code Institute template.

### Media 

CBS Interactive Inc.(2019): https://www.cbsnews.com/pictures/five-most-dangerous-sharks-to-humans/

Data obtained from: https://data.opendatasoft.com/explore/dataset/global-shark-attack%40public-us/export/

Dataset info for global-shark-attack@public-us; http://www.sharkattackfile.net/incidentlog.htm

Favicon image downloaded from: https://www.shutterstock.com/image-vector/dangerous-sea-life-207907852?studio=1

Favicon – created using http://www.favicomatic.com/done

Shark and Surfer Image: https://usatunofficial.files.wordpress.com/2011/10/shark-in-a-wave-with-surfer.jpg

### Acknowledgments

Thank you to the Carcharodon Carcharias (White Shark) species whom I find so intriguing and awesome and the people at sharkattackfile.net for compiling such a 
huge and detailed dataset. I would like to thank Anthony Ngene (https://github.com/tonymontaro) for his invaluable feedback, as supervisor for this project. 