ALTER TABLE items
ADD CONSTRAINT fk_item_manufacturer
FOREIGN KEY (manufacturer_id)
REFERENCES manufacturers(manufacturer_id);

ALTER TABLE transactions
ADD CONSTRAINT fk_transaction_member
FOREIGN KEY (membership_id)
REFERENCES members(membership_id);

ALTER TABLE transaction_items
ADD CONSTRAINT fk_transaction_item_transaction
FOREIGN KEY (transaction_id)
REFERENCES transactions(transaction_id);

ALTER TABLE transaction_items
ADD CONSTRAINT fk_transaction_item_item
FOREIGN KEY (item_id)
REFERENCES items(item_id);

CREATE INDEX idx_transaction_member
ON transactions(membership_id);

CREATE INDEX idx_transaction_date
ON transactions(transaction_date);

CREATE INDEX idx_transaction_item_item
ON transaction_items(item_id);

CREATE INDEX idx_item_manufacturer
ON items(manufacturer_id);