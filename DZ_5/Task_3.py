import timeit
from  typing import Callable

from b_m_s import boyer_moore_search
from k_m_p import kmp_search
from r_k_s import rabin_karp_search

def read_file(filename):
    with open(filename, 'r', encoding='cp1251') as f:
        return f.read()


def benchmark(func: Callable, text_: str, pattern_: str):
    setup_code = f"from __main__ import {func.__name__}"
    stmt = f"{func.__name__}(text, pattern)"
    return timeit.timeit(stmt=stmt, setup=setup_code, globals={'text': text_, 'pattern': pattern_}, number=10)


if __name__ == '__main__':
    text_1 = read_file(r"..\goit-algo-hw-05\DZ_5\article_1.txt")
    text_2 = read_file(r"..\goit-algo-hw-05\DZ_5\article_1.txt")
    real_pattern = "логарифмічний пошук"
    fake_pattern = "Не всі, хто блукає, загублені."

    results_1 = []
    for pattern in (real_pattern, fake_pattern):
        time = benchmark(boyer_moore_search, text_1, pattern)
        results_1.append((boyer_moore_search.__name__, pattern, time))
        time = benchmark(kmp_search, text_1, pattern)
        results_1.append((kmp_search.__name__, pattern, time))
        time = benchmark(rabin_karp_search, text_1, pattern)
        results_1.append((rabin_karp_search.__name__, pattern, time))
    title = f"{'Алгоритм':<30} | {'Підрядок':<30} | {'Час виконання, сек'}"
    print(title)
    print("-" * len(title))
    for result in results_1:
        print(f"{result[0]:<30} | {result[1]:<30} | {result[2]}")
        
    print("\nРезультати пошуку в другій статті:")

    results_2 = []
    for pattern in (real_pattern, fake_pattern):
        time = benchmark(boyer_moore_search, text_2, pattern)
        results_2.append((boyer_moore_search.__name__, pattern, time))
        time = benchmark(kmp_search, text_2, pattern)
        results_2.append((kmp_search.__name__, pattern, time))
        time = benchmark(rabin_karp_search, text_2, pattern)
        results_2.append((rabin_karp_search.__name__, pattern, time))
    title = f"{'Алгоритм':<30} | {'Підрядок':<30} | {'Час виконання, сек'}"
    print(title)
    print("-" * len(title))
    for result in results_2:
        print(f"{result[0]:<30} | {result[1]:<30} | {result[2]}")
        
print("\nДослідження показало що алгоритм Бойера-Мура найшвидший")
