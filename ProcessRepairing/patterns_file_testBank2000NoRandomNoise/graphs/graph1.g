v 1 SRP
v 2 SRPP
v 3 RBPC
v 4 RIBPC
v 5 REPC
v 6 FRPP
v 7 REPP
v 8 REPP
v 9 SRPP
v 10 RIBPC
v 11 REPC
v 12 RBPC
v 13 FRPP
v 14 REPP
v 15 FRPP
v 16 RBPC
v 17 RIBPC
v 18 REPC
v 19 SRPP
v 20 EPP
v 21 SLRRP
v 22 LRERV
v 23 LRIRV
v 24 FLRRP
v 25 LRRR
v 26 FRP

e 1 2 SRP__SRPP
e 2 3 SRPP__RBPC
e 2 4 SRPP__RIBPC
e 2 5 SRPP__REPC
e 3 6 RBPC__FRPP
e 4 6 RIBPC__FRPP
e 5 6 REPC__FRPP
e 6 7 FRPP__REPP
e 9 10 SRPP__RIBPC
e 9 11 SRPP__REPC
e 9 12 SRPP__RBPC
e 10 13 RIBPC__FRPP
e 11 13 REPC__FRPP
e 12 13 RBPC__FRPP
e 13 14 FRPP__REPP
e 20 21 EPP__SLRRP
e 21 22 SLRRP__LRERV
e 21 23 SLRRP__LRIRV
e 23 24 LRIRV__FLRRP
e 22 24 LRERV__FLRRP
e 7 8 REPP__REPP
e 8 9 REPP__SRPP
e 14 15 REPP__FRPP
e 15 16 FRPP__RBPC
e 15 17 FRPP__RIBPC
e 15 18 FRPP__REPC
e 18 19 REPC__SRPP
e 17 19 RIBPC__SRPP
e 16 19 RBPC__SRPP
e 19 20 SRPP__EPP
e 24 25 FLRRP__LRRR
e 25 26 LRRR__FRP

