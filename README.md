This is a webapp based project that helps to automate a resume based on information that you provide. The webapp also provides job recommendations based on Indeed.

We built an online resume builder. It is a webapp developed to simplify the task of creating a resume for individuals, providing effective means of designing a professional looking resume. The webapp is especially designed for individuals who have a hard time creating their resume such as graduate students. This way, they will get a clear idea of the sections and information that should be included in a resume. The system is pretty simple without too much flexibility but can be expanded to include different templates, sections and so on. This project is user-friendly and requires minimum human intervention. Individuals just have to fill up a form that specifies questions from all required fields such as personal questions, educational, experience and skills. The answers provided by the users are stored and the system automatically generates a well structured resume.

OVERVIEW OF RECOMMENDATION SYSTEM The webapp also provides a site to input the preferred job title and location in order to generate the top job postings on Indeed. This way, the user can immediately start applying to job right after building their resume.

The webapp is built on three main components: Indeed Scraper, Flask Webapp and HTML and CSS Files.

SOFTWARE REQUIREMENTS:
- Programming Language: Python
- User Interface: HTML and CSS

The first component, we will be talking about the Flask Webapp aspect of our project. In order for this webapp to work, we created an init.py in the directory. Then, we created a templates folder to store all html files for the different pages on our webapp. There is also a style.css and resume_style.css file in a separate static folder. First, we imported all the necessary packages. When the webapp is first launched by the user, it follows the command @app.route(“/”) and the main( ) function is called. After this, the function render_template (), which has been imported from Flask, is returned so that the main_better.html template is rendered. In other words, this means that when someone looks up the website, it will show the home page of the webapp, which displays instructions on how to use the webapp. Next, the @app.route(“/about/”) calls the function hello( ), which renders the about.html template. Basically, when the user clicks “About Us” on our website, the url adds “/about/” to the end and redirects the user to the about us page.

Now, let’s talk about how the filling out and generating the resume works. Now if the user selects “Form”, the @app.route(“/form/”) calls the ask( ) function. This is the page where the user fills out their information. In this function command we considered two methods; get and post. The get method is when the user first arrives to the form page. In the function ask( ), the form.html template is rendered when the user enters the page through the get method. On the other hand, the post method is when the user has already been to the form page and has filled out the information the form requests. In the function ask( ), if the post is the method, then we use a flask import function called redirect( ) in order to redirect the page to the resume command. Once the user fills out the information and is redirected, the @app.route(“/resume/”) calls the resume( ) function. In this function, we take the information that the user inputted and store it in a python variable in order to pass the parameters. The syntax for this is first_name=request.form[‘first_name’]. Once we store all the inputs, we return the function render_template (), which has been imported from Flask, so that the resume.html template is rendered. Since we are passing the parameters, we also need to pass the parameters through the render_template () function with the syntax “first_name= first_name”. then the resume.html template is rendered and now the user can view their resume on the webapp!

Below is a description of our html and CSS files

HTML was used in creating the formatting for the website including the following subpages:
about.html: about us page gives a brief introduction of what the webapp is for
base.html: specifies the base URL and/or target for all relative URLs in a document. The tag must have either an href or a target attribute present, or both. There can only be one single element in a document, and it must be inside the <head> element.
form.html: contains the code prompting for user input such as personal questions and education. These information will then be stored in different variables to be used in building the resume
indeed_test.html: prompts for input desired job and location. It will then output the job recommendations generated by the indeed scraper
main_better.html: represents the dominant content of the <body> of a document. The main content area consists of content that is directly related to or expands upon the central topic of a document, or the central functionality of an application.
resume.html: provides a skeleton for our resume pdf. (This is assisted by the style1.css file instead of style.css)
  
style.css: creates the style formatting for about.html, base.html, form.html, indeed_test.html, main_better.html
resume_style.css: creates the style formatting for resume.html


As an extension of the resume builder, The indeed scraper, we wanted to generate job recommendations for the user based on their desired job and location. Currently, our code is able to take the user’s input and execute a search on indeed.com and return the corresponding search results from the site in the form of a table. Users are able to see information about the job posting, including the job title, a brief job description, as well as the link to the job posting itself. We initially intended to scrape job postings from LinkedIn, but eventually landed on Indeed.com due to challenges with bypassing LinkedIn’s login requirements. Our code makes use of Beautiful Soup library to scrape the job postings, and the web driver from selenium to test out our automated search. By using Beautiful Soup functions such as select(),find(),get_text() in tandem with CSS selectors, the program extracts the job title, the company name, the company location, the date of posting, the job description, and the link to the job posting from the first 10 results of the search. The information would then be loaded into a table formatted in HTML and displayed on the same page.
  

  In conclusion, Bob the Builder Project is designed a developed by a team of four UCLA undergraduates. The project objectives was to integrate web scraping and flask to design a “quick-and-easy” resume builder deployed through heroku. This resume would be able to help fellow undergraduates especially freshman and sophomores who are starting from scratch. The project was set to also include job and keyword recommendations through web scraping but the team decided to only implement job recommendations which was done through scraping Indeed as mentioned before. However, this program can be further developed to include it along with other creative aspects.
Some ideas to further develop the webapp is to allow users to choose different templates for the resume, check for punctuation, spelling and grammar mistakes or provide selections for user input. This project served its purpose in allowing the team to understand more about building a webapp from scratch! It was fun, frustrating at times but definitely fulfilling. That is it for our project.
