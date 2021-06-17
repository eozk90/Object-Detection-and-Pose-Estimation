# http://exampleprogramming.com/specialvars.html

def stevens_hoboken():
    # whenever python runs a file at first it sets a few special variables
    # when python runs a python file directly it sets this name variable equal to main
    print("First modules name: {}".format(__name__))


# Is this file being run directly by Python or is it being imported?
if __name__ == '__main__':
    stevens_hoboken()

# if __name__ == '__main__':
#     print("Run directly")
# else:
#     print("Run from import")
