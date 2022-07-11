import glob
from time import time

import pandas as pd
import matplotlib.pyplot as plt

import math
from statistics import mean

"""
Tickets folder Setup

This code assigns the relative filepath for the tickets folder.
"""

drivePath = 'tickets'

""" Binning
This means to group similar data values together. For example, you might want to group similar levels of performance together to then count how many values fall in each group.
Feel free to use this function as is, or experiment with it / do your own research to best adjust it to suit your needs.
"""

def binning(old_col, df, xlabel, new_col):
    ''' Distributes data across bins '''

    df[new_col] = pd.cut(df[old_col], 30) # split into 30 bins
    new_data = df[new_col].value_counts().sort_index() # count how many goes into which bins
    new_df = pd.DataFrame(new_data)
    new_df.index.name = xlabel
    new_df.reset_index(inplace=True)

    return new_df

""" Data Mining

It is standard these days for technology companies to have access to large amounts of data about how their products and services are used. By intelligently using this data, companies can gain insight into how to optimise their business plan. Using data mining techniques we can programmaticaly achieve this goal on large data sets.

Read Throughput Performance

This example function reads a JSON file (a text file structured to be easily machine readable) of performance data, and stores information on read throughput (kilobytes/second, or how fast data is being read). 

For each ticket, the average read throughput is saved. At the end this data is then grouped into bins and counted, before being saved as a graph.

This gives us an indication of how regularly these machines are being pushed to the limit of their read throughput capacity.
"""

def read_throughput_miner(path = f'{drivePath}/'):
    ''' Loops through disk metrics calculating average '''

    print('Starting read throughput analysis...')
    start = time()

    data = {}
    avg_read_throughput = []

    tickets = glob.glob(path + '/*')

    # Goes through each ticket and finds the average of each performance metric for each ticket
    for ticket in tickets:
        print(ticket)
        try:
            disk_json = pd.read_json(ticket + '/resource-monitoring/resmon_parametrics-disk_day.json')
        except ValueError as e:
            pass
        else:
            read_throughput = []
            for obj in disk_json['members']:
                read_throughput.append(obj['disks'][0]['readThroughput'])
                    
            # Averaging out the metrics
            avg_read_throughput.append(mean(read_throughput))

    data['avg_read_throughput'] = avg_read_throughput
    df = pd.DataFrame(data)

    xlabel = 'kilobytes/second'
    ylabel = 'Count'
    art_df = binning('avg_read_throughput', df, xlabel, ylabel)    

    #processes data for barplot
    nparray = art_df.to_numpy()
    interv = [item[0] for item in nparray]
    height = [item[1] for item in nparray]

    #increases the size of the figure
    plt.figure(1, figsize=(10,6))

    #creates the barplot
    left = range(0, 30)
    plt.bar(left, height, tick_label=interv, width=0.8)

    #rotates and add labels
    plt.xticks(rotation=40, ha='right')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title('Read throughput miner')

    end = time()
    print(end - start, 'seconds')

""" System Version

Another type of data that could be collected if what version of the operating system each machine is running. Here we have given you the steps that would need to be completed, but not the code itself. 

If you would like, fill in this function using the steps as a guide. Otherwise, feel free to create your own functions after this one. 

If you make your own, don't forget to add them to main() so you can execute them with the others!
"""

def sys_version(path = f'{drivePath}/'):
    ''' Describe your function here '''

    print('Starting system version analysis...')
    start = time()

    # Step 1: Define all your *initial* variables

    # Step 2: For each ticket, go through the file you are looking at and gather data
                
    # Step 3: Store that data in a dataframe, and if necessary do any processing required

    # Step 4: Plot a graph with the data

    end = time()
    print(end - start, 'seconds')

    plt.show()
    plt.close()


""" Main Function
This is the starting point for the program, where each function in the program is called. Having a main function in Python programming is essential for when you need to execute a program as a whole, rather than just individually executing every function.
"""

def main():
    read_throughput_miner()
    sys_version()
    


main()



