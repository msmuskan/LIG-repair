v 1 SRP
v 2 SRPP
v 3 REPC
v 4 RIBPC
v 5 RBPC
v 6 FRPP
v 7 REPP
v 8 FRPP
v 9 RIBPC
v 10 RBPC
v 11 REPC
v 12 SRPP
v 13 EPP
v 14 SRP
v 15 FRP
v 16 HRHA
v 17 SHRRPC
v 18 AHRRPC
v 19 HRRAN
v 20 FHRRPC
v 21 RHRRPC
v 22 SHRRPC
v 23 AHRRPC
v 24 FHRRPC
v 25 HRRR
v 26 FHRRP
v 27 FRP

e 1 2 SRP__SRPP
e 2 3 SRPP__REPC
e 2 4 SRPP__RIBPC
e 2 5 SRPP__RBPC
e 3 6 REPC__FRPP
e 4 6 RIBPC__FRPP
e 5 6 RBPC__FRPP
e 6 7 FRPP__REPP
e 16 25 HRHA__HRRR
e 17 18 SHRRPC__AHRRPC
e 18 20 AHRRPC__FHRRPC
e 19 25 HRRAN__HRRR
e 20 21 FHRRPC__RHRRPC
e 21 22 RHRRPC__SHRRPC
e 22 23 SHRRPC__AHRRPC
e 23 24 AHRRPC__FHRRPC
e 24 25 FHRRPC__HRRR
e 25 26 HRRR__FHRRP
e 26 27 FHRRP__FRP
e 7 8 REPP__FRPP
e 8 9 FRPP__RIBPC
e 8 10 FRPP__RBPC
e 8 11 FRPP__REPC
e 11 12 REPC__SRPP
e 10 12 RBPC__SRPP
e 9 12 RIBPC__SRPP
e 12 13 SRPP__EPP
e 13 14 EPP__SRP
e 15 16 FRP__HRHA
e 15 17 FRP__SHRRPC
e 15 19 FRP__HRRAN
e 14 15 SRP__FRP

