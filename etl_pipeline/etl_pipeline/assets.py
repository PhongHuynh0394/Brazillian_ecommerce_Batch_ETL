from dagster import op, graph

@op
def return_one(context) -> int:
    return 1


@op
def add_one(context, number: int):
    return number + 1


@op
def adder(context, a: int, b: int) -> int:
    return a + b


@graph
def inputs_and_outputs():
    value = return_one()
    a = add_one(value)
    b = add_one(value)
    adder(a, b)
