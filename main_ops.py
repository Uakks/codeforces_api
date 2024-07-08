import json


def asc_sort():
    asc = input("Do you want to sort problemset by rating? (y/n) ")
    if asc.lower() == 'y' or asc.lower() == 'yes':
        asc = input("Ascending/Descending? (a/d) ")
        if asc.lower() == 'a':
            asc = 1
        else:
            asc = -1
    else:
        asc = 0
    return asc


def lower_b():
    lower = input("Lower bound for elo: (leave blank to skip)")
    if lower != "":
        lower = int(lower)
    else:
        lower = 0
    return lower


def upper_b():
    upper = input("Upper bound for elo: (leave blank to skip)")
    if upper != "":
        upper = int(upper)
    else:
        upper = 5000
    return upper


def functionality(choice, data):
    if choice == 2:  # problemset, all problems
        problemset = json.loads(data)
        asc = asc_sort()
        lower = lower_b()
        upper = upper_b()
        ls = []
        final = []
        for i, problem in enumerate(problemset["result"]["problems"]):
            problem["solves"] = problemset["result"]["problemStatistics"][i]['solvedCount']
            problem["rating"] = problem.setdefault("rating", 100)
            ls.append([problem['contestId'], problem['index'], problem['name'],
                       problem["rating"], problem['tags'], problem['solves']])
        if asc != 0:
            ls.sort(key=lambda p: (p[3], -p[-1]))
        for problem in ls:
            if lower <= problem[3] <= upper:
                final.append(problem)
        final.sort(key=lambda a: a[3]*asc)
        return final
    elif choice == 4:  # user status
        user_stat = json.loads(data)
        ls = []
        oks = []
        unsolved = []
        solved = {}
        for sol in user_stat["result"]:
            tmp = [sol['id'], sol['contestId'], sol['problem']['name'], sol['problem']['rating'],
                   sol['problem']['tags'], sol['verdict'], sol['passedTestCount']]
            if sol['verdict'] == 'OK':
                oks.append(tmp)
                solved[sol['problem']['name']] = 1
            ls.append(tmp)

        for sol in user_stat["result"]:
            tmp = [sol['id'], sol['contestId'], sol['problem']['name'], sol['problem']['rating'],
                   sol['problem']['tags'], sol['verdict'], sol['passedTestCount']]
            if sol['verdict'] != 'OK' and sol['problem']['name'] not in solved:
                unsolved.append(tmp)

        ls.sort(key=lambda p: (p[3], p[4]))
        oks.sort(key=lambda p: (p[3], p[4]))
        unsolved.sort(key=lambda p: (p[3], p[4]))
        return [ls, oks, unsolved, solved]
