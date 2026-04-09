# author: T. Urness and M. Moore
# description: Flask example using redirect, url_for, and flash
# credit: the template html files were constructed with the help of ChatGPT

#Clayton Gustafson

from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash
from dbCode import *

app = Flask(__name__)
app.secret_key = 'your_secret_key' # this is an artifact for using flash displays; 
                                   # it is required, but you can leave this alone

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add-city', methods=['GET', 'POST'])
def add_city():
    if request.method == 'POST':
        # Extract form data
        f_name = request.form['f_name']
        l_name = request.form['l_name']
        genre = request.form['genre']
        
        # Process the data (e.g., add it to a database)
        # For now, let's just print it to the console
        print("Name:", f_name + " "+ l_name, ":", "Favorite Genre:", genre)
        
        flash('User added successfully! Huzzah!', 'success')  # 'success' is a category; makes a green banner at the top
        # Redirect to home page or another page upon successful submission
        return redirect(url_for('home'))
    else:
        # Render the form page if the request method is GET
        return render_template('add_city.html')

@app.route('/delete-city',methods=['GET', 'POST'])
def delete_city():
    if request.method == 'POST':
        # Extract form data
        name = request.form['name']
        
        # Process the data (e.g., add it to a database)
        # For now, let's just print it to the console
        print("Name to delete:", name)
        
        flash('User deleted successfully! Hoorah!', 'warning') 
        # Redirect to home page or another page upon successful submission
        return redirect(url_for('home'))
    else:
        # Render the form page if the request method is GET
        return render_template('delete_city.html')


@app.route('/display-cities')
def display_cities():
    # hard code a value to the users_list;
    # note that this could have been a result from an SQL query :) 
    rows = execute_query("""
        SELECT city.name as City, country.name as Country, country.continent as Continent, city.population as Population
        FROM city
        JOIN country
        Where city.countrycode = country.code
        LIMIT 20"""
    )

    # cursor.execute(rows) # Change this after implementing 'cursor=' in dbCode

    return display_html(rows)


# these two lines of code should always be the last in the file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
