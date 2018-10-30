import time
from selenium import webdriver
from lep.selenium import utils 

def vanilla(driver, details):
    driver.get("https://www.facebook.com")
    
    utils.slow_fill(
        driver.find_element_by_xpath("//input[@name='firstname']"),     
        details["first_name"]
    )

    utils.slow_fill(
        driver.find_element_by_xpath("//input[@name='lastname']"), 
        details["last_name"]
    )

    utils.slow_fill(
        driver.find_element_by_xpath("//input[@name='reg_email__']"), 
        details["mail"]
    )

    utils.slow_fill(
        driver.find_element_by_xpath("//input[@name='reg_passwd__']"), 
        details["password"]
    )

    driver.find_element_by_xpath("//select[@name='birthday_day']").send_keys(details["birth_day"])
    time.sleep(0.3)

    driver.find_element_by_xpath("//select[@name='birthday_month']").send_keys(details["birth_month"])
    time.sleep(0.3)

    driver.find_element_by_xpath("//select[@name='birthday_year']").send_keys(details["birth_year"])
    time.sleep(0.3)

    gender_string = "Male" if details["male"] else "Female"  
    driver.find_element_by_xpath("//label[text()='{}']".format(gender_string)).click()

    utils.slow_fill(
        driver.find_element_by_xpath("//input[@name='reg_email_confirmation__']"),
         details["mail"]
    )

    time.sleep(0.2)    
    driver.find_element_by_xpath("//button[@name='websubmit']").click()