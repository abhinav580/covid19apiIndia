# COVID 19 India API

##Brief

This was developed using webscraping to obtain COVID-19 cases data specifically in India. The code is open to all as well as I have hosted it in a VM for you all to access.

If you are interested in developing a visualisation tool or contribute to the API, please contact me [Avirup Basu](mailto:avirup.basu@live.com?subject=[COVID-19%20API%20GITHUB]) or simply create a pull request in dev branch.

##How to use

* **Endpoint**:  52.171.216.227:5001/api/v1.0/covid19
* **Request Type**: GET

##Response pattern

It contains a json with the following fields

* **total_cases**
* **total_death**
* **total_recovered**
* **state_information**

State information contains a list of all the state level cases. Following are the information that are contained

* state_name
* total_case_local
* total_death
* total_discharged
* total_case_foreign

##Data sources

* [MOHFW](https://www.mohfw.gov.in/)
* [Woldometer](https://www.worldometers.info/)

