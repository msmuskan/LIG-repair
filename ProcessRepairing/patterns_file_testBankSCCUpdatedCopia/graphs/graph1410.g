v 1 SRP
v 2 SRPP
v 3 RIBPC
v 4 RBPC
v 5 FRPP
v 6 REPP
v 7 REPP
v 8 FRPP
v 9 RBPC
v 10 REPC
v 11 RIBPC
v 12 SRPP
v 13 EPP
v 14 REPC
v 15 SRP
v 16 FRP
v 17 HRRAN
v 18 SHRRPC
v 19 AHRRPC
v 20 HRHA
v 21 FHRRPC
v 22 HRRR
v 23 FHRRP
v 24 FRP
e 1 2  SRP__SRPP
e 2 3  SRPP__RIBPC
e 2 4  SRPP__RBPC
e 3 5  RIBPC__FRPP
e 4 5  RBPC__FRPP
e 5 6  FRPP__REPP
e 17 22  HRRAN__HRRR
e 18 19  SHRRPC__AHRRPC
e 19 21  AHRRPC__FHRRPC
e 20 22  HRHA__HRRR
e 21 22  FHRRPC__HRRR
e 22 23  HRRR__FHRRP
e 23 24  FHRRP__FRP
e 6 7  REPP__REPP
e 8 9  FRPP__RBPC
e 8 10  FRPP__REPC
e 8 11  FRPP__RIBPC
e 7 8  REPP__FRPP
e 11 12  RIBPC__SRPP
e 10 12  REPC__SRPP
e 9 12  RBPC__SRPP
e 12 13  SRPP__EPP
e 13 14  EPP__REPC
e 16 17  FRP__HRRAN
e 16 18  FRP__SHRRPC
e 16 20  FRP__HRHA
e 14 15  REPC__SRP
e 15 16  SRP__FRP

