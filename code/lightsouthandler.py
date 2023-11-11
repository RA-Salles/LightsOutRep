"""
    written by badcodelocust, aprxl

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
import os
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
    (define (domain lights-out)

    (:requirements :strips :fluents :typing :conditional-effects :negative-preconditions :equality :disjunctive-preconditions)

    (:types
        ;; Corresponds to the X and Y coordenates on the game's map.
        PosX
        PosY
    )

    (:constants )

    (:predicates
        ;; Used to indicate if a specific location is lit up.
        ( is-lit ?x - PosX ?y - PosY )

        ;; Used to indicate if a specific location has a broken switch.
        ( is-broken ?x - PosX ?y - PosY )

        ;; Represents hows the map is organized.
        ( adj ?x ?x2 - PosX ?y ?y2 - PosY )

        ;; A flag that is active whenever the game is done.
        ( success )
    )

    ;; Responsible for inverting the tiles states around this tile, including itself.
    (:action press-lit
        :parameters ( ?x - PosX ?y - PosY )
        :precondition (and
            ( is-lit ?x ?y )
            ( not ( is-broken ?x ?y ) )
        )
        :effect (and
            ;; Dims the original tile.
            ( not ( is-lit ?x ?y ) )

            ;; Loops for each X and Y coordinates.
            (forall (?xIt - PosX)
                (forall (?yIt - PosY)
                    ;; Checks if this tile is adjacent to the original tile.
                    (when ( and
                        ( or ( adj ?x ?xIt ?y ?yIt ) ( adj ?xIt ?x ?yIt ?y ) )
                        ( is-lit ?xIt ?yIt )
                    )
                        ( not ( is-lit ?xIt ?yIt ) )
                    )
                )
            )

            (forall (?xIt - PosX)
                (forall (?yIt - PosY)
                    ;; Checks if this tile is adjacent to the original tile.
                    (when ( and
                        ( or ( adj ?x ?xIt ?y ?yIt ) ( adj ?xIt ?x ?yIt ?y ) )
                        ( not (is-lit ?xIt ?yIt ) )
                    )
                        ( is-lit ?xIt ?yIt )
                    )
                )
            )
        )
    )

    (:action press-unlit
        :parameters ( ?x - PosX ?y - PosY )
        :precondition (and
            ( not ( is-lit ?x ?y ) )
            ( not ( is-broken ?x ?y ) )
        )
        :effect (and
            ;; Lights up the original tile.
            ( is-lit ?x ?y )

            ;; Loops for each X and Y coordinates.
            (forall (?xIt - PosX)
                (forall (?yIt - PosY)
                    ;; Checks if this tile is adjacent to the original tile.
                    (when ( and
                        ( or ( adj ?x ?xIt ?y ?yIt ) ( adj ?xIt ?x ?yIt ?y ) )
                        ( is-lit ?xIt ?yIt )
                    )
                        ( not ( is-lit ?xIt ?yIt ) )
                    )
                )
            )

            (forall (?xIt - PosX)
                (forall (?yIt - PosY)
                    ;; Checks if this tile is adjacent to the original tile.
                    (when ( and
                        ( or ( adj ?x ?xIt ?y ?yIt ) ( adj ?xIt ?x ?yIt ?y ) )
                        ( not (is-lit ?xIt ?yIt ) )
                    )
                        ( is-lit ?xIt ?yIt )
                    )
                )
            )
        )
    )

    ;; Also inverts tile states, however, it ignores the clicked tile.
    (:action press-lit-broken
        :parameters ( ?x - PosX ?y - PosY )
        :precondition (and
            ( is-lit ?x ?y )
            ( is-broken ?x ?y )
        )
        :effect (and
            ;; Loops for each X and Y coordinates.
            (forall (?xIt - PosX)
                (forall (?yIt - PosY)
                    ;; Checks if this tile is adjacent to the original tile.
                    (when ( and
                        ( or ( adj ?x ?xIt ?y ?yIt ) ( adj ?xIt ?x ?yIt ?y ) )
                        ( is-lit ?xIt ?yIt )
                    )
                        ( not ( is-lit ?xIt ?yIt ) )
                    )
                )
            )

            (forall (?xIt - PosX)
                (forall (?yIt - PosY)
                    ;; Checks if this tile is adjacent to the original tile.
                    (when ( and
                        ( or ( adj ?x ?xIt ?y ?yIt ) ( adj ?xIt ?x ?yIt ?y ) )
                        ( not (is-lit ?xIt ?yIt ) )
                    )
                        ( is-lit ?xIt ?yIt )
                    )
                )
            )
        )
    )

    ;; Also inverts tile states, however, it ignores the clicked tile.
    (:action press-unlit-broken
        :parameters ( ?x - PosX ?y - PosY )
        :precondition (and
            ( not ( is-lit ?x ?y ) )
            ( is-broken ?x ?y )
        )
        :effect (and
            ;; Loops for each X and Y coordinates.
            (forall (?xIt - PosX)
                (forall (?yIt - PosY)
                    ;; Checks if this tile is adjacent to the original tile.
                    (when ( and
                        ( or ( adj ?x ?xIt ?y ?yIt ) ( adj ?xIt ?x ?yIt ?y ) )
                        ( is-lit ?xIt ?yIt )
                    )
                        ( not ( is-lit ?xIt ?yIt ) )
                    )
                )
            )

            (forall (?xIt - PosX)
                (forall (?yIt - PosY)
                    ;; Checks if this tile is adjacent to the original tile.
                    (when ( and
                        ( or ( adj ?x ?xIt ?y ?yIt ) ( adj ?xIt ?x ?yIt ?y ) )
                        ( not (is-lit ?xIt ?yIt ) )
                    )
                        ( is-lit ?xIt ?yIt )
                    )
                )
            )
        )
    )

    ;; Responsible for setting the flag that says the game is complete.
    ;; This is our goal for every problem.
    (:action done
        :parameters ( )
        :precondition (and
            (forall ( ?x - PosX )
                (forall ( ?y - PosY )
                    ( not ( is-lit ?x ?y ) )
                )
            )
        )
        :effect (and
            ( success )
        )
    )

    )
    """
    with open("domain.pddl", "w") as f:  # as simple as that. ultrafun!
        f.write(domain)
        f.close()


def callsolver():  # this guy SHOULD call the solver with the problem generated.
    import subprocess
    # added solverpath :>
    solverpath = "/tmp/dir/software/planners/madagascar/Mp"
    try:
        home_dir = os.path.expanduser("~")
        solverhandler = subprocess.run(
            [solverpath, "domain.pddl", "problem.pddl", "-o", format(f"{home_dir}/output.txt")])

    except:
        print("solver not found")


def problemcreator():
    # this serves to fix an annoying bug because it seems the function is unable to access the definition up there.
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
                if i > 0:
                    adjac.append(f"(adj x{i} x{i - 1} y{j} y{j})")

                if i < matrixsize - 1:
                    adjac.append(f"(adj x{i} x{i + 1} y{j} y{j})")

                if j > 0:
                    adjac.append(f"(adj x{i} x{i} y{j} y{j - 1})")

                if j < matrixsize - 1:
                    adjac.append(f"(adj x{i} x{i} y{j} y{j + 1})")

        # GETTING TYPES!
        # print(inputs)
        # print(matrixsize)
        i = -1
        j = -1
        for line in inputs:
            j += 1  # this takes care of telling us where the fuck we are!
            # print(f"Line ({i}): {line}")  # debug line
            for char in line:
                i += 1  # this too!!!
                # print(f"Char ({i}, {j}): {char}")  # this also
                if char == 'D':  # this does nothing. VERY FUN!
                    pass
                if char == 'd':
                    types.append(f"(is-broken x{i} y{j})")
                if char == 'L':
                    types.append(f"(is-lit x{i} y{j})")
                if char == 'l':
                    types.append(f"(is-lit x{i} y{j})")
                    types.append(f"(is-broken x{i} y{j})")
            i = -1

        # CREATING OBJECTS BASED ON MATRIX SIZE
        for i in range(matrixsize):
            objects[0] += " x" + str(i)
            objects[1] += " y" + str(i)
            pass
        objects[0] += " - PosX"
        objects[1] += " - PosY"

        # checking checking checking! see if it works! if it does REMEMBER TO COMMENT IT FOR THE USER'S SAKE! and performance :>>>
        # print(inputs)
        # print(adjac)
        # print(types)
        # print(objects)

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
        # print(full)
        # NOW WRITE SOMETHING TO WRITE THIS DOWN TO A FILE LAZY PIECE OF SHIT.
        with open("problem.pddl", "w") as f:  # as simple as that. ultrafun!
            f.write(full)
            f.close()


def parsesolution():
    crudesolution = []
    formatted = []
    # try:
    with open("output.txt", "rb") as f:
        for line in f:
            line = str(line)
            if line.find("done") == -1:
                while line.find(",") != -1:
                    xposit = line.find('x')
                    cposit = line.find(",")
                    end = line.find(")")
                    firstnum = line[xposit+1:cposit]
                    secondnum = line[cposit+2:end]
                    formatted.append(
                        str("(" + str(firstnum) + ", " + str(secondnum) + ")"))
                    line = line.replace("x", "", 1)
                    line = line.replace(",", "", 1)
                    line = line.replace(")", "", 1)
    # except:
        # print("output.txt not found. Verify if solver is running or smth")
    full = ";"
    full = full.join(formatted)
    print(full)


if __name__ == "__main__":
    """
    putdomain()
    problemcreator()
    callsolver()
    parsesolution()
    finish!
    activate each function accordingly to test and debug!
    """
    putdomain()
    problemcreator()
    callsolver()
    parsesolution()


"""
tail commentary!
    in brazilian portuguese, stomachache is called diarreia.
    To comment someone is shitting blood, you'd say goreia (gore + diarreia).
    the more you know!




some dumb shit:

lines = ["STEP 0: press-lit(x1,y1)", "STEP 0: press-lit(x1,y1)", "done"]
for line in lines:
                if "done" not in line:
                    while line.find(",") != -1:
                        xposit = line.find('x')
                        cposit = line.find(",")
                        end = line.find(")")
                        firstnum = line[xposit+1:cposit]
                        secondnum = line[cposit+2:end]
                        formatted.append(
                            str("(" + str(firstnum) + ", " + str(secondnum) + ")"))
                        line = line.replace("x", "", 1)
                        line = line.replace(",", "", 1)
                        line = line.replace(")", "", 1)
full = ";"
full = full.join(formatted)
print(full)
"""
