import requests
from bs4 import BeautifulSoup
import csv
from multiprocessing import Pool

class flat:
    def __init__(self , page, main_class , child_class, second_page,  link_new):
        self.page = page
        self.main_class = main_class
        self.child_class = child_class
        self.link_new = link_new
        self.second_page = second_page
        print(link_new)
    def find(self):
        arr = []
        new_arr = []

        page_new = requests.get(self.page)
        encoding = page_new.encoding if 'charset' in page_new.headers.get('content-type', '').lower() else None
        soup = BeautifulSoup(page_new.content, "lxml" , from_encoding=encoding)

        first_class = soup.find_all(class_=self.main_class)
        self.children_loop_format(soup, first_class , arr)
        for i in range (len(arr)):
            arr[i] = self.link_new+arr[i]

        self.find_in_each( arr , new_arr)

    def children_loop_format(self, first_class, soup , arr):

        for a in first_class.find_all('a',class_=self.child_class, href=True):
            name = a['href']
            arr.append(name)
    def find_in_each(self , arr, new_arr ):

        for i in range(len(arr)):
            print(arr[i])
            page = requests.get(arr[i])
            soup = BeautifulSoup(page.content, 'html.parser')
            first_class = soup.find_all(self.second_page )

            for a in first_class:
                a = a.get_text()
                a = a.replace(u'\xa0', u' ')
                a = a.splitlines()

                new_arr.append(a)




            with open('flat.txt' , 'a',encoding='utf-8')as f :
                writer = csv.writer(f)
                for i in range (len(arr)):
                    str_arr = ', '.join(map(str, new_arr))
                    str_arr = str_arr.replace(' ' , '')
                    str_arr = str_arr.replace(']' , '')
                    str_arr = str_arr.replace('[' , '')
                    str_arr = str_arr.replace('↓' , '')

                    writer.writerow([arr[i]  , str_arr])
def main():
    new_flat = flat('https://dom.ria.com/ru/%D0%9A%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3/%D0%9F%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0/%D0%9A%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80%D1%8B/%D0%9A%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80%D0%B0/%D0%9E%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C/%D0%9A%D0%B8%D0%B5%D0%B2%D1%81%D0%BA%D0%B0%D1%8F/%D0%93%D0%BE%D1%80%D0%BE%D0%B4/%D0%9A%D0%B8%D0%B5%D0%B2/%D0%9C%D0%B5%D1%82%D1%80%D0%BE/%D0%94%D0%B5%D0%BC%D0%B8%D0%B5%D0%B2%D1%81%D0%BA%D0%B0%D1%8F/?page=5', 'wrap_desc' , 'blue' , 'dd' , 'https://dom.ria.com' )
    new_flat.find()

if __name__ == "__main__":
    main()
