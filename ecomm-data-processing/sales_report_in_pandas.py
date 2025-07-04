import pandas as pd


class Report:
    def __init__(self):
        self.orders = pd.read_json("data/orders.json")
        self.suppliers = pd.read_json("data/suppliers.json")
        self.products = pd.read_json("data/products.json")

    def sales(self):
        merged = self.orders.merge(self.products, left_on="product_id", right_on="id")
        return sum(merged["quantity"] * merged["price"])

    def best_selling_product(self):
        merged = self.orders.merge(self.products, left_on="product_id", right_on="id")
        product_quantities = merged.groupby("name")["quantity"].sum()
        return product_quantities.idxmax(), product_quantities.max()

    def top_customer(self):
        merged = self.orders.merge(self.products, left_on="product_id", right_on="id")
        # I don't really like Pandas for this kind of operation
        customer_spending = merged.groupby("customer_id").agg(
            total_spent=("price", lambda x: (x * merged.loc[x.index, "quantity"]).sum())
        )
        return customer_spending["total_spent"].idxmax(), customer_spending["total_spent"].max()

    def average_order_value(self):
        merged = self.orders.merge(self.products, left_on="product_id", right_on="id")
        return sum(merged["quantity"] * merged["price"]) / len(merged["order_id"].unique())


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
