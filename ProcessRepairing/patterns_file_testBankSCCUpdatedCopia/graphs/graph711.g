v 1 SRP
v 2 SRPP
v 3 REPC
v 4 SHRRP
v 5 RIBPC
v 6 RBPC
v 7 FRPP
v 8 REPP
v 9 REPP
v 10 FRPP
v 11 RIBPC
v 12 MHRRPC
v 13 REPC
v 14 RBPC
v 15 SRPP
v 16 EPP
v 17 SLRRP
v 18 LRIRV
v 19 LRERV
v 20 LRRR
v 21 FLRRP
v 22 FRP
e 1 2  SRP__SRPP
e 2 3  SRPP__REPC
e 2 5  SRPP__RIBPC
e 2 6  SRPP__RBPC
e 5 7  RIBPC__FRPP
e 6 7  RBPC__FRPP
e 7 8  FRPP__REPP
e 16 17  EPP__SLRRP
e 17 18  SLRRP__LRIRV
e 17 19  SLRRP__LRERV
e 18 20  LRIRV__LRRR
e 19 20  LRERV__LRRR
e 20 21  LRRR__FLRRP
e 21 22  FLRRP__FRP
e 4 7  SHRRP__FRPP
e 3 4  REPC__SHRRP
e 8 9  REPP__REPP
e 10 11  FRPP__RIBPC
e 10 13  FRPP__REPC
e 10 14  FRPP__RBPC
e 9 10  REPP__FRPP
e 11 12  RIBPC__MHRRPC
e 14 15  RBPC__SRPP
e 13 15  REPC__SRPP
e 12 15  MHRRPC__SRPP
e 15 16  SRPP__EPP

