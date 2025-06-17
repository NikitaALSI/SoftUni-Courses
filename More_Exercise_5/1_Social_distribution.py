def social_distribution(some_list, minimum):
    if len(some_list) * minimum > sum(some_list):
        return "No equal distribution possible"
    while any(map(lambda x: x < minimum, some_list)):
        new_list = some_list[:]
        some_list[some_list.index(min(some_list))] += (minimum - min(some_list))
        some_list[some_list.index(max(some_list))] -= (minimum - min(new_list))
    return some_list


wealth_list = list(map(int, input().split(", ")))
minimum_wealth = int(input())
print(social_distribution(wealth_list, minimum_wealth))
