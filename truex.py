from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Firefox()
driver.get('https://opensource-demo.orangehrmlive.com/')

user = driver.find_element_by_id('txtUsername')
user.send_keys('Admin')

password = driver.find_element_by_id('txtPassword')
password.send_keys('admin123')

driver.find_element_by_id('btnLogin').click()
driver.implicitly_wait(5)

driver.find_element_by_xpath('//*[@class="menu"]/ul/li[2]/a').click()
driver.find_element_by_xpath('//*[@class="menu"]/ul/li[2]/a/b').click()
driver.find_element_by_id('menu_pim_viewPimModule').click()
driver.implicitly_wait(10)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'menu_pim_addEmployee')))
driver.find_element_by_id('menu_pim_addEmployee').click() 
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'firstName')))

empName = driver.find_element_by_id('firstName')
empName.send_keys('Purple')
driver.implicitly_wait(10)

mpMiddleName = driver.find_element_by_id('middleName')
mpMiddleName.send_keys('Hrm')
driver.implicitly_wait(10)

lastName = driver.find_element_by_id('lastName')
lastName.send_keys('Automation')

saveButton = driver.find_element_by_xpath('//*[@id="btnSave"]')
saveButton.click()
#sometimes click doesn't work depending on the browser version
try:
 saveButton.send_keys(Keys.RETURN)
except:
 print("Error")
 
driver.find_element_by_id('menu_pim_viewEmployeeList').click()
empNameSearch = driver.find_element_by_id('empsearch_employee_name_empName')
driver.implicitly_wait(10)
empNameSearch.send_keys('Purple Hrm Automation')
driver.implicitly_wait(10)
driver.find_element_by_id('searchBtn').click()

table_id = driver.find_element(By.ID, 'resultTable')
rows = table_id.find_elements(By.TAG_NAME, "tr")
col = row.find_elements(By.TAG_NAME, "td")[1] 
assert 'Purple' in col

driver.close()
driver.quit()
