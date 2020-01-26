# SharepointTag
 Used to extract rtags relating to files uploaded to a SP /library.

 Steps.
 1. Install/Check if we have virtualenv module installed
 2. Create a requirements.txt file and list down all modules needed for this app
 3. Create venv using python -m venv virtualenv
 4. Activate it using ./virtualenv/Scripts/Activate.ps1
 5. Now run pip-install -r requirements.txt this will install all needed packages to virtualenv\include\lib
 6. Create  a .env file and list all variables here as key value pair  Password=mypassword
 7. Create a git ignore file to ignore .env from checking in to sc
 8. Looks like evertyhing is fine from desktop now let's host it as a Azure webapp
 9.Also Commit all the chnages from VS code which will sync to the local git.In GitHub Desktop publish this to web
 10. Make sure to get Azure Web App extensiion in VS Code and you can directly push the file
 

