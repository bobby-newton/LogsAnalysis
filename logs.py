#!/usr/bin/env python3
import psycopg2

# 1. What are the most popular three articles of all time?
query1_title = ("What are the most popular articles of all time?")
query1 = open("query1.sql", "r").read()

# 2. Who are the most popular article authors of all time?
query2_title = ("Who are the most popular article authors of all time?")
query2 = open("query2.sql", "r").read()

# 3. On which days did more than 1% of requests lead to errors?
query3_title = ("On which days did more than 1% of requests lead to errors?")
query3 = open("query3.sql", "r").read()


def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except psycopg2.Error as e:
        print("Connect Failed: " + e.diag.message_primary)


def get_query_results(query):
    db, cursor = connect()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()


def print_query_results(query_results):
    print(query_results[1])
    for index, results in enumerate(query_results[0]):
        print(
            str(index+1) + ": " + results[0] + " --> " +
            str(results[1]) + " views")


def print_error_results(query_results):
    print(query_results[1])
    for results in query_results[0]:
        print(results[0] + " ---> " + str(results[1]) + "% errors")


if __name__ == '__main__':
    # store query results
    popular_articles_results = get_query_results(query1), query1_title
    popular_authors_results = get_query_results(query2), query2_title
    load_error_days = get_query_results(query3), query3_title

    # print query results
    print_query_results(popular_articles_results)
    print_query_results(popular_authors_results)
    print_error_results(load_error_days)
