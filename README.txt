This project was built to run using google colab.

You can import either the .py or the .ipynb file to google colab for the program to work.

To run this outside of google colab you will need to remove the google imports and change the drivepath to something local.

You will need to log out of any non speakers for schools google account for the tickets to load in properly.

If the tickets will not load or get deleted you will need to re upload them to a shareddrive in order for the students to have access.

The functions:

Binning - groups similar values together and returns a Dataframe. Takes a title, dataframe, x-axis label and y-axis label as inputs

read_throughput_miner - Example function given to the students. reads in a JSON file from each ticket gets the information about the read throughput (in kilobytes/second), bins the data using the binning function and displays it as a graph using seaborn.

sys_version - A skeleton function for the students to use as a starting point. Analyzes the system version.

Main function - As the name suggests.