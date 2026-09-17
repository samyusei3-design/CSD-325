#Samuel Guizar
#9/16/26
#Module 7.2 Assignment 

#Create a function that accepts a city and country name as parameters
def city_country(city, country, population='', language=''):

    #If elif statements to check if population and language are provided
    if population and language:
        return f"{city}, {country} - Population: {population}, {language}"
    elif population:
        return f"{city}, {country} - Population: {population}"
    elif language:
        return f"{city}, {country}, {language}"
    else:
        return f"{city}, {country}"

#Call the function with different parameters to test it
print(city_country("Santiago", "Chile"))
print(city_country("Winston Salem", "United States", 257271))
print(city_country("Puebla", "Mexico", 1692181, "Spanish"))


