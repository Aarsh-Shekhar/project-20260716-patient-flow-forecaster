# Risk Explanation

Domain: healthcare operations

This note records an implementation detail for Patient Flow Forecaster. The current operating
threshold is `0.77` and review should happen within `72` hours
for records above that level.

## Checks

- confirm input fields are present
- verify score ordering is stable
- compare high exposure records against the review queue
