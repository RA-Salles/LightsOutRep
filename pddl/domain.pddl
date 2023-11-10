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
                (when ( or ( adj ?x ?xIt ?y ?yIt ) ( adj ?xIt ?x ?yIt ?y ) )
                    ;; Switches the tile off.
                    ( not ( is-lit ?xIt ?yIt ) )
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
                (when ( or ( adj ?x ?xIt ?y ?yIt ) ( adj ?xIt ?x ?yIt ?y ) )
                    ;; Switches the tile on.
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
        ( not ( is-broken ?x ?y ) )
    )
    :effect (and 
        ;; Loops for each X and Y coordinates.
        (forall (?xIt - PosX)
            (forall (?yIt - PosY)
                ;; Checks if this tile is adjacent to the original tile.
                (when ( or ( adj ?x ?xIt ?y ?yIt ) ( adj ?xIt ?x ?yIt ?y ) )
                    ;; Switches the tile off.
                    ( not ( is-lit ?xIt ?yIt ) )
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
        ( not ( is-broken ?x ?y ) )
    )
    :effect (and 
        ;; Loops for each X and Y coordinates.
        (forall (?xIt - PosX)
            (forall (?yIt - PosY)
                ;; Checks if this tile is adjacent to the original tile.
                (when ( or ( adj ?x ?xIt ?y ?yIt ) ( adj ?xIt ?x ?yIt ?y ) )
                    ;; Switches the tile on.
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