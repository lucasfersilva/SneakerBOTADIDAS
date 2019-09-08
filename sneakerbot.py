from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def UrlGenwithSize(size,model,name):
    base=590 #for a shoe size 7
    mySize=(size-7)+20 #increment 8= 610
    finalSize=base+mySize
    Url="https://www.adidas.com.au/"+name+"/"+model+".html?forceSelSize="+model+"_"+srt(finalSize)
    print(Url)

def UrlGenProduct(name,model):
    url="https://www.adidas.com.au/"+name+"/"+model+".html"
    print(url)
    
 
def CheckStock(myUrl, model):
    try:
        driver= webdriver.Chrome()
        driver.get(myUrl)
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, "add_to_bag_form___22702")))
        username= driver.find_elements_by_tag_name("option") 
        opitionsList=[]
        for options in options:
            optionsList.append(option.get_attribute("innerHTML"))
            for sizes in opitionsList:
                print("size"+ sizes + "For" + model + "is available")
    finally:
        driver.quit()

    UrlGenProduct("ultraboost-19-shoes", "G54011")

    UrlGenwithSize(7,"G54011","ultraboost-19-shoes" )
  















    