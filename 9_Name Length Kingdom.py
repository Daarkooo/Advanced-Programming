cities = []

while True:
    city_name = input("Enter the city name (or type 'stop' to finish): ")
    if city_name.lower() == "stop":
        break
    else:
        population = len(city_name) * 1000000
        cities.append((city_name, population))


cities.sort(key=lambda x: x[1], reverse=True)


for city, population in cities:
    print(f"{city}: {population} citizens")
