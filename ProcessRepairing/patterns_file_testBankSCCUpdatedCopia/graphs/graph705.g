v 1 SRP
v 2 FRPP
v 3 RBPC
v 4 SHRRPC
v 5 RIBPC
v 6 REPC
v 7 SRPP
v 8 EPP
v 9 SLRRP
v 10 LRERV
v 11 LRIRV
v 12 LRRR
v 13 FLRRP
v 14 FRP
e 8 9  EPP__SLRRP
e 9 10  SLRRP__LRERV
e 9 11  SLRRP__LRIRV
e 10 12  LRERV__LRRR
e 11 12  LRIRV__LRRR
e 12 13  LRRR__FLRRP
e 13 14  FLRRP__FRP
e 1 2  SRP__FRPP
e 2 3  FRPP__RBPC
e 2 5  FRPP__RIBPC
e 2 6  FRPP__REPC
e 3 4  RBPC__SHRRPC
e 6 7  REPC__SRPP
e 5 7  RIBPC__SRPP
e 4 7  SHRRPC__SRPP
e 7 8  SRPP__EPP

