import duckdb as db


class Report:
    def __init__(self):
        self.orders = db.read_json("data/orders.json")
        self.suppliers = db.read_json("data/suppliers.json")
        self.products = db.read_json("data/products.json")

    def sales(self):
        return db.sql("""
            SELECT SUM(quantity * price) 
            FROM "data/orders.json" 
            JOIN "data/products.json" 
            ON orders.product_id = products.id
        """).fetchone()[0]


    def best_selling_product(self):
        return db.sql("""
            SELECT name, SUM(quantity) as total_quantity
            FROM "data/orders.json"
            JOIN "data/products.json"
            ON orders.product_id = products.id
            GROUP BY name
            ORDER BY total_quantity DESC
            LIMIT 1
        """).fetchone()

        merged = self.orders.merge(self.products, left_on="product_id", right_on="id")
        product_quantities = merged.groupby("name")["quantity"].sum()
        return product_quantities.idxmax(), product_quantities.max()

    def top_customer(self):
        return db.sql("""
            SELECT customer_id, SUM(quantity * price) as total_spent
            FROM "data/orders.json"
            JOIN "data/products.json"
            ON orders.product_id = products.id
            GROUP BY customer_id
            ORDER BY total_spent DESC
            LIMIT 1
        """).fetchone()

    def average_order_value(self):
        return db.sql("""
            SELECT AVG(quantity * price) as average_order_value
            FROM "data/orders.json"
            JOIN "data/products.json"
            ON orders.product_id = products.id
        """).fetchone()[0]


if __name__ == "__main__":
    report = Report()
    print("Total Revenue: $", report.sales())

    best_selling_product = report.best_selling_product()
    print(
        "Best Selling Product: $",
        best_selling_product[0],
        "(",
        best_selling_product[1],
        "units sold)",
    )

    top_customer = report.top_customer()
    print("Top Customer: ", top_customer[0], "($", top_customer[1], "spent)")

    print("Average Order Value: $", report.average_order_value())
