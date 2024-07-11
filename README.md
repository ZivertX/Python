# Python Task

# Jenkins Configuration
Install Required Plugins: Ensure that your Jenkins instance has the necessary plugins installed, including the Git plugin
and Python requests library (run in command line `sudo apt install python3-pip && python -m pip install requests`) or via Pipeline

Configure Pipeline Job:

Create a new pipeline job in Jenkins.

Configure the job to use the Jenkinsfile from your Git repository.

Configure Parameters:

Generate new token for push action (Support for password authentication was removed on August 13, 2021.) 
Add TOKEN variable under system variables in Jenkins configuration and paste token string

Run the Pipeline:

After first pipeline run you can provide the URLs of the JSON files as parameters in Jenkins GUI.
