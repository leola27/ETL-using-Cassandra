# Udacity Data Engineer Nanodegree project

## Data Modeling with Cassandra

### Introduction

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. 

### ETL process
The project involves working with one dataset: event_data directory. This is a directory of CSV files partitioned by date. In the course of ETL, the files are processed 
to create a denormalized dataset.Then the tables are modeled keeping in mind the queries provided. The data is loaded  into tables you create in Apache Cassandra 
on which the queries can be ran.

### Files in repository

### Project_1B_ Project_Template.ipynb
Creates a file event_datafile_new.csv from source data. Then creates a Cassandra cluster and tables modeled based on the Queries presented. Then data is then inserted into the 
tables and a select is ran corresponding to original query. After this, connection is dropped and tables deleted.

### create_tables.py
Drops and creates tables using queries in queries.py

### etl.py
Implements the whole ETL concept tested in Project_1B_ Project_Template.ipynb

### selects.py
Contains select scripts based on original queries to test the ETL process

