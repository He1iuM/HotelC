from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import re

page = 0
browser = webdriver.Chrome()
headers = ['Name', 'Address', 'Diamond', 'Value', 'Medal', 'Price']
titlen = re.compile(r"title=\"(.*?)\"")
with open('hotels_gz20180909.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    browser.get('http://hotels.ctrip.com/hotel/guangzhou32#ctm_ref=ctr_hp_sb_lst')
    for page in range(1, 450):
        time.sleep(8)
        print(page)
        hotel_list = browser.find_element_by_id('hotel_list')
        html = hotel_list.get_attribute('innerHTML')
        soup = BeautifulSoup(html)
        head_tag = soup.find_all('div', 'hotel_new_list')
        total_list = []
        for i in head_tag:
            tlist = []
            soup2 = BeautifulSoup(str(i))
            title_tag = soup2.find('h2')
            if len(title_tag.contents[0]) > 2:
                title = title_tag.contents[0].contents[2]
            else:
                title = title_tag.contents[0].contents[1]
            tlist.append(title)

            address_tag = soup2.find('p', 'hotel_item_htladdress')
            address = ""
            for string in address_tag.strings:
                address = address + string
            # try:
            #     address_1 = address_tag.contents[1].contents[0]
            #     address_2 = address_tag.contents[2]
            #     print(type(address_2))
            #     # if address_2 == " " :
            #     #     address_2 = address_tag.contents[3].contents[0]
            #     #     address_3 = address_tag.contents[4].contents[0]
            #     #     address = '【' + str(address_1) + str(address_2) + str(address_3)
            #     # else:
            #     address = '【' + str(address_1) + str(address_2)
            # except:
            #     address = address_tag.contents[0]
            tlist.append(address)


            diamond_tag = soup2.select('span[class*="hotel_diamond"]')
            if not diamond_tag:
                diamond_tag = soup2.select('span[class*="hotel_stars"]')
                if diamond_tag == []:
                    diamond_tag = []
                    tlist.append(diamond_tag)
                else:
                    tlist.append(diamond_tag[0]['class'])
            else:
                tlist.append(diamond_tag[0]['class'])

            value_tag = soup2.find('span', 'hotel_value')
            if value_tag:
                value = value_tag.contents[0]
            else:
                value_tag = []
            tlist.append(value)
            # print (value)

            medal_tag = soup2.find('p', 'medal_list')
            mlist = []
            if medal_tag.contents:
                for i in medal_tag.contents[0].contents:
                    mlist.append(i.contents[0])
                # print (i.contents[0])
            tlist.append(mlist)

            price_tag = soup2.find('span', 'J_price_lowList')
            price = price_tag.contents[0]
            tlist.append(price)

            total_list.append(tlist)
        # print (price)
        try:
            writer.writerows(total_list)
        except:
            pass
        adClose = browser.find_element_by_id('appd_wrap_close')
        linkElem = browser.find_element_by_id('downHerf')
        try:
            adClose.click()
            time.sleep(3)
        except:
            pass
        try:
            linkElem.click()
            print('click')
        except:
            pass
