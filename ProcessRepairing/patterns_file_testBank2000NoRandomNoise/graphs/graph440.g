v 1 SRP
v 2 FRPP
v 3 REPC
v 4 RIBPC
v 5 RBPC
v 6 SRPP
v 7 REPP
v 8 FRPP
v 9 REPC
v 10 RBPC
v 11 RIBPC
v 12 SRPP
v 13 EPP
v 14 SHRRP
v 15 SHRRPC
v 16 HRHA
v 17 HRRAN
v 18 AHRRPC
v 19 FHRRPC
v 20 EPP
v 21 SLRRP

e 13 14 EPP__SHRRP
e 14 15 SHRRP__SHRRPC
e 14 16 SHRRP__HRHA
e 14 17 SHRRP__HRRAN
e 15 18 SHRRPC__AHRRPC
e 18 19 AHRRPC__FHRRPC
e 1 2 SRP__FRPP
e 2 3 FRPP__REPC
e 2 4 FRPP__RIBPC
e 2 5 FRPP__RBPC
e 3 6 REPC__SRPP
e 4 6 RIBPC__SRPP
e 5 6 RBPC__SRPP
e 7 8 REPP__FRPP
e 6 7 SRPP__REPP
e 8 9 FRPP__REPC
e 12 13 SRPP__EPP
e 9 10 REPC__RBPC
e 10 11 RBPC__RIBPC
e 11 12 RIBPC__SRPP
e 20 21 EPP__SLRRP
e 16 20 HRHA__EPP
e 17 20 HRRAN__EPP
e 19 20 FHRRPC__EPP

