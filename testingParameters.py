import logging
import re

"""
Text fields examples:=========================

['Худи мужская Adidas R.Y.V. ALIEN',
 'HC9451',
  '-30%',
   '257 р. 60 к. BYN',
    'Все дело в деталях. Приглядись к Трилистнику на этой худи adidas. Что 
    ты видишь? Даем подсказку. Он шлет тебе привет из самых далеких глубин 
    космоса. Мягкий махровый трикотаж дарит вполне земной комфорт. Рифленые 
    манжеты и нижний край усиливают ощущение уюта.']
"""


class TestFunctions:

    def __init__(self, lst):
        self.lst = lst
        self.productname, \
        self.label, \
        self.discount, \
        self.price, \
        self.description = lst

    def length_check(self):
        def min_max_len_check_log(p, mn, mx):
            if len(p) < mn:
                logging.info(f"Widget \"{p}\" should have more "
                             f"symbols than {mn}.")
            if len(p) > mx:
                logging.info(f"Widget \"{p}\" should have less "
                             f"symbols. The limit is {mx}.")

        for param in self.lst:
            # Zero content check
            if len(param) <= 0:
                logging.info(f"Widget is empty. Information "
                             f"indication is a must in this field.")
            # Min/max amount of characters check.
            if param == self.productname:
                min_len = 10
                max_len = 50
                min_max_len_check_log(param, min_len, max_len)
            if param == self.description:
                min_len = 30
                max_len = 500
                min_max_len_check_log(param, min_len, max_len)

    def content_check(self):
        # Brand name incorporation. Case-insensitive.
        pattern_brand = re.compile(r"\bAdidas\b", re.IGNORECASE)
        # Serial number of label check.
        pattern_label = re.compile(r"^[A-Z]{2}[0-9]{4}$")
        # Price discount check.
        pattern_discount = re.compile(r"^-[0-9]{1,3}%$")
        # Price format check.
        pattern_price = re.compile(r"^[0-9]{1,5}\sр\.\s[0-9]{2}\sк\.\sBYN$", )

        if not re.search(pattern_brand, self.productname):
            logging.info(f"Widget \"productname\" should have "
                         f"brand name in it.")
        if not re.search(pattern_label, self.label):
            logging.info(f"Widget \"label\" should meet a pattern.")
        if not re.search(pattern_discount, self.discount):
            logging.info(f"Widget \"discount\" should meet a pattern.")
        if not re.search(pattern_price, self.price):
            logging.info(f"Widget \"price\" should meet a pattern.")
        if not re.search(pattern_brand, self.description):
            logging.info(f"Widget \"description\" should should have "
                         f"brand name in it.")


logging.basicConfig(filename='failed_tests_info.log',
                    level=logging.INFO,
                    filemode="w", )

if __name__ == '__main__':
    pass
