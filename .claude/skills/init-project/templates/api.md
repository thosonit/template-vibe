<!--
Stage 3d · docs/api/api.md · conventions + index of endpoint groups. One doc per group in docs/api/endpoints/ (see api-endpoint.md).
Adjust the conventions to the project; they apply to every endpoint.
-->

# API

## List of APIs

| Group   | Doc                                        |
| ------- | ------------------------------------------ |
| <Group> | [endpoints/<group>.md](endpoints/<group>.md) |

## Convention

- Base path: `/api/v1`
- Format: JSON request/response bodies, `Content-Type: application/json`
- Naming: resource paths are plural, kebab-case
- HTTP methods: `GET` read, `POST` create/action, `PATCH` partial update, `DELETE` remove
- Response envelope:
  ```json
  { "success": true, "data": {}, "error": null }
  ```
- Errors use the same envelope with `success: false`, `data: null`, `error: { "code": "...", "message": "..." }`

## Authentication

- <how clients authenticate; what unauthenticated requests get>

## Rules

- Never return sensitive fields in any response
- Validate all input server-side
- Rate limit sensitive endpoints at the API layer
- Error messages must not leak whether a resource exists
- Every new endpoint is documented in `docs/api/endpoints/*.md` before merge
