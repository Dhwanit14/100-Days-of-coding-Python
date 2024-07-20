# #Nestings

# capitals = {
#     "France" : "Paris",
#     "Germany" : "Berlin",
# }

# #Nesting a list in a Dictionary
# travel_vlog = {
#     {"country":"india"  ,
#       "cities_visited" : ["Ahmedbad" , "Surat" , "Bhavnagar"] ,
#        "total_visits" : 50 
#     } ,
#     {"country":"Canada"  ,
#       "cities_visited" : ["Kitchener" , "Waterloo" , "Toronto"] ,
#        "total_visits" : 5 
#     } 
# }

# #Nesting a dictionary in a list
# travel_vlog = [
#     {"country":"india"  ,
#       "cities_visited" : ["Ahmedbad" , "Surat" , "Bhavnagar"] ,
#        "total_visits" : 50 
#     } ,
#     {"country":"Canada"  ,
#       "cities_visited" : ["Kitchener" , "Waterloo" , "Toronto"] ,
#        "total_visits" : 5 
#     } 
# ]
# print(travel_vlog)


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

country_name = input("Enter the country name you visited:")
visits = input("Enter the no. visits in the country :")
cities = input("Enter the cities you visted in the country:")
cities_list = list(cities.split(","))
def add_new_country(country_name,visits,cities):
    new_country = {
        "country" : country_name ,
        "visits" : visits,
        "cities" : cities
    }
    travel_log.append(new_country)
print(f"you visites {country_name} {visits} times." )

print(f"you have been to {cities} cities." )
     

add_new_country(country_name,visits,cities)

print(travel_log)

   



