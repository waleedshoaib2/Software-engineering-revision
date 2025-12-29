def runner_up(array):
    unique = list(set(array))
    unique.sort(reverse =  True)
    runner_up = unique[1]

    return runner_up

array = [33,41,42,42,55,636,66,636]
print(runner_up(array))


