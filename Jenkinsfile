#!/usr/bin/env groovy
build_number = "${env.BUILD_NUMBER}"
job = env.JOB_NAME.split('/')
job_name = job[0]
branch_name = job[1]
git_branch_name = branch_name.replaceAll("%2F","/")
url_branch_name = git_branch_name.replaceAll("/","%252F")

node{
        try
        {
            stage('Checkout') {
            checkout scm
            }

            stage('Test_Python_Code') {
            withPythonEnv('python') {  
            echo "Running: Test_Python_Code"
            // supress echo 
              sh '''
               #!/bin/bash
                export BOT_TOKEN=xxxxxx
                export BOT_ID=xxxx
                export REAN_DEPLOY_URL=https://deploynow.reancloud.com/DeployNow/rest
                export REAN_DEPLOY_USERNAME=xxxxx
                export REAN_DEPLOY_PASSWORD=xxxxx
                export JENKINS_URL=http://35.161.44.53:8080
                export JENKINS_TOKEN=xxxxx
                export JENKINS_USERNAME=dmin
                set +x
                virtualenv my_project
                virtualenv -p /usr/bin/python2.7 my_project
                export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python2.7
                source my_project/bin/activate
                pip install python-lambda
              '''
            }
         }
        }

            catch(e)
            {
                stage('Email_Notification_For_Failures') {
        
                    step([$class: 'WsCleanup', cleanWhenFailure: true])
                }
                throw e
            }
              echo "testing ......"
    }