# MapReduce-Intro
Real-world Big-Data problems with Hadoop MapReduce  

This repository covers several simple application with MapReduce in multi-node Hadoop cluster.

The 4-node hadoop cluster is hosted by Udacity for courses

Due to the file size limition (<25MB), only sample dataset is attached



To upload dataset into Hadoop:

% hadoop fs -mkdir input

% hadoop fs -put "datafile"


To run a job on Hadoop with MapReduce:

% hs mapper.py reducer.py input output


To enable combiner:

% hsc mapper.py reducer.py input output


To check result:

% hadoop fs -cat output/part-00000

