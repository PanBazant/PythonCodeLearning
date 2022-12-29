#Nesting Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits":5},
}

#Nesting Dictionary in a List
travel_log_list = [
    {"country": "France", "cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits": 12},
    {"country": "Germany", "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
]

def add_new_country(country, total_visits, cities_visited):
    new_record = {"country": country, "cities_visited": cities_visited, "total_visits": total_visits}
    travel_log_list.append(new_record)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log_list)
