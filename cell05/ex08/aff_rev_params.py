import sys

txt = sys.argv
if len(sys.argv) > 2:
    for i in reversed(txt[1:]):
        print(i)
else:
    print("none")