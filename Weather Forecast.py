import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# DATA FOR 2019 EACH MONTH
# Import data by copying file path in the read_csv function
data_2019 = pd.read_csv("<file path>")



# DATA NEEDED TO TRAIN (maybe add "Day", "Time",)
data_2019 = data_2019[["Date/Time", "Rel Hum (%)", "Dew Point Temp (°C)", "Temp (°C)"]]

# PREDICT THE TEMPERATURE
# Let the person input preferred date and time
month = input("Enter a month (between 1 and 12): ")
month = month.zfill(2)

date = input("Enter a date (between 1 and 31): ")
date = date.zfill(2)

time = input("Enter a time (between 0 and 23): ")
time = time.zfill(2)

date_and_time = "2019-" + month + "-" + date + " " + time + ":00"

# Set X = 'Date/Time and Y = 'Temp (°C)'
X = np.array(range(data_2019.shape[0]))
Y = np.array(data_2019["Temp (°C)"])
# Convert DataFrame to list
lst_2019 = data_2019["Date/Time"].values.tolist()




# GET RID OF ALL NaN IN Y
if np.isnan(np.sum(Y)) == True:
    # Find the location/index of all NaN values
    location_of_nan = np.argwhere(np.isnan(Y))

    # Combine the nested list into a single list to make things easier
    single_list_location_of_nan = [item for sublist in location_of_nan for item in sublist]

    # Make it into a new array
    X = np.delete(X, single_list_location_of_nan)
    Y = Y[np.logical_not(np.isnan(Y))]





# PREDICT VALUE
# Create the polynomial best fit
polynomial = np.polyfit(X, Y, 60)

# Convert the date to date number
number = lst_2019.index(date_and_time)

# Equation of polynomial equation
temp_predict = 0
for ind in range(len(polynomial)):
    temp_predict += polynomial[ind] * number**((len(polynomial) - 1) - ind)

print("Predicted Temperature", temp_predict)
actual_temp = Y[number]
print("Actual Temperature", actual_temp)



# OPTIONAL - Plot the points and polynomial function
plt.scatter(X, Y, color='m')
plt.plot(X, np.polyval(polynomial, X), 'b-')
plt.show()
