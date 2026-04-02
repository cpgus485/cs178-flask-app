# dbCode.py
# Author: Clayton Gustafson
# Helper functions for database connection and queries

from flask import Flask, render_template, request
import pymysql
import creds

def get_conn():
    """Returns a connection to the MySQL RDS instance."""
    conn = pymysql.connect(
        host=creds.host,
        user=creds.user,
        password=creds.password,
        db=creds.db,
    )
    return conn

def execute_query(query, args=()):
    """Executes a SELECT query and returns all rows as dictionaries."""
    cur = get_conn().cursor(pymysql.cursors.DictCursor)
    cur.execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows

def display_html(rows):
    html = "<table border='1'>"
    for row in rows:
        html += "<tr>"
        for col in row:
            html += f"<td>{col}</td>"
        html += "</tr>"
    html += "</table>"
    return html