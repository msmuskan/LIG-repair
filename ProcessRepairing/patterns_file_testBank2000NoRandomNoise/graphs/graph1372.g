v 1 SRP
v 2 SRPP
v 3 REPC
v 4 RIBPC
v 5 RBPC
v 6 FRPP
v 7 REPP
v 8 SRPP
v 9 REPC
v 10 RIBPC
v 11 RBPC
v 12 FRPP
v 13 REPP
v 14 FRPP
v 15 RBPC
v 16 RIBPC
v 17 REPC
v 18 SRPP
v 19 EPP
v 20 SLRRP
v 21 LRERV
v 22 LRIRV
v 23 LRRR
v 24 FLRRP
v 25 FRP

e 1 2 SRP__SRPP
e 2 3 SRPP__REPC
e 2 4 SRPP__RIBPC
e 2 5 SRPP__RBPC
e 3 6 REPC__FRPP
e 4 6 RIBPC__FRPP
e 5 6 RBPC__FRPP
e 6 7 FRPP__REPP
e 7 8 REPP__SRPP
e 8 9 SRPP__REPC
e 8 10 SRPP__RIBPC
e 8 11 SRPP__RBPC
e 9 12 REPC__FRPP
e 10 12 RIBPC__FRPP
e 11 12 RBPC__FRPP
e 12 13 FRPP__REPP
e 19 20 EPP__SLRRP
e 20 21 SLRRP__LRERV
e 20 22 SLRRP__LRIRV
e 21 23 LRERV__LRRR
e 22 23 LRIRV__LRRR
e 23 24 LRRR__FLRRP
e 24 25 FLRRP__FRP
e 13 14 REPP__FRPP
e 14 15 FRPP__RBPC
e 14 16 FRPP__RIBPC
e 14 17 FRPP__REPC
e 17 18 REPC__SRPP
e 16 18 RIBPC__SRPP
e 15 18 RBPC__SRPP
e 18 19 SRPP__EPP

