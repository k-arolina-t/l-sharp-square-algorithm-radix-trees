from collections import deque


class Apartness:
    @staticmethod
    def compute_witness(state1, state2, ob_tree, index=0):
        if state1 is None or state2 is None: 
            raise ValueError("States cannot be None")
        # Finds a distinguishing sequence between two states if they are apart based on the observation tree
        if ob_tree.automaton_type == 'mealy':
            state1_destination = Apartness._show_states_are_apart_mealy(
                state1, state2, ob_tree.alphabet, index)
        else:
            state1_destination = Apartness._show_states_are_apart_moore(
                state1, state2, ob_tree.alphabet)
        if not state1_destination:
            return
        return ob_tree.get_transfer_sequence(state1, state1_destination)

    @staticmethod
    def states_are_apart(state1, state2, ob_tree):
        # Checks if two states are apart by checking any output difference in the observation tree
        if ob_tree.automaton_type == 'mealy':
            return Apartness._show_states_are_apart_mealy(state1, state2, ob_tree.alphabet) is not None
        else:
            return Apartness._show_states_are_apart_moore(state1, state2, ob_tree.alphabet) is not None

    @staticmethod
    def _show_states_are_apart_mealy(first, second, alphabet, index=0):
        # Identifies if two states can be distinguished by any input-output pair in the provided alphabet
        if first is None or second is None:
            raise ValueError("States cannot be None")
        pairs = deque([(first, second, index, 0)])
        # if type(first) == tuple: print(first)

        while pairs:
            first_node, second_node, counter_one, counter_two, = pairs.popleft()
            next_counter_one, next_counter_two = counter_one, counter_two
            for input_val in alphabet:
                #if type(first_node) == tuple: print(first_node)
                if hasattr(first_node, "nodes"): 
                    first_output, _ = first_node.get_output(input_val, counter_one)
                else: 
                    first_output = first_node.get_output(input_val)
                if hasattr(second_node, "nodes"): 
                    second_output, _ = second_node.get_output(input_val, counter_two)
                else:
                    second_output = second_node.get_output(input_val)

                if first_output is not None and second_output is not None:
                    if first_output != second_output:
                        if hasattr(first_node, "nodes"):
                            return first_node.get_successor(input_val, counter_one)[0]
                        else: return first_node.get_successor(input_val)
                    
                    
                    if hasattr(first_node, "nodes"):
                        first_successor, next_counter_one = first_node.get_successor(input_val, counter_one)
                    else: first_successor = first_node.get_successor(input_val)
                    if hasattr(second_node, "nodes"):
                        second_successor, next_counter_two = second_node.get_successor(input_val, counter_two)
                    else: second_successor = second_node.get_successor(input_val)
                    pairs.append((first_successor, second_successor, next_counter_one, next_counter_two))

        return None

    @staticmethod
    def _show_states_are_apart_moore(first, second, alphabet):
        # Identifies if two states can be distinguished by any input-output pair in the provided alphabet
        pairs = deque([(first, second)])

        while pairs:
            first_node, second_node = pairs.popleft()
            if first_node is not None and second_node is not None:
                first_output = first_node.output
                second_output = second_node.output
                if first_output != second_output:
                    return first_node

                for input_val in alphabet:
                    pairs.append((first_node.get_successor(
                        input_val), second_node.get_successor(input_val)))

        return None

    @staticmethod
    def compute_witness_in_tree_and_hypothesis_states(ob_tree, ob_tree_state, hyp_state):
        """
        Determines if the observation tree and the hypothesis are distinguishable based on their state outputs
        """
        if ob_tree.automaton_type == 'mealy':
            return Apartness.compute_witness_in_tree_and_hypothesis_states_mealy(ob_tree, ob_tree_state, hyp_state)
        else:
            return Apartness.compute_witness_in_tree_and_hypothesis_states_moore(ob_tree, ob_tree_state, hyp_state)

    @staticmethod
    def compute_witness_in_tree_and_hypothesis_states_mealy(ob_tree, ob_tree_state, hyp_state):
        """
        Determines if the observation tree and the hypothesis are distinguishable based on their state outputs
        """
        pairs = deque([(ob_tree_state, hyp_state, 0)])
        while pairs:
            tree_state, hyp_state, counter = pairs.popleft()
            next_counter = counter
            for input_val in ob_tree.alphabet:
                if hasattr(tree_state, "nodes"): 
                    tree_output, _ = tree_state.get_output(input_val, counter)
                else: 
                    tree_output = tree_state.get_output(input_val)

                if tree_output is not None and input_val in hyp_state.output_fun:
                    hyp_output = hyp_state.output_fun[input_val]

                    if hasattr(tree_state, "nodes"):
                        tree_dest, next_counter = tree_state.get_successor(input_val, counter)
                    else: tree_dest = tree_state.get_successor(input_val)

                    if tree_output != hyp_output:
                        return ob_tree.get_transfer_sequence(ob_tree_state, tree_dest)

                    pairs.append((tree_dest, hyp_state.transitions[input_val], next_counter))

        return None

    @staticmethod
    def compute_witness_in_tree_and_hypothesis_states_moore(ob_tree, ob_tree_state, hyp_state):
        """
        Determines if the observation tree and the hypothesis are distinguishable based on their state outputs
        """
        pairs = deque([(ob_tree_state, hyp_state)])

        while pairs:
            tree_state, hyp_state = pairs.popleft()
            if (tree_state is not None) and (hyp_state is not None):
                tree_output = tree_state.output
                if ob_tree.automaton_type == 'dfa':
                    hyp_output = hyp_state.is_accepting
                else:
                    hyp_output = hyp_state.output

                if tree_output != hyp_output:
                    return ob_tree.get_transfer_sequence(ob_tree_state, tree_state)

                for input_val in ob_tree.alphabet:
                    if input_val in hyp_state.transitions:
                        pairs.append((tree_state.get_successor(
                            input_val), hyp_state.transitions[input_val]))

        return None
