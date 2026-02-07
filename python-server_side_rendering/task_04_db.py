from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)


# ---------- JSON ----------
def read_json():
    path = os.path.join(os.path.dirname(__file__), "products.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ---------- CSV ----------
def read_csv():
    path = os.path.join(os.path.dirname(__file__), "products.csv")
    data = []

    with open(path, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            row["price"] = float(row["price"])
            data.append(row)

    return data


# ---------- SQLite ----------
def read_sql():
    db_path = os.path.join(os.path.dirname(__file__), "products.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()

    conn.close()

    data = []
    for r in rows:
        data.append({
            "id": r[0],
            "name": r[1],
            "category": r[2],
            "price": r[3]
        })

    return data


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source not in ["json", "csv", "sql"]:
        return render_template(
            "product_display.html",
            error="Wrong source",
            products=None
        )

    try:
        if source == "json":
            products = read_json()
        elif source == "csv":
            products = read_csv()
        else:
            products = read_sql()
    except Exception:
        return render_template(
            "product_display.html",
            error="Failed to read data source",
            products=None
        )

    # filter by id
    if product_id:
        product_id = int(product_id)
        products = [p for p in products if p["id"] == product_id]

        if not products:
            return render_template(
                "product_display.html",
                error="Product not found",
                products=None
            )

    return render_template(
        "product_display.html",
        error=None,
        products=products
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
