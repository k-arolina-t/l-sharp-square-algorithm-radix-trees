# run via: python -m aalpy.learning_algs.deterministic.ObservationTreeTests, must be in AALpy folder

from aalpy.learning_algs.deterministic.ObservationTree import CompressedMealyNode, MealyNode

parent_node = MealyNode()
node1 = CompressedMealyNode([(23, "start", "a")], parent_node)
node2 = CompressedMealyNode([(23, "start", "ax"), (2, "mid", "b"), (3, "end", None)], parent_node)
node3 = CompressedMealyNode([(23, "start", "a"), (2, "mid", "b"), (3, "end", None)], parent_node)
node4 = CompressedMealyNode([(23, "start", "a"), (2, "mid", "b"), (3, "end", None)], parent_node)
parent_node.successors['a'] = ("start", node1)
parent_node.successors['b'] = ("start", node2)
parent_node.successors['c'] = ("start", node3)
parent_node.successors['d'] = ("start", node4)
node1.successors['b'] = ("heeg", "goop")
node2.successors['b'] = ("heeg", "goop")
node3.successors['b'] = ("heeg", MealyNode(node3))
node4.successors['b'] = ("heeg", "goop")
node2.input_to_parent = 'b'
node3.input_to_parent = 'c'
node4.input_to_parent = 'd'

print("format: id, parent id/nodes, parent's successors, successors nodes, successor's parent id")
print("len 1:", node1.uncompress_node_at_index(0).nodes)
un2 = node2.uncompress_node_at_index(0)
print("start:", un2.id, un2.parent.id, un2.parent.successors["b"][1].id, un2.successors['ax'][1].nodes, un2.successors['ax'][1].parent.id)
un3 = node3.uncompress_node_at_index(2)
print("end:", un3.id, un3.parent.nodes, un3.parent.successors["b"][1].id, un3.successors['b'][1].id, un3.successors['b'][1].parent.id)
un4 = node4.uncompress_node_at_index(1)
print("middle:", un4.id, un4.parent.nodes, un4.parent.successors["a"][1].id, un4.successors['b'][1].nodes, un4.successors['b'][1].parent.id)

# # Create a basic node structure
# # nodes = (id, output, input_to_next)
# root_nodes = [
#     (0, "start", "a"),
#     (1, "mid", "b"),
#     (2, "end", None)
# ]

# root = CompressedMealyNode(root_nodes)

# print("Initial nodes:", root.nodes)
# print("Initial successors:", root.successors)


# # Test add_sucessor_end
# print("\n--- Testing add_sucessor_end ---")
# dummy_successor = MealyNode()
# result = root.add_sucessor_end("c", "out_c", dummy_successor)

# print("Nodes after add_sucessor_end:", root.nodes)
# print("Successors after add_sucessor_end:", root.successors)
# print("Returned node:", result)


# # Test get_successor
# print("\n--- Testing get_successor ---")
# succ = root.get_successor("c", len(root.nodes) - 1)
# print("Successor for input 'c':", succ)


# # Test get_output
# print("\n--- Testing get_output ---")
# output = root.get_output("c", len(root.nodes) - 1)
# print("Output for input 'c':", output)


# # Test get_input_to_parent
# print("\n--- Testing get_input_to_parent ---")
# print("Index 0:", root.get_input_to_parent(0))
# print("Index 1:", root.get_input_to_parent(1))


# # Test get_parent
# print("\n--- Testing get_parent ---")
# print("Parent at index 0:", root.get_parent(0))
# print("Parent at index 1:", root.get_parent(1))


# # Test extend_and_get
# print("\n--- Testing extend_and_get ---")
# try:
#     new_node = root.extend_and_get("d", "out_d", len(root.nodes) - 1)
#     print("New node created:", new_node)
#     print("Updated successors:", root.successors)
#     print(root.nodes)
# except Exception as e:
#     print("extend_and_get raised exception:", e)


# # Test add_successor_middle (may fail if MealyNode isn't properly defined)
# print("\n--- Testing add_successor_middle ---")
# try:
#     middle_successor = MealyNode()
#     root.add_successor_middle("x", "out_x", middle_successor, 0)
#     print("Nodes after middle split:", root.nodes)
#     print("Successors after middle split:", root.successors)
# except Exception as e:
#     print("add_successor_middle raised exception:", e)