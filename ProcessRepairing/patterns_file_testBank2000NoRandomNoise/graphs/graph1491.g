v 1 SRP
v 2 FRPP
v 3 REPC
v 4 RIBPC
v 5 RBPC
v 6 SRPP
v 7 REPP
v 8 FRPP
v 9 RBPC
v 10 REPC
v 11 RIBPC
v 12 SRPP
v 13 EPP
v 14 SLRRP
v 15 LRIRV
v 16 LRERV
v 17 LRRR
v 18 FLRRP
v 19 FRP

e 13 14 EPP__SLRRP
e 14 15 SLRRP__LRIRV
e 14 16 SLRRP__LRERV
e 15 17 LRIRV__LRRR
e 16 17 LRERV__LRRR
e 17 18 LRRR__FLRRP
e 18 19 FLRRP__FRP
e 1 2 SRP__FRPP
e 2 3 FRPP__REPC
e 2 4 FRPP__RIBPC
e 2 5 FRPP__RBPC
e 3 6 REPC__SRPP
e 4 6 RIBPC__SRPP
e 5 6 RBPC__SRPP
e 7 8 REPP__FRPP
e 6 7 SRPP__REPP
e 8 9 FRPP__RBPC
e 12 13 SRPP__EPP
e 9 10 RBPC__REPC
e 10 11 REPC__RIBPC
e 11 12 RIBPC__SRPP

