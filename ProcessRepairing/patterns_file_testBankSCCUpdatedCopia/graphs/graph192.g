v 1 SRP
v 2 SRPP
v 3 FRPP
v 4 HRRR
v 5 RIBPC
v 6 REPC
v 7 RBPC
v 8 SRPP
v 9 REPP
v 10 REPP
v 11 SRPP
v 12 RBPC
v 13 RIBPC
v 14 REPC
v 15 FRPP
v 16 EPP
v 17 SLRRP
v 18 LRIRV
v 19 LRERV
v 20 FLRRP
v 21 LRRR
v 22 FRP
e 1 2  SRP__SRPP
e 11 12  SRPP__RBPC
e 11 13  SRPP__RIBPC
e 11 14  SRPP__REPC
e 12 15  RBPC__FRPP
e 13 15  RIBPC__FRPP
e 14 15  REPC__FRPP
e 15 16  FRPP__EPP
e 16 17  EPP__SLRRP
e 17 18  SLRRP__LRIRV
e 17 19  SLRRP__LRERV
e 19 20  LRERV__FLRRP
e 18 20  LRIRV__FLRRP
e 2 3  SRPP__FRPP
e 4 5  HRRR__RIBPC
e 4 6  HRRR__REPC
e 4 7  HRRR__RBPC
e 3 4  FRPP__HRRR
e 7 8  RBPC__SRPP
e 6 8  REPC__SRPP
e 5 8  RIBPC__SRPP
e 8 9  SRPP__REPP
e 9 10  REPP__REPP
e 10 11  REPP__SRPP
e 20 21  FLRRP__LRRR
e 21 22  LRRR__FRP

