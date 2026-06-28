## System Design Skill

Use this guidance when writing architecture, access-control, and cloud-design sections.

### Goal

Produce concise, defensible system design documentation that explains the tradeoffs behind the chosen architecture and makes the visuals easy to review.

### Required Coverage

- Access strategy for shared databases and team-specific permissions.
- Cloud architecture for ingestion, processing, retention, and BI access.

### Design Expectations

- State assumptions explicitly.
- Address security, retention, scaling, high availability, fault tolerance, and least privilege.
- Explain how the design handles data at rest and in transit.
- Keep the diagram and the narrative consistent.
- Prefer a small number of clear diagrams over one overloaded diagram.

### Test-First Expectations

- Treat each design section like a spec with acceptance criteria.
- Check that every stakeholder concern appears somewhere in the document.
- Verify that the diagram labels match the written explanation.
- Review the design as if another engineer must be able to reproduce it.

### Validation Artifacts

- A markdown design document for each prompt or a single document with clearly separated sections.
- A diagram file or diagram source that can be reviewed independently.
- A short assumptions section for anything not defined in the prompt.

### Visual Approach

- Use AWS architecture icons as the visual language.
- Build one high-level context diagram and one detailed AWS architecture diagram.
- Label trust boundaries, public vs private paths, and retention boundaries.
- Show data flow with arrows, not prose.
- Keep the diagram readable at presentation size.

### Well-Architected Approach

- Use the AWS Well-Architected Framework as the reasoning checklist, not as a diagram overlay.
- Security: IAM least privilege, KMS encryption, private subnets, audit logging.
- Reliability: multi-AZ services, retries, dead-letter handling, durable storage.
- Operational excellence: monitoring, alarms, IaC, and runbooks.
- Performance efficiency: decouple ingestion and processing, autoscaling, right-sized compute.
- Cost optimization: managed services, lifecycle expiration, avoid overprovisioning.
- Sustainability: include only if it strengthens the argument.

### AWS Service Mapping

- Identify workload boundaries first: actors, ingestion paths, processing services, storage, analytics, and administration.
- Map each requirement to an AWS service after the boundaries are clear.
- Prefer managed services where they simplify operations and improve reliability.
- Call out tradeoffs when a managed and self-managed option are both plausible.

### Writing Pattern

- For each major AWS service, explain why it exists.
- For each key tradeoff, explain the alternative that was rejected.
- Tie every stakeholder concern back to a concrete architectural choice.
- Keep the prose short enough that the diagram still does the heavy lifting.

### Tooling Guidance

- If a diagramming surface is available, use it to produce a clean AWS-style architecture diagram.
- If diagramming is not available, generate Mermaid flowcharts or diagram source that can be rendered later.
- Keep the source text organized so it can be moved into a diagramming tool without rewriting the design.
