CREATE OR REPLACE VIEW top_items_by_quantity AS
SELECT
    i.item_name,
    SUM(ti.quantity) AS total_quantity_sold
FROM items i
JOIN transaction_items ti
ON i.item_id = ti.item_id
GROUP BY
    i.item_id,
    i.item_name
ORDER BY total_quantity_sold DESC;

CREATE OR REPLACE VIEW top_members_by_spending AS
SELECT
    m.membership_id,
    m.first_name,
    m.last_name,
    SUM(t.total_items_price) AS total_spent
FROM members m
JOIN transactions t
ON m.membership_id = t.membership_id
GROUP BY
    m.membership_id,
    m.first_name,
    m.last_name
ORDER BY total_spent DESC;

CREATE OR REPLACE VIEW top_manufacturers_by_revenue AS
SELECT
    m.manufacturer_id,
    m.manufacturer_name,
    SUM(ti.quantity * ti.unit_price) AS total_revenue
FROM manufacturers m
JOIN items i
    ON m.manufacturer_id = i.manufacturer_id
JOIN transaction_items ti
    ON i.item_id = ti.item_id
GROUP BY
    m.manufacturer_id,
    m.manufacturer_name
ORDER BY
    total_revenue DESC;