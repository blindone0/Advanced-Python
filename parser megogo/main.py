from bs4 import BeautifulSoup
import json


class MegogoEntity:
    count = 0
    subscriptions_list = []

    def __init__(self, id, title, title_en, categories, genres, serial, page, type, kinopoisk, vod, qual, budget,
                 country, duration, dvd, premiere, year, subscriptions):
        MegogoEntity.count += 1
        self.subscriptions = subscriptions
        for s in subscriptions:
            if s not in MegogoEntity.subscriptions_list:
                MegogoEntity.subscriptions_list.append(s)
        self.country = country
        self.duration = duration
        self.dvd = dvd
        self.premiere = premiere
        self.year = year
        self.budget = budget
        self.qual = qual
        self.categories = categories
        self.genres = genres
        self.serial = serial
        self.page = page
        self.type = type
        self.kinopoisk = kinopoisk
        self.vod = vod
        self.title_en = title_en
        self.id = id
        self.title = title

    def dump(self):
        print(f' id: {self.id} ; title : {self.title} ; category: {self.categories} : subs: {self.subscriptions} ')

    def getObjectsCoutn(self):
        print(MegogoEntity.count)

    def getSubscriptionList(self):
        print(MegogoEntity.subscriptions_list)

    def serialize(self):
        return {
            'title': self.title,
            'categories': self.categories,
            'subscriptions': self.subscriptions
        }


with open("tv_mgg_3.xml", encoding="UTF-8") as fp:
    soup = BeautifulSoup(fp, "lxml")

objects = soup.find_all('object')

json_array = []

for o in objects:
    o_qual = []
    subscriptions = []
    for q in o.contents[20].contents:
        for ii in q:
            if ii.attrs['service_name'] not in subscriptions:
                subscriptions.append(ii.attrs['service_name'])

    for q in o.contents[0]:
        o_qual.append(q.attrs['value'])
    a = o.attrs
    budget = o.contents[1].attrs['budget']
    country = o.contents[1].attrs['country']
    duration = o.contents[1].attrs['duration']
    dvd = o.contents[1].attrs['dvd']
    premiere = o.contents[1].attrs['premiere']
    year = o.contents[1].attrs['year']
    meg = MegogoEntity(a['id'], a['title'], a['title_en'], a['categories'], a['genres'], a['serial'], a['page'],
                       a['type'], a['kinopoisk_id'], a['vod'], o_qual, budget, country, duration, dvd, premiere, year,
                       subscriptions)
    meg.getObjectsCoutn()
    # meg.dump()
    json_array.append(meg.serialize())

y = json.dumps(json_array).encode('utf8')

yy = y
print(yy)
f = open("json.txt", "w")
f.write(yy)
f.close()

x = 0
# for o in objects:
#     for i in o.contents[20]:
#         print(x)
#         x = x + 1
#         print(i)


# for i in range(len(objects[0].contents)):
#     print(i)
#     print(objects[0].contents[i])
# v = 0
# for i in objects:
#     v+=1
#     print(v)
#     print(i.contents[20].contents)

# print(objects[0].contents)
