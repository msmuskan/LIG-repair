v 1 FLRRP
v 2 SRP
v 3 SRPP
v 4 RIBPC
v 5 RBPC
v 6 REPC
v 7 FRPP
v 8 EPP
v 9 SLRRP
v 10 LRIRV
v 11 LRIRV
v 12 LRERV
v 13 FLRRP
v 14 LRRR
v 15 FRP
e 2 3  SRP__SRPP
e 3 4  SRPP__RIBPC
e 3 5  SRPP__RBPC
e 3 6  SRPP__REPC
e 4 7  RIBPC__FRPP
e 5 7  RBPC__FRPP
e 6 7  REPC__FRPP
e 7 8  FRPP__EPP
e 8 9  EPP__SLRRP
e 9 10  SLRRP__LRIRV
e 9 12  SLRRP__LRERV
e 14 15  LRRR__FRP
e 1 2  FLRRP__SRP
e 10 11  LRIRV__LRIRV
e 12 13  LRERV__FLRRP
e 11 13  LRIRV__FLRRP
e 13 14  FLRRP__LRRR

