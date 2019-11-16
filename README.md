# ATG_UI_automation
********************

This is web automation framework, implemented using Python & Webdriver. Page Object Model (POM) is used to make the code more readable, maintainable, and reusable

The framework has following features:
******************************************

	* Modular Design
	* Implemented POM 
	* Reporting support : nosetest (as of now)

Prerequisite:
*********************	

	* Python
	* pip
	* Selenium/WebDriver
	* nosetests & nose-html-reporting
	* Browsers (Firefox, Chrome, IE)
	* Respective Browser drivers
	* Pycharm
	
Automation Framework Structure :
*********************************

	ATG_UI_automation 
		data
			- contains data generation file
		drivers
			- contains executable file of drivers
		locators
		pages
			- all Web Elements of the application and the method that operate on these Web Elements are maintained
		testcases
			- contains Testcases/scenarios
		testrun_evidences
			- contains video of testcase
		utilities
			- contains utils as DriverManager, Services etc. for creation of automation instance and wrapper of selenium methods
		README.	MD
		
## Execution Commands :
*********************************

Single Testcase Run Command:
> nosetests -s -v --nologcapture LoginTest.py

All testcase run in one flow:
> ls *.py|xargs -n 1 -P 1 nosetests 

Single testcase which is with given tag name:
> nosetests -s -v --nologcapture -a website=party LoginTest.py

All testcase of given tag:
> ls *.py|xargs -n 1 -P 1 nosetests -s -v --nologcapture -a website=party

		
## UI Automation Scenarios automated :
*****************************************

https://docs.google.com/spreadsheets/d/1LaULZaSckJcK0goFkBN-6rc9038WdZBapSts_cJWquw/edit#gid=1777955675

## Running Scrapers:
> python "filename"
