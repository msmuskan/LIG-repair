v 1 SRP
v 2 SRPP
v 3 RIBPC
v 4 RBPC
v 5 REPC
v 6 FRPP
v 7 REPP
v 8 FRPP
v 9 RBPC
v 10 RIBPC
v 11 REPC
v 12 SRPP
v 13 EPP
v 14 SHRRP
v 15 SHRRPC
v 16 MHRRPC
v 17 FHRRPC
v 18 HRHA
v 19 HRRAN
v 20 HRRR
v 21 FHRRP
v 22 FRP

e 1 2 SRP__SRPP
e 2 3 SRPP__RIBPC
e 2 4 SRPP__RBPC
e 2 5 SRPP__REPC
e 3 6 RIBPC__FRPP
e 4 6 RBPC__FRPP
e 5 6 REPC__FRPP
e 6 7 FRPP__REPP
e 13 14 EPP__SHRRP
e 14 15 SHRRP__SHRRPC
e 14 18 SHRRP__HRHA
e 14 19 SHRRP__HRRAN
e 15 16 SHRRPC__MHRRPC
e 16 17 MHRRPC__FHRRPC
e 17 20 FHRRPC__HRRR
e 18 20 HRHA__HRRR
e 19 20 HRRAN__HRRR
e 20 21 HRRR__FHRRP
e 21 22 FHRRP__FRP
e 7 8 REPP__FRPP
e 8 9 FRPP__RBPC
e 8 10 FRPP__RIBPC
e 8 11 FRPP__REPC
e 11 12 REPC__SRPP
e 10 12 RIBPC__SRPP
e 9 12 RBPC__SRPP
e 12 13 SRPP__EPP

