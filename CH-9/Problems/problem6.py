with open("CH-9/Problems/log.txt") as f:
    con = f.read()

if("Python" in con):
    print("It's in the log file")
else:
    print("No python is not in log file")