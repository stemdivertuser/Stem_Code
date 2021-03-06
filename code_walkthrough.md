## What is the program about?
This program is all about data mining, as a developer one of your most important
tools is large amounts of data, particularly when this data is about how
customers use the product you’ve developed. If we can retrieve and utilise this
data effectively then we can gain a true insight into how we can improve our
code, based on how customers use it.

## Why do we need the program?
One big issue is the sheer amount of data we get, this would be an easy enough
task if we had about 10 customers with products, we could just manually comb
through the data and calculate averages, but what about when you have tens of
thousands of customers, not so easy anymore! This is where data mining comes in,
using a program just like the one you’re about to develop, we can
programmatically (using code) get all of this useful information from such a
large data set (data from tens of thousands of customers).

## Where do we get the data?
You might be wondering where all of this data comes from? Well do you remember
when you set up your phone, or downloaded a new program and you got that
slightly annoying pop-up: ‘Would you like to share analytics data with <whatever
company> so we can improve our product’. This is exactly what we do with our HPE
StoreOnce boxes. These are essentially disk based storage boxes that customers
can back up their data to, we also developed some rather clever algorithms on
there that reduce the amount of backup data customers need to store by about
95%. Back to the point though, one of the teams in this Bristol office actually
develop the software that runs these StoreOnce boxes, so we love it when
customers choose to share analytics with us because it helps us improve the
software! Everyday StoreOnce boxes all over the world send back analytics data
that we need to process so that we can analyse it.

## Looking through the code
Let’s take a high-level look at the program you’ll be working on. If we scroll
down to the bottom we can see the `main` function, this is entry point to the
program, essentially telling Python, this is the first bit of code I want you to
execute.

You can see the first this that the `main` function does is call the
`read_throughput_miner` function, at it’s core this function is used to read a
specific file that we get back from each StoreOnce called
`resmon_parametrics-disk_day.json` . This file contains data about the read
throughput which is essentially how fast our StoreOnce boxes are reading data
(in kilobytes/second). The function then calculates an the average read
throughput and plots it on a graph that we can easily read.

Looking back to the `main` function we can see that the next line of code calls
the `sys_version` function, this will be used to find out what version of our
software the customer is running on their StoreOnce. There are loads of reasons
this is useful, most importantly it allows us to see if the new software we
release is better! We can use this program to see what the average read
throughput is on an older version of software, and then compare it to a
(hopefully) faster read throughput on a newer version of software.
