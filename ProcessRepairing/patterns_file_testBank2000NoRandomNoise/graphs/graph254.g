v 1 SRP
v 2 SRPP
v 3 RIBPC
v 4 RBPC
v 5 REPC
v 6 FRPP
v 7 EPP
v 8 SHRRP
v 9 SHRRPC
v 10 MHRRPC
v 11 HRHA
v 12 FHRRPC
v 13 HRRAN
v 14 EPP
v 15 SLRRP

e 1 2 SRP__SRPP
e 2 3 SRPP__RIBPC
e 2 4 SRPP__RBPC
e 2 5 SRPP__REPC
e 3 6 RIBPC__FRPP
e 4 6 RBPC__FRPP
e 5 6 REPC__FRPP
e 6 7 FRPP__EPP
e 7 8 EPP__SHRRP
e 8 9 SHRRP__SHRRPC
e 8 11 SHRRP__HRHA
e 8 13 SHRRP__HRRAN
e 9 10 SHRRPC__MHRRPC
e 10 12 MHRRPC__FHRRPC
e 14 15 EPP__SLRRP
e 11 14 HRHA__EPP
e 12 14 FHRRPC__EPP
e 13 14 HRRAN__EPP

