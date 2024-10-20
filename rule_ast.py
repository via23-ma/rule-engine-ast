import re

class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.node_type = node_type  # 'operator' or 'operand'
        self.value = value  # Condition value for operand, AND/OR for operator
        self.left = left  # Left child for operators
        self.right = right  # Right child for operators

    def __repr__(self):
        if self.node_type == "operand":
            return f"Operand({self.value})"
        else:
            return f"Operator({self.value})"

def create_condition_node(condition):
    match = re.match(r'(\w+)\s*(>|<|=)\s*(\S+)', condition.strip())
    if match:
        return Node("operand", {"attribute": match.group(1), "operator": match.group(2), "value": match.group(3)})
    return None

def create_rule(rule_string):
    tokens = re.findall(r'(\w+|\(|\)|AND|OR|>|<|=|\d+|\'.+?\')', rule_string)
    print(f"Tokens: {tokens}")  # Debugging print to inspect tokens
    stack = []

    def process_operator():
        print(f"Processing operator: Stack before processing: {stack}")  # Debugging print
        right = stack.pop()
        op = stack.pop()
        left = stack.pop()
        # Create a proper operator node and push it back to the stack
        stack.append(Node("operator", op, left, right))
        print(f"Processing operator: Stack after processing: {stack}")  # Debugging print

    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        if token in ('AND', 'OR'):
            # Process AND/OR operator
            stack.append(token)
        
        elif token == '(':
            stack.append(token)  # Handle left parentheses
        
        elif token == ')':
            # Handle right parentheses by processing the operator inside
            while stack[-2] != '(':
                process_operator()
            stack.pop()  # Remove '('
        
        elif token in ('>', '<', '='):
            # Handle conditions like 'age > 30' by looking ahead to the next token
            attribute = tokens[i - 1]
            operator = token
            value = tokens[i + 1]
            condition_str = f"{attribute} {operator} {value}"
            condition_node = create_condition_node(condition_str)
            stack.append(condition_node)
            i += 1  # Skip the next token since it's already used in the condition
        
        i += 1

    # Process any remaining operators in the stack
    while len(stack) > 1:
        process_operator()

    return stack[0]  # Root of the AST

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

def evaluate_rule(node, data):
    if node is None:
        print("Error: Node is None.")
        return False  # Return False if the node is None to prevent errors.

    print(f"Evaluating Node: {node}")  # Print the current node being evaluated
    
    if node.node_type == "operand":
        return evaluate_condition(data, node.value)
    
    left_result = evaluate_rule(node.left, data)
    right_result = evaluate_rule(node.right, data)

    if node.value == 'AND':
        return left_result and right_result
    elif node.value == 'OR':
        return left_result or right_result
    return False



