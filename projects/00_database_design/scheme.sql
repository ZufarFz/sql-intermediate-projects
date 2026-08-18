-- ==========================================
-- TECHNOVA ENTERPRISE DATABASE SCHEMA
-- PostgreSQL
-- ==========================================


-- ==========================================
-- 1. COUNTRIES
-- ==========================================

CREATE TABLE countries (
    country_id VARCHAR(10) PRIMARY KEY,
    country_name VARCHAR(100) NOT NULL
);


-- ==========================================
-- 2. CITIES
-- ==========================================

CREATE TABLE cities (
    city_id VARCHAR(10) PRIMARY KEY,
    city_name VARCHAR(100) NOT NULL,
    country_id VARCHAR(10) NOT NULL,

    FOREIGN KEY (country_id)
        REFERENCES countries(country_id)
);


-- ==========================================
-- 3. DEPARTMENTS
-- ==========================================

CREATE TABLE departments (
    department_id VARCHAR(10) PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);


-- ==========================================
-- 4. EMPLOYEES
-- ==========================================

CREATE TABLE employees (
    employee_id VARCHAR(10) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    gender VARCHAR(10)
        CHECK (gender IN ('Male', 'Female')),
    department_id VARCHAR(10) NOT NULL,
    job_title VARCHAR(100) NOT NULL,
    salary DECIMAL(12, 2) NOT NULL
        CHECK (salary >= 0),
    hire_date DATE NOT NULL,
    city_id VARCHAR(10) NOT NULL,
    age INT
        CHECK (age >= 17),

    FOREIGN KEY (department_id)
        REFERENCES departments(department_id),

    FOREIGN KEY (city_id)
        REFERENCES cities(city_id)
);


-- ==========================================
-- 5. CATEGORIES
-- ==========================================

CREATE TABLE categories (
    category_id VARCHAR(10) PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL
);


-- ==========================================
-- 6. PRODUCTS
-- ==========================================

CREATE TABLE products (
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    category_id VARCHAR(10) NOT NULL,
    price DECIMAL(12, 2) NOT NULL
        CHECK (price >= 0),
    stock_quantity INT NOT NULL DEFAULT 0
        CHECK (stock_quantity >= 0),
    created_date DATE NOT NULL,

    FOREIGN KEY (category_id)
        REFERENCES categories(category_id)
);


-- ==========================================
-- 7. CUSTOMERS
-- ==========================================

CREATE TABLE customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(10)
        CHECK (gender IN ('Male', 'Female')),
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    city_id VARCHAR(10) NOT NULL,
    signup_date DATE NOT NULL,

    FOREIGN KEY (city_id)
        REFERENCES cities(city_id)
);


-- ==========================================
-- 8. ORDERS
-- ==========================================

CREATE TABLE orders (
    order_id VARCHAR(20) PRIMARY KEY,
    customer_id VARCHAR(20) NOT NULL,
    order_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL
        CHECK (
            status IN (
                'Completed',
                'Shipped',
                'Processing',
                'Cancelled',
                'Returned'
            )
        ),
    payment_method VARCHAR(50) NOT NULL,

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);


-- ==========================================
-- 9. ORDER ITEMS
-- ==========================================

CREATE TABLE order_items (
    order_item_id VARCHAR(10) PRIMARY KEY,
    order_id VARCHAR(20) NOT NULL,
    product_id VARCHAR(10) NOT NULL,
    quantity INT NOT NULL
        CHECK (quantity > 0),
    unit_price DECIMAL(12, 2) NOT NULL
        CHECK (unit_price >= 0),
    discount_percent DECIMAL(5, 2) NOT NULL DEFAULT 0.00
        CHECK (discount_percent BETWEEN 0 AND 100),

    FOREIGN KEY (order_id)
        REFERENCES orders(order_id),

    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);


-- ==========================================
-- INDEXES
-- ==========================================

CREATE INDEX idx_orders_customer_id
    ON orders(customer_id);

CREATE INDEX idx_orders_order_date
    ON orders(order_date);

CREATE INDEX idx_order_items_order_id
    ON order_items(order_id);

CREATE INDEX idx_order_items_product_id
    ON order_items(product_id);

CREATE INDEX idx_customers_signup_date
    ON customers(signup_date);