v 1 SRP
v 2 FHRRP
v 3 SRPP
v 4 RBPC
v 5 RIBPC
v 6 REPC
v 7 FRPP
v 8 REPP
v 9 SRPP
v 10 RIBPC
v 11 RBPC
v 12 REPC
v 13 FRPP
v 14 EPP
v 15 SLRRP
v 16 LRERV
v 17 LRIRV
v 18 FLRRP
v 19 LRRR
v 20 FRP
e 3 4  SRPP__RBPC
e 3 5  SRPP__RIBPC
e 3 6  SRPP__REPC
e 4 7  RBPC__FRPP
e 5 7  RIBPC__FRPP
e 6 7  REPC__FRPP
e 7 8  FRPP__REPP
e 8 9  REPP__SRPP
e 9 10  SRPP__RIBPC
e 9 11  SRPP__RBPC
e 9 12  SRPP__REPC
e 10 13  RIBPC__FRPP
e 11 13  RBPC__FRPP
e 12 13  REPC__FRPP
e 13 14  FRPP__EPP
e 14 15  EPP__SLRRP
e 15 16  SLRRP__LRERV
e 15 17  SLRRP__LRIRV
e 17 18  LRIRV__FLRRP
e 16 18  LRERV__FLRRP
e 1 2  SRP__FHRRP
e 2 3  FHRRP__SRPP
e 18 19  FLRRP__LRRR
e 19 20  LRRR__FRP

