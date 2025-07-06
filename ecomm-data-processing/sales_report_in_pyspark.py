from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg

spark = SparkSession.builder.appName(
    "SalesReport"
).getOrCreate()  # require JDK 17, not higher version


class Report:
    def __init__(self):
        self.orders = spark.read.json("data/orders.json")
        self.suppliers = spark.read.json("data/suppliers.json")
        self.products = spark.read.json("data/products.json")

    def sales(self):
        joined = self.orders.join(
            self.products, self.orders.product_id == self.products.id
        )
        total_revenue = joined.selectExpr(
            "sum(quantity * price) as total_revenue"
        ).collect()[0][0]
        return total_revenue

    def best_selling_product(self):
        joined = self.orders.join(
            self.products, self.orders.product_id == self.products.id
        )
        product_quantities = joined.groupBy("name").sum("quantity").collect()
        best_product = max(product_quantities, key=lambda x: x["sum(quantity)"])
        return best_product["name"], best_product["sum(quantity)"]

    def top_customer(self):
        joined = self.orders.join(
            self.products, self.orders.product_id == self.products.id
        )

        customer_spending = (
            joined.withColumn("spent", col("price") * col("quantity"))
            .groupBy("customer_id")
            .agg(sum("spent").alias("total_spent"))
        )
        top_customer = customer_spending.orderBy("total_spent", ascending=False).first()
        return top_customer["customer_id"], top_customer["total_spent"]

    def average_order_value(self):
        joined = self.orders.join(
            self.products, self.orders.product_id == self.products.id
        )
        return (
            joined.withColumn("order revenue", col("quantity") * col("price"))
            .select(avg("order revenue"))
            .collect()[0][0]
        )


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
