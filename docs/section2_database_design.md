## Problem statement

The task is to set up a database for an e-commerce business's sales transactions.

I have to set up a PostgreSQL database using the Docker [image](https://hub.docker.com/_/postgres) provided. There must be a Dockerfile which to stand up your database with the DDL statements to create the necessary tables. You are required to produce entity-relationship diagrams as necessary to illustrate your design, along with the DDL statements that will be required to stand up the database.

## Considerations for OLAP or OLTP

The database is designed as an OLTP schema using third normal form (3NF). Though the statement states to account for business queries, which might include aggregate reporting, the requested analytical queries can be efficiently executed using SQL aggregation and indexes. For larger analytical workloads, the transactional database could later feed an OLAP data warehouse through an ETL pipeline without requiring changes to the operational schema.

## Database design (OLTP)

<img src="../src/database/er_diagram/ER_diagram.png" alt="ERD diagram" width="auto"/>

### Considerations made during the design process

We can read the ERD from left to right, top to bottom.

The `User` entity stores information about registered members, including membership_id, first_name, last_name, email, phone_number. membership_id uniquely identifies each member and serves as the primary key. We note that the email field is unique for each user but cannot be shown in the diagram. The membership_id is the primary key for the user entity. The makes relationship between user and transaction is seen above.

The relationship between `User` and `Transaction` is a one-to-many relationship. A user may have zero or many (0,n) transactions over their lifetime, while each transaction belongs to exactly one user (1,1). The membership_id appears as a foreign key in the Transaction table. The `Transaction` entity contains the attributes from section 2, which include transaction_id, membership_id, date, total_items_price, and total_items_weight. The transaction_id is the primary key for the `Transaction` entity.

`Transactions` and `Items` have a many-to-many relationship, since a transaction may contain multiple items and each item may appear in many different transactions. To implement this relationship in a relational database, an associative entity/aggregate entity named `Transaction_Item` is introduced. Both the transaction and item entities have a cardinality of 1,n, which means that a transaction can contain 1 or more items and an item can be contained in 1 or more transactions. This confirms that it is a many-to-many relationship, . The `has`/`Transaction_Item` aggregate has attributes unit_price and quantity to support future business queries.

Note that we set a unit_price attribute in the `Transaction_Item` entity to support future business queries. This is because the price of an item may change over time, and we want to ensure that the price of an item at the time of purchase is recorded in the transaction. The quantity attribute is also included to support future business queries, as a member may purchase multiple quantities of an item in a single transaction.

The `Item` entity contains the attributes item_id, name, manufacturer_id, cost, and weight. The item_id is the primary key for the `Item` entity.

The `Manufacturer` entity includes manufacturer_id and name. The manufacturer_id is the primary key for the `Manufacturer` entity. The `Makes` relationship between manufacturer and item is a one-to-many relationship, as a manufacturer can produce 0 or many items, but an item can only be produced by one manufacturer.
