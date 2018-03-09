#!/usr/bin/env groovy
build_number = "${env.BUILD_NUMBER}"
job = env.JOB_NAME.split('/')
job_name = job[0]
branch_name = job[1]
git_branch_name = branch_name.replaceAll("%2F","/")
url_branch_name = git_branch_name.replaceAll("/","%252F")

node{
 withPythonEnv('python2.7') {  
        try
        {
            stage('Checkout') {
            checkout scm
            }

            stage('Test_Python_Code') {
             
            echo "Running: Test_Python_Code"
            // supress echo
              sh '''set +x;
                export BOT_TOKEN=xxxxxx
                export BOT_ID=xxxx
                export REAN_DEPLOY_URL=https://deploynow.reancloud.com/DeployNow/rest
                export REAN_DEPLOY_USERNAME=xxxxx
                export REAN_DEPLOY_PASSWORD=xxxxx
                export JENKINS_URL=http://35.161.44.53:8080
                export JENKINS_TOKEN=xxxxx
                export JENKINS_USERNAME=admin
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
}