#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Rover-Reanbot app
    ~~~~~~~~~~~~~~~~
"""

import jenkins


#JENKINS_URL = os.environ["JENKINS_URL"] + "/"
#JENKINS_USERNAME = os.environ["JENKINS_USERNAME"]
#JENKINS_TOKEN = os.environ["JENKINS_TOKEN"]
#headers={'Authorization': JENKINS_USERNAME +":"+ JENKINS_TOKEN, 'Accept': 'application/json'}

PRINT "HELLP"
def take_action():
        #server = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_TOKEN)
        server = jenkins.Jenkins("http://jenkins.platform.itsreaning.com:80", username="mayuri.patil", password="kklKL")
        print server