v 1 SRP
v 2 HRRAN
v 3 FRPP
v 4 REPC
v 5 RBPC
v 6 RIBPC
v 7 SRPP
v 8 EPP
v 9 SLRRP
v 10 LRERV
v 11 LRIRV
v 12 LRIRV
v 13 LRRR
v 14 FLRRP
v 15 FRP
e 8 9  EPP__SLRRP
e 9 10  SLRRP__LRERV
e 9 11  SLRRP__LRIRV
e 13 14  LRRR__FLRRP
e 14 15  FLRRP__FRP
e 1 2  SRP__HRRAN
e 3 4  FRPP__REPC
e 3 5  FRPP__RBPC
e 3 6  FRPP__RIBPC
e 2 3  HRRAN__FRPP
e 6 7  RIBPC__SRPP
e 5 7  RBPC__SRPP
e 4 7  REPC__SRPP
e 7 8  SRPP__EPP
e 10 12  LRERV__LRIRV
e 11 12  LRIRV__LRIRV
e 12 13  LRIRV__LRRR

