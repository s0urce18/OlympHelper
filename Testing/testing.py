from typing import Any, Callable

class Test:
    
    __func: Callable[..., Any] = None
    __params: list = []
    __results: list = []

    def __init__(self) -> None:
        pass

    def set_funcion(self, func: Callable[..., Any]) -> None:
        self.__func = func

    def add_test_cases(self, *args: list) -> None:
        for a in args:
            self.__params.append(a[0])
            self.__results.append(a[1])
    
    def test_all(self) -> bool:
        for i in range(0, len(self.__params)):
            if self.__func(*self.__params[i]) != self.__results[i]:
                return False
        return True

    def test(self, func: Callable[..., Any], args: list, res: Any) -> bool:
        return func(*args) == res

    def find_valid(self) -> list:
        result: list = []
        for i in range(0, len(self.__params)):
            try:
                if self.__func(*self.__params[i]) == self.__results[i]:
                    result.append([[*self.__params[i]], self.__results[i]])
            except:
                pass
        return result

    def find_invalid(self) -> list:
        result: list = []
        for i in range(0, len(self.__params)):
            try:
                if self.__func(*self.__params[i]) != self.__results[i]:
                    result.append([[*self.__params[i]], self.__results[i]])
            except:
                pass
        return result

    def find_failed(self) -> list:
        result: list = []
        for i in range(0, len(self.__params)):
            try:
                self.__func(*self.__params[i])
            except:
                result.append([[*self.__params[i]], self.__results[i]])
        return result

    def print_results(self) -> None:
        print("Function: {}".format(self.__func.__name__))
        totaly: dict = {"valid": 0, "invalid": 0, "failed": 0}
        for i in range(0, len(self.__params)):
            try:
                if self.__func(*self.__params[i]) != self.__results[i]:
                    print("Arguments: {}, Correct result: {}, Desicion: INVALID".format([*self.__params[i]], self.__results[i]))
                    totaly["invalid"] += 1
                else:
                    print("Arguments: {}, Correct result: {}, Desicion: VALID".format([*self.__params[i]], self.__results[i]))
                    totaly["valid"] += 1
            except Exception as err:
                    print("Arguments: {}, Correct result: {}, Desicion: FAILED ( {} )".format([*self.__params[i]], self.__results[i], err))
                    totaly["failed"] += 1
        print("Totaly: {} VALID, {} INVALID, {} FAILED".format(totaly["valid"], totaly["invalid"], totaly["failed"]))