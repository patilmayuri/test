#!/usr/bin/env groovy

pipeline {
  agent {
    node {
      label 'master'
    }
  }
  stages {
    stage('Build Environment') {
      steps {
        echo "\u001B[34m\u001B[1mPreparing build environment\u001B[0m"
        script {
          ansiColor('xterm') {
            withPythonEnv('python2.7') {
            int exitCode = 0
            try {
              stage('Getting the dependencies') {
                echo "\u001B[34m\u001B[1mInstalling the Dependencies\u001B[0m"
                try {
                  pysh '''
                        #!/bin/bash -l
                        set -e
                        pip install -r requirements.txt
                        
                  '''
                }
                catch (Exception e) {
                  println "\u001B[31mInstalling dependencies failed. Please fix the issues\u001B[0m"
                  sh "exit 1"
                }
              }
              stage('Code Style Linting') {
                echo "\u001B[34m\u001B[1mCode Style Linting\u001B[0m"
                try {
                  pysh '''
                        #!/bin/bash
                        set -x
                        lambda build --use-requirements
                        lambda invoke -v
                  '''
                }
                catch (Exception e) {
                  println "\u001B[31mCode style linting failed. Please fix the issues\u001B[0m"
                  sh "exit 1"
                }
              }



          
              println "\u001B[31m\u001B[1m Continuous Integration pipeline passed\u001B[0m"
            }
            catch (Exception e) {
              println "\u001B[31m\u001B[1mERROR: Continuous Integration pipeline failed\u001B[0m"
              currentBuild.result = 'FAILURE'
            }
          }
        }
        }
        
      }
    }
  }

}