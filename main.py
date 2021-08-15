from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# To be printed dollar
dollar = "$" * 99

# User Inputs

print('\n', dollar)

print('')


print('\n', dollar)




# Importing Chrome Driver

driver_path = "./chromedriver.exe"
chrome_options = Options()
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

# Where the Magic happens function


# Browser Maximized
time.sleep(2)
driver.maximize_window()

# Getting Url
time.sleep(2)
driver.get("https://www.thesparksfoundationsingapore.org/")

# Logo Checked
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="home"]/div/div[1]/h1/a"""))).click()
print('\n' + """Test Case - 1 
Logo Checked""" + '\n')

# Dropdown Togger About US Button Checked
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[1]/a"))).click()
print("""Test Case - 2 
About US Button Checked""" + '\n')

# Dropdown Togger About US 1st Element Checked
time.sleep(2)
driver.find_element_by_xpath("""/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[1]/ul/li[1]/a""").click()
print("""Test Case - 3
1st Element Checked 'Vision, Mission And Values'""" + '\n')

time.sleep(2)
driver.find_element_by_xpath("""/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[1]/a""").click() #Again Clicking on About us Button

# Dropdown Togger About US 2st Element Checked
time.sleep(2)
driver.find_element_by_xpath("""/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[1]/ul/li[2]/a""").click()
print("""Test Case - 4
2nd Element Checked 'Guiding Principles'""" + '\n')

time.sleep(2)
driver.find_element_by_xpath("""/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[1]/a""").click() #Again Clicking on About us Button

# Dropdown Togger About US 3st Element Checked
time.sleep(2)
driver.find_element_by_xpath("""/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[1]/ul/li[3]/a""").click()
print("""Test Case - 5
3rd Element Checked 'Advisors And Patrons'""" + '\n')

time.sleep(2)
driver.find_element_by_xpath("""/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[1]/a""").click() #Again Clicking on About us Button

# Dropdown Togger About US 4st Element Checked
time.sleep(2)
driver.find_element_by_xpath("""/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[1]/ul/li[4]/a""").click()
print("""Test Case - 6
4th Element Checked 'Executive Team'""" + '\n')

time.sleep(2)
driver.find_element_by_xpath("""/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[1]/a""").click() #Again Clicking on About us Button

# Dropdown Togger About US 5th Element Checked
time.sleep(2)
driver.find_element_by_xpath("""/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[1]/ul/li[5]/a""").click()
print("""Test Case - 7
5th Element Checked 'Corporate Partners'""" + '\n')

time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[2]/a"))).click()
print("""Test Case - 8
6th Element Checked """ + '\n')

time.sleep(4)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[3]/a"))).click()
print("""Test Case - 9
7th Element Checked """ + '\n')

time.sleep(4)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[4]/a"))).click()
print("""Test Case - 10
8th Element Checked """ + '\n')

time.sleep(4)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[5]/a"))).click()
print("""Test Case - 11
9th Element Checked """ + '\n')

# Contact US
time.sleep(4)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[6]/a"))).click()
print("""Test Case - 12
10th Element Checked """ + '\n')

time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="home"]/div/div[1]/h1/a"""))).click()





#################### Footer Section Start ####################


html = driver.find_element_by_tag_name("html")
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)
html.send_keys(Keys.DOWN)



# FB 
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[1]/a"))).click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
driver.close()
driver.switch_to.window(driver.window_handles[0])

time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[2]/a"))).click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
driver.close()
driver.switch_to.window(driver.window_handles[0])

time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[3]/a"))).click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
driver.close()
driver.switch_to.window(driver.window_handles[0])

time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[4]/a"))).click()
print("")
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
driver.close()
driver.switch_to.window(driver.window_handles[0])

time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[5]/a"))).click()
print("")
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
driver.close()
driver.switch_to.window(driver.window_handles[0])

time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[6]/a"))).click()
print("")
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
driver.close()
driver.switch_to.window(driver.window_handles[0])



time.sleep(60)
driver.quit()