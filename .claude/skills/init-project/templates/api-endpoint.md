<!--
Stage 3d · save as docs/api/endpoints/<group>.md and list it in docs/api/api.md. One file per endpoint group, not per feature CODE.
-->

# <Group> Endpoints

Related spec: [CODE-feature-name](../../specs/CODE-feature-name.spec.md)

## <METHOD> /<path>

<one-line purpose>

**Request**

```json
{
  "field": "type or example"
}
```

**Response 200**

```json
{
  "success": true,
  "data": {},
  "error": null
}
```

<side effects: cookies set, records revoked, events emitted>

**Errors**

- `<status> <error_code>` — <when it happens>

---
