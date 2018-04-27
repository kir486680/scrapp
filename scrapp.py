import requests
from bs4 import BeautifulSoup
from tqdm import *
import io

class flat:
    def __init__(self , page, main_class , child_class, tag_class):
        self.page = page
        self.main_class = main_class
        self.child_class = child_class
        self.tag_class = tag_class
    def sort_encode(self , first_class , arr):

        for i in  tqdm(range(len(first_class))):
            if self.tag_class == True:
                name = first_class[i].find(class_=self.child_class)
            else :
                name = first_class[i].find(self.child_class)
            main = (name.get_text())
            main = main.replace(u'\xa0', u' ')
            main = main.replace(u'\n', u' ')
            main = str(main)
            arr.append(main)
    def save(self, new_arr):
        with open('hello.txt' , "w", encoding="utf-8" ) as f:
            f.write(new_arr)
    def find(self):
        page_new = requests.get(self.page)
        soup = BeautifulSoup(page_new.content, 'html.parser')
        first_class = soup.find_all(class_=self.main_class)
        arr = []
        self.sort_encode(first_class , arr)
        arr = [x.strip(' ') for x in arr]
        arr = ''.join(arr)
        self.save(arr)


new_flat = flat('https://dom.ria.com/ru/search/?#new_search=&category=1&realty_type=2&operation_type=1&state_id=10&city_id%5B15%5D=10&metro_station_id%5B23%5D=13&characteristic%5B209%5D%5Bfrom%5D=&characteristic%5B209%5D%5Bto%5D=&characteristic%5B214%5D%5Bfrom%5D=&characteristic%5B214%5D%5Bto%5D=&characteristic%5B216%5D%5Bfrom%5D=&characteristic%5B216%5D%5Bto%5D=&characteristic%5B218%5D%5Bfrom%5D=&characteristic%5B218%5D%5Bto%5D=&characteristic%5B227%5D%5Bfrom%5D=&characteristic%5B227%5D%5Bto%5D=&characteristic%5B228%5D%5Bfrom%5D=&characteristic%5B228%5D%5Bto%5D=&characteristic%5B1607%5D%5Bfrom%5D=&characteristic%5B1607%5D%5Bto%5D=&characteristic%5B1608%5D%5Bfrom%5D=&characteristic%5B1608%5D%5Bto%5D=&characteristic%5B234%5D%5Bfrom%5D=&characteristic%5B234%5D%5Bto%5D=&characteristic%5B247%5D=252&characteristic%5B265%5D=0&characteristic%5B242%5D=239&sort=inspected_sort&period=0&realty_id_only=&with_phone=&date_from=&date_to=', 'wrap_desc' , 'blue' , True)
new_flat.find()
second_flat = flat('https://rieltor.ua/flats-sale/%D0%94%D0%B5%D0%BC%D0%B8%D0%B5%D0%B2%D1%81%D0%BA%D0%B0%D1%8F-o340/' , 'catalog-item__title' , 'a' , False)
second_flat.find()
