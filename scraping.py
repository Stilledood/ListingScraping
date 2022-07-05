from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.by import By
import datetime
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Scrapping:


    def __init__(self,name=None):
        self.name=name


    def scrapping(self,search_criteria,number_of_pages,location_file,custom_name=None):
        CHROMEDRIVER_PATH = 'chromedriver_win32/chromedriver.exe'
        DRIVER = webdriver.Chrome(CHROMEDRIVER_PATH)

        DRIVER.get('https://www.publi24.ro/')

        search_bar=DRIVER.find_element("xpath","//*[@id='keyword']")
        search_bar.send_keys(search_criteria)
        DRIVER.implicitly_wait(3)
        search_button=DRIVER.find_element('xpath',"//*[@id='btn-search']/span")
        search_button.click()
        dataframe=pd.DataFrame(columns=['title','details','listing_body','location','date_added','price'])
        i=0
        while i < number_of_pages:


            listing_list=DRIVER.find_element('xpath',"//*[@id='content']/div/div/div[5]/ul[1]")
            items=listing_list.find_elements(By.TAG_NAME,'li')
            

            for item in items:
                try:
                    listing_details=item.find_element(By.CLASS_NAME,'listing-data')
                    listing_details_dict={}
                    try:
                        title_link=listing_details.find_element(By.CLASS_NAME,'maincolor')
                        title=title_link.get_property('text')
                        if title is None:
                            title='No title'
                        listing_details_dict['title']=title
                    except:
                        pass


                    try:
                        listing_body=listing_details.find_element(By.CSS_SELECTOR,"div[class='small-12 columns description'] > p ").text
                        listing_details_dict['listing_body']=listing_body
                    except:
                        pass


                    try:
                        details=listing_details.find_element(By.CLASS_NAME,"article-details").text
                        listing_details_dict['details']=details
                    except:
                        pass


                    try:
                        location=listing_details.find_element(By.CLASS_NAME,'article-location').text
                        listing_details_dict['location'] = location
                    except:
                        pass


                    try:
                        date_dict={
                            'ianuarie':'01',
                            'februarie':'02',
                            'martie':'03',
                            'aprilie':'04',
                            'mai':'05',
                            'iunie':'06',
                            'iulie':'07',
                            'august':'08',
                            'septembrie':'09',
                            'octombrie':'10',
                            'noiembrie':'11',
                            'decembrie':'12'
                        }
                        date_added=listing_details.find_element(By.CLASS_NAME,'article-date').text
                        if date_added[:3] == 'azi':
                            date_added=str(datetime.date.today())
                        else:
                            date_list=date_added.split(' ')
                            date_added=str(datetime.datetime.now().year)+' '+date_dict[date_list[1]]+' '+date_list[0]
                        listing_details_dict['date_added']=date_added
                    except:
                        pass

                    try:
                        price=listing_details.find_element(By.CSS_SELECTOR,"div[class='large-4 medium-5 large-text-right medium-text-right columns prices'] > strong").text
                        listing_details_dict['price']=price
                    except:
                        pass

                    listing_details_dict_dataframe=pd.DataFrame([listing_details_dict])
                    dataframe=pd.concat([dataframe,listing_details_dict_dataframe],ignore_index=True)

                except:
                    pass
            i+=1
            pages=DRIVER.find_element('xpath',"//*[@id='content']/div/div/div[5]/ul[2]")
            pages_list=pages.find_elements(By.TAG_NAME,'li')


            next_page=pages_list[-1]


            WebDriverWait(DRIVER, 5).until(expected_conditions.element_to_be_clickable(next_page))
            time.sleep(5)
        if len(custom_name) > 0:
            dataframe.to_excel(f'{location_file}\{custom_name}.xlsx',sheet_name='Sheet_1')
        else:
            file_name=''.join(search_criteria.split(' '))
            dataframe.to_excel(f'{location_file}\{file_name}.xlsx', sheet_name='Sheet_1')




a=Scrapping('todo')
a.scrapping('Dacia Logan',2,'C:/Users/User/Desktop','logan')