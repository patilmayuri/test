#!/usr/bin/env groovy
build_number = "${env.BUILD_NUMBER}"
job = env.JOB_NAME.split('/')
job_name = job[0]
branch_name = job[1]
git_branch_name = branch_name.replaceAll("%2F","/")
url_branch_name = git_branch_name.replaceAll("/","%252F")


node{
stage('Checkout') {
            checkout scm
}

stage('Test_Python_Code') {
                createVirtualEnv 'env'
    executeIn 'env', 'pip install -r requirements.txt'
    executeIn 'env', './manage.py test'
    executeIn 'env', './manage.py integration-test'
    
    virtualEnv('true')
    runCmd('pip install -r requirements.txt')

}

}