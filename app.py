import requests
import configparser
from flask import Flask, render_template , url_for, request, redirect


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/fresh_latex", methods=['GET', 'POST'])
def fresh_latex():
    rubber_prices = {
        2546: 37.97,
        2547: 43.69,
        2548: 52.51,    
        2549: 50.00,
        2550: 68.01,
        2551: 75.33,
        2552: 55.96,
        2553: 101.89,
        2554: 122.36,
        2555: 89.98,
        2556: 73.78,
        2557: 55.25,
        2558: 45.08,
        2559: 50.03,
        2560: 57.12,
        2561: 42.74,
        2562: 43.69,
        2563: 44.74,
        2564: 53.4,
        2565: 54.84,
        2566: 45.41,
    }

    if request.method == 'POST':
        years_fresh = request.form.get("years")
        selected_year = int(years_fresh.split()[1])  
        selected_price_ = rubber_prices.get(selected_year, "N/A")
    else:
        years_fresh = None
        selected_price_ = None

    list_year = [2546, 2547, 2548, 2549, 2550, 2551, 2552, 2553, 2554, 2555, 2556, 2557, 2558, 2559, 2560, 2561, 2562, 2563, 2564, 2565, 2566]
    mylist_ = [f"พ.ศ. {year}" for year in list_year]
    
    return render_template("fresh_latex.html", list_year=mylist_, years_fresh=years_fresh, selected_price_=selected_price_)



@app.route("/raw_rubber_sheet", methods=['GET', 'POST'])
def raw_rubber_sheet():
    rubber_prices = {
        2546: 104.66,
        2547: 45.47,
        2548: 53.61,
        2549: 69.96,
        2550: 70.25,
        2551: 77.86,
        2552: 57.77,
        2553: 104.49,
        2554: 129.96,
        2555: 91.07,
        2556: 75.55,
        2557: 55.53,
        2558: 45.88,
        2559: 50.37,
        2560: 58.63,
        2561: 41.83,
        2562: 42.99,
        2563: 44.48,
        2564: 54.02,
        2565: 53.46,
        2566: 45.04,
        # ... (add more years and prices)
    }

    if request.method == 'POST':
        selected_year_str = request.form.get('years')
        selected_year = int(selected_year_str.split()[1])  
        selected_price = rubber_prices.get(selected_year, "N/A")
    else:
        selected_year = None
        selected_price = None

    list_year = [2546, 2547, 2548, 2549, 2550, 2551, 2552, 2553, 2554, 2555, 2556, 2557, 2558, 2559, 2560, 2561, 2562, 2563, 2564, 2565, 2566]
    mylist_ = [f"พ.ศ. {year}" for year in list_year]

    return render_template("raw_rubber_sheet.html", list_year=mylist_, selected_year=selected_year, selected_price=selected_price)



if __name__ == "__main__":
    app.run()
    

'''years = [2546, 2547, 2548, 2549, 2550, 2551, 2552, 2553, 2554, 2555, 2556, 2557, 2558, 2559, 2560, 2561, 2562, 2563, 2564, 2565, 2566, 2567, 2568, 2569, 2570, 2571, 2572, 2573, 2574, 2575, 2576]
    raw_rubber_prices = [104.66, 45.47, 53.61, 69.96, 70.25, 77.86, 57.77, 104.49, 129.96, 91.07, 75.55, 55.53, 45.88, 50.37, 58.63, 41.83, 42.99, 44.48, 54.02, 53.46]
    latex_prices = [37.97, 43.69, 52.51, 67.88, 68.01, 75.33, 55.96, 101.89, 122.36, 89.98, 73.78, 55.25, 45.08, 50.03, 57.12, 42.74, 43.69, 44.74, 53.4, 54.84, 45.41,]
    x_values = [-19, -17, -15, -13, -11, -9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 31, 33, 35, 37, 39]

    raw_rubber_predictions = [-0.0502 * x ** 2 - 0.8964 * x + 73.067 for x in x_values]
    latex_predictions = [-0.0974 * x ** 2 - 0.3498 * x + 74.768 for x in x_values]

    raw_rubber_data = zip(years, raw_rubber_prices, raw_rubber_predictions)
    latex_data = zip(years, latex_prices, latex_predictions)

    return render_template('index.html', raw_rubber_data=raw_rubber_data, latex_data=latex_data)'''
    
'''{% extends 'base.html' %}

{% block title %}Raw Rubber Price Prediction{% endblock %}

{% block content %}
<h1>Raw Rubber Price Prediction</h1>
{% include 'select_year.html' %}
<table>
    <tr>
        <th>Year</th>
        <th>Actual Price</th>
        <th>Predicted Price</th>
    </tr>
    {% for year, actual, predicted in zip(years, raw_rubber_prices, raw_rubber_predictions) %}
    <tr>
        <td>{{ year }}</td>
        <td>{{ actual }}</td>
        <td>{{ predicted }}</td>
    </tr>
    {% endfor %}
</table>
{% endblock %}
'''