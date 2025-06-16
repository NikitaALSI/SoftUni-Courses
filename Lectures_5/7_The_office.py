happiness_list = list(map(int, input().split()))
improvement_factor = int(input())
happiness_list = list(map(lambda x: x * improvement_factor, happiness_list))
average = sum(happiness_list) / len(happiness_list)
happy_count = len(list(filter(lambda x: x >= average, happiness_list)))
if happy_count >= len(happiness_list)/2:
    print(f"Score: {happy_count}/{len(happiness_list)}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{len(happiness_list)}. Employees are not happy!")