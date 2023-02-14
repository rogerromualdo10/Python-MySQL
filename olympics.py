from getpass import getpass
from mysql.connector import connect, Error


# 3. Create a query for each table

try:
    with connect(
        host="localhost",
        user=input("Enter username"),
        password=getpass("Enter password: "),
        database="olympics"
    ) as connection:
        athletes_table_query = "SELECT * FROM athletes"
        coaches
        entries_gender
        medals_table_query = "SELECT * FROM medals"
        teams
        with connection.cursor(buffered=True) as cursor:
            cursor.execute(athletes_table_query)
            cursor.execute(medals_table_query)
            connection.commit()
except Error as e:
    print(e)

# 4. Do some Exploratory Data Analysis over this data set.
# We need to find out the number of athletes by country,
# the Distribution of disciplines by gender,
# and the Number of Medals by country (top 10).


try:
    with connect(
        host="localhost",
        user=input("Enter username"),
        password=getpass("Enter password: "),
        database="olympics"
    ) as connection:
        number_athletes_query = "CREATE VIEW number_athletes_view AS SELECT noc,count(*) as number FROM athletes GROUP BY noc ORDER BY noc"
        dist_disc_query = "CREATE VIEW dist_disc_view AS SELECT discipline,female,male FROM entries_gender"
        number_of_medals_by_country = "CREATE VIEW number_of_medals_view AS SELECT team_noc,total,rank_by_total FROM medals WHERE rank_by_total<=10 ORDER BY rank_by_total DESC"
        with connection.cursor(buffered=True) as cursor:
            cursor.execute(number_athletes_query)
            cursor.execute(dist_disc_query)
            cursor.execute(number_of_medals_by_country)
            connection.commit()
except Error as e:
    print(e)

# 5. Graphical analysis
try:
    with connect(
        host="localhost",
        user=input("Enter username"),
        password=getpass("Enter password: "),
        database="olympics"
    ) as connection:
        show_view_query = "SELECT * FROM number_of_medals_view"
        with connection.cursor() as cursor:
            cursor.execute(show_view_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
except Error as e:
    print(e)