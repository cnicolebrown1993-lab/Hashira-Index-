# Hashira Index (In Progress)

A multidimensional behavioral assessment and analytics project.

## Project Goal

The Hashira Index compares behavioral patterns across multiple dimensions rather than assigning users to a single personality type.

The project will include:

- Python scoring
- JSON-driven assessment configuration
- work vs. home behavioral comparisons
- character similarity scoring
- automated testing
- a Streamlit interface

## Assessment Data Structure

Assessment questions are stored in `data/questions.json` instead of being hardcoded into the Python application.

Each question contains:
- A unique question ID
- The scenario text
- Four possible responses
- Hidden behavioral-dimension weights for each response

Example:

```json
{
  "id": "Q001",
  "scenario": "Example behavioral scenario...",
  "responses": [
    {
      "id": "A",
      "text": "Example response...",
      "weights": {
        "AU": 2,
        "DS": 1
      }
    }
  ]
}
```

Response weights affect behavioral dimensions rather than assigning points directly to a Hashira. The user's behavioral profile will later be compared against separate Hashira profile vectors.

### Behavioral Dimensions

| Code | Dimension |
|------|-----------|
| SI | Social Initiation |
| SR | Social Responsiveness |
| DS | Decision Speed |
| ET | Evidence Threshold |
| AU | Autonomy |
| EE | Emotional Expression |
| CC | Conflict Conviction |
| LM | Leadership / Mentorship |
| FT | Frustration Tolerance |
| RS | Recovery / Resilience |
| CW | Change Willingness |