# MapReduce-Intro
Real-world Big-Data problems with Hadoop MapReduce  

This repository covers several simple application with MapReduce.

The hadoop virtual machine is downloaded from Udacity. 

Due to the file size limition (<25MB), only sample dataset is uploaded 



To update dataset:

% hadoop fs -mkdir input

% hadoop fs -put <dataset file>


To run a job:

% hs mapper.py reducer.py input output


To enable combiner:

% hsc mapper.py reducer.py input output


To check result:

% hadoop fs -cat output/part-00000

