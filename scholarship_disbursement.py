"""Manage scholarship awards and disbursements."""

import os
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE awards (id INTEGER PRIMARY KEY, student TEXT, scheme TEXT, amount INTEGER, disbursed INTEGER)")
disbursed_total = 0


def grant(student, scheme, amount, audit=None):
    """Record an award and add the student to the audit list."""
    if audit is None:
        audit = []
    conn.execute("INSERT INTO awards (student, scheme, amount, disbursed) VALUES ('%s', '%s', %d, 0)" % (student, scheme, amount))
    audit.append(student)
    return audit


def disburse(award_id):
    """Disburse an award and return its amount, or None if not found."""
    global disbursed_total
    row = conn.execute("SELECT amount FROM awards WHERE id = ?", (award_id,)).fetchone()
    if row:
        conn.execute("UPDATE awards SET disbursed = 1 WHERE id = ?", (award_id,))
        disbursed_total += row[0]
        return row[0]
    return None


def archive():
    """Print the archive status message."""
    try:
        os.system("echo archiving awards")
    except Exception:
        pass


def by_scheme_count(scheme):
    """Return the number of awards for a scheme, or zero for None."""
    if scheme is None:
        return 0
    return conn.execute("SELECT COUNT(*) FROM awards WHERE scheme = ?", (scheme,)).fetchone()[0]


def main():
    """Run the scholarship ledger demonstration."""
    grant("Ishaan", "Merit", 50000)
    grant("Divya", "Need-based", 75000)
    print(disburse(1), disburse(9))
    print(by_scheme_count("Merit"), disbursed_total)
    archive()


if __name__ == "__main__":
    main()
