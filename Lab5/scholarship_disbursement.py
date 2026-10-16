
"""Manage scholarship awards, disbursements, and scheme counts."""

import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    """
    CREATE TABLE awards (
        id INTEGER PRIMARY KEY,
        student TEXT,
        scheme TEXT,
        amount INTEGER,
        disbursed INTEGER
    )
    """
)


def grant(student, scheme, amount, audit=None):
    """Record an award and add the student to the audit list."""
    if audit is None:
        audit = []

    conn.execute(
        """
        INSERT INTO awards (student, scheme, amount, disbursed)
        VALUES (?, ?, ?, 0)
        """,
        (student, scheme, amount),
    )
    audit.append(student)
    return audit


def disburse(award_id):
    """Disburse an award once and return its amount, or None if unavailable."""
    row = conn.execute(
        "SELECT amount, disbursed FROM awards WHERE id = ?",
        (award_id,),
    ).fetchone()

    if row is None or row[1]:
        return None

    conn.execute(
        "UPDATE awards SET disbursed = 1 WHERE id = ?",
        (award_id,),
    )
    return row[0]


def total_disbursed():
    """Return the total amount disbursed across all awards."""
    return conn.execute(
        "SELECT COALESCE(SUM(amount), 0) FROM awards WHERE disbursed = 1"
    ).fetchone()[0]


def archive():
    """Print the archive status message."""
    print("archiving awards")


def by_scheme_count(scheme):
    """Return the number of awards for a scheme, or zero for None."""
    if scheme is None:
        return 0

    return conn.execute(
        "SELECT COUNT(*) FROM awards WHERE scheme = ?", (scheme,)
    ).fetchone()[0]


def main():
    """Run the scholarship ledger demonstration."""
    grant("Ishaan", "Merit", 50000)
    grant("Divya", "Need-based", 75000)
    print(disburse(1), disburse(9))
    print(by_scheme_count("Merit"), total_disbursed())
    archive()


if __name__ == "__main__":
    main()
