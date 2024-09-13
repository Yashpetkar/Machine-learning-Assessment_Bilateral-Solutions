
# Weather Data Aggregator and Prime Factorization

## Description

This project contains two Python functions and one SQL query that address distinct problems:

1. **Weather Data Aggregation**: A function to calculate average weather data (temperature and humidity) for cities, while gracefully handling missing information.
2. **Prime Factorization**: A function to compute the prime factorization of a given integer, returning each prime factor with its corresponding exponent.
3. **SQL Query**: A query to update and display product prices after applying a 10% increase.

---

## Contents

- `aggregate_weather_data(records)`: This function accepts a list of records, where each record is a dictionary containing city names and weather data. The function calculates the average temperature and humidity for each city, handling missing data.
  
- `prime_factorization(n)`: This function takes an integer `n` and returns a list of tuples where each tuple contains a prime factor and its exponent.

- `SQL Query`: Increases the price of all products in a `products` table by 10%, then selects and displays the updated prices along with the product names.

---

## How to Use

### 1. **Weather Data Aggregation**

This function takes a list of dictionaries where each dictionary contains weather information for a city. It aggregates the data and returns the average temperature and humidity for each city.

Example input:

```python
records = [
    {'city': 'New York', 'temperature': 22, 'humidity': 55},
    {'city': 'Los Angeles', 'temperature': 30, 'humidity': 60},
    {'city': 'Chicago', 'humidity': 65}
]
```

# Prime Factorization

## Description

This project contains a Python function that performs the prime factorization of a given integer. The function returns the prime factors along with their corresponding exponents in the form of a list of tuples. For example, given the integer `60`, the function will return `[(2, 2), (3, 1), (5, 1)]`, since `60 = 2^2 * 3^1 * 5^1`.

---

## Contents

- `prime_factorization(n)`: A function that takes an integer `n` as input and returns a list of tuples. Each tuple contains a prime factor and its corresponding exponent.

---

## How to Use

### Prime Factorization

This function performs the prime factorization of an integer and returns the prime factors along with their exponents.

### Example

Given the input integer `n = 60`:

```python
n = 60
prime_factorization(n)
[(2, 2), (3, 1), (5, 1)]
```

# SQL Query to Increase Product Prices

## Description

This project contains an SQL query that updates the prices of all products in a database table by increasing them by 10%. After updating the prices, the query selects and displays the updated prices along with the product names.

---

## Contents

- SQL query to update product prices by 10% in a `products` table.
- SQL query to display the updated prices and product names.

---

## How to Use

### SQL Query to Increase Prices

The SQL query increases the price of every product in the `products` table by 10%.

```sql
UPDATE products
SET price = price * 1.10;
