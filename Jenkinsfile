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
                set -e
                pip install python-jenkins
              '''
            }
         }
        }

            catch(e)
            {
                stage('Email_Notification_For_Failures') {
                    notifyBuild("FAILED","${e}")
                    step([$class: 'WsCleanup', cleanWhenFailure: true])
                }
                throw e
            }
                notifyBuild(currentBuild.result,"NULL")
    }

def sendEmail(toAddress, emailSubject, emailBody) {
  mail to: toAddress,
  subject: emailSubject,
  body: emailBody
}

def notifyBuild(String buildStatus = 'STARTED',String thiserr) {
  buildStatus =  buildStatus ?: 'SUCCESSFUL'

        def colorName = 'RED'
        def colorCode = '#FF0000'

  if (buildStatus == 'STARTED') {
    color = 'YELLOW'
    colorCode = '#FFFF00'
  } else if (buildStatus == 'SUCCESSFUL') {
    color = 'GREEN'
    colorCode = '#00FF00'
          step([$class: 'GitHubCommitStatusSetter',
        contextSource: [$class: 'ManuallyEnteredCommitContextSource',
        context: 'BUILD STATUS'],
        statusResultSource: [$class: 'ConditionalStatusResultSource',
        results: [[$class: 'AnyBuildResult',
        message: 'SUCCESSFUL',
        state: 'SUCCESS']]]])
        echo "status set to ${buildStatus}."
  } else if (buildStatus == 'FAILED') {
    color = 'RED'
    colorCode = '#FF0000'
          step([$class: 'GitHubCommitStatusSetter',
        contextSource: [$class: 'ManuallyEnteredCommitContextSource',
        context: 'BUILD STATUS'],
        statusResultSource: [$class: 'ConditionalStatusResultSource',
        results: [[$class: 'AnyBuildResult',
        message: 'FAILED',
        state: '${buildStatus}']]]])
        echo "status set to ${buildStatus}."
        def subject = "${buildStatus}: Job '${job} [${build_number}]'"
        sh "git log --after 1.days.ago|egrep -io '[a-z0-9\\-\\._@]++\\.[a-z0-9]{1,4}'|head -1 >lastAuthor"
        sh "set +x;sed -i 's/ //g' lastAuthor"  //fixing the email adddress
        def lines = readFile("lastAuthor")
        println "Email notifications will be send to : ${lines}"
          sendEmail("${lines}, ashish.modak@reancloud.com", "${subject}", "Details available at ${env.BUILD_URL}")
}
        step([$class: 'WsCleanup', cleanWhenFailure: true])
}