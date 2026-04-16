from MooreNode import MooreNode

class CompressedNode:
    __slots__ = ['nodes', 'successors','parent', 'input_to_parent', 'access_sequence', 'leads_to_known']

    def __init__(self, parent=None, nodes=[]):
        self.nodes = nodes #node = (id, output, input_to_next)
        self.successors = {}
        self.parent = parent
        self.input_to_parent = None
        self.access_sequence = []
        self.leads_to_known = False

    def set_output(self, output, index):
        self.nodes[index] = self.nodes[index][:1] + (output,) + self.nodes[index][2:]
        if index == len(self.nodes) and (output is True or output is False): #uh oh -- toto prerobit
            self.leads_to_known = True
            node = self
            while node.parent is not None and not node.parent.leads_to_known:
                node = node.parent
                node.leads_to_known = True

    def get_access_sequence(self):
        access_sequence = []
        for node in self.nodes:
            if node[2] is not None:
                access_sequence.append(node[1])
        return access_sequence

    def add_successor(self, input_val, output_val, successor_node, index):
        """ Adds a successor node to the current node based on input """
        if index == (len(self.nodes) - 1):
            if self.successors == {}:
                self.nodes[-1] = self.nodes[-1][:2] + (input_val,)
                self.nodes.append((successor_node.id, successor_node.output, None))
                return self
            else:
                self.successors[input_val] = successor_node
                self.successors[input_val].parent = self
                self.successors[input_val].input_to_parent = input_val
                self.successors[input_val].set_output(output_val)
                self.successors[input_val].access_sequence = self.access_sequence + self.get_access_sequence() + [input_val]
                return self.successors[input_val]
        else:
            split_nodes = self.nodes[index+1:]
            self.successors[input_val] = successor_node
            self.successors[input_val].parent = self
            self.successors[input_val].input_to_parent = input_val
            self.successors[input_val].set_output(output_val)
            other_node = self.nodes[index+1]
            self.nodes = self.nodes[:index+1]
            next = self.nodes[index][2]
            self.nodes[index] = self.nodes[index][:2] + (None,)
            self.successors[next] = CompressedNode(parent=self, nodes=split_nodes)
            self.successors[input_val].input_to_parent = next
            self.successors[input_val].access_sequence = self.access_sequence + self.get_access_sequence() + [input_val]
            self.successors[input_val].access_sequence = self.access_sequence + self.get_access_sequence() + [input_val]
            return self.successors[next]

    # def get_successor(self, input_val):
    #     """ Returns the successor node for the given input """
    #     if input_val in self.successors:
    #         return self.successors[input_val]
    #     return None

    def extend_and_get(self, inp, output, index):
        """ Extend the node with a new successor and return the successor node """
        if index == (len(self.nodes) - 1):
            if inp in self.successors:
                return self.successors[inp]
        else:
            print(self.nodes[index])
            if self.nodes[index][2] == inp and self.nodes[index+1][1] == output:
                return self #figure out if this works
        successor_node = MooreNode(parent=self)
        return self.add_successor(inp, output, successor_node, index)

    # def __str__(self):
    #     compact_counter_examples = True
    #     if compact_counter_examples and self.output is None and len(self.successors) == 1:
    #         # skip printing this node and print the child instead.
    #         successor = list(self.successors.values())[0]
    #         result = str(successor)
    #         return result
    #     else:
    #         inputs = []
    #         current_node = self
    #         while not current_node.parent is None:
    #             inputs.insert(0, current_node.input_to_parent)
    #             current_node = current_node.parent

    #         result = "node " + str(inputs) + " / " + str(self.output)
    #         for input_val, successor in self.successors.items():
    #             result += "\n" + str(input_val) + ":\n"
    #             result += "\t" + str(successor).replace("\n", "\n\t")
    #         return result
