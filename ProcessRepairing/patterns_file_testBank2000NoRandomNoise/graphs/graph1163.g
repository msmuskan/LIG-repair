v 1 SRP
v 2 SRPP
v 3 RIBPC
v 4 REPC
v 5 RBPC
v 6 FRPP
v 7 REPP
v 8 SRPP
v 9 RIBPC
v 10 RBPC
v 11 REPC
v 12 FRPP
v 13 REPP
v 14 FRPP
v 15 RIBPC
v 16 REPC
v 17 RBPC
v 18 SRPP
v 19 EPP
v 20 SHRRP
v 21 HRHA
v 22 HRRAN
v 23 SHRRPC
v 24 AHRRPC
v 25 FHRRPC
v 26 RHRRPC
v 27 SHRRPC
v 28 AHRRPC
v 29 FHRRPC
v 30 HRRR
v 31 FHRRP
v 32 FRP

e 1 2 SRP__SRPP
e 2 3 SRPP__RIBPC
e 2 4 SRPP__REPC
e 2 5 SRPP__RBPC
e 3 6 RIBPC__FRPP
e 4 6 REPC__FRPP
e 5 6 RBPC__FRPP
e 6 7 FRPP__REPP
e 7 8 REPP__SRPP
e 8 9 SRPP__RIBPC
e 8 10 SRPP__RBPC
e 8 11 SRPP__REPC
e 9 12 RIBPC__FRPP
e 10 12 RBPC__FRPP
e 11 12 REPC__FRPP
e 12 13 FRPP__REPP
e 19 20 EPP__SHRRP
e 20 21 SHRRP__HRHA
e 20 22 SHRRP__HRRAN
e 20 23 SHRRP__SHRRPC
e 21 30 HRHA__HRRR
e 22 30 HRRAN__HRRR
e 23 24 SHRRPC__AHRRPC
e 24 25 AHRRPC__FHRRPC
e 25 26 FHRRPC__RHRRPC
e 26 27 RHRRPC__SHRRPC
e 27 28 SHRRPC__AHRRPC
e 28 29 AHRRPC__FHRRPC
e 29 30 FHRRPC__HRRR
e 30 31 HRRR__FHRRP
e 31 32 FHRRP__FRP
e 13 14 REPP__FRPP
e 14 15 FRPP__RIBPC
e 14 16 FRPP__REPC
e 14 17 FRPP__RBPC
e 17 18 RBPC__SRPP
e 16 18 REPC__SRPP
e 15 18 RIBPC__SRPP
e 18 19 SRPP__EPP

