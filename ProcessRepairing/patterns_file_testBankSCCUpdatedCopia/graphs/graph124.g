v 1 SRP
v 2 SRPP
v 3 RBPC
v 4 RIBPC
v 5 REPC
v 6 FHRRP
v 7 FRPP
v 8 REPP
v 9 REPP
v 10 SRPP
v 11 RBPC
v 12 RIBPC
v 13 FRPP
v 14 EPP
v 15 SLRRP
v 16 LRIRV
v 17 LRERV
v 18 LRRR
v 19 FLRRP
v 20 FRP
e 1 2  SRP__SRPP
e 2 3  SRPP__RBPC
e 2 4  SRPP__RIBPC
e 2 5  SRPP__REPC
e 7 8  FRPP__REPP
e 10 11  SRPP__RBPC
e 10 12  SRPP__RIBPC
e 11 13  RBPC__FRPP
e 12 13  RIBPC__FRPP
e 13 14  FRPP__EPP
e 14 15  EPP__SLRRP
e 15 16  SLRRP__LRIRV
e 15 17  SLRRP__LRERV
e 16 18  LRIRV__LRRR
e 17 18  LRERV__LRRR
e 18 19  LRRR__FLRRP
e 19 20  FLRRP__FRP
e 3 6  RBPC__FHRRP
e 4 6  RIBPC__FHRRP
e 5 6  REPC__FHRRP
e 6 7  FHRRP__FRPP
e 8 9  REPP__REPP
e 9 10  REPP__SRPP

