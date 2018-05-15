import smtplib
import requests
from bs4 import BeautifulSoup
import csv
class flat:
    def __init__(self , page, main_class , child_class,  link_new):
        self.page = page
        self.main_class = main_class
        self.child_class = child_class
        self.link_new = link_new
        print(link_new)
    def find(self):
        arr = []
        new_arr = []

        page_new = requests.get(self.page)
        encoding = page_new.encoding if 'charset' in page_new.headers.get('content-type', '').lower() else None
        soup = BeautifulSoup(page_new.content, "lxml" , from_encoding=encoding)

        first_class = soup.find_all(class_=self.main_class)
        print(first_class)


        self.children_loop_format(soup, first_class , arr)
        arr = list(set(arr))

        for i in range (len(arr)):
            arr[i] = self.link_new+arr[i]

        print(arr)
        self.find_in_each(arr, new_arr)
        print(new_arr)
    def children_loop_format(self, first_class, soup , arr):

        for a in first_class.find_all('a', href=True):
            name = a['href']

            if 'object' in name:

                arr.append(name)

    def find_in_each(self , arr, new_arr):

        for i in range(len(arr)):
            print(arr[i])
            page = requests.get(arr[i])
            soup = BeautifulSoup(page.content, 'html.parser')
            first_class = soup.find_all(class_='object-overall' )
            for a in first_class:
                a = a.get_text()
                print("+++++++++++++++")
                with open ('flat.txt' , 'a' , encoding='utf-8')as f:
                    writer = csv.writer(f)
                    if 'Голосеевская' in a:
                        writer.writerow([arr[i] , a,])
            self.send_mail(a)
    def send_mail(a):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("kir486680@gmail.com", "My2ndmail")

        msg = a
        server.sendmail("kir486680@gmail.com", "THE EMAIL ADDRESS TO SEND TO", msg)
        server.quit()
def main():
    #new_flat = flat('https://dom.ria.com/ru/%D0%9A%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3/%D0%9F%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0/%D0%9A%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80%D1%8B/%D0%9A%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80%D0%B0/%D0%9E%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C/%D0%9A%D0%B8%D0%B5%D0%B2%D1%81%D0%BA%D0%B0%D1%8F/%D0%93%D0%BE%D1%80%D0%BE%D0%B4/%D0%9A%D0%B8%D0%B5%D0%B2/%D0%9C%D0%B5%D1%82%D1%80%D0%BE/%D0%94%D0%B5%D0%BC%D0%B8%D0%B5%D0%B2%D1%81%D0%BA%D0%B0%D1%8F/?page=5', 'wrap_desc' , 'blue' , 'https://dom.ria.com' )
    #new_flat.find()
    new_flat1 = flat('https://100realty.ua/realty_search/apartment/sale/rc_78/cur_3/kch_2', 'object-address' , 'object-address'  , 'https://100realty.ua' )
    new_flat1.find()
if __name__ == '__main__':
    main()
