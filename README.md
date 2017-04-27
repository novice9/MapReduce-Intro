# MapReduce-Intro
Real-world Big-Data problems with Hadoop MapReduce  

This repository covers several simple application with MapReduce in a pseudo-distributed Hadoop cluster.

Due to the file size limition (up to 25MB, however each data file is greater than 200MB), only sample dataset is attached

To upload dataset into Hadoop:

% hadoop fs -mkdir input

% hadoop fs -put input/datafile


To run a job on Hadoop with MapReduce:

% hs mapper.py reducer.py input output


To enable combiner:

% hsc mapper.py reducer.py input output


To check result:

% hadoop fs -cat output/part-00000

