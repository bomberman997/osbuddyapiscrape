import requests
import pprint

class ScraperThing():
    def __init__(self):
        self.info = ''
        self.link = 'https://rsbuddy.com/exchange/summary.json'
        #self.theJson = 
        self.sortbyBuy = []

    def scrape(self):
        res = requests.get(self.link)
        return res.json()

    def changeLink(self,newLink):
        self.link = newLink

    def getHighBuyList(self,mportedList):
        for x in mportedList:
            #print(mportedList[x]['name'],' : ', mportedList[x]['id'],' : ', mportedList[x]['buy_quantity'])
            tmp = mportedList[x]['buy_quantity']
            tmp2 = mportedList[x]['name']
            tmp3 = mportedList[x]['sell_quantity']
            tmp4 = mportedList[x]['buy_average']
            tmp5 = mportedList[x]['sell_average']
            self.sortbyBuy.append([int(tmp),tmp2,int(tmp3),int(tmp4),int(tmp5)])
            self.sortbyBuy.sort()
    
    def printList(self,listToPrint):
        if listToPrint == '1':
            for x in self.sortbyBuy:
                if x[3] < x[4]:
                    print(x)




scrapingObject = ScraperThing()
scrapingObject.changeLink('https://rsbuddy.com/exchange/summary.json')
thing = scrapingObject.scrape()
scrapingObject.getHighBuyList(thing)
scrapingObject.printList('1')
