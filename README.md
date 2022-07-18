# STEM Work Experience Project

This project was built for work experience students at Hewlett Packard Enterprise.
It is fundamentally about data mining, retrieving and displaying data sent home by a StoreOnce.

The tickets.zip file will need to be extracted to ./tickets

The functions:

*read_throughput_miner* - Example function given to the students. reads in a JSON
file from each ticket gets the information about the read throughput (in
kilobytes/second), bins the data using the binning function and displays it as a
graph using seaborn.

*software_version* - A skeleton function for the students to use as a starting point.
Analyses the software version.

*Binning* - groups similar values together and returns a Dataframe. Takes a
title, dataframe, x-axis label and y-axis label as inputs

*Main function* - As the name suggests.
