import importlib

modules = [
    "a01_make_solar_cell",
    "a02_make_PV_module",
    "a03_make_tandem_cell",
    "a04_make_PV_string",
    "a05_simple_cell_compared_to_LT_spice",
    "a06_simple_module_compared_to_LT_spice",
    "a07_simple_uniform_module_compared_to_LT_spice",
    "a08_simple_string_compared_to_LT_spice",
    "a09_simple_uniform_string_compared_to_LT_spice",
    "a10_simple_parallel_strings_compared_to_LT_spice",
]

def test_all_examples():
    """
    Pytest entry point: run all example modules' run_test() functions.

    Any assertion or exception inside those run_test() functions will
    cause this test to fail and thus fail CI.
    """
    for i, name in enumerate(modules):
        print(f"\n-------------------------------\nRunning Test {i+1}: {name}\n")
        mod = importlib.import_module(name)
        mod.run_test()

if __name__ == "__main__":
    # Keep the old CLI behavior for running locally:
    test_all_examples()