import daft

class Report:
    def __init__(self):
        self.orders = daft.read_json("data/orders.json")
        self.suppliers = daft.read_json("data/suppliers.json")
        self.products = daft.read_json("data/products.json")

    def sales(self):
       pass

    def best_selling_product(self):
       pass

    def top_customer(self):
       pass

    def average_order_value(self):
       pass


if __name__ == "__main__":
    pass
 