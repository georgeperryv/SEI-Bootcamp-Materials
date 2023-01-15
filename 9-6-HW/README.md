# SQL Lab

<img src="https://i.imgur.com/OGKTx2f.jpg">

# Where In The World Is Carmen Sandiego?

## Introduction

#### Use SQL to find Carmen Sandiego

We're going to use what we've learned already about querying a database using SQL commands to to chase down and capture an elusive and world-renowned thief, Carmen Sandiego!

## Set Up

1. Ensure that you're **in this lab's folder** within the class repo. Fork and clone this github repo.

2. Open pgAdmin and right click Database. Click Create Database and name it carmen.

3. Click carmen to open it. Scroll down, right click Tables and select PSQL tool.


4. Within the PSQL cli create `city`, `country` & `countrylanguage` tables and seed their data using the _import_ (`\i`) psql command:

	```sql
	\i /<replace with correct path>/world.sql
	```
	
	![image (1)](https://media.git.generalassemb.ly/user/43652/files/a986e4a4-58ab-4def-8b99-8b11bda60121)
	
5. Right click Tables and select Query Tool. Test your queries here.

6. Open a terminal session and run `ls`.  Ensure that you see the three files: `clues.sql`, `sql-lab.md` & `world.sql`.

7. Open VS Code: `$ code .` read your prompts and save your commands.









## Exercise

The goal is to figure out what city Carmen Sandiego is heading to so that she can be met by the proper authorities.

You'll be writing SQL queries within `clues.sql` to answer each clue.

Run the queries in psql by typing `\i clues.sql`.

## Hints

- Use the psql `\d` & `\dt tablename` commands to list & display the schema of each of the three tables.

- Google and collaborate to reach the goal of finding out where Carmen's destination is.

- For example, you'll certainly need to know about the [ORDER BY](http://www.postgresqltutorial.com/postgresql-order-by/) clause.

## Additional Resources

- [PostgreSQL official documentation](http://www.postgresql.org/docs/)

## Encore 

If you finish this exercise and want to learn more about SQL, do some of [these exercises here](https://pgexercises.com/).
