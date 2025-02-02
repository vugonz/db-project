#!/usr/bin/python3
from wsgiref.handlers import CGIHandler
from flask import Flask
from flask import render_template, request
import psycopg2
import psycopg2.extras

## SGBD configs
DB_HOST = "db.tecnico.ulisboa.pt"
DB_USER = "" # FIXME removed
DB_DATABASE = DB_USER
DB_PASSWORD = "" # FIXME removed
DB_CONNECTION_STRING = "host=%s dbname=%s user=%s password=%s" % (
    DB_HOST,
    DB_DATABASE,
    DB_USER,
    DB_PASSWORD,
)

app = Flask(__name__)


@app.route("/")
def index():
    try:
        return render_template("index.html", params=request.args)
    except Exception as e:
        return str(e)


@app.route("/ivm")
def list_ivm():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM ivm;"
        cursor.execute(query)
        return render_template("ivm.html", cursor=cursor)
    except Exception as e:
        return str(e)  # Renders a page with the error.
    finally:
        cursor.close()
        dbConn.close()


@app.route("/product")
def list_product():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM product;"
        cursor.execute(query)
        return render_template("product.html", cursor=cursor)
    except Exception as e:
        return str(e)  # Renders a page with the error.
    finally:
        cursor.close()
        dbConn.close()


@app.route("/shelf")
def list_shelf():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM shelf;"
        cursor.execute(query)
        return render_template("shelf.html", cursor=cursor)
    except Exception as e:
        return str(e)  # Renders a page with the error.
    finally:
        cursor.close()
        dbConn.close()


@app.route("/point_of_retail")
def list_point_of_retail():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM point_of_retail;"
        cursor.execute(query)
        return render_template("pointofretail.html", cursor=cursor)
    except Exception as e:
        return str(e)  # Renders a page with the error.
    finally:
        cursor.close()
        dbConn.close()


@app.route("/retailer")
def list_retailer():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM retailer;"
        cursor.execute(query)
        return render_template("retailer.html", cursor=cursor)
    except Exception as e:
        return str(e)  # Renders a page with the error.
    finally:
        cursor.close()
        dbConn.close()



@app.route("/category")
def list_category():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM category;"
        cursor.execute(query)
        return render_template("category.html", cursor=cursor)
    except Exception as e:
        return str(e)  # Renders a page with the error.
    finally:
        cursor.close()
        dbConn.close()


@app.route("/super_category")
def list_super_category():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM super_category;"
        cursor.execute(query)
        return render_template("supercategory.html", cursor=cursor)
    except Exception as e:
        return str(e)  # Renders a page with the error.
    finally:
        cursor.close()
        dbConn.close()



@app.route("/simple_category")
def list_simple_category():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM simple_category;"
        cursor.execute(query)
        return render_template("simplecategory.html", cursor=cursor)
    except Exception as e:
        return str(e)  # Renders a page with the error.
    finally:
        cursor.close()
        dbConn.close()


@app.route("/replenishment_event")
def list_replenishment_event():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM replenishment_event;"
        cursor.execute(query)
        return render_template("replenishmentevent.html", cursor=cursor)
    except Exception as e:
        return str(e)  # Renders a page with the error.
    finally:
        cursor.close()
        dbConn.close()


@app.route("/planogram")
def list_planogram():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM planogram;"
        cursor.execute(query)
        return render_template("planogram.html", cursor=cursor)
    except Exception as e:
        return str(e)  # Renders a page with the error.
    finally:
        cursor.close()
        dbConn.close()


@app.route("/responsible_for")
def list_responsible_for():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM responsible_for;"
        cursor.execute(query)
        return render_template("responsiblefor.html", cursor=cursor)
    except Exception as e:
        return str(e)  # Renders a page with the error.
    finally:
        cursor.close()
        dbConn.close()


@app.route("/installed_at")
def list_installed_at():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM installed_at;"
        cursor.execute(query)
        return render_template("installedat.html", cursor=cursor)
    except Exception as e:
        return str(e)  # Renders a page with the error.
    finally:
        cursor.close()
        dbConn.close()


@app.route("/has_category")
def list_has_category():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM has_category;"
        cursor.execute(query)
        return render_template("hascategory.html", cursor=cursor)
    except Exception as e:
        return str(e)  # Renders a page with the error.
    finally:
        cursor.close()
        dbConn.close()


@app.route("/has_other")
def list_has_other():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM has_other;"
        cursor.execute(query)
        return render_template("hasother.html", cursor=cursor)
    except Exception as e:
        return str(e)  # Renders a page with the error.
    finally:
        cursor.close()
        dbConn.close()


@app.route("/remove_category")
def remove_category():
    try:
        return render_template("removecategory.html", params=request.args)
    except Exception as e:
        return str(e)


@app.route("/remove_retailer")
def remove_retailer():
    try:
        return render_template("removeretailer.html", params=request.args)
    except Exception as e:
        return str(e)



@app.route("/add_simple_category")
def add_category_simple():
    try:
        return render_template("createcategorysimple.html", params=request.args)
    except Exception as e:
        return str(e)



@app.route("/add_super_category")
def add_category_super():
    try:
        return render_template("createcategorysuper.html", params=request.args)
    except Exception as e:
        return str(e)


@app.route("/add_retailer")
def add_retailer():
    try:
        return render_template("createretailer.html", params=request.args)
    except Exception as e:
        return str(e)


@app.route("/select_ivm")
def select_ivm():
    try:
        return render_template("selectivm.html", params=request.args)
    except Exception as e:
        return str(e)


@app.route("/select_super_category")
def select_super_category():
    try:
        return render_template("selectsupercategory.html", params=request.args)
    except Exception as e:
        return str(e)


@app.route("/created_simple_category", methods=["POST"])
def create_category_simple():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        category_name = request.form["category_name"]
        query = "INSERT INTO category VALUES (%s); INSERT INTO simple_category VALUES (%s);"
        data = (category_name, category_name)
        cursor.execute(query, data)
        return query
    except Exception as e:
        return str(e)
    finally:
        dbConn.commit()
        cursor.close()
        dbConn.close()


@app.route("/created_super_category", methods=["POST"])
def create_category_super():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        category_name = request.form["category_name"]
        query = "INSERT INTO category VALUES (%s); INSERT INTO super_category VALUES (%s);"
        data = (category_name, category_name)
        cursor.execute(query, data)
        return query
    except Exception as e:
        return str(e)
    finally:
        dbConn.commit()
        cursor.close()
        dbConn.close()


@app.route("/created_retailer", methods=["POST"])
def create_retailer():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        retailer_name = request.form["retailer_name"]
        tin = request.form["tin"]
        query = "INSERT INTO retailer VALUES (%s, %s);" 
        data = (tin, retailer_name)
        cursor.execute(query, data)
        return query
    except Exception as e:
        return str(e)
    finally:
        dbConn.commit()
        cursor.close()
        dbConn.close()


@app.route("/deleted_category", methods=["POST"])
def delete_category():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        category_name = request.form["category_name"]
        query = "DELETE FROM category WHERE category_name = %s;"
        data = (category_name,)
        cursor.execute(query, data)
        return query
    except Exception as e:
        return str(e)
    finally:
        dbConn.commit()
        cursor.close()
        dbConn.close()


@app.route("/deleted_retailer", methods=["POST"])
def delete_retailer():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        retailer_name = request.form["retailer_name"]
        query = "DELETE FROM retailer WHERE retailer_name = %s;" # Deletion is easier when made by name instead of TIN.
        data = (retailer_name,)
        cursor.execute(query, data)
        return query
    except Exception as e:
        return str(e)
    finally:
        dbConn.commit()
        cursor.close()
        dbConn.close()


@app.route("/ivm_events", methods=["POST"])
def ivm_events():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        serial_number = request.form["serial_number"]
        query = "SELECT serial_number, SUM(replenished_units) AS sum, category_name FROM ((replenishment_event NATURAL JOIN responsible_for) NATURAL JOIN planogram) WHERE serial_number = %s GROUP BY serial_number, category_name;"
        data = (serial_number,)
        cursor.execute(query, data)
        return render_template("ivmevents.html", cursor=cursor)
    except Exception as e:
        return str(e)
    finally:
        dbConn.commit()
        cursor.close()
        dbConn.close()


@app.route("/super_category_subs", methods=["POST"])
def super_category_subs():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        serial_number = request.form["serial_number"]
        query = "WITH RECURSIVE subcategories AS ( SELECT category FROM has_other WHERE super_category = %s UNION ALL SELECT child.category FROM has_other AS child JOIN subcategories AS parent ON parent.category = child.super_category) SELECT * FROM subcategories;"
        data = (serial_number,)
        cursor.execute(query, data)
        return render_template("supercategorysubs.html", cursor=cursor)
    except Exception as e:
        return str(e)
    finally:
        dbConn.commit()
        cursor.close()
        dbConn.close()


CGIHandler().run(app)
