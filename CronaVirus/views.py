import json
from .models import CronaVirus

# Create your views here.

# you can also keep this inside a view

print("Something")

# class CronaView()
with open('https://ncov.dxy.cn/ncovh5/view/pneumonia', encoding='utf-8') as data_file:
    json_data = json.loads(data_file.read())

    for movie_data in json_data:
        movie = CronaVirus.create(**movie_data)
