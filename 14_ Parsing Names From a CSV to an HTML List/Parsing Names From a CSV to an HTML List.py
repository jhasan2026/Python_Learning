
import csv

html_output = ''
names = []

# With List approch
# with open('patrons.csv','r') as dat_files:
#     csv_data = csv.reader(dat_files)
#
#     # for item in csv_data:
#     #     print(item)
#
#     # we dont want header or first line on bad data
#     next(csv_data)
#     next(csv_data)
#
#     for line in csv_data:
#         if line[0] == "No Reward":
#             break
#         names.append(f"{line[0]} {line[1]}")

# for name in names:
#     print(name)







# Dictionary approach
with open('patrons.csv','r') as dat_files:
    csv_data = csv.DictReader(dat_files)

    # we dont want first line on bad data

    next(csv_data)

    for line in csv_data:
        if line['FirstName'] == "No Reward":
            break
        names.append(f"{line['FirstName']} {line['LastName']}")




html_output += f'<p> There are currently {len(names)} public contributors. Thank You!</p>'
html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)