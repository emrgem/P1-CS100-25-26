"""
db_explorer.py — Interactive SQL Explorer
==========================================
Type SQL queries and see results instantly.
Type 'quit' to exit.

Usage:
    python db_explorer.py              ← opens movies.db by default
    python db_explorer.py mydata.db    ← opens a specific database
"""

import sqlite3
import sys
import os


def print_results(cursor):
    """Print query results in a clean formatted table."""
    rows = cursor.fetchall()

    if not rows:
        print("  (no results)")
        return

    # Get column names from cursor description
    columns = [desc[0] for desc in cursor.description]

    # Calculate column widths
    widths = []
    for i, col in enumerate(columns):
        max_width = len(str(col))
        for row in rows:
            max_width = max(max_width, len(str(row[i])))
        widths.append(min(max_width, 40))  # Cap at 40 chars

    # Print header
    header = " | ".join(str(col).ljust(widths[i]) for i, col in enumerate(columns))
    print(f"  {header}")
    print(f"  {'-+-'.join('-' * w for w in widths)}")

    # Print rows
    for row in rows:
        line = " | ".join(str(val)[:40].ljust(widths[i]) for i, val in enumerate(row))
        print(f"  {line}")

    # Print count
    print(f"\n  ({len(rows)} row{'s' if len(rows) != 1 else ''})")


def run_explorer(db_file):
    """Main interactive loop."""
    if not os.path.exists(db_file):
        print(f"❌ File not found: {db_file}")
        print(f"   Make sure {db_file} is in the same folder as this script.")
        return

    print(f"╔══════════════════════════════════════════╗")
    print(f"║       🗄️  SQL Explorer                   ║")
    print(f"║  Connected to: {db_file:<25s} ║")
    print(f"╠══════════════════════════════════════════╣")
    print(f"║  Type SQL queries and press Enter.       ║")
    print(f"║  Type 'tables' to see all tables.        ║")
    print(f"║  Type 'schema' to see table structure.   ║")
    print(f"║  Type 'quit' to exit.                    ║")
    print(f"╚══════════════════════════════════════════╝")

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    while True:
        print()
        try:
            query = input("SQL> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not query:
            continue

        if query.lower() == "quit":
            print("Goodbye!")
            break

        # Special commands
        if query.lower() == "tables":
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
            tables = cursor.fetchall()
            print("  Tables in database:")
            for t in tables:
                print(f"    📋 {t[0]}")
            continue

        if query.lower() == "schema":
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
            tables = cursor.fetchall()
            for t in tables:
                print(f"\n  📋 {t[0]}:")
                cursor.execute(f"PRAGMA table_info({t[0]})")
                cols = cursor.fetchall()
                for col in cols:
                    pk = " ⭐ PRIMARY KEY" if col[5] else ""
                    nn = " (required)" if col[3] else ""
                    print(f"    {col[1]:20s} {col[2]:10s}{nn}{pk}")
            continue

        # Run the SQL query
        try:
            cursor.execute(query)

            # If it's a SELECT query, show results
            if cursor.description:
                print_results(cursor)
            else:
                # INSERT/UPDATE/DELETE — show affected rows
                conn.commit()
                print(f"  ✅ Done. ({cursor.rowcount} row{'s' if cursor.rowcount != 1 else ''} affected)")

        except Exception as e:
            print(f"  ❌ Error: {e}")

    conn.close()


if __name__ == "__main__":
    # Use command line argument or default to movies.db
    db_file = sys.argv[1] if len(sys.argv) > 1 else "movies.db"
    run_explorer(db_file)
