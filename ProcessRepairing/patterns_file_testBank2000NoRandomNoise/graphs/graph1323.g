v 1 SRP
v 2 SRPP
v 3 RIBPC
v 4 RBPC
v 5 REPC
v 6 FRPP
v 7 EPP
v 8 SRP
v 9 FRP
v 10 HRRAN
v 11 SHRRPC
v 12 MHRRPC
v 13 HRHA
v 14 FHRRPC
v 15 RHRRPC
v 16 SHRRPC
v 17 AHRRPC
v 18 FHRRPC
v 19 RHRRPC
v 20 SHRRPC
v 21 AHRRPC
v 22 FHRRPC
v 23 EPP
v 24 SLRRP

e 1 2 SRP__SRPP
e 2 3 SRPP__RIBPC
e 2 4 SRPP__RBPC
e 2 5 SRPP__REPC
e 3 6 RIBPC__FRPP
e 4 6 RBPC__FRPP
e 5 6 REPC__FRPP
e 6 7 FRPP__EPP
e 11 12 SHRRPC__MHRRPC
e 12 14 MHRRPC__FHRRPC
e 14 15 FHRRPC__RHRRPC
e 15 16 RHRRPC__SHRRPC
e 16 17 SHRRPC__AHRRPC
e 17 18 AHRRPC__FHRRPC
e 18 19 FHRRPC__RHRRPC
e 19 20 RHRRPC__SHRRPC
e 20 21 SHRRPC__AHRRPC
e 21 22 AHRRPC__FHRRPC
e 7 8 EPP__SRP
e 9 10 FRP__HRRAN
e 9 11 FRP__SHRRPC
e 9 13 FRP__HRHA
e 8 9 SRP__FRP
e 23 24 EPP__SLRRP
e 10 23 HRRAN__EPP
e 13 23 HRHA__EPP
e 22 23 FHRRPC__EPP

