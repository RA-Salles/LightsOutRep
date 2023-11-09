"""
written by badcodelocust

what is this
    this is a problem generator to be used with main to solve lights out's problems and stuff
what it does (asof 07112023)
    NOTHING! But uglier (asof091123)
what it should do
    create domain file, write it down
    create problem based on args OR a file. preferably a file
    call solver and wait for a solution
    parse solution
    FUCKING DIE IN A FIRE!
"""

import sys
import argparse
import numpy as np
K_DOMAIN_PATH = "domainpath"
K_MAD_PATH = "madpath"
K_DOWNWARD_PATH = "downwardpath"
K_PREFIXFORPOSIT = ""
# this guy checks for them fucking errors. If it finds a runtime error caused by the user, IT FUCKING QUITS. Deal with it.
K_ERRORFLAG = 0


def parseargs():
    parser = argparse.ArgumentParser(
        usage="use this program to generate problem files for the lights out domain. provide either an inline layout or a layout file.")
    parser.add_argument("--layout", type=str, default="NONE",
                        help="Layout argument. input a layout for the problem")
    parser.add_argument("--layoutfile", type=str, default="NONE",
                        help="Layout file. Separate lines with linebreak")
    parser.add_argument("--outputname", type=str, default="pf01.pddl",
                        help="Name for the problem. End the name with '.pddl', else there shall be bloodshed")
    return parser.parse_args()


def putdomain():  # this function writes the domain to the root of execution. Then it kills all of your lineage. Very fun!!!!
    domain = """
    insert a domain here, will ya?
    """


def callsolver():  # this guy SHOULD call the solver with the problem generated.
    arguments = parseargs()
    problemfile = arguments.outputname  # this should work.
    pass


def problemcreator():
    # 0. get args phase
    arguments = parseargs()
    # 0.1. Check for major fuckups.
    if arguments.layout == 'NONE' and arguments.layoutfile == 'NONE':
        print("No layout or layout file! Averting erratic behaviour!")
        # well, we can't generate an output file if there's no input...
        K_ERRORFLAG = 1
        quit()  # meaning a major fuckup.
    # OR
    # 0.2. CHECK FOR DOUBLE INPUT!
    # PRETTY PLEASE, let at least one of these be a NONE.
    if arguments.layout != 'NONE' and arguments.layoutfile != 'NONE':
        print("Double input! Averting erratic behaviour!")
        K_ERRORFLAG = 1  # Cant fucking handle you can't decide to give an input file or an input arg. DONT FUCKING USE BOTH!
        quit()          # meaning a major fuckup :)

    else:  # if there's no fuckup, move on
        # 1. input phase!
        inputs = []
        adjac = []
        types = []
        if arguments.layoutfile != 'NONE':
            with open(arguments.layoutfile, "rb") as file:
                for line in file:
                    inputs.append(line)
            matrixsize = len(inputs)

        if arguments.layout != 'NONE':
            # remember to comment this when implemented
            print("not implemented! Write your layout in a .txt and pass it here :>")
            # as it is always square perfect, this SHOULD work. Else i WILL kms :>
            matrixsize = int(np.sqrt(len(arguments.layout)))
            for i in range(matrixsize):
                # which SHOULD generate a very beauteefool [[DdLl],[DdLl],[DdLl],[DdLl]] on a 4-square.
                inputs.append(
                    arguments.layout[0+(matrixsize*i): matrixsize+(matrixsize*i)])

        # ADJUSTING FOR ADJACENTS AND STUFF...
        for i in range(matrixsize):
            for j in range(matrixsize):  # loops through all possible matrix positions
                actual = [i, j]  # this is the actual position.
                up = actual
                up[0] -= 1  # meaning it gets line up.
                left = actual
                left[1] -= 1  # gets one column less
                down = actual
                down[0] += 1  # and so on!
                right = actual
                right[1] += 1  # ...
                # NOW WE CHECK THIS STUFF!
                # these checks means we only register if it does !NOT! goes beyond borders
                if not up[0] < 0:  # meaning it doesn't go into negatives!
                    adjac.append("( point([" + str(actual[0]) + str(
                        actual[1]) + "]) is adjacent to point(~[]" + str(up[0]) + "," + str(up[1]) + "]))")
                if not down[0] > matrixsize:  # meaning it doesn't go beyond borders!
                    adjac.append("( point(" + str(actual[0]) + str(
                        actual[1]) + ") is adjacent to point(" + str(down[0]) + str(down[1]) + "))")
                if not left[1] < 0:  # Same as up
                    adjac.append("( point(" + str(actual[0]) + str(
                        actual[1]) + ") is adjacent to point(" + str(left[0]) + str(left[1]) + "))")
                if not right[1] > matrixsize:  # Same as down
                    adjac.append("( point(" + str(actual[0]) + str(
                        actual[1]) + ") is adjacent to point(" + str(right[0]) + str(right[1]) + "))")
                # TODO! Get domain and code actual language so it works!!!!!!!!!!

        # GETTING TYPES!
        i = 0
        j = 0
        for line in inputs:
            i += 1  # this takes care of telling us where the fuck we are!
            for char in line:
                j += 1  # this too!!!
                if char == 'D':
                    types.append(
                        "((point[" + str(i) + "," + str(j) + "])is off)")
                if char == 'd':
                    types.append(
                        "((point[" + str(i) + "," + str(j) + "])is off)")
                    types.append(
                        "((point[" + str(i) + "," + str(j) + "])is broken)")
                if char == 'L':
                    types.append(
                        "((point[" + str(i) + "," + str(j) + "])is on)")
                if char == 'l':
                    types.append(
                        "((point[" + str(i) + "," + str(j) + "])is on)")
                    types.append(
                        "((point[" + str(i) + "," + str(j) + "])is broken)")
        # checking checking checking! see if it works! if it does REMEMBER TO COMMENT IT FOR THE USER'S SAKE!
        print(input)
        print(adjac)
        print(types)

        # THIS IS THE LAZIEST FUCKING PIECE OF TRASH I COULD THINK OF!
        # start is the head of the file and starts the stuff.
        start = """
        Insert here a head for the problem. PLEASE
        """  # TODO! Get an actual model here!
        # this is the end.
        tail = """
        Insert here a tail. It should simply have a goal and the remainder ")" stuff...
        """
        for adj in adjac:
            start.append(adj)
        for ty in types:
            start.append(ty)


if __name__ == "__main__":
    """
    putdomain()
    problemcreator()
    callsolver()
    parsesolution()
    finish!
    activate each function accordingly to test and debug!
    """

    pass
