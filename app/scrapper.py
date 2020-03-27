import requests
import lxml.html as lh
import json
from flask import jsonify

def getData():
    url_state="https://www.mohfw.gov.in/"
    page=requests.get(url_state)
    doc=lh.fromstring(page.content)
    state_json={}
    response_json={}
    state_dat=[]
    ##Total stats
    url_total="https://www.worldometers.info/coronavirus/country/india/"
    page_total=requests.get(url_total)
    total_doc=lh.fromstring(page_total.content)
    root_list=total_doc.xpath('//div[@class="maincounter-number"]')
    
    total_cases_object=root_list[0].xpath('.//span')
    total_cases_value=total_cases_object[0].text
    response_json["total_cases"]=total_cases_value.replace(" ", "")

    total_death_object=root_list[1].xpath('.//span')
    total_death_value=total_death_object[0].text
    print(total_death_value)
    response_json["total_death"]=total_death_value.replace(" ", "")

    total_recovered_object=root_list[2].xpath('.//span')
    total_recovered_value=total_recovered_object[0].text
    response_json["total_recovered"]=total_recovered_value.replace(" ", "")

    root=doc.xpath('//div[@class="table-responsive"]')
    table_object=root[7]
    table_list=table_object.xpath('.//tbody')
    table_data_list=table_list[0].xpath('.//tr')
    length=len(table_data_list)
    count=0
    for state_table_list in table_data_list:
        if count==(length-2):
            break
        count=count+1
        state_information_list=state_table_list.xpath('td')
        state_json["state_name"]=state_information_list[1].text
        state_json["total_case_local"]=state_information_list[2].text
        state_json["total_case_foreign"]=state_information_list[3].text
        state_json["total_discharged"]=state_information_list[4].text
        state_json["total_death"]=state_information_list[5].text
        state_json_processed=json.dumps(state_json)
        state_json_decoded=json.loads(state_json_processed)
        #print(state_json_processed)
        state_dat.append(state_json_decoded)

    response_json["state_information"]=state_dat
    return response_json

def main():
    data = getData()
    print(data)
if __name__ == '__main__':
    main()
