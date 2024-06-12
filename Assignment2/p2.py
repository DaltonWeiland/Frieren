import importlib.util

# Found this way to import modules. Works But the other method
# is probably better
spec = importlib.util.spec_from_file_location("p2mod", "./module/module_1/p2mod.py")

func = importlib.util.module_from_spec(spec)        
spec.loader.exec_module(func)


def main():
    for i in range(10):
        print(func.ShowRecommendations(i))


main()