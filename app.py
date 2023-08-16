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
        2550: 11.00,
        2551: 11.00,
        2552: 11.00,
        
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
    app.run(debug =True)
    
