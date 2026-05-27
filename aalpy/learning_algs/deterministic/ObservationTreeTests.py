# run via: python -m aalpy.learning_algs.deterministic.ObservationTreeTests, must be in AALpy folder

from aalpy.learning_algs.deterministic.ObservationTree import CompressedMealyNode, MealyNode

# Create a basic node structure
# nodes = (id, output, input_to_next)
root_nodes = [
    (0, "start", "a"),
    (1, "mid", "b"),
    (2, "end", None)
]

root = CompressedMealyNode(root_nodes)

print("Initial nodes:", root.nodes)
print("Initial successors:", root.successors)


# Test add_sucessor_end
print("\n--- Testing add_sucessor_end ---")
dummy_successor = MealyNode()
result = root.add_successor_end("c", "out_c", dummy_successor)

print("Nodes after add_sucessor_end:", root.nodes)
print("Successors after add_sucessor_end:", root.successors)
print("Returned node:", result)


# Test get_successor
print("\n--- Testing get_successor ---")
succ = root.get_successor("c", len(root.nodes) - 1)
print("Successor for input 'c':", succ)


# Test get_output
print("\n--- Testing get_output ---")
output = root.get_output("c", len(root.nodes) - 1)
print("Output for input 'c':", output)


# Test get_input_to_parent
print("\n--- Testing get_input_to_parent ---")
print("Index 0:", root.get_input_to_parent(0))
print("Index 1:", root.get_input_to_parent(1))


# Test get_parent
print("\n--- Testing get_parent ---")
print("Parent at index 0:", root.get_parent(0))
print("Parent at index 1:", root.get_parent(1))


# Test extend_and_get
print("\n--- Testing extend_and_get ---")
try:
    new_node = root.extend_and_get("d", "out_d", len(root.nodes) - 1)
    print("New node created:", new_node)
    print("Updated successors:", root.successors)
    print(root.nodes)
except Exception as e:
    print("extend_and_get raised exception:", e)


# Test add_successor_middle (may fail if MealyNode isn't properly defined)
print("\n--- Testing add_successor_middle ---")
try:
    middle_successor = MealyNode()
    root.add_successor_middle("x", "out_x", middle_successor, 0)
    print("Nodes after middle split:", root.nodes)
    print("Successors after middle split:", root.successors)
except Exception as e:
    print("add_successor_middle raised exception:", e)