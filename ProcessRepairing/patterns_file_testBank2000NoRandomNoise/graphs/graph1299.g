v 1 SRP
v 2 SRPP
v 3 RBPC
v 4 RIBPC
v 5 REPC
v 6 FRPP
v 7 REPP
v 8 REPP
v 9 FRPP
v 10 REPC
v 11 RIBPC
v 12 RBPC
v 13 SRPP
v 14 REPP
v 15 REPP
v 16 SRPP
v 17 RBPC
v 18 REPC
v 19 RIBPC
v 20 FRPP
v 21 EPP
v 22 SHRRP
v 23 SHRRPC
v 24 AHRRPC
v 25 HRRAN
v 26 HRHA
v 27 FHRRPC
v 28 HRRR
v 29 FHRRP
v 30 FRP

e 1 2 SRP__SRPP
e 2 3 SRPP__RBPC
e 2 4 SRPP__RIBPC
e 2 5 SRPP__REPC
e 3 6 RBPC__FRPP
e 4 6 RIBPC__FRPP
e 5 6 REPC__FRPP
e 6 7 FRPP__REPP
e 16 17 SRPP__RBPC
e 16 18 SRPP__REPC
e 16 19 SRPP__RIBPC
e 17 20 RBPC__FRPP
e 18 20 REPC__FRPP
e 19 20 RIBPC__FRPP
e 20 21 FRPP__EPP
e 21 22 EPP__SHRRP
e 22 23 SHRRP__SHRRPC
e 22 25 SHRRP__HRRAN
e 22 26 SHRRP__HRHA
e 23 24 SHRRPC__AHRRPC
e 24 27 AHRRPC__FHRRPC
e 25 28 HRRAN__HRRR
e 26 28 HRHA__HRRR
e 27 28 FHRRPC__HRRR
e 28 29 HRRR__FHRRP
e 29 30 FHRRP__FRP
e 7 8 REPP__REPP
e 9 10 FRPP__REPC
e 9 11 FRPP__RIBPC
e 9 12 FRPP__RBPC
e 8 9 REPP__FRPP
e 12 13 RBPC__SRPP
e 11 13 RIBPC__SRPP
e 10 13 REPC__SRPP
e 13 14 SRPP__REPP
e 14 15 REPP__REPP
e 15 16 REPP__SRPP

