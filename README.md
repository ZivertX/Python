# Python Task

# Jenkins Configuration
Install Required Plugins: Ensure that your Jenkins instance has the necessary plugins installed, including the Git plugin and any plugins required for Python scripting.

Configure Pipeline Job:

Create a new pipeline job in Jenkins.

Configure the job to use the Jenkinsfile from your Git repository.

Configure Parameters:

Generate new token for push action (Support for password authentication was removed on August 13, 2021.) 
Add TOKEN variable under system variables in Jenkins configuration and paste token string

Run the Pipeline:

Trigger the pipeline build and provide the URLs of the JSON files as parameters.
Monitor the Jenkins console output for any errors or issues.

Example URLs for Testing
For testing purposes, you can use the following example URLs:

URL1: https://example.com/json1.json
URL2: https://example.com/json2.json

Replace these with actual URLs pointing to JSON files you want to merge.
