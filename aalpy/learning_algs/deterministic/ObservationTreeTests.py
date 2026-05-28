# run via: python -m aalpy.learning_algs.deterministic.ObservationTreeTests, must be in AALpy folder

from aalpy.learning_algs.deterministic.ObservationTree import CompressedMealyNode, MealyNode

# Create a basic node structure
# nodes = (id, output, input_to_next)
root_nodes = [
    (0, "start", "a"),
    (1, "mid", "b"),
    (2, "end", None)
]

root = MealyNode()
root.extend_and_get("a", "start", {}, {})[0].extend_and_get("b", "mid", {}, {})[0].extend_and_get("c", "mid2", {}, {})[0].extend_and_get("d", "end", 2)[0]

print("Initial nodes:", root.successors["a"][1].nodes)
print("Initial successors:", root.successors)

rootsucc = root.successors["a"][1]

# Test add_sucessor_end
print("\n--- Testing add_sucessor_end ---")
dummy_successor = MealyNode()
result = rootsucc.add_successor_end("c", "out_c", dummy_successor)

print("Nodes after add_sucessor_end:", rootsucc.nodes)
print("Successors after add_sucessor_end:", rootsucc.successors)
print("Returned node:", result)


# Test get_successor
print("\n--- Testing get_successor ---")
succ = rootsucc.get_successor("c", len(rootsucc.nodes) - 1)
print("Successor for input 'c':", succ)


# Test get_output
print("\n--- Testing get_output ---")
output = rootsucc.get_output("c", len(rootsucc.nodes) - 1)
print("Output for input 'c':", output)


# Test get_input_to_parent
print("\n--- Testing get_input_to_parent ---")
print("Index 0:", rootsucc.get_input_to_parent(0))
print("Index 1:", rootsucc.get_input_to_parent(1))


# Test get_parent
print("\n--- Testing get_parent ---")
print("Parent at index 0:", rootsucc.get_parent(0))
print("Parent at index 1:", rootsucc.get_parent(1))


# Test extend_and_get
print("\n--- Testing extend_and_get ---")
try:
    new_node = rootsucc.extend_and_get("d", "out_d", len(rootsucc.nodes) - 1)
    print("New node created:", new_node)
    print("Updated successors:", rootsucc.successors)
    print(rootsucc.nodes)
except Exception as e:
    print("extend_and_get raised exception:", e)


# Test add_successor_middle (may fail if MealyNode isn't properly defined)
print("\n--- Testing add_successor_middle ---")
try:
    middle_successor = MealyNode()
    rootsucc.add_successor_middle("x", "out_x", middle_successor, 0)
    print("Nodes after middle split:", rootsucc.nodes)
    print("Successors after middle split:", rootsucc.successors)
except Exception as e:
    print("add_successor_middle raised exception:", e)

print("\n--- Deep Inspection of the Graph State After Split ---")

# 1. Check if the newly added middle path is actually reachable from root
print("Is 'x' in root's successors?", "x" in rootsucc.successors)
if "x" in rootsucc.successors:
    print("  -> Points to node:", rootsucc.successors["x"][1])
    print("  -> Output of 'x':", rootsucc.successors["x"][0])

# 2. Check the transition linking the split halves
# The original transition at index 0 was 'a'. Let's see what happened to it.
print("\nIs the remaining chain transition ('a') still in root's successors?", "a" in rootsucc.successors)
if "a" in rootsucc.successors:
    remainder_node = rootsucc.successors["a"][1]
    print(f"  -> Remainder node type: {type(remainder_node).__name__}")
    if hasattr(remainder_node, "nodes"):
        print("  -> Remainder internal nodes:", remainder_node.nodes)
        print("  -> Remainder downstream successors:", remainder_node.successors)
    else:
        print("  -> Remainder node ID:", remainder_node.id)

# 3. Check for the "Ghost Reference" Trap
# If add_successor_middle executed the `new_self = MealyNode(...)` block,
# our local variable `root` might still point to the old, un-updated object.
print("\n--- The Reference Health Check ---")
print(f"Current local 'root' object type: {type(rootsucc).__name__}")
print("Current local 'root' nodes array:", getattr(rootsucc, 'nodes', 'No nodes array!'))

if len(rootsucc.successors) == 0:
    print(" BUG DETECTED: The 'root' object's successors are completely empty!")
    print("   This means the modifications were trapped inside a local variable ")
    print("   in your method and never made it back out to this script.")
else:
    print(" SUCCESS: The local 'root' object successfully retained its transitions.")


# 4. Verify Post-Split Lookups
print("\n--- Post-Split Traversal Test ---")
try:
    # Let's see if get_output still works correctly for the new path
    if hasattr(rootsucc, "nodes"):
        print("Output for 'x' via get_output:", rootsucc.get_output("x", 0))
    else:
        print("Output for 'x' via get_output:", rootsucc.get_output("x"))
except Exception as e:
    print(" Traversal crashed after split:", e)