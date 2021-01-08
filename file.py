from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import csv 



fields = ['Full Name', 'Gender', 'Title', 'Race','Birthday','Social Security Number','Street','City','State','State Full','Zip Code','Phone Number','Mobile Number','Temporary mail','Height','Weight','Hair Colour','Blood Type','Mother Maiden Name','Civil Status','Educational Background','Driver License','Employment Status','Monthly Salary','Occupation(Job Title)','Company Name','Company Size','Industry','Credit Card Type','Credit Card Number','CVV2','Expires','Vehicle','Car License Plate','Online Status','Online Signature','Online Biography','Interest','Favorite Color','Favorite Movie','Favorite Music','Favorite Song','Favorite Book','Favorite Sports','Favorite TV','Favorite Movie Star','Favorite Singer','Favorite Food','Personality','Personal Style','Username','Password','Website','Security Question','Security Answer','Browser User Agent','System','GUID','Telephone Country Code']

# name of csv file  
filename = "data.csv"
num = int(input('enter the number of users data you want to be scraped : \n'))
# writing to csv file  
with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)


    chrome_options = Options()

    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://www.fakeaddressgenerator.com/')
    data_final = []
    for i in range(1,num+1):
        print(i)
        try:
            data = []
            # BASIC INFORMATION
            for j in range(1,7):
                user = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, f'/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/div[2]/table/tbody/tr[{j}]/td[2]/strong')
                    )
                ).text
                data.append(user)
            # ADDRESS
            for j in range(3,11):
                inputs = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, f'/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[{j}]/div[2]/strong/input')
                    )
                )
                
                data.append(inputs.get_attribute('value'))
            # MORE BASIC INFORMATION   
            for j in range(12,19):
                inputs = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, f'/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[{j}]/div[2]/strong/input')
                    )
                )
                data.append(inputs.get_attribute('value'))
                #print(j)
            
            user =  WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, f'/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[19]/div[2]/strong')
                )
            ).text
            data.append(user)
            # EMPLOYMENT & FINANCE 
            for j in range(21,31):
                inputs = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, f'/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[{j}]/div[2]/strong/input')
                    )
                )
                data.append(inputs.get_attribute('value'))
            # PERSONAL INFO & ONLINE PROFILE 
            for j in range(32,61):
                if(j == 38 or j == 51):
                    continue
                try:
                    inputs = driver.find_element_by_xpath(f'/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[{j}]/div[2]/strong/input')
                    data.append(inputs.get_attribute('value'))
                except:
                    inputs = WebDriverWait(driver, 2).until(
                        EC.presence_of_element_located(
                            (By.XPATH, f'/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[{j}]/div[2]/strong')
                        )
                    ).text
                    data.append(inputs)
            
            
            csvwriter.writerow(data)
            driver.get('https://www.fakeaddressgenerator.com/')
        except:
            driver.get('https://www.fakeaddressgenerator.com/')
            i = i-1
            
            
            
driver.close()
            
if __name__ == "__main__":
    print('done')
