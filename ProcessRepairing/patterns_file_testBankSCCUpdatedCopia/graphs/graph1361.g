v 1 SRP
v 2 SRPP
v 3 REPC
v 4 RIBPC
v 5 RBPC
v 6 FRPP
v 7 EPP
v 8 SHRRP
v 9 HRHA
v 10 MHRRPC
v 11 SHRRPC
v 12 HRRAN
v 13 AHRRPC
v 14 FHRRPC
v 15 FRP
v 16 RHRRPC
v 17 SHRRPC
v 18 MHRRPC
v 19 FHRRPC
v 20 HRRR
v 21 FHRRP
v 22 FRP
e 1 2  SRP__SRPP
e 2 3  SRPP__REPC
e 2 4  SRPP__RIBPC
e 2 5  SRPP__RBPC
e 3 6  REPC__FRPP
e 4 6  RIBPC__FRPP
e 5 6  RBPC__FRPP
e 6 7  FRPP__EPP
e 7 8  EPP__SHRRP
e 8 9  SHRRP__HRHA
e 8 11  SHRRP__SHRRPC
e 8 12  SHRRP__HRRAN
e 11 13  SHRRPC__AHRRPC
e 12 20  HRRAN__HRRR
e 13 14  AHRRPC__FHRRPC
e 16 17  RHRRPC__SHRRPC
e 17 18  SHRRPC__MHRRPC
e 18 19  MHRRPC__FHRRPC
e 19 20  FHRRPC__HRRR
e 20 21  HRRR__FHRRP
e 21 22  FHRRP__FRP
e 10 20  MHRRPC__HRRR
e 9 10  HRHA__MHRRPC
e 14 15  FHRRPC__FRP
e 15 16  FRP__RHRRPC

