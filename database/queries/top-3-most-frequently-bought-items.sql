SELECT
    i.item_name,
    SUM(ti.quantity) AS total_quantity_sold
FROM items i
JOIN transaction_items ti
ON i.item_id = ti.item_id
GROUP BY
    i.item_id,
    i.item_name
ORDER BY total_quantity_sold DESC
LIMIT 3;