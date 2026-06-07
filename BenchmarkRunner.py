from aalpy.utils import load_automaton_from_file
from aalpy.SULs import MealySUL
from aalpy.oracles import WpMethodEqOracle
from aalpy.learning_algs import run_Lsharp
import tracemalloc

def run_benchmark(file_path):

    mealy_machine = load_automaton_from_file(file_path, automaton_type='mealy')
    input_alphabet = mealy_machine.get_input_alphabet()

    sul_mealy = MealySUL(mealy_machine)
    eq_oracle = WpMethodEqOracle(input_alphabet, sul_mealy, len(mealy_machine.states))

    # Extension rule options: {"Nothing", "SepSeq", "ADS"}
    # Separation rule options: {"SepSeq", "ADS"}
    learned_mealy = run_Lsharp(input_alphabet, sul_mealy, eq_oracle, automaton_type='mealy', extension_rule="SepSeq",
                               separation_rule="SepSeq", max_learning_rounds=50, print_level=1)

print("BitVise.dot")
for i in range(5):
    tracemalloc.start()
    run_benchmark('./BenchmarkDots/BitVise.dot')
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 1024 / 1024:.1f} MB")
    print(f"Peak usage: {peak / 1024 / 1024:.1f} MB")
    tracemalloc.stop()
print("Benchmark completed.")

print("GNUTLS_3.3.8_client_full.dot")
for i in range(5):
    tracemalloc.start()
    run_benchmark('./BenchmarkDots/GNUTLS_3.3.8_client_full.dot')
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 1024 / 1024:.1f} MB")
    print(f"Peak usage: {peak / 1024 / 1024:.1f} MB")
    tracemalloc.stop()
print("Benchmark completed.")

print("mosquitto__two_client_will_retain.dot")
for i in range(5):
    tracemalloc.start()
    run_benchmark('./BenchmarkDots/mosquitto__two_client_will_retain.dot')
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 1024 / 1024:.1f} MB")
    print(f"Peak usage: {peak / 1024 / 1024:.1f} MB")
    tracemalloc.stop()
print("Benchmark completed.")

print("passport.dot")
for i in range(5):
    tracemalloc.start()
    run_benchmark('./BenchmarkDots/passport.dot')
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 1024 / 1024:.1f} MB")
    print(f"Peak usage: {peak / 1024 / 1024:.1f} MB")
    tracemalloc.stop()
print("Benchmark completed.")

print("tcp_server_ubuntu_trans.dot")
for i in range(5):
    tracemalloc.start()
    run_benchmark('./BenchmarkDots/tcp_server_ubuntu_trans.dot')
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 1024 / 1024:.1f} MB")
    print(f"Peak usage: {peak / 1024 / 1024:.1f} MB")
    tracemalloc.stop()
print("Benchmark completed.")

print("Volksbank_learnresult_MAESTRO_fix.dot")
for i in range(5):
    tracemalloc.start()
    run_benchmark('./BenchmarkDots/Volksbank_learnresult_MAESTRO_fix.dot')
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 1024 / 1024:.1f} MB")
    print(f"Peak usage: {peak / 1024 / 1024:.1f} MB")
    tracemalloc.stop()
print("Benchmark completed.")
