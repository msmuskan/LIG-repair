v 1 SRP
v 2 SRPP
v 3 RIBPC
v 4 RBPC
v 5 REPC
v 6 FRPP
v 7 EPP
v 8 SLRRP
v 9 LRERV
v 10 EPP
v 11 LRIRV
v 12 LRRR
v 13 FLRRP
v 14 FRP
e 1 2  SRP__SRPP
e 2 3  SRPP__RIBPC
e 2 4  SRPP__RBPC
e 2 5  SRPP__REPC
e 3 6  RIBPC__FRPP
e 4 6  RBPC__FRPP
e 5 6  REPC__FRPP
e 6 7  FRPP__EPP
e 7 8  EPP__SLRRP
e 8 9  SLRRP__LRERV
e 8 11  SLRRP__LRIRV
e 11 12  LRIRV__LRRR
e 12 13  LRRR__FLRRP
e 13 14  FLRRP__FRP
e 10 12  EPP__LRRR
e 9 10  LRERV__EPP

