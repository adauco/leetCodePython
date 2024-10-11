import itertools
import csv
import pdb


# Define the lists for protocol, media, apps, and path
nss_path = "/opt/tiger/ftest_lowcode_core/nss_bench_repo/nss_bench"
media_path = "/opt/tiger/ftest_lowcode_core/media_cache/"
post_parameters = " --type rtmp --duration 600 -n 1"
stream_url = "stream_test_01"
protocol = ['HTTPS-FLV']
media = ['H.265', 'H.264', 'Pure Audio']
apps = ['Stage', 'Game', 'Activity']
path = ['Push Row-Source to Pull-TTP source', 'Push TTP-Edge to Pull TTP Post-Processing']

# Generate all possible permutations while following the provided rules
rows = []
counter = 0

for p, m, a, pa in itertools.product(protocol, media, apps, path):
    if 'HTTP' in p and m and 'HTTPS' not in p and m == 'H.265':
        continue
    elif 'RTMPQ' in p and m == 'H.265':
        continue
    else:
        counter += 1
        rows.append([p, m, a, pa, nss_path + ' ' + media_path + m + stream_url + " " + post_parameters])

# Write the result to a CSV file
with open('test_cases.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Protocol', 'Media', 'Apps', 'Path', 'Push Command'])
    writer.writerows(rows)

print(f"Generated {counter} test cases and wrote to 'test_cases.csv'.")