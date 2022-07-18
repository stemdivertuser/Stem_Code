# Glob allows us to generate large lists of filenames, which we can use to read
# data from all our different tickets.
import glob

# Time provides utilities for interacting with the computer's internal clock,
# which we can use for timing how long it takes for a function to execute. How
# do you think we can time how long a function takes to execute?
from time import time

import pandas as pd
import matplotlib.pyplot as pyplot

# The json package will help us load in json files and read the data from them
import json

# Python's standard library also has a lot of facilities for various maths and
# statistics that we can use for calculating values like the mean average.
import math
from statistics import mean

"""
Tickets folder Setup

This code assigns the relative filepath for the tickets folder.
"""

drivePath = 'tickets'


"""
Data Mining

It is standard these days for technology companies to have access to large
amounts of data about how their products and services are used.  By
intelligently using this data, companies can gain insight into how to optimise
their business plan.  Using data mining techniques we can programmaticaly
achieve this goal on large data sets.

Read Throughput Performance

This example function reads a JSON file (a text file structured to be easily
machine readable) of performance data, and stores information on read throughput
(kilobytes/second, or how fast data is being read).

For each ticket, the average read throughput is saved.  At the end this data is
then grouped into bins and counted, before being saved as a graph.

This gives us an indication of how regularly these machines are being pushed to
the limit of their read throughput capacity.
"""

def read_throughput_miner(path = f'{drivePath}/'):
    ''' Loops through disk metrics calculating average '''

    print('Starting read throughput analysis...')
    start = time()

    data = {}
    avg_read_throughput = []

    # The * is a wildcard, this means everything it can find in that directory
    tickets = glob.glob(path + '/*')

    # Goes through each ticket and finds the average of each performance metric
    # for each ticket
    for ticket in tickets:
        print(ticket)
        try:
            # Code to try
            with open(ticket + '/resource-monitoring/resmon_parametrics-disk_day.json') as json_file:
                disk_json = json.load(json_file)
        except FileNotFoundError as e:
            # If we can't find the file then 'pass' which means skip this file
            pass
        else:
            # Run this code if there weren't any exceptions (so if the file was found)
            read_throughput = []
            for obj in disk_json['members']:
                read_throughput.append(obj['disks'][0]['readThroughput'])
                    
            # Averaging out the metrics
            avg_read_throughput.append(mean(read_throughput))

    data['avg_read_throughput'] = avg_read_throughput
    df = pd.DataFrame(data)

    x_label = 'kilobytes/second'
    y_label = 'Count'
    binned_data = binning('avg_read_throughput', df, x_label, y_label)

    # Convert the binned data into a numpy-format array.
    nparray = binned_data.to_numpy()

    intervals = []
    for item in nparray:
        intervals.append(item[0])

    heights = []
    for item in nparray:
        heights.append(item[1])

    #increases the size of the figure
    pyplot.figure(
        # figsize defines the width and height of the whole graph (in inches)
        figsize=(10, 6)
    )

    #creates the barplot
    x_axis = range(0, 30)
    pyplot.bar(
        x_axis,               # x-coordinates of the bars
        heights,              # list of bar heights
        tick_label=intervals, # labels for the x-axis,
        # width=1             # what do you think happens if set this value?
    )

    # We can use pyplot to determine the graph appearance using the following
    # functions:
    pyplot.xticks(      # xticks refers to the x axis labels
        rotation=40,    # rotate the labels by 40 degrees
        ha='right'      # HA=Horizontal Alignment of labels
    )
    pyplot.xlabel(x_label)
    pyplot.ylabel(y_label)
    pyplot.title('Read throughput miner')

    end = time()
    print(end - start, 'seconds')

"""
Software Version

Another type of data that could be collected if what version of the software each machine is running. 
Here we have given you the steps that would need to be completed, but not the code itself.

If you would like, fill in this function using the steps as a guide.  Otherwise,
feel free to create your own functions after this one.

If you make your own, don't forget to add them to main() so you can execute them
with the others!

Hint: look in systemInfo.json for the data you might need
"""

def software_version(path = f'{drivePath}/'):
    ''' Describe your function here '''

    print('Starting software version analysis...')
    start = time()

    # Step 1: Define all your *initial* variables

    # Step 2: For each ticket, go through the file you are looking at and gather
    # data

    # Step 3: Store that data, and if necessary do any processing required

    # Step 4: Plot a graph with the data

    end = time()
    print(end - start, 'seconds')

    pyplot.show()
    pyplot.close()

"""
Binning

This means to group similar data values together.  For example, you might want
to group similar levels of performance together to then count how many values
fall in each group.  Feel free to use this function as is, or experiment with it
/ do your own research to best adjust it to suit your needs.
"""

def binning(old_col, df, xlabel, new_col):
    ''' Distributes data across bins '''

    df[new_col] = pd.cut(df[old_col], 30) # split into 30 bins
    new_data = df[new_col].value_counts().sort_index() # count how many goes into which bins
    new_df = pd.DataFrame(new_data)
    new_df.index.name = xlabel
    new_df.reset_index(inplace=True)

    return new_df

"""
Main Function

This is the starting point for the program, where each function in the program
is called.  Having a main function in Python programming is essential for when
you need to execute a program as a whole, rather than just individually
executing every function.
"""

if __name__ == '__main__':
    read_throughput_miner()
    software_version()
