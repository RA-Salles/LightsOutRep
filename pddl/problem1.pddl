(define (problem p01) (:domain lights-out)
(:objects 
    x0 x1 x2 - PosX
    y0 y1 y2 - PosY
)

(:init
    ;; Define quais tiles tao acesos.
    ( is-lit x1 y0 )
    ( is-lit x0 y1 )
    ( is-lit x1 y1 )
    ( is-lit x2 y1 )
    ( is-lit x1 y2 )

    ;; Define quais tiles sao adjacentes. E.x.: o tile (0, 0) é adjacente ao (1, 0)
    ;; e vice-versa.
    ( adj x0 x1 y0 y0 )
    ( adj x0 x0 y0 y1 )
    ( adj x0 x1 y1 y1 )
    ( adj x0 x0 y1 y0 )
    ( adj x0 x0 y1 y2 )
    ( adj x0 x1 y2 y2 )
    ( adj x0 x0 y2 y1 )
    ( adj x1 x0 y0 y0 )
    ( adj x1 x2 y0 y0 )
    ( adj x1 x1 y0 y1 )
    ( adj x1 x0 y1 y1 )
    ( adj x1 x2 y1 y1 )
    ( adj x1 x1 y1 y0 )
    ( adj x1 x1 y1 y2 )
    ( adj x1 x0 y2 y2 )
    ( adj x1 x2 y2 y2 )
    ( adj x1 x1 y2 y1 )
    ( adj x2 x1 y0 y0 )
    ( adj x2 x2 y0 y1 )
    ( adj x2 x1 y1 y1 )
    ( adj x2 x2 y1 y0 )
    ( adj x2 x2 y1 y2 )
    ( adj x2 x1 y2 y2 )
    ( adj x2 x2 y2 y1 )
)

(:goal (and
    ( success )
    
    ; ( forall ( ?x - PosX )
    ;     ( forall ( ?y - PosY )
    ;         ( not ( is-lit ?x ?y ) )
    ;     )
    ; )
))

)
