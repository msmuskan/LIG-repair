v 1 SRP
v 2 SRPP
v 3 RBPC
v 4 REPC
v 5 RIBPC
v 6 FRPP
v 7 EPP
v 8 SHRRP
v 9 SHRRPC
v 10 AHRRPC
v 11 HRHA
v 12 FHRRPC
v 13 HRRAN
v 14 SHRRPC
v 15 MHRRPC
v 16 FHRRPC
v 17 HRRR
v 18 FRP
e 1 2  SRP__SRPP
e 2 3  SRPP__RBPC
e 2 4  SRPP__REPC
e 2 5  SRPP__RIBPC
e 3 6  RBPC__FRPP
e 4 6  REPC__FRPP
e 5 6  RIBPC__FRPP
e 6 7  FRPP__EPP
e 7 8  EPP__SHRRP
e 8 9  SHRRP__SHRRPC
e 8 11  SHRRP__HRHA
e 8 13  SHRRP__HRRAN
e 9 10  SHRRPC__AHRRPC
e 10 12  AHRRPC__FHRRPC
e 11 17  HRHA__HRRR
e 13 17  HRRAN__HRRR
e 14 15  SHRRPC__MHRRPC
e 15 16  MHRRPC__FHRRPC
e 16 17  FHRRPC__HRRR
e 12 14  FHRRPC__SHRRPC
e 17 18  HRRR__FRP

