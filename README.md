# W2 form parser

Welcome to the W2 form parser. This project is created as part of my recruitment assignment at TaxGpt. In this file, you can find basic setup, some major dependencies and and overview of the project's workflow.

## About W2 form parser

W2 parser is the web-based application designed to allow uploading of a scanned copy of W2 form. It uses Nanonets OCR API to extract data from the uploaded file and gpt3.5-turbo for interactive querying on the extracted W2 data, stored in the sqlite database. The application is hosted on netlify and can be accessed at:
https://taxgpt-assignment.netlify.app/

## How to Use

- Choose a pdf file of the scanned W2 form from device, click on the "Upload" button. The upload response will be displayed. 
- Ask any question regarding the file. To make it easy for the LLM to answer, please begin your prompt with "My Employee SSA number is <enter SSA number>. and then the question "How much is my gross pay?" i.e.:
  "My Employee SSA number is <enter SSA number>. How much is my gross pay?"
  For general questions that require taking in account of all entries irrespective of employers, you can ask directly like "What is the average of social security tax"
- Please note it might take a little while to respond, sometimes you might have to ask twice to get a response as LLM is currently an amateur.

## Getting Started

To get started with this project, follow these steps:

1. Cloning the repository

`git clone https://github.com/IqraSiddiqui/taxgpt`

2. Install the required libraries for python

`cd taxgpt/w2parser/ && pip install -r requirements.txt`

3. Install the required libraries for js

`cd ../w2_front && npm install`

4. Deployment

Open terminal and cd to project root folder and run

`cd /taxgpt/w2parser/ && python manage.py runserver`

Open another terminal and cd to project root folder and run

`cd /taxgpt/w2_front/ && npm start` or simply access it through the netlify link provided above

All set if everything running without errors. Now the deployed web application should open in a browser. If not, open a browser and navigate to http://localhost:3000

## Dependencies
- React `18.3.1`
- Django `5.0.4`
- Langchain `0.1.16`
- g4f `0.3.0.7`
