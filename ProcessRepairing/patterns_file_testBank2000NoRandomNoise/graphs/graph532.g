v 1 SRP
v 2 SRPP
v 3 RBPC
v 4 REPC
v 5 RIBPC
v 6 FRPP
v 7 EPP
v 8 SRP
v 9 FRP
v 10 HRRAN
v 11 SHRRPC
v 12 MHRRPC
v 13 FHRRPC
v 14 HRHA
v 15 RHRRPC
v 16 SHRRPC
v 17 MHRRPC
v 18 FHRRPC
v 19 RHRRPC
v 20 SHRRPC
v 21 MHRRPC
v 22 FHRRPC
v 23 HRRR
v 24 FHRRP
v 25 FRP

e 1 2 SRP__SRPP
e 2 3 SRPP__RBPC
e 2 4 SRPP__REPC
e 2 5 SRPP__RIBPC
e 3 6 RBPC__FRPP
e 4 6 REPC__FRPP
e 5 6 RIBPC__FRPP
e 6 7 FRPP__EPP
e 10 23 HRRAN__HRRR
e 11 12 SHRRPC__MHRRPC
e 12 13 MHRRPC__FHRRPC
e 13 15 FHRRPC__RHRRPC
e 14 23 HRHA__HRRR
e 15 16 RHRRPC__SHRRPC
e 16 17 SHRRPC__MHRRPC
e 17 18 MHRRPC__FHRRPC
e 18 19 FHRRPC__RHRRPC
e 19 20 RHRRPC__SHRRPC
e 20 21 SHRRPC__MHRRPC
e 21 22 MHRRPC__FHRRPC
e 22 23 FHRRPC__HRRR
e 23 24 HRRR__FHRRP
e 24 25 FHRRP__FRP
e 7 8 EPP__SRP
e 9 10 FRP__HRRAN
e 9 11 FRP__SHRRPC
e 9 14 FRP__HRHA
e 8 9 SRP__FRP

