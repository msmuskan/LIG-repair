v 1 SRP
v 2 SRPP
v 3 REPC
v 4 RBPC
v 5 RIBPC
v 6 FRPP
v 7 EPP
v 8 SLRRP
v 9 LRERV
v 10 SRPP
v 11 LRIRV
v 12 FLRRP
v 13 LRRR
v 14 FRP
e 1 2  SRP__SRPP
e 2 3  SRPP__REPC
e 2 4  SRPP__RBPC
e 2 5  SRPP__RIBPC
e 3 6  REPC__FRPP
e 4 6  RBPC__FRPP
e 5 6  RIBPC__FRPP
e 6 7  FRPP__EPP
e 7 8  EPP__SLRRP
e 8 9  SLRRP__LRERV
e 8 11  SLRRP__LRIRV
e 11 12  LRIRV__FLRRP
e 10 12  SRPP__FLRRP
e 9 10  LRERV__SRPP
e 12 13  FLRRP__LRRR
e 13 14  LRRR__FRP

