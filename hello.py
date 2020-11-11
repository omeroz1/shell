import sys

if len(sys.argv) > 1:
    print("hello " + sys.argv[1], end="")
    # if the input contains a name besides 'hello', it will print also the name.
else:
    print("hi omer", end="")
    # if the input is 'hello', it will print "hi omer".
