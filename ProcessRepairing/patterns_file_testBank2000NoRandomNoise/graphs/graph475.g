v 1 SRP
v 2 SRPP
v 3 REPC
v 4 RIBPC
v 5 RBPC
v 6 FRPP
v 7 EPP
v 8 SHRRP
v 9 HRRAN
v 10 SHRRPC
v 11 HRHA
v 12 AHRRPC
v 13 FHRRPC
v 14 RHRRPC
v 15 SHRRPC
v 16 MHRRPC
v 17 FHRRPC
v 18 EPP
v 19 SLRRP

e 1 2 SRP__SRPP
e 2 3 SRPP__REPC
e 2 4 SRPP__RIBPC
e 2 5 SRPP__RBPC
e 3 6 REPC__FRPP
e 4 6 RIBPC__FRPP
e 5 6 RBPC__FRPP
e 6 7 FRPP__EPP
e 7 8 EPP__SHRRP
e 8 9 SHRRP__HRRAN
e 8 10 SHRRP__SHRRPC
e 8 11 SHRRP__HRHA
e 10 12 SHRRPC__AHRRPC
e 12 13 AHRRPC__FHRRPC
e 13 14 FHRRPC__RHRRPC
e 14 15 RHRRPC__SHRRPC
e 15 16 SHRRPC__MHRRPC
e 16 17 MHRRPC__FHRRPC
e 18 19 EPP__SLRRP
e 9 18 HRRAN__EPP
e 11 18 HRHA__EPP
e 17 18 FHRRPC__EPP

