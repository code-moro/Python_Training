def decorator_with_args(decorator_args1, decorator_args2, decorator_args3):
    def decorator(func):
        def wrapper(function_args1, function_args2, function_args3):
            print("The wrapper can access all the variables\n"
                  "\t from the decorator maker:{0} {1} {2} \n"
                  "\t from the function call:{3} {4} {5} \n"
                  "and pass them into decorator function".format(decorator_args1, decorator_args2, decorator_args3,
                                                                 function_args1, function_args2, function_args3))
            return func(function_args1, function_args2, function_args3)

        return wrapper

    return decorator


pandas = "Pandas"


@decorator_with_args(pandas, "Numnnj", "gudehj")
def actual_function(function_args1, function_args2, function_args3):
    print("\n This is decorated function and it only knows about its arguments {0} {1} {2}".format(function_args1,
                                                                                                   function_args2,
                                                                                                   function_args3))


# calling
actual_function("prajakta", "Prakash", "Shewale")
