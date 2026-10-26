# Repository agent policy

- The visible coordinator agent is `QA Lead`.
- The `Bug Fixer` is a hidden internal subagent and must not appear in the public agent menu.
- `QA Lead` is the only agent allowed to invoke `Bug Fixer`.
- Fixes must be scoped to a single ticket and must not modify unrelated files.
- Each bug fix must include: ticket ID, root cause (one line), change made, and test result.
- Prefer the smallest possible patch and validate it with the narrowest relevant test command.
