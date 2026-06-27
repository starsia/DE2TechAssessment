## Database Design Skill

Use this guidance when designing the PostgreSQL schema and analytic queries.

### Goal

Model membership, items, and transactions so the database can support reporting and operational queries.

### Required Deliverables

- PostgreSQL DDL that can stand up the schema.
- Dockerfile or equivalent startup instructions for the database.
- Entity-relationship diagram or clear relational description.
- SQL for the top 10 members by spending.
- SQL for the top 3 most frequently bought items.

### Design Expectations

- Normalize core entities so members, items, and transactions are represented clearly.
- Add primary keys, foreign keys, and constraints where they enforce integrity.
- Include indexes only where they support the documented queries or future scale.
- Keep the schema understandable for analysts and maintainers.

### Test-First Expectations

- Write the schema and query assumptions down before coding DDL.
- Validate that each analyst query maps cleanly to the chosen tables and joins.
- Check that the schema can answer the two sample questions without ad hoc interpretation.

### Validation Artifacts

- A SQL file or folder containing the DDL and sample queries.
- A markdown explanation of entity relationships and tradeoffs.
- Any supporting notes needed to reproduce the database locally.
