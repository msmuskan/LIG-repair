v 1 SRP
v 2 SRPP
v 3 REPC
v 4 RIBPC
v 5 RBPC
v 6 FRPP
v 7 EPP
v 8 SHRRP
v 9 HRRAN
v 10 SHRRPC
v 11 AHRRPC
v 12 HRHA
v 13 FHRRPC
v 14 FRP
v 15 RHRRPC
v 16 SHRRPC
v 17 AHRRPC
v 18 FHRRPC
v 19 SHRRPC
v 20 MHRRPC
v 21 FHRRPC
v 22 HRRR
v 23 FHRRP
v 24 FRP
e 1 2  SRP__SRPP
e 2 3  SRPP__REPC
e 2 4  SRPP__RIBPC
e 2 5  SRPP__RBPC
e 3 6  REPC__FRPP
e 4 6  RIBPC__FRPP
e 5 6  RBPC__FRPP
e 6 7  FRPP__EPP
e 7 8  EPP__SHRRP
e 8 9  SHRRP__HRRAN
e 8 10  SHRRP__SHRRPC
e 8 12  SHRRP__HRHA
e 9 22  HRRAN__HRRR
e 10 11  SHRRPC__AHRRPC
e 11 13  AHRRPC__FHRRPC
e 12 22  HRHA__HRRR
e 15 16  RHRRPC__SHRRPC
e 16 17  SHRRPC__AHRRPC
e 17 18  AHRRPC__FHRRPC
e 19 20  SHRRPC__MHRRPC
e 20 21  MHRRPC__FHRRPC
e 21 22  FHRRPC__HRRR
e 22 23  HRRR__FHRRP
e 23 24  FHRRP__FRP
e 18 19  FHRRPC__SHRRPC
e 13 14  FHRRPC__FRP
e 14 15  FRP__RHRRPC

