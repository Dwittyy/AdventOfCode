from time import perf_counter_ns
from colorama import Fore
  
def timer(function):
    def wrap_function(*args, **kwargs):
        start = perf_counter_ns()
        result = function(*args, **kwargs)
        end = perf_counter_ns()
        runtime = (end - start) / (10 ** 6)
        print(f'{Fore.CYAN}Executed in {Fore.GREEN}{runtime:.4f}ms{Fore.RESET}')
        return result
    return wrap_function