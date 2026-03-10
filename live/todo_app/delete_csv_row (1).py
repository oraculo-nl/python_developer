import csv

def delete_row_by_number(input_file, row_number, output_file=None):
    """
    Delete a row from a CSV file by its row number (0-indexed, excluding header).

    Args:
        input_file (str): Path to the input CSV file.
        row_number (int): Row number to delete (0-indexed, not counting the header).
        output_file (str): Path to save the result. If None, overwrites the input file.
    """
    output_file = output_file or input_file

    with open(input_file, newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    if row_number < 0 or row_number >= len(rows):
        print(f"Error: row_number {row_number} is out of range (file has {len(rows)} data rows).")
        return

    deleted_row = rows[row_number]
    del rows[row_number]

    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Deleted row {row_number} ({deleted_row}). Saved to '{output_file}'.")


def delete_row_by_value(input_file, column, value, output_file=None):
    """
    Delete all rows where a specific column matches a given value.

    Args:
        input_file (str): Path to the input CSV file.
        column (str): Column name to match against.
        value (str): Value to match for deletion.
        output_file (str): Path to save the result. If None, overwrites the input file.
    """
    output_file = output_file or input_file

    with open(input_file, newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    original_count = len(rows)
    rows = [row for row in rows if row[column] != value]
    deleted = original_count - len(rows)

    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Deleted {deleted} row(s) where {column}='{value}'. Saved to '{output_file}'.")


# --- Example usage ---
if __name__ == "__main__":
    # Delete the 2nd data row (0-indexed) by position:
    # delete_row_by_number("data.csv", row_number=1)

    # Delete all rows where "name" column equals "Alice":
    # delete_row_by_value("data.csv", column="name", value="Alice")

    # --- Quick demo ---
    import os
    demo_file = "demo.csv"

    with open(demo_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name"])
        writer.writeheader()
        writer.writerows([{"name": "Alice"}, {"name": "Bob"}, {"name": "Carol"}, {"name": "Bob"}])

    print("Before:")
    with open(demo_file) as f:
        print(f.read())

    delete_row_by_number(demo_file, row_number=0)       # removes "Alice"

    print("After deleting row 0:")
    with open(demo_file) as f:
        print(f.read())

    delete_row_by_value(demo_file, column="name", value="Bob")  # removes both "Bob" rows

    print("After deleting all 'Bob' rows:")
    with open(demo_file) as f:
        print(f.read())

    os.remove(demo_file)
