v 1 SRP
v 2 SRPP
v 3 RIBPC
v 4 REPC
v 5 RBPC
v 6 FRPP
v 7 REPP
v 8 REPP
v 9 SRPP
v 10 REPC
v 11 RIBPC
v 12 RBPC
v 13 FRPP
v 14 EPP
v 15 SLRRP
v 16 LRERV
v 17 LRIRV
v 18 LRRR
v 19 RIBPC
v 20 FRP
e 1 2  SRP__SRPP
e 2 3  SRPP__RIBPC
e 2 4  SRPP__REPC
e 2 5  SRPP__RBPC
e 3 6  RIBPC__FRPP
e 4 6  REPC__FRPP
e 5 6  RBPC__FRPP
e 6 7  FRPP__REPP
e 9 10  SRPP__REPC
e 9 11  SRPP__RIBPC
e 9 12  SRPP__RBPC
e 10 13  REPC__FRPP
e 11 13  RIBPC__FRPP
e 12 13  RBPC__FRPP
e 13 14  FRPP__EPP
e 14 15  EPP__SLRRP
e 15 16  SLRRP__LRERV
e 15 17  SLRRP__LRIRV
e 16 18  LRERV__LRRR
e 17 18  LRIRV__LRRR
e 7 8  REPP__REPP
e 8 9  REPP__SRPP
e 18 19  LRRR__RIBPC
e 19 20  RIBPC__FRP

