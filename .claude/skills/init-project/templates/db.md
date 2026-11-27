<!--
Stage 3e · docs/database/db.md · ONE shared schema doc for the whole project, extended in place per feature (no per-CODE file).
-->

# Database Schema

The schema below is written in [DBML](https://dbml.dbdiagram.io/docs/). To view the ERD: copy the code block, open https://dbdiagram.io/d, paste it.

## Schema

```dbml
Table <table_name> {
  id uuid [pk, default: `gen_random_uuid()`]
  <column> <type> [not null]
  created_at timestamp [not null, default: `now()`]
  updated_at timestamp [not null, default: `now()`]

  Note: '<what this table holds and which spec defines it>'
}
```

## Notes

- `<table.column>`: <meaning, lifecycle, invariants that the schema cannot express>
- Migration notes: <ordering, backfills, destructive changes>
