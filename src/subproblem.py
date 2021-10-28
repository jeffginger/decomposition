import pulp as pl

class SubProblem():

    def __init__(self) -> None:
        _local_constraints = None
        _local_costs = None
        _local_dualised_variables = None
        _current_objective_function = None