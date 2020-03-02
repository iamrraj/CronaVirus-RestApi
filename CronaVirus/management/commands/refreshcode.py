from django.core.management.base import BaseCommand
import requests
from CronaVirus.models import CronaVirus, Area, Cities, News, Remours


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
        r = requests.get(url)
        titles = r.json()
        print("Hello", titles)
        for title in titles['results']:
            CronaVirus.objects.update_or_create(
                currentConfirmedCount=title['currentConfirmedCount'],
                confirmCount=title['confirmedCount'],
                suspectedCount=title['suspectedCount'],
                curedCount=title['curedCount'],
                deadCount=title['deadCount'],
                seriousCount=title['seriousCount'],
                currentConfirmedIncr=title['currentConfirmedIncr'],
                confirmIncr=title['confirmedIncr'],
                suspectedIncr=title['suspectedIncr'],
                curedIncr=title['curedIncr'],
                seriousIncr=title['seriousIncr'],
                deadIncr=title['deadIncr'],
                updateTime=title['updateTime'],
                note1=title['note1'],
                note2=title['note2'],
                note3=title['note3'])

         # Then pass this dict below as the template context
        context = {'titles': CronaVirus.objects.all()}

        url1 = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
        r = requests.get(url1)
        titles1 = r.json()
        print("Hello", titles1)

        for titlee in titles1['results']:

            for name in titlee['cities'] or []:
                print(name)
                # if name is isNull:
                #     return
                Cities.objects.update_or_create(
                    cityName=name['cityName'],
                    locationId=name['locationId'],
                    currentConfirmedCount=name['currentConfirmedCount'],
                    confirmCount=name['confirmedCount'],
                    suspectedCount=name['suspectedCount'],
                    curedCount=name['suspectedCount'],
                    deadCount=name['deadCount']
                )

            context = {'name': Cities.objects.all()}

        for title in titles1['results']:
            Area.objects.update_or_create(
                updateTime=title['updateTime'],
                locationId=title['locationId'],
                continentName=title['continentEnglishName'],
                country=title['countryEnglishName'],
                provinceName=title['provinceEnglishName'],
                currentConfirmedCount=title['currentConfirmedCount'],
                confirmCount=title['confirmedCount'],
                suspectedCount=title['suspectedCount'],
                curedCount=title['suspectedCount'],
                deadCount=title['deadCount']
            )


# For New Api

        context = {'titles1': Area.objects.all()}

        url1 = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
        r = requests.get(url1)
        titles1 = r.json()
        #print("Remour", titles1[0:10])

        for title in titles1['results']:
            News.objects.update_or_create(
                pubdate=title['pubDate'],
                title=title['title'],
                summary=title['summary'],
                infosource=title['sourceUrl'],
                provinceName=title['provinceName'],
                provinceId=title['provinceId']
            )

        context = {'titles': News.objects.all()}


# For Remour Api

        url1 = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
        r = requests.get(url1)
        titles1 = r.json()

        for title in titles1['results']:
            Remours.objects.update_or_create(
                _id=title['_id'],
                title=title['title'],
                mainSummary=title['mainSummary'],
                infosource=title['sourceUrl'],
                body=title['body'],
            )

        context = {'titles': Remours.objects.all()}
