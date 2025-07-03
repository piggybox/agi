# Interview Question: E-commerce Data Processing

## Problem Statement

You're working with an e-commerce platform that stores data across multiple JSON files. Your task is to write a Python program that processes and analyzes this data.

## Given Files

You have three JSON files:

**products.json**
```json
[
  {"id": 1, "name": "Laptop", "category": "Electronics", "price": 999.99, "supplier_id": 101},
  {"id": 2, "name": "Coffee Mug", "category": "Kitchen", "price": 12.50, "supplier_id": 102},
  {"id": 3, "name": "Headphones", "category": "Electronics", "price": 79.99, "supplier_id": 101},
  {"id": 4, "name": "Desk Chair", "category": "Furniture", "price": 150.00, "supplier_id": 103}
]
```

**orders.json**
```json
[
  {"order_id": "ORD001", "product_id": 1, "quantity": 2, "customer_id": "CUST001", "order_date": "2024-01-15"},
  {"order_id": "ORD002", "product_id": 2, "quantity": 1, "customer_id": "CUST002", "order_date": "2024-01-16"},
  {"order_id": "ORD003", "product_id": 1, "quantity": 1, "customer_id": "CUST001", "order_date": "2024-01-17"},
  {"order_id": "ORD004", "product_id": 3, "quantity": 3, "customer_id": "CUST003", "order_date": "2024-01-18"}
]
```

**suppliers.json**
```json
[
  {"id": 101, "name": "TechCorp", "contact": "tech@techcorp.com", "rating": 4.5},
  {"id": 102, "name": "HomeGoods Inc", "contact": "sales@homegoods.com", "rating": 4.2},
  {"id": 103, "name": "Office Solutions", "contact": "info@officesolutions.com", "rating": 3.8}
]
```

## Requirements

Write a Python program that:

1. **Loads and validates** all three JSON files
2. **Generates a sales report** containing:
   - Total revenue
   - Best-selling product (by quantity)
   - Top customer (by total spent)
   - Average order value
3. **Creates an enriched orders file** (`enriched_orders.json`) that includes:
   - All original order data
   - Product name and price
   - Supplier name and rating
4. **Handles errors gracefully** (missing files, malformed JSON, missing references)

## Expected Output Format

Your program should print a sales report like this:
```
=== SALES REPORT ===
Total Revenue: $2,239.95
Best-Selling Product: Laptop (3 units sold)
Top Customer: CUST001 ($2,999.97 spent)
Average Order Value: $559.99

Enriched orders saved to: enriched_orders.json
```

## Bonus Points

- Add input validation (e.g., negative quantities, invalid dates)
- Support command-line arguments for file paths
- Add logging for debugging
- Handle duplicate order IDs
- Calculate supplier performance metrics

## Time Limit
45 minutes

## Evaluation Criteria
- **Correctness**: Does the solution produce accurate results?
- **Code Quality**: Is the code clean, readable, and well-structured?
- **Error Handling**: How well does it handle edge cases and errors?
- **Efficiency**: Is the solution reasonably efficient for the data size?
- **Problem-Solving**: How well does the candidate break down the problem?