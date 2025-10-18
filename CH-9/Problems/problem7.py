with open("CH-9/Problems/log.txt") as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    if("Python" in line):
        print(f"It's in the log file on the line {lineno}")
        break
    lineno += 1

else:
    print("No python is not in log file")