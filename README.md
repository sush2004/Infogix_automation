# Infogix_automation
Contents: I. Introduction II. Resources III. The implementation: Approach and description of the test case

I. Introduction: Create in Python using Pytest an automated test case for the website https://www.infogix.com/.

Task: • Write an automated test for https://www.infogix.com/

II. Resources and commands to install it in Pycharm IDE. •The program has been developed using Pycharm Python IDE Community Edition Release 2020.2.3 (Python version 3.8.1) •Selenium WebDriver Language Binding 3.141.0 for Python on windows 10. -- pip install selenium. •Pytest(version - 6.2.4) framework has been used here. -- pip install pytest •Pytest html report(version 0.2.6) for test execution report -- pip install pytest-html-reporter

III. The implementation: There are 2 test cases.

Description of the test case: It access the web application and the performs 2 different verification and validations (using assert) on different elements available on the web application. It verifies Thank you message in test case1 which comes after filling up of the form available on the web application. It inserts different values fields available in the form. The test case2 verifies the url embedded inside the link.

Finally, the automation script is integrated with Jenkins to build, test, and deploy the script.
