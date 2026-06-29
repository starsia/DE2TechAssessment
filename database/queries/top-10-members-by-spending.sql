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
ORDER BY total_spent DESC
LIMIT 10;