# Selenium Tests Example on Python

### Requirements
- `Java Runtime Environment (JRE)` or `OpenJDK` to run `Allure`. Download from [here](https://www.oracle.com/ru/java/technologies/javase-jre8-downloads.html) (or use package managers).
- `Allure` - reporting tool. Download from [here](https://docs.qameta.io/allure/). Don't forget to add Allure executable file directory into your system PATH variable (to be able to use `allure` command from your CLI - cmd, powershell or terminal).

### Install packages
> pip install -r requirements.txt

### Run tests
> pytest alluredir=allure-results 

### Report scripts
Generate Allure report:
> allure generate allure-results -o allure-report

Open Allure report:
> allure open allure-report