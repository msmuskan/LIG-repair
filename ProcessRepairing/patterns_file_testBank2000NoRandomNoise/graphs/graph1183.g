v 1 SRP
v 2 SRPP
v 3 RIBPC
v 4 REPC
v 5 RBPC
v 6 FRPP
v 7 REPP
v 8 REPP
v 9 SRPP
v 10 RIBPC
v 11 REPC
v 12 RBPC
v 13 FRPP
v 14 REPP
v 15 REPP
v 16 FRPP
v 17 REPC
v 18 RBPC
v 19 RIBPC
v 20 SRPP
v 21 EPP
v 22 SHRRP
v 23 HRRAN
v 24 HRHA
v 25 SHRRPC
v 26 MHRRPC
v 27 FHRRPC
v 28 RHRRPC
v 29 SHRRPC
v 30 AHRRPC
v 31 FHRRPC
v 32 RHRRPC
v 33 SHRRPC
v 34 AHRRPC
v 35 FHRRPC
v 36 HRRR
v 37 FHRRP
v 38 FRP

e 1 2 SRP__SRPP
e 2 3 SRPP__RIBPC
e 2 4 SRPP__REPC
e 2 5 SRPP__RBPC
e 3 6 RIBPC__FRPP
e 4 6 REPC__FRPP
e 5 6 RBPC__FRPP
e 6 7 FRPP__REPP
e 9 10 SRPP__RIBPC
e 9 11 SRPP__REPC
e 9 12 SRPP__RBPC
e 10 13 RIBPC__FRPP
e 11 13 REPC__FRPP
e 12 13 RBPC__FRPP
e 13 14 FRPP__REPP
e 21 22 EPP__SHRRP
e 22 23 SHRRP__HRRAN
e 22 24 SHRRP__HRHA
e 22 25 SHRRP__SHRRPC
e 23 36 HRRAN__HRRR
e 24 36 HRHA__HRRR
e 25 26 SHRRPC__MHRRPC
e 26 27 MHRRPC__FHRRPC
e 27 28 FHRRPC__RHRRPC
e 28 29 RHRRPC__SHRRPC
e 29 30 SHRRPC__AHRRPC
e 30 31 AHRRPC__FHRRPC
e 31 32 FHRRPC__RHRRPC
e 32 33 RHRRPC__SHRRPC
e 33 34 SHRRPC__AHRRPC
e 34 35 AHRRPC__FHRRPC
e 35 36 FHRRPC__HRRR
e 36 37 HRRR__FHRRP
e 37 38 FHRRP__FRP
e 7 8 REPP__REPP
e 8 9 REPP__SRPP
e 14 15 REPP__REPP
e 16 17 FRPP__REPC
e 16 18 FRPP__RBPC
e 16 19 FRPP__RIBPC
e 15 16 REPP__FRPP
e 19 20 RIBPC__SRPP
e 18 20 RBPC__SRPP
e 17 20 REPC__SRPP
e 20 21 SRPP__EPP

