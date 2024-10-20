from rule_ast import create_rule, evaluate_rule  # Removed combine_rules import
from database import create_db, store_rule, get_rules

def evaluate_condition(data, condition):
    attribute = condition["attribute"]
    operator = condition["operator"]
    value = condition["value"]

    if operator == '>':
        return data.get(attribute, 0) > int(value)
    elif operator == '<':
        return data.get(attribute, 0) < int(value)
    elif operator == '=':
        return data.get(attribute, '') == value.strip("'")
    return False

def main():
    # Initialize database
    create_db()

    # Example: Create a rule
    rule_string = "age > 30 AND department = 'Sales'"
    rule_ast = create_rule(rule_string)
    
    # Store the rule in the database
    store_rule(rule_string)

    # Retrieve rules from the database
    rules = get_rules()
    print("Stored Rules:")
    for rule in rules:
        print(rule)

    # Example data to evaluate
    data = {"age": 35, "department": "Sales"}

    # Evaluate the rule
    result = evaluate_rule(rule_ast, data)
    print(f"Evaluation Result: {result}")

if __name__ == "__main__":
    main()
