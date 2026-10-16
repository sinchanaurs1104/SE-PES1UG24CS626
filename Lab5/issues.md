# Static Code Analysis Issues

The following issues were identified in the original `scholarship_disbursement.py` using Pylint, Bandit, and Flake8. Line numbers refer to the original file and may change after fixes.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| SQL injection risk | Security — Medium | 10 | SQL query is constructed using string interpolation, which may allow SQL injection. | Use a parameterized SQL query with placeholders. |
| Shell command execution | Security — Low | 26 | `os.system()` invokes a shell to print an archive message. | Replace it with `print()` if the goal is only to display a message. |
| Silent exception handling | Security / Quality — Low | 25–28 | A broad exception is caught and ignored with `pass`, hiding failures. | Remove the unnecessary `try/except`, or handle a specific exception meaningfully. |
| Mutable default argument | Bug / Quality | 9 | `audit=[]` is shared across calls to `grant()`. | Default to `None` and create a new list inside the function when needed. |
| Global state modification | Code quality | 15–20 | `disburse()` modifies `disbursed_total` using a `global` statement. | Refactor state management to avoid the global, if appropriate for the program design. |
| Inconsistent return values | Code quality | 15–21 | `disburse()` returns the amount for a found award but implicitly returns `None` when no award is found. | Define and implement a consistent return-value contract. |
| Missing module/function docstrings | Code quality | 1, 9, 15, 24, 31, 37 | The module and several functions do not have docstrings. | Add concise docstrings describing the module and each function. |
| Naming conventions | Style / Code quality | 6, 31 | `disbursed_total` is flagged for the expected naming style in its context, and `bySchemeCount()` does not use `snake_case`. | Use consistent, descriptive names that follow Python conventions; consider `by_scheme_count()`. |
| Comparison with `None` | Style / Code quality | 32 | The code uses `scheme == None`. | Use `scheme is None`. |
| Long lines | Style | 5, 10, 17, 19, 34 | Several lines exceed the configured line-length limits. | Split long SQL statements and expressions across multiple lines. |
| Regular string formatting | Code quality | 10 | Pylint recommends avoiding `%` formatting for this SQL construction; the security fix should take priority over changing it to an f-string. | Use SQL parameter binding rather than an f-string or interpolated SQL. |
| Repeated disbursement | Functional bug found during code review | 19–20 | An award can be disbursed more than once, increasing `disbursed_total` repeatedly for the same award. | Check the current `disbursed` status before updating or adding the amount. Add a test for repeated disbursement. |

## Notes

- The original Pylint score was **5.00/10**.
- Bandit reported **1 medium-severity** finding and **3 low-severity** findings.
- Flake8 reported **6** findings.
- Findings from different tools may overlap; each underlying issue is documented only once where practical.
- The repeated-disbursement issue was found by code review and was not listed in the supplied static-analysis reports.
