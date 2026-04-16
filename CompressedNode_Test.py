from CompressedNode import CompressedNode

new_node = CompressedNode(None, [(1,'a','a'), (2,'b','b'), (3,'c',None)])
print(new_node.nodes)
new_node.set_output(True, 2)
print(new_node.nodes)
new_node.extend_and_get(4, 'd', 2)
print(new_node.nodes)
new_node.extend_and_get(5, 'e', 2)
print(new_node.nodes)
print(new_node.successors)
new_node.extend_and_get(6, 'f', 2)
print(new_node.successors)