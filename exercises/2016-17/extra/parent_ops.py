def min_cost(i, j, vals, ops):
    """
    :param i: int
        Start expr here
    :param j: int
        End expr here
    :param vals: list of numbers
        List of values
    :param ops: list of str
        List of ops between values
    :return: float
        Minimum cost of expression [i ... j]
    """

    if (i == j) and (i in range(len(vals))) and (j in range(len(vals))):
        return vals[i], "(" + str(vals[i]) + ")"

    if (i > j - 1) or (i not in range(len(ops))) or (j - 1 not in range(len(ops))):
        return None, ""

    if (i == j - 1) and (i in range(len(vals))) and (j not in range(len(vals))):
        if ops[j - 1] == "+":
            return vals[i] + vals[j], "(" + str(vals[i]) + " + " + str(vals[j]) + ")"
        else:
            return vals[i] * vals[j], "(" + str(vals[i]) + " x " + str(vals[j]) + ")"

    sol, expr = None, ""
    if ops[i] == ops[j - 1] == "+":
        prev_cost, sol = min_cost(i + 1, j - 1, vals, ops)
        if prev_cost is None:
            sol, expr = vals[i] + vals[j], "(" + str(vals[i]) + " + " + str(vals[j]) + ")"
        else:
            sol, expr = prev_cost + vals[i] + vals[j], "(" + str(vals[i]) + " + " + str(sol) + " + " + str(vals[j]) + ")"
    elif ops[i] == ops[j - 1] == "x":
        prev_cost, sol = min_cost(i + 1, j - 1, vals, ops)
        if prev_cost is None:
            sol, expr = vals[i] * vals[j], "(" + str(vals[i]) + " x " + str(vals[j]) + ")"
        else:
            sol, expr = vals[i] * prev_cost * vals[j], "(" + str(vals[i]) + " x " + str(sol) + " x " + str(vals[j]) + ")"
    else:  # bounds ops are + and x
        if ops[i] == "+":
            adding_sol, sol = min_cost(i + 1, j, vals, ops)
            if adding_sol is None:
                adding_sol = vals[i]
                adding_str_sol = "(" + str(vals[i]) + ")"
            else:
                adding_sol += vals[i]
                adding_str_sol = "(" + str(vals[i]) + " + " + str(sol) + ")"

            multi_sol, sol = min_cost(i, j - 1, vals, ops)
            if multi_sol is None:
                multi_sol = vals[j]
                multi_str_sol = "(" + str(vals[j]) + ")"
            else:
                multi_sol *= vals[j]
                multi_str_sol = "(" + str(vals[i]) + " * " + str(sol) + ")"
        else:
            adding_sol, sol = min_cost(i, j - 1, vals, ops)
            if adding_sol is None:
                adding_sol = vals[j]
                adding_str_sol = "(" + str(vals[j]) + ")"
            else:
                adding_sol += vals[j]
                adding_str_sol = "(" + str(sol) + " + " + str(vals[j]) + ")"

            multi_sol, sol = min_cost(i + 1, j, vals, ops)
            if multi_sol is None:
                multi_sol = vals[i]
                multi_str_sol = "(" + str(vals[i]) + ")"
            else:
                multi_sol *= vals[i]
                multi_str_sol = "(" + str(sol) + " * " + str(vals[i]) + ")"
            
        if min(adding_sol, multi_sol) == adding_sol:
            sol, expr = adding_sol, adding_str_sol
        else:
            sol, expr = multi_sol, multi_str_sol

    return sol, expr


def main():
    values = [7, 10, 2, 4]
    operations = ["+", "x", "+"]
    sol_cost, how_cost = min_cost(0, len(values) - 1, values, operations)
    
    print("minimum cost is", sol_cost)
    print("via", how_cost)


if __name__ == '__main__':
    main()
