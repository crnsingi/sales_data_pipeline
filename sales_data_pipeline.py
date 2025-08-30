# --- create_db.py ---
import sqlite3

def init_db():
    conn = sqlite3.connect('sales.db')
    cursor = conn.cursor()
    
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY,
        date TEXT,
        product TEXT,
        quantity INTEGER,
        price REAL
    )
    '''
        )
    
    data = [
        ('2025-08-25','Widget A',10, 9.99),
        ('2025-08-25','Widget B',10, 19.99),
        ('2025-08-26','Widget A',10, 9.99),
        ('2025-08-26','Widget C',10, 29.99),
    ]
    cursor.executemany('INSERT INTO sales (date, product, quantity, price) VALUES(?,?,?,?)',data)
    
    conn.commit()
    conn.close()
    
    if __name__ == "__main__":
        init_db()