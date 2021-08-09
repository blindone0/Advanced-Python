import json
import codecs


class Laptop:
    name = 'My Laptop'
    processor = 'Intel Core'


# create object
laptop1 = Laptop()
laptop1.name = 'ЮТФ ТЕСТ'
laptop1.processor = 'Intel Core i7'

# convert to JSON string
jsonStr = json.dumps(laptop1.__dict__, ensure_ascii=False) #dump to console

with codecs.open('your_file.txt', 'w', encoding='utf-8') as f:
    json.dump({"message":"xin chào việt nam"}, f, ensure_ascii=False)

# print json string
print(jsonStr)