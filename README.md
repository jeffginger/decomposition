# decomposition
Generic code for a Lagrangian decomposition problem using pulp

The purpose of this code is to test improvements made to the pulp resolve function in a forked pulp repository.

Currently it is rather difficult to use pulp for decomposition problems where many small linear programming problems are to be solved iteratively due to an lp being written or a translation between pulp and API data structures. A workaround is provided as comments to the following issue: https://github.com/coin-or/pulp/issues/497
