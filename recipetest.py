__author__ = 'hannavaj'
print "starts here"

import urllib2
import pprint
import json,xmltodict
dishName = 'poha';
response = urllib2.urlopen('http://api.bigoven.com/recipes?title_kw='+dishName+'&api_key=eMJWJQ5O3650gQlzMap35EV1JQhdOZXr&pg=1&rpp=20').read()
response = xmltodict.parse(response)
response = json.dumps(response)
response = json.loads(response)
for recipeInfo in response[u'RecipeSearchResult'][u'Results'][u'RecipeInfo']:
    #print recipeInfo[u'Cuisine']
    if recipeInfo[u'Cuisine'] == "Indian" and recipeInfo[u'Title'] == "Poha":
        #print recipeInfo[u'RecipeID']
        recipeId = recipeInfo[u'RecipeID']
        break
print "after FOR LOOP"

recipeResponse = urllib2.urlopen('http://api.bigoven.com/recipe/'+recipeId+'?api_key=eMJWJQ5O3650gQlzMap35EV1JQhdOZXr').read()
recipeResponse = xmltodict.parse(recipeResponse)
recipeResponse = json.dumps(recipeResponse)
recipeResponse = json.loads(recipeResponse)
for ingredient in recipeResponse[u'Recipe'][u'Ingredients'][u'Ingredient']:
    print ingredient[u'Name']
#pprint.pprint(recipeResponse)

#pprint.pprint(response)
"""
import urllib2
url = "webservice"
s = urllib2.urlopen(url)
contents = s.read()
file = open("export.xml", 'w')
file.write(contents)
file.close()
"""