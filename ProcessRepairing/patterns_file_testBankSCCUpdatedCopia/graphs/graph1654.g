v 1 SRP
v 2 SRPP
v 3 REPC
v 4 RBPC
v 5 FRPP
v 6 EPP
v 7 SHRRP
v 8 SHRRPC
v 9 AHRRPC
v 10 HRRAN
v 11 FHRRPC
v 12 HRHA
v 13 HRRR
v 14 FHRRP
v 15 FRP
e 1 2  SRP__SRPP
e 2 3  SRPP__REPC
e 2 4  SRPP__RBPC
e 3 5  REPC__FRPP
e 4 5  RBPC__FRPP
e 5 6  FRPP__EPP
e 6 7  EPP__SHRRP
e 7 8  SHRRP__SHRRPC
e 7 10  SHRRP__HRRAN
e 7 12  SHRRP__HRHA
e 8 9  SHRRPC__AHRRPC
e 9 11  AHRRPC__FHRRPC
e 10 13  HRRAN__HRRR
e 11 13  FHRRPC__HRRR
e 12 13  HRHA__HRRR
e 13 14  HRRR__FHRRP
e 14 15  FHRRP__FRP

