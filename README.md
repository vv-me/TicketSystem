# TicketSystem
#### Set up a data pipeline which loads a CSV file to a ticket system database with ticket sales event table. This data tracks all ticket sales for various events, including when a third-party reseller submits their records of ticket sales for a new day.

## Installation and settup
### Clone the repository

$ git clone https://github.com/vv-me/TicketSystem.git

### Install MySql

[MySql](https://dev.mysql.com/downloads/installer/)

### Database set up and creation
Create MySQL database called ticketingsystem(The script has username as root, password as croak and server name as localhost - Not parameterised yet)

#### Run the following DML

1. Script.sql DDL script

### Execute Runner.py

It first asks for db details - hostname, database name, username and password.
It next asks for file path of the csv

Returns the most popular(top 5) events for the latest month from the records
