v 1 SRP
v 2 SRPP
v 3 RBPC
v 4 REPC
v 5 RIBPC
v 6 FRPP
v 7 EPP
v 8 SLRRP
v 9 LRIRV
v 10 LRERV
v 11 LRRR
v 12 FHRRPC
v 13 FLRRP
v 14 FRP
e 1 2  SRP__SRPP
e 2 3  SRPP__RBPC
e 2 4  SRPP__REPC
e 2 5  SRPP__RIBPC
e 3 6  RBPC__FRPP
e 4 6  REPC__FRPP
e 5 6  RIBPC__FRPP
e 6 7  FRPP__EPP
e 7 8  EPP__SLRRP
e 8 9  SLRRP__LRIRV
e 8 10  SLRRP__LRERV
e 9 11  LRIRV__LRRR
e 10 11  LRERV__LRRR
e 13 14  FLRRP__FRP
e 11 12  LRRR__FHRRPC
e 12 13  FHRRPC__FLRRP

