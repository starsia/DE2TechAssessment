CREATE TABLE members (
    membership_id VARCHAR(100) PRIMARY KEY,
    name VARCHAR(25) NOT NULL,
    above_18 BOOLEAN NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(255) NOT NULL,
    mobile_no VARCHAR(8) NOT NULL
);

CREATE TABLE manufacturers (
    manufacturer_id SERIAL PRIMARY KEY,
    manufacturer_name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,
    manufacturer_id INTEGER NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    weight_kg NUMERIC(10,3) NOT NULL
);

CREATE TABLE transactions (
    transaction_id BIGSERIAL PRIMARY KEY,
    membership_id VARCHAR(100) NOT NULL,
    transaction_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    total_items_price NUMERIC(12,2) NOT NULL,
    total_items_weight NUMERIC(12,3) NOT NULL
);

CREATE TABLE transaction_items (
    transaction_id BIGINT NOT NULL,
    item_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price NUMERIC(10,2) NOT NULL,
    PRIMARY KEY (transaction_id, item_id)
);