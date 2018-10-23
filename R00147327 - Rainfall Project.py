# Name: Graeme Hosford
# Student ID: R00147327
# Programming for Data Analytics Project 01

import numpy as np


def show_menu():
    """This method shows the menu to the user and asks for their choice on what to run"""

    print("Menu")
    print("1. Basic Statistics for Total Rainfall (Millimetres)")
    print("2. Basic Statistics for Most Rainfall in a Day (Millimetres)")
    print("3. Basic Statistics for Number of Rain Days (0.2mm or More)")
    print("4. Wettest Location")
    print("5. Percentage of Rain Days")
    print("6. Exit")

    menu_option = int(input("Please select one of the above options: "))

    return menu_option


def show_cities():
    """This method displays the list of cities and asks for the users choice on what one to view info on"""

    print("1. Cork")
    print("2. Belfast")
    print("3. Dublin")
    print("4. Galway")
    print("5. Limerick")

    city_picked = int(input("Please select a location: "))

    city = ""

    if city_picked == 1:
        city = "Cork"
    elif city_picked == 2:
        city = "Belfast"
    elif city_picked == 3:
        city = "Dublin"
    elif city_picked == 4:
        city = "Galway"
    elif city_picked == 5:
        city = "Limerick"

    return city


def show_basic_city_stats(city, filename):
    """This method shows thee basic stats of the cities for the first menu option"""

    file = np.genfromtxt(filename, dtype=float, delimiter=" ")

    rain_array = file[:, 2]

    print(city, "Max Total Rainfall =", np.max(rain_array))
    print(city, "Average Total Rainfall =", np.mean(rain_array))


def show_stats_for_total_rainfall():
    """Menu Option 1: Asks for the users choice of city before passing their choice to show the basic stats"""
    city = show_cities()
    show_basic_city_stats(city, city + "Rainfall.txt")


def show_rain_per_day_stats(city, filename):
    file = np.genfromtxt(filename, dtype=float, delimiter=" ")

    rain_per_day_array = file[:, 3]

    print(city, "Max Most rainfall in a Day", np.max(rain_per_day_array))
    print(city, "Average Rainfall in a Day", np.mean(rain_per_day_array))


def show_rainfall_in_a_day_stats():
    """Menu Option 2: Asks for choice of city then displays the rainfall info by calling show_rain_days_stats"""

    city = show_cities()
    show_rain_per_day_stats(city, city + "Rainfall.txt")


def show_rain_days_stats(city, filename):
    """Shows the stats for the rain days info"""
    file = np.genfromtxt(filename, dtype=float, delimiter=" ")

    rain_days_array = file[:, 4]

    print(city, "Max Number of Rain Days", np.max(rain_days_array))
    print(city, "Average Number of rain Days", np.mean(rain_days_array))


def show_rain_days():
    """Menu Option 3: Gets city then shows the rain days info"""

    city = show_cities()
    show_rain_days_stats(city, city + "Rainfall.txt")


def show_wettest_location():
    """Menu Option 4: Shows the wettest location out of all the cities"""

    cork_file = np.genfromtxt("CorkRainfall.txt", dtype=float, delimiter=" ")
    belfast_file = np.genfromtxt("BelfastRainfall.txt", dtype=float, delimiter=" ")
    dublin_file = np.genfromtxt("DublinRainfall.txt", dtype=float, delimiter=" ")
    galway_file = np.genfromtxt("GalwayRainfall.txt", dtype=float, delimiter=" ")
    limerick_file = np.genfromtxt("LimerickRainfall.txt", dtype=float, delimiter=" ")

    cork_array = cork_file[:, 2]
    belfast_array = belfast_file[: 2]
    dublin_array = dublin_file[:, 2]
    galway_array = galway_file[:, 2]
    limerick_array = limerick_file[:, 2]

    cork_value = np.sum(cork_array)
    belfast_value = np.sum(belfast_array)
    dublin_value = np.sum(dublin_array)
    galway_value = np.sum(galway_array)
    limerick_value = np.sum(limerick_array)

    values = np.array([cork_value, belfast_value, dublin_value, galway_value, limerick_value])

    max_value = np.max(values)

    if max_value == cork_value:
        wettest_city = "Cork"
    elif max_value == belfast_value:
        wettest_city = "Belfast"
    elif max_value == dublin_value:
        wettest_city = "Dublin"
    elif max_value == galway_value:
        wettest_city = "Galway"
    else:
        wettest_city = "Limerick"

    print("1. Cork", cork_value, "mm")
    print("2. Belfast", belfast_value, "mm")
    print("3. Dublin", dublin_value, "mm")
    print("4. Galway", galway_value, "mm")
    print("5. Limerick", limerick_value, "mm")

    print("The wettest location in Ireland is", wettest_city, "with a rainfall figure of", max_value, "mm")


def get_city_percent(city, number):
    """Returns the percentage of rain days for a given city and under or equal to  a given number"""

    file = np.genfromtxt(city + "Rainfall.txt", dtype=float, delimiter=" ")

    array = file[:, 4]

    num_rows = 0

    for row in array:
        if row <= number:
            num_rows += 1

    percent = (num_rows / len(array)) * 100

    return percent


def show_percentage_rain_days():
    """Menu Option 5: Shows the percentage of raind ays for each city"""

    number = int(input("Please enter maximum threshold value for number of rain days"))

    print("The following are the percentage of rain days less than or equal to", number)

    cork_value = get_city_percent("Cork", number)

    print("1. Cork", cork_value, "%")

    belfast_value = get_city_percent("Belfast", number)

    print("2. Belfast", belfast_value, "%")

    dublin_value = get_city_percent("Dublin", number)

    print("3. Dublin", dublin_value, "%")

    galway_value = get_city_percent("Galway", number)

    print("4. Galway", galway_value, "%")

    limerick_value = get_city_percent("Limerick", number)

    print("5. Limerick", limerick_value, "%")


def main():
    """Shows the menu to the user and runs the correct method based on their input"""

    menu_choice = -1

    while menu_choice != 6:
        menu_choice = show_menu()

        if menu_choice == 1:
            show_stats_for_total_rainfall()
        elif menu_choice == 2:
            show_rainfall_in_a_day_stats()
        elif menu_choice == 3:
            show_rain_days()
        elif menu_choice == 4:
            show_wettest_location()
        elif menu_choice == 5:
            show_percentage_rain_days()


main()
