v 1 SRP
v 2 SRPP
v 3 RBPC
v 4 REPC
v 5 FRPP
v 6 EPP
v 7 SHRRP
v 8 HRRAN
v 9 SHRRPC
v 10 AHRRPC
v 11 HRHA
v 12 FHRRPC
v 13 HRRR
v 14 FHRRP
v 15 FRP
e 1 2  SRP__SRPP
e 2 3  SRPP__RBPC
e 2 4  SRPP__REPC
e 3 5  RBPC__FRPP
e 4 5  REPC__FRPP
e 5 6  FRPP__EPP
e 6 7  EPP__SHRRP
e 7 8  SHRRP__HRRAN
e 7 9  SHRRP__SHRRPC
e 7 11  SHRRP__HRHA
e 8 13  HRRAN__HRRR
e 9 10  SHRRPC__AHRRPC
e 10 12  AHRRPC__FHRRPC
e 11 13  HRHA__HRRR
e 12 13  FHRRPC__HRRR
e 13 14  HRRR__FHRRP
e 14 15  FHRRP__FRP

