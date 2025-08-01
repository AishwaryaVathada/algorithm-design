import sys

class TreeNode:
    def __init__(self, value):
        self.value = int(value)  # Convert the value to int
        self.left = None
        self.right = None

def find_root_node(tree_str):
    # Split the input into sub arrays of relations
    nodes = tree_str.split()

    # Initialize sets to store parents and children (use set because it doesn't store repeats)
    parents = set()
    children = set()

    # Iterate through each node relationship
    for node in nodes:
        # Split each relationship into parent, left child, and right child
        parent, left, right = node.split(':')
        
        # Add parent to the set of parents
        parents.add(parent)
        
        # Add left and right to the set of children if they're not 'x' (pointing to NULL node)
        if left != 'x':
            children.add(left)
        if right != 'x':
            children.add(right)

    # Find the root node by checking which parent is not a child
    root = parents - children

    # Return the root node (it should contain exactly one element)
    return root.pop() if root else None

def build_tree(tree_str):
    nodes = {}
    relationships = tree_str.split()

    # Create all nodes and store them in a dictionary
    for relationship in relationships:
        parent_val, left_val, right_val = relationship.split(':')
        
        # Create or get the parent node
        if parent_val not in nodes:
            nodes[parent_val] = TreeNode(parent_val)
        
        parent = nodes[parent_val]
        
        # Create or get the left child node if not 'x'
        if left_val != 'x':
            if left_val not in nodes:
                nodes[left_val] = TreeNode(left_val)
            parent.left = nodes[left_val]
        
        # Create or get the right child node if not 'x'
        if right_val != 'x':
            if right_val not in nodes:
                nodes[right_val] = TreeNode(right_val)
            parent.right = nodes[right_val]

    # Find the root node
    root_value = find_root_node(tree_str)
    return nodes[root_value] if root_value else None

def inorder_traversal(root, nodes):
    if not root:
        return 
    
    #In Order traversal is because in binary search tree the elements in In Order traversal remain sorted and we need to directly replace

    inorder_traversal(root.left, nodes) 
    nodes.append(root.value)
    inorder_traversal(root.right, nodes)

def inorder_replace(root, sorted_values):
    if not root:
        return
    
    # In order replace

    inorder_replace(root.left, sorted_values)
    root.value = sorted_values.pop(0)
    inorder_replace(root.right, sorted_values)

def pre_order_traversal(root, result):
    if not root:
        return
    
    # Visit the root node
    result.append(str(root.value))
    
    # Traverse the left subtree
    pre_order_traversal(root.left, result)
    
    # Traverse the right subtree
    pre_order_traversal(root.right, result)

def get_pre_order_string(root):
    """Generates the pre-order traversal as a formatted string."""
    result = []
    pre_order_traversal(root, result)
    return ' '.join(result)
    
def to_CBST(tree_input):
    """Converts the binary tree to a binary search tree (BST)."""
    node_values = []

    # Step 1: Build the tree
    root = build_tree(tree_input)
    
    # Step 2: Extract all node values using in-order traversal
    inorder_traversal(root, node_values)

    # Step 3: Sort the extracted node values
    sorted_values = sorted(node_values)

    # Step 4: Replace the node values with the sorted values (to form BST)
    inorder_replace(root, sorted_values)

    # Step 5: Get the result in the format desired using pre-order traversal
    result = get_pre_order_string(root)

    return result


num_line = int(sys.stdin.readline())
for _ in range(num_line):
    tree_input = sys.stdin.readline().strip()
    if tree_input:
        print(to_CBST(tree_input))