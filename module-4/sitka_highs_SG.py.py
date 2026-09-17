import csv
import sys
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

#Reads dates and temperatures from the CSV file and returns them as lists
#Created a function to prevent duplicating code for both high and low temperatures
def load_data(columns):

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        #Get dates and temperatures from this file
        dates, temps = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            temp = int(row[columns])
            temps.append(temp)

    return dates, temps

#Plot and format the data
#Created a function to plot and format the highs and lows, and added ability to change the color and label for plotting
def plot_temps(dates, temps, color, label):

    #plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)

    # Format plot.
    plt.title(f"Daily {label} temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

#Display menu instructions
#Created function to display the menu instructions
def display_menu():

    print('Sitka Weather Data - 2018')
    print('Select which data you would like to view:')
    print('High - View High Temperatures')
    print('Low - View Low Temperatures')
    print('Exit - End the program')

#Main function to run the program and loop to let the user choose which data to view
#Created a main function to run the program and handle user input
def main():

    display_menu()

    while True:
        choice = input('Enter your choice (High, Low, Exit): ').strip().lower()

        if choice == 'high':
            dates, temps = load_data(5)  
            plot_temps(dates, temps, 'red', 'High')

        elif choice == 'low':
            dates, temps = load_data(6)
            plot_temps(dates, temps, 'blue', 'Low')

        elif choice == 'exit':
            print('Exiting the program.')

            sys.exit()

        else:
            print('Invalid choice. Please enter High, Low, or Exit.')


#Run the main function
if __name__ == '__main__':
    main()