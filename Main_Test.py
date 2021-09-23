'''
Created on Sep 19, 2021

@author: luckyseven67
'''
import asyncio
import logging
import aiohttp
import pyxivapi
from pyxivapi.models import Filter, Sort


async def findCharacterTest(): 
    client = pyxivapi.XIVAPIClient(api_key = "")
    character = await client.character_search(
        world = "Jenova", 
        forename = "Lucky", 
        surname = "Seven",
        )
    
    print(character)
    await client.session.close()
    
async def findItem(): 
    client = pyxivapi.XIVAPIClient(api_key = "")
    
    item = await client.index_search(
        name = "Curtana Ultima", 
        indexes = ["Item"], 
        columns = ["ID", "Name", "LevelItem", "Icon", "LevelEquip"],
        #filters = [Filter("LevelItem", "gte", 350), Filter("LevelItem", "lte", 375)],
    )
    
    for i in item['Results']:
        print(i['ID'])
        print(i['Name'])
        print(i['LevelItem'])
        print(i['Icon'])
        print(i['LevelEquip'])
    
    
    await client.session.close()
    
async def getItemById():
    client = pyxivapi.XIVAPIClient(api_key = "")
    
    itemID = await client.index_by_id(
        index = "Item", 
        content_id = 22868, 
        columns = ["ID", "Name", "Icon", "ItemResult.Description"], 
        language = "en")
    
    
    print(itemID)
    await client.session.close()
    
async def getRecipe():
    client = pyxivapi.XIVAPIClient(api_key = "")
    recipe = await client.index_search(
        name = "Smoked Chicken",
        indexes = ["Recipes"],
        columns = ["Name"]
        
    )
    
    for y in recipe['Results']:
        print(y['Name'])
        break
   
    
    recipe2 = await client.index_search( 
        name = "Smoked Chicken",
        indexes = ["Recipes"],
        columns = ["ItemResult.Description"]
    )
    
    for i in recipe2['Results']:
        if i['ItemResult']['Description'] == 'None':
            pass
        else: 
            print(i['ItemResult']['Description'])
            
    
    
    await client.session.close()
if __name__ == '__main__': 
    
    
    #client = pyxivapi.XIVAPIClient(api_key = "d0d5e08c4eae43418ed8961aa8ab98da6d73185a77854606ae9d87313d6923d6")
    logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='%H:%M')
    loop = asyncio.get_event_loop()
    #loop.run_until_complete(findCharacterTest())
    #loop.run_until_complete(getRecipe())
    #loop.run_until_complete(findItem())
    #loop.run_until_complete(getItemById())

    #loop.run_until_complete(loreSearch())
    
    
    

    
    