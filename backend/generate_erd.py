import os

# Define your database URI
# Example for PostgreSQL: postgresql://username:password@localhost/database_name
# Example for SQLite: sqlite:///path/to/database.db
DATABASE_URI = "postgresql://postgres:password@localhost/court_db"

# Output file path
output_file = "erd.png"

# Generate the ER diagram
def generate_er_diagram(uri, output_path):
    try:
        os.system(f"eralchemy -i {uri} -o {output_path}")
        print(f"ER diagram generated and saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

generate_er_diagram(DATABASE_URI, output_file)
