import sqlite3

def create_db():
    conn = sqlite3.connect('rules.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS rules
                 (id INTEGER PRIMARY KEY, rule TEXT)''')
    conn.commit()
    conn.close()

def store_rule(rule_string):
    conn = sqlite3.connect('rules.db')
    c = conn.cursor()
    c.execute("INSERT INTO rules (rule) VALUES (?)", (rule_string,))
    conn.commit()
    conn.close()

def get_rules():
    conn = sqlite3.connect('rules.db')
    c = conn.cursor()
    c.execute("SELECT * FROM rules")
    rules = c.fetchall()
    conn.close()
    return rules
