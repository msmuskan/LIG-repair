v 1 SRP
v 2 SRPP
v 3 REPC
v 4 RBPC
v 5 RIBPC
v 6 FRPP
v 7 REPP
v 8 REPP
v 9 FRPP
v 10 RBPC
v 11 REPC
v 12 RIBPC
v 13 SRPP
v 14 EPP
v 15 SLRRP
v 16 LRERV
v 17 LRIRV
v 18 LRRR
v 19 FLRRP
v 20 FRP

e 1 2 SRP__SRPP
e 2 3 SRPP__REPC
e 2 4 SRPP__RBPC
e 2 5 SRPP__RIBPC
e 3 6 REPC__FRPP
e 4 6 RBPC__FRPP
e 5 6 RIBPC__FRPP
e 6 7 FRPP__REPP
e 14 15 EPP__SLRRP
e 15 16 SLRRP__LRERV
e 15 17 SLRRP__LRIRV
e 16 18 LRERV__LRRR
e 17 18 LRIRV__LRRR
e 18 19 LRRR__FLRRP
e 19 20 FLRRP__FRP
e 7 8 REPP__REPP
e 9 10 FRPP__RBPC
e 9 11 FRPP__REPC
e 9 12 FRPP__RIBPC
e 8 9 REPP__FRPP
e 12 13 RIBPC__SRPP
e 11 13 REPC__SRPP
e 10 13 RBPC__SRPP
e 13 14 SRPP__EPP

