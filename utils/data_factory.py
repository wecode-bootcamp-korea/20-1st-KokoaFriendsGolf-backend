import csv
import random

from faker import Faker

from data.mockup_data import CATEGORY, PRODUCT_IMAGES, PRODUCT_NAME_PREFIX, ENG_KO, DETAIL_CONTENTS

USER_NUMBER      = 1000
NEW_RATE         = 0.05
SALE_RATE        = 0.1
SOLDOUT_RATE     = 0.03
SET_RATE         = 0.01
PICKED_RATE      = 0.05
PRICE_VOLATILITY = 0.03

class DataFactory:
    def __init__(self):
        self.fake = Faker('ko_KR')

    def gen_user(self):
        profile = self.fake.profile()
        user = {
            'email'       : profile['mail'],
            'password'    : self.fake.password(),
            'phone_number': self.fake.unique.phone_number(),
            'name'        : profile['name'],
            'birthday'    : profile['birthdate'],
            'gender'      : profile['sex']
            }
        
        return user

    def gen_users(self, num_users):
        users = []
        
        for _ in range(num_users):
            users.append(self.gen_user())

        return users

    def gen_product(self, product_image_url):
        [ category_eng, subcategory_eng, character_eng, _ ] = product_image_url.split('.')[-2].split('/')[-1].split('-')
        category_ko                                         = ENG_KO[category_eng]
        subcategory_ko                                      = ENG_KO[subcategory_eng]
        character_ko                                        = ENG_KO[character_eng]
        name                                                = self.get_random_element(PRODUCT_NAME_PREFIX) + " " + subcategory_ko + "-" + character_ko
        avg_price                                           = self.search_data('name', subcategory_ko, self.search_data('name', category_ko, CATEGORY)['subcategory'])['avg_price']
        price                                               = 1000 * round(random.randint(avg_price*(1-PRICE_VOLATILITY), avg_price*(1+PRICE_VOLATILITY))/1000)
        thumbnail_url                                       = product_image_url
        is_new                                              = self.get_random_true(NEW_RATE)
        is_sale                                             = self.get_random_true(SALE_RATE)
        is_soldout                                          = self.get_random_true(SOLDOUT_RATE)
        is_set                                              = self.get_random_true(SET_RATE)
        is_picked                                           = self.get_random_true(PICKED_RATE)
        contents                                            = DETAIL_CONTENTS[category_eng]
        discount_ratio                                      = 0 if not is_sale else (random.randint(1,5)/10)

        return {
            "category"      : category_ko,
            "subcategory"   : subcategory_ko,
            "character"     : character_ko,
            "name"          : name,
            "price"         : price,
            "thumbnail_url" : thumbnail_url,
            "is_new"        : is_new,
            "is_sale"       : is_sale,
            "is_soldout"    : is_soldout,
            "is_set"        : is_set,
            "is_picked"     : is_picked,
            "contents"      : contents,
            "discount_ratio": discount_ratio,
        }


    def gen_products(self, image_urls = PRODUCT_IMAGES):
        products = []
        for url in image_urls:
            products.append(self.gen_product(url))
        return products
    
    def save_to_csv(self, db, file_path):
        
        with open(file_path, 'w', encoding="utf-8-sig", newline="") as f:
            column_names = list(db[0].keys())
            writer       = csv.DictWriter(f, fieldnames= column_names)
            writer.writeheader()

            for data in db: 
                writer.writerow(data)
        
        return

    def get_random_true(self, probability):
        return random.random() < probability
    
    def get_random_element(self, array):
        index = random.randint(0, len(array)-1)
        return array[index]
    
    def search_data(self, key, value, data):
        return list(filter(lambda d: d[key] == value, data))[0]