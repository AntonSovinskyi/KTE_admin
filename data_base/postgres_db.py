import psycopg2
from data_base.config import config


conn = None


def connect():
    global conn, cur

    params = config()
    conn = psycopg2.connect(**params)
    conn.autocommit = True
    cur = conn.cursor()


# Change the DJ in the database
def milonga_change_dj_sql(dj, day):
    cur.execute(f"UPDATE milonga SET dj= '{dj}' WHERE day_of_the_week= '{day}'")
    mil_dj = cur.fetchone()
    return mil_dj


def milonga_change_time_sql(time_, day):
    cur.execute(f"UPDATE milonga SET time= '{time_}' WHERE day_of_the_week= '{day}'")
    mil_time = cur.fetchone()
    return mil_time


def milonga_change_price_sql(price, day):
    cur.execute(f"UPDATE milonga SET price= '{price}' WHERE day_of_the_week= '{day}'")
    mil_price = cur.fetchone()
    return mil_price


def practice_change_time_sql(time_, day):
    cur.execute(f"UPDATE practice SET time= '{time_}' WHERE day_of_the_week= '{day}'")
    prac_dj = cur.fetchone()
    return prac_dj


def practice_change_price_sql(price, day):
    cur.execute(f"UPDATE practice SET price= '{price}' WHERE day_of_the_week= '{day}'")
    prac_price = cur.fetchone()
    return prac_price


def practice_change_location_sql(location, day):
    cur.execute(f"UPDATE practice SET location= '{location}' WHERE day_of_the_week= '{day}'")
    prac_loc = cur.fetchone()
    return prac_loc
