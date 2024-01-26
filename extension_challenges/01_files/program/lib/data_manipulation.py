import os
import csv

# == INSTRUCTIONS ==
#
# Below, you'll find lots of incomplete functions.
#
# Your job: Implement each function so that it does its job effectively.
#
# Tips:
# * Use the material, Python Docs and Google as much as you want
#
# * A warning: the data you are using may not contain quite what you expect;
#   cleaning data (or changing your program) might be necessary to cope with
#   "imperfect" data

# == EXERCISES ==

# Purpose: return a boolean, False if the file doesn't exist, True if it does
# Example:
#   Call:    does_file_exist("nonsense")
#   Returns: False
#   Call:    does_file_exist("AirQuality.csv")
#   Returns: True
# Notes:
# * Use the already imported "os" module to check whether a given filename exists
def does_file_exist(filename):
    try:
        open(filename, 'r')
        return True
        
    except:
        return False

# Purpose: get the contents of a given file and return them; if the file cannot be
# found, return a nice error message instead
# Example:clear
#   Call: get_file_contents("AirQuality.csv")
#   Returns:
#     Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);[...]
#     10/03/2004;18.00.00;2,6;1360;150;11,9;1046;166;1056;113;1692;1268;[...]
#     [...]
#   Call: get_file_contents("nonsense")
#   Returns: "This file cannot be found!"
# Notes:
# * Learn how to open file as read-only
# * Learn how to close files you have opened
# * Use readlines() to read the contents
# * Use should use does_file_exist()
def get_file_contents(filename):
    if does_file_exist(filename):
        f = open(filename, 'r')
        return (f.readlines())
    else:
        return 'This file cannot be found!'



# Purpose: fetch Christmas Day (25th December) air quality data rows, and if
# boolean argument "include_header_row" is True, return the first header row
# from the filename as well (if it is False, omit that row)
# Example:
#   Call: christmas_day_air_quality("AirQuality.csv", True)
#   Returns:
#     Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);[...]
#     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
#     [...]
#   Call: christmas_day_air_quality("AirQuality.csv", False)
#   Returns:
#     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
#     [...]
# Notes:
# * should use get_file_contents() - N.B. as should any subsequent
# functions you write, using anything previously built if and where necessary
def christmas_day_air_quality(filename, include_header_row):
    list_func = lambda item: [i for i in x if i.split(';')[0] == item]
    x = get_file_contents(filename)
    if include_header_row == True:
        return(list_func('Date') + list_func('25/12/2004'))
    else:
        return(list_func('25/12/2004'))
    
list1 = christmas_day_air_quality("AirQuality.csv", True)






# Purpose: fetch Christmas Day average of "PT08.S1(CO)" values to 2 decimal places
# Example:
#   Call: christmas_day_average_air_quality("AirQuality.csv")
#   Returns: 1439.21
# Data sample:
# Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);NOx(GT);PT08.S3(NOx);NO2(GT);PT08.S4(NO2);PT08.S5(O3);T;RH;AH;;
# 10/03/2004;18.00.00;2,6;1360;150;11,9;1046;166;1056;113;1692;1268;13,6;48,9;0,7578;;
def christmas_day_average_air_quality(filename):
    value = 0.0
    for i in christmas_day_air_quality(filename,False):
        value += float(i.split(';')[3])
    return round(value/len(christmas_day_air_quality(filename,False)),2)
    



# Purpose: scrape all the data and calculate average values for each of the 12 months
#          for the "PT08.S1(CO)" values, returning a dictionary of keys as integer
#          representations of months and values as the averages (to 2 decimal places)
# Example:
#   Call: get_averages_for_month("AirQuality.csv")
#   Returns: {1: 1003.47, [...], 12: 948.71}
# Notes:
# * Data from months across multiple years should all be averaged together
def get_averages_for_month(filename):
    new_dict = {}
    number_list = []
    x = get_file_contents(filename)
    for x in [i for i in x if i.split(';') if i.split(';')[0] != 'Date']:
        number_list.append(x.split(';')[0][3:5])
    dictionary = dict.fromkeys(filter(None, number_list))
    for i in dictionary.keys():
        new_dict[int(i)] = None
    for i in dictionary.keys():
       new_dict[int(i)] = pop_list('AirQuality.csv',i)
    return(new_dict)     
def pop_list(filename,mounth):
    mounth_list_value = 0
    x = get_file_contents(filename)
    index = 0
    for x in [i for i in x if i.split(';') if i.split(';')[0] != 'Date']:
        if x.split(';')[0][3:5] == mounth:
            mounth_list_value += float(x.split(';')[3])
            index +=1
    return round(mounth_list_value/index,2)







    



# Purpose: write only the rows relating to March (any year) to a new file, in the same
# location as the original, including the header row of labels
# Example
#   Call: create_march_data("AirQuality.csv")
#   Returns: nothing, but writes header + March data to file called
#            "AirQualityMarch.csv" in same directory as "AirQuality.csv"

def create_march_data(filename):
    list_func_heading = lambda item: [i for i in x if i.split(';')[0] == item]
    list_func_values = lambda item: [i for i in x if i.split(';')[0][3:5] == item]
    x = get_file_contents(filename)
    values = (list_func_heading('Date')+list_func_values('03'))
    with open(r'AirQualityMarch.csv', 'w') as file:
        for item in values:
            file.write(item)
        

   

# Purpose: write monthly responses files to a new directory called "monthly_responses",
# in the same location as AirQuality.csv, each using the name format "mm-yyyy.csv",
# including the header row of labels in each one.
# Example
#   Call: create_monthly_responses("AirQuality.csv")
#   Returns: nothing, but files such as monthly_responses/05-2004.csv exist containing
#            data matching responses from that month and year
def create_monthly_responses(filename):
    try:  
        os.mkdir('monthly_responses')
    except OSError as error:  
        print(error) 
    
    list_func_heading = lambda item: [i for i in x if i.split(';')[0] == item]
    list_func_values = lambda item: [i for i in x if i.split(';')[0][3:10] == item]
    x = get_file_contents(filename)
    number_list = []
    for x in [i for i in x if i.split(';') if i.split(';')[0] != 'Date']:
        number_list.append(x.split(';')[0][3:10])
        new_dict = dict.fromkeys(filter(None, number_list))
    date_list = new_dict.keys()
    
    x = get_file_contents(filename)
    for i in date_list:
        
        values = (list_func_heading('Date')+list_func_values(i))
        
        with open('/Users/jameswiehe/Documents/projects/python_foundations/extension_challenges/01_files/program/monthly_responses/'+i.replace('/','-')+'.csv', 'w') as file:
            for item in values:
                file.write(item)


        

