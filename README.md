# Appium

Task Completed for Project
==========================
- Android automation using Appium
- iOS automation using Appium
- Created separate codex file for android
- Automated surveymonkey android app
- Written script to add 5 type of question in survey and preview survey
  including sign-in and sign-out
- Script contains 4 testcases, in that one is forcefully failed to 
  show reports.
  
Userdefine Command Line Parameters/Options for project :
========================================================

--device
    usage   : Run script on emulator/simulator or real android/ios 
              devices
    options : "Android Emulator", "Android device"
    default : "Android Emulator"
    
--codexFile
    usage   : Automate android app or ios app
    options : "android", ios
    default : "android"
    
Pytest built-in Command Line Parameters/Options for project :
=============================================================

--html
    usage  : Generate html report for test result
    option : Path-for-report-file
             In our case report will be generate in this path
             "/home/vishal/gitrepo/appiumDemo/Results/report.html" 

    
Commmand to run script :
========================
   py.test --device="Android device" --codexFile=android test-path 
           --html=path-for-report-file
   In our case :
   Command :
   py.test --device="Android device" --codexFile=android /home/vishal/gitrepo/appiumDemo/createSurvey_using_appium.py 
   --html=/home/vishal/gitrepo/appiumDemo/Results/report.html
   
Flow :
======

   Script -> Selenium grid -> Appium Node -> Appium server -> emulator/
      real device
   You can run script using jenkins job.
     