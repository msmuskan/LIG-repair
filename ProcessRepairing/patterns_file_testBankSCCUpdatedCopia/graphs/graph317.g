v 1 SRP
v 2 SRPP
v 3 RIBPC
v 4 REPC
v 5 RBPC
v 6 FRPP
v 7 EPP
v 8 SHRRP
v 9 HRRAN
v 10 SHRRPC
v 11 AHRRPC
v 12 HRHA
v 13 FHRRPC
v 14 RHRRPC
v 15 AHRRPC
v 16 FHRRPC
v 17 HRRR
v 18 FHRRP
v 19 FRP
v 20 LRRR
e 1 2  SRP__SRPP
e 2 3  SRPP__RIBPC
e 2 4  SRPP__REPC
e 2 5  SRPP__RBPC
e 3 6  RIBPC__FRPP
e 4 6  REPC__FRPP
e 5 6  RBPC__FRPP
e 6 7  FRPP__EPP
e 7 8  EPP__SHRRP
e 8 9  SHRRP__HRRAN
e 8 10  SHRRP__SHRRPC
e 8 12  SHRRP__HRHA
e 9 17  HRRAN__HRRR
e 10 11  SHRRPC__AHRRPC
e 11 13  AHRRPC__FHRRPC
e 12 17  HRHA__HRRR
e 13 14  FHRRPC__RHRRPC
e 15 16  AHRRPC__FHRRPC
e 16 17  FHRRPC__HRRR
e 17 18  HRRR__FHRRP
e 18 19  FHRRP__FRP
e 14 15  RHRRPC__AHRRPC
e 19 20  FRP__LRRR

