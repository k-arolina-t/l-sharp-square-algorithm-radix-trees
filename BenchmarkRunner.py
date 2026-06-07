from aalpy.utils import load_automaton_from_file
from aalpy.SULs import MealySUL
from aalpy.oracles import WpMethodEqOracle
from aalpy.learning_algs import run_Lsharp

def run_benchmark():

    mealy_machine = load_automaton_from_file(f'./BenchmarkDots/BitVise.dot', automaton_type='mealy')
    input_alphabet = mealy_machine.get_input_alphabet()

    sul_mealy = MealySUL(mealy_machine)
    eq_oracle = WpMethodEqOracle(input_alphabet, sul_mealy, len(mealy_machine.states))

    # Extension rule options: {"Nothing", "SepSeq", "ADS"}
    # Separation rule options: {"SepSeq", "ADS"}
    learned_mealy = run_Lsharp(input_alphabet, sul_mealy, eq_oracle, automaton_type='mealy', extension_rule="SepSeq",
                               separation_rule="SepSeq", max_learning_rounds=50, print_level=3)
    
    return learned_mealy

run_benchmark()
