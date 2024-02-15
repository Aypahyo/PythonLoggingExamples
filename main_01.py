
import sys

print("info: main_01") #default is sys.stdout
print("error: main_01", file=sys.stderr)

#python main_01.py > main_01_stdout 2> main_01_stderr