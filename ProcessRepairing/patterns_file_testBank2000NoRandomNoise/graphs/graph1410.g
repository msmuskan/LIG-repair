v 1 SRP
v 2 SRPP
v 3 RIBPC
v 4 REPC
v 5 RBPC
v 6 FRPP
v 7 REPP
v 8 FRPP
v 9 RIBPC
v 10 REPC
v 11 RBPC
v 12 SRPP
v 13 EPP
v 14 SRP
v 15 FRP
v 16 SHRRPC
v 17 MHRRPC
v 18 HRHA
v 19 HRRAN
v 20 FHRRPC
v 21 RHRRPC
v 22 SHRRPC
v 23 MHRRPC
v 24 FHRRPC
v 25 RHRRPC
v 26 SHRRPC
v 27 AHRRPC
v 28 FHRRPC
v 29 EPP
v 30 SLRRP

e 1 2 SRP__SRPP
e 2 3 SRPP__RIBPC
e 2 4 SRPP__REPC
e 2 5 SRPP__RBPC
e 3 6 RIBPC__FRPP
e 4 6 REPC__FRPP
e 5 6 RBPC__FRPP
e 6 7 FRPP__REPP
e 16 17 SHRRPC__MHRRPC
e 17 20 MHRRPC__FHRRPC
e 20 21 FHRRPC__RHRRPC
e 21 22 RHRRPC__SHRRPC
e 22 23 SHRRPC__MHRRPC
e 23 24 MHRRPC__FHRRPC
e 24 25 FHRRPC__RHRRPC
e 25 26 RHRRPC__SHRRPC
e 26 27 SHRRPC__AHRRPC
e 27 28 AHRRPC__FHRRPC
e 7 8 REPP__FRPP
e 8 9 FRPP__RIBPC
e 8 10 FRPP__REPC
e 8 11 FRPP__RBPC
e 11 12 RBPC__SRPP
e 10 12 REPC__SRPP
e 9 12 RIBPC__SRPP
e 12 13 SRPP__EPP
e 13 14 EPP__SRP
e 15 16 FRP__SHRRPC
e 15 18 FRP__HRHA
e 15 19 FRP__HRRAN
e 14 15 SRP__FRP
e 29 30 EPP__SLRRP
e 18 29 HRHA__EPP
e 19 29 HRRAN__EPP
e 28 29 FHRRPC__EPP

