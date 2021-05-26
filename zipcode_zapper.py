f = open("zipcodes.txt", "r")
content = f.read()

content_list = content.split()
f.close()
for i in range(0, len(content_list)):
    if "-" in content_list[i]:
        content_list[i] = content_list[i].replace("---", "00...")
        content_list[i] += "99"
    if "*" in content_list[i]:
        content_list[i] = content_list[i].replace("*", "")
    if "+" in content_list[i]:
        content_list[i] = content_list[i].replace("+", "")
    if len(content_list[i]) == 3:
        content_list[i] = content_list[i] + "00" + "..." + content_list[i] + "99"

iterator = iter(content_list)
values = list(zip(iterator, iterator))
print(content_list)
print(values)

organized_dict = {}
zone_integers = []

for i in range(0, len(values)):
    organized_dict[int(values[i][1])] = []
    if int(values[i][1]) not in zone_integers:
        zone_integers.append(int(values[i][1]))

for i in range(0, len(values)):
    organized_dict[int(values[i][1])].append(values[i][0])

zone_integers = sorted(zone_integers)

print(organized_dict)
print(zone_integers)

zone_output = ""

for i in zone_integers:
    zone_output += str(i)
    zone_output += "\n"
    zone_output += "\n".join(organized_dict[i])
    zone_output += "\n"

print(zone_output)