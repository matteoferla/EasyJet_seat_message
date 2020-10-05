from .square import Square, Border, Line

pattern = [
    [
        Square(Border.inner, Line.square), # first row headrest and tray
        Square(Border.outer, Line.BL),
        Square(Border.outer, Line.BR),
        Square(Border.none, Line.TR),
        Square(Border.outer, Line.square),
        Square(Border.outer, Line.BL),
        Square(Border.inner, Line.square),
        Square(Border.outer, Line.TL), # under toggle
        Square(Border.none, Line.BR),
        Square(Border.outer, Line.TL),
        Square(Border.none, Line.BL),
        Square(Border.outer, Line.TR),
    ],[
        Square(Border.inner, Line.square), # seocnd row
        Square(Border.outer, Line.TR),
        Square(Border.none, Line.BL),
        Square(Border.outer, Line.TL),
        Square(Border.none, Line.TL),
        Square(Border.outer, Line.TR),
        Square(Border.outer, Line.TL),
        Square(Border.none, Line.TL),
        Square(Border.none, Line.BR),
        Square(Border.outer, Line.TL),
        Square(Border.inner, Line.TL),
        Square(Border.outer, Line.TL) # end of sequence
    ],[
        Square(Border.outer, Line.TL), # third head
        Square(Border.outer, Line.TL),
        Square(Border.none, Line.TL),
        Square(Border.outer, Line.BR),
        Square(Border.outer, Line.BL),
        Square(Border.none, Line.BR), #4th tray
        Square(Border.outer, Line.square),
        Square(Border.outer, Line.BR),
        Square(Border.outer, Line.TL),
        Square(Border.none, Line.TL),
        Square(Border.outer, Line.BL),
        Square(Border.none, Line.BL) #sequence repeats
    ],[
        Square(Border.none, Line.TR),
        Square(Border.outer, Line.square),
        Square(Border.outer, Line.BL),
        Square(Border.inner, Line.square),
        Square(Border.outer, Line.TL),
        Square(Border.none, Line.BR),
        Square(Border.outer, Line.TL),
        Square(Border.none, Line.BL),
        Square(Border.outer, Line.TR),
        Square(Border.inner, Line.square),
        Square(Border.outer, Line.BL),
        Square(Border.outer, Line.BR)
    ], [
        Square(Border.outer, Line.TL),
        Square(Border.none, Line.TL),
        Square(Border.none, Line.BR),
        Square(Border.outer, Line.TL),
        Square(Border.inner, Line.TL),
        Square(Border.outer, Line.TL),
        Square(Border.inner, Line.square),
        Square(Border.outer, Line.TR),
        Square(Border.none, Line.BL),
        Square(Border.outer, Line.TL),
        Square(Border.none, Line.TL),
        Square(Border.outer, Line.TR)
    ], [
        Square(Border.outer, Line.square),
        Square(Border.outer, Line.BR),
        Square(Border.outer, Line.TR),
        Square(Border.none, Line.TL),
        Square(Border.outer, Line.BR),
        Square(Border.none, Line.BR),
        Square(Border.outer, Line.TL),
        Square(Border.outer, Line.TL),
        Square(Border.none, Line.TL),
        Square(Border.outer, Line.BR),
        Square(Border.outer, Line.BL),
        Square(Border.none, Line.BR)
    ]
]