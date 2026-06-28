-- Optional.
-- Demonstrates how a read-only analyst role could be created.

CREATE ROLE analyst LOGIN PASSWORD 'analyst';

GRANT CONNECT ON DATABASE ecommerce TO analyst;

GRANT USAGE ON SCHEMA public TO analyst;

GRANT SELECT ON ALL TABLES IN SCHEMA public TO analyst;