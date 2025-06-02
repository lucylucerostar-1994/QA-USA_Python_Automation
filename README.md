# Sprint 7 project

The project contains various api tests ensuring that they function properly. All tests are stable and work conjunctively.
The files consist of DELETE,GET,POST & PUT requests.
Each method contains two tests and both tests are saved within their respective file.

The purpose of this project is to verify that various API request methods correctly function as expected through tests ran with the framework Jest in the VS code terminal.

--Downloading the projects depedencies:

        Firstly, you will want to link your GitHub account to TripleTen by clicking the "Link GitHub account" button in the widget at the top of the project 7 description page.
            Next you will want to clone the repository to your computer to work with it locally. Doing this entails:
            1. opening the terminal on your computer (Git Bash if you are on windows) .
            2. Next you create a directory to store this project and any future projects we may have by entering cd ~, mkdir projects, cd projects. 
            3. You will want to clone the repository at this point by entering into your console git clone git@github.com:username/hm07-qa-us.git(for ssh authentication users) or git clone https://github.com/username/hm07-qa-us.git(for https authentication users) you will want to replace "username" in the command with your GitHub username.
            4. You can now work with the project locally on your computer. Once inside of your project folder you will want to run npm install.

--Setting the URL:

        First you will to click the "Start" button on the TripleTen project 7 description page.
            Next you will want to copy this URL.
                Lastly you will want to paste the copied URL in the config.js file within the project folder.
                    Make sure that you past the URL between the double quotation marks after the variable API_URL:.



--The documentation source used was apiDoc.
    
    To access apiDoc you will want to copy the forementioned TripleTen project 7 description page URL and place this in your broswer address bar
        You will then add after the pasted URL /docs/ and enter the full address. This will take you to apiDocs where we have our documentation.

--Running the test suite:

    (In order to run the test suite properly you must have already written a test within the respective file for each method.)
        There are two ways to running your tests. Individually by file name or all together at once.

            To run a test by its individual file (Leaving the rest of the tests out of it):
                You will click the fourth button down from the file explorer in VScode(This buttons symbol is a play button with an insect on the bottom left)
                    You will then select "JavaScript Debug Terminal" (OR you can drag the bottom bar up and the terminal will appear this way)
                        Once within the terminal you must enter the command "npx jest ./tests/"filename.js". npx jest is to call the jest framework and after this is the directory.
                        This will run solely this individual file.

    To run the entire test suite as a whole you must:
        Follow the same forementioned steps for running an individual test obtaining the terminal within your VScode
            The command entered to run the entire test suite will be "npx jest" Which calls on the jest framework to run the entire test suite conjunctively



DELETE:

1. My first test for the DELETE method will check if the status code returned when attempting to delete a kit is 200 OK.

    -First a POST request is created in order to keep the other methods stable and functioning.

    --Next I used the endpoint to retrieve the kitId from this newly created kit.

    ---Then I made the DELETE request and expected a 200 status code returned.

2. My second test for the DELETE method will check if deleting a kit returns a Ok: True response.

   -Like the first test a POST request is created prior to the delete to keep the tests overall stable.

    --Next my endpoint retrieves the kitId from this newly created kit.

    ---Then the delete request is made and we expect a ok: true response in the body.

GET:

1. My first test for the GET method will check if requesting a kit provides a 200 status code.

    -First the statusCode variable is declared.

    --Then the try catch method is used to retrieve the response from the url.

    ---Finally the test expects a 200 status code.

2. My second test for the GET request will show Pizza as the name of the first kit in cardId2.

    -First the responseBody variable is declared.

    --then the try catch method is used to retrieve the response from the url using responseBody to store the returned name from the data.

    ---Finally the test expects the name to be Pizza.


POST:

    1. My first test for the POST method will ensure that checking the delivery cost will return a successful status code.

    -First the requestBody is declared with the respective information stored.

    --Then the statusCode variable is delcared in order to later store the statusCode itself.

    ---Finally the test expects a returned statusCode of 200.


    2. My second test for the POST method will check that the delivery cost for Speedy is 7.

    -First the speedyDeliveryCost variable is declared to store the delivery cost for the speedy method.

    --Then the try catch method is used to return the response from the URL and also return the JSON response as a string.

    ---Finally the test expects the speedy value in the response to be 7.

PUT:

    1. My first test for the PUT method will check that changing the kit name will return a successful status code.

    -First the requestBody is delcared with its respective data.

    --Then the try catch method is used to retrieve the response from the URL and return the JSON response as a string.

    ---Finally the test expects the statusCode to be 200.

    2. My second test will ensure that the responseBody once the kit name is changed returns OK: true showing a successful request.

    -First The responseBody variable is declared to store the response.

    --Then the try catch method is used to retrieve the response from the URL, return the JSON response as a string and extract data.ok from the response.

    ---Finally the test expects the responseBody to return a ok: true response.
