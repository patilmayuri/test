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
            int exitCode = 0
            try {
              stage('Getting the dependencies') {
                echo "\u001B[34m\u001B[1mInstalling the Dependencies\u001B[0m"
                try {
                  sh '''
                        #!/bin/bash
                        set -e
                        pip install -r collect/src/requirements.txt
                  '''
                }
                catch (Exception e) {
                  println "\u001B[31mInstalling dependencies failed. Please fix the issues\u001B[0m"
                  sh "exit 1"
                }
              }

            }
            }
            }
        }
    }                   