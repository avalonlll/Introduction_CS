import json, requests
movie=raw_input("Please give movie's name \n")
movie= movie.replace(" ", "+") #replace space with + 
url = "http://www.omdbapi.com/?t="+movie #omdb link with movie's information
response = requests.get(url) #fetching movie's information
print "Awards:" +json.loads(response.text)['Awards'] #print movie's awards
print "imdbRating:" +json.loads(response.text)['imdbRating'] #print movie's rating


