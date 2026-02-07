from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)


def read_json():
    path = os.path.join(os.path.dirname(__file__), "products.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


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


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source not in ["json", "csv"]:
        return render_template(
            "product_display.html",
            error="Wrong source",
            products=None
        )

    try:
        products = read_json() if source == "json" else read_csv()
    except Exception:
        return render_template(
            "product_display.html",
            error="Failed to read data file",
            products=None
        )

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
