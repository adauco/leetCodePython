import math


def get_permuations(s1, s2):
    answer = []
    x = 0
    for i in s2:
        permuted_list = list(s1)
        y = 0
        for j in permuted_list:
            if permuted_list[y] in s1[x]:
                permuted_list.pop(y)
            y=+1
        x =+1
    return answer

# get_permuations("fa", "fffaf")


# Assign values to variables
play_start_time = 1727842114
last_play_stop_time = 1727842117
start = "1727842114763"
end = "1727842117788"

# Define the lambda function
result = (lambda play_start_time, last_play_stop_time, start, end:
          {"start_diff": math.fabs(play_start_time - float(start)/1000),
           "end_diff": math.fabs(last_play_stop_time - float(end)/1000)}
         )(play_start_time, last_play_stop_time, start, end)

# Output the result
print(result)
# Output: {"start_diff": 1.351, "end_diff": 0.071}