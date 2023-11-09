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
    !FUCKING DIE IN A  F I R E ! :>>>
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

"""
def initializeglobalvars():
    
        #I HAD TO WRITE THIS BECAUSE THE FUCKING LANGUAGE HAS NEVER AND I MEAN N E V E R SEEN A FUCKING GLOBAL VARIABLE
        #IN ITS ENTIRE 30 PLUS YEARS LIFE CYCLE FUCKING PIECE OF CRAP FUKC YOU FUCKING NORWEGIANS BITCH ASS MFS!!!!!!

    try:
        global K_DOMAIN_PATH
        K_DOMAIN_PATH = "domainpath"
        global K_MAD_PATH
        K_MAD_PATH = "madpath"
        global K_DOWNWARD_PATH
        K_DOWNWARD_PATH = "downwardpath"
        global K_PREFIXFORPOSIT
        K_PREFIXFORPOSIT = ""
        # this guy checks for them fucking errors. If it finds a runtime error caused by the user, IT FUCKING QUITS. Deal with it.
        global K_ERRORFLAG
        K_ERRORFLAG = 0
        print("global vars initialized successfully")
    except:
        print("global vars not initialized. start praying.")

        GUESS WHAT? IT DOESN'T FUCKING WORK :>
"""


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
    K_ERRORFLAG = 0
    inputs = []
    adjac = []
    types = []
    objects = ["", ""]
    # 0. get args phase

    arguments = parseargs()
    # 0.1. Check for major fuckups.
    # then the user should wanna go ahead an input the layout for himself. Very fun!
    if arguments.layout == 'NONE' and arguments.layoutfile == 'NONE':
        inp: str
        while (True):
            inp = input()
            if inp == -1 or inp == "-1":
                break
            inputs.append(inp)
        # if all goes well, this should not make me wanna puke blood.
        matrixsize = len(inputs[0])

    # OR
    # 0.2. CHECK FOR DOUBLE INPUT!
    # PRETTY PLEASE, let at least one of these be a NONE.
    if arguments.layout != 'NONE' and arguments.layoutfile != 'NONE':
        print("Double input! Averting erratic behaviour!")
        K_ERRORFLAG = 1  # Cant fucking handle you can't decide to give an input file or an input arg. DONT FUCKING USE BOTH!
        quit()           # meaning a major fuckup :)

    if K_ERRORFLAG == 0:  # if there's no fuckup, move on
        # 1. input phase!
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
                    adjac.append("(adj x" + str(actual[0]) + " x" + str(
                        up[0]) + " y" + str(actual[1]) + " y" + str(up[1]) + " )")
                if not down[0] > matrixsize:  # meaning it doesn't go beyond borders!
                    adjac.append("(adj x" + str(actual[0]) + " x" + str(
                        down[0]) + " y" + str(actual[1]) + " y" + str(down[1]) + " )")
                if not left[1] < 0:  # Same as up
                    adjac.append("(adj x" + str(actual[0]) + " x" + str(
                        left[0]) + " y" + str(actual[1]) + " y" + str(left[1]) + " )")
                if not right[1] > matrixsize:  # Same as down
                    adjac.append("(adj x" + str(actual[0]) + " x" + str(
                        right[0]) + " y" + str(actual[1]) + " y" + str(right[1]) + " )")
                # TODO! Get domain and code actual language so it works!!!!!!!!!!

        # GETTING TYPES!
        i = -1
        j = -1
        for line in inputs:
            i += 1  # this takes care of telling us where the fuck we are!
            for char in line:
                j += 1  # this too!!!
                if char == 'D':  # this does nothing. VERY FUN!
                    # types.append("((point[" + str(i) + "," + str(j) + "])is off)")
                    pass
                if char == 'd':
                    # types.append("((point[" + str(i) + "," + str(j) + "])is off)")
                    types.append(
                        "( is-broken x" + str(i) + " y" + str(j) + " )")
                if char == 'L':
                    types.append("( is-lit x" + str(i) + " y" + str(j) + " )")
                if char == 'l':
                    types.append("( is-lit x" + str(i) + " y" + str(j) + " )")
                    types.append(
                        "( is-broken x" + str(i) + " y" + str(j) + " )")

        # CREATING OBJECTS BASED ON MATRIX SIZE
        for i in range(matrixsize):
            objects[0] += " x" + str(i)
            objects[1] += " y" + str(i)
            pass
        objects[0] += "- PosX"
        objects[1] += "- PosY"

        # checking checking checking! see if it works! if it does REMEMBER TO COMMENT IT FOR THE USER'S SAKE! and performance :>>>
        print(inputs)
        print(adjac)
        print(types)
        print(objects)

        # THIS IS THE LAZIEST FUCKING PIECE OF TRASH I COULD THINK OF! but. It should. SHOULD. work. :>
        # start is the head of the file and starts the stuff.
        head1 = """
        (define (problem p01) (:domain lights-out)
        (:objects
        """
        # x0 x1 x2 - PosX
        # y0 y1 y2 - PosY
        head2 = """   
        )

        (:init
        """
        # this is the end.
        tail = """
        )
            (:goal (and
                ( success )
                
                ; ( forall ( ?x - PosX )
                ;     ( forall ( ?y - PosY )
                ;         ( not ( is-lit ?x ?y ) )
                ;     )
                ; )
            )))
        """
        for obj in objects:
            head1 += "\n" + obj
        for adj in adjac:
            head2 += "\n" + adj
        for ty in types:
            head2 += "\n" + ty
        full = head1 + head2 + tail
        print(full)
        # NOW WRITE SOMETHING TO WRITE THIS DOWN TO A FILE LAZY PIECE OF SHIT.


if __name__ == "__main__":
    """
    putdomain()
    problemcreator()
    callsolver()
    parsesolution()
    finish!
    activate each function accordingly to test and debug!
    """
    problemcreator()


"""
tail commentary!
    in brazilian portuguese, stomachache is called diarreia. 
    To comment someone is shitting blood, you'd say goreia (gore + diarreia).
    the more you know!
"""
