v 1 SRP
v 2 SRPP
v 3 RBPC
v 4 RIBPC
v 5 REPC
v 6 EPP
v 7 SHRRP
v 8 SHRRPC
v 9 HRRAN
v 10 HRHA
v 11 AHRRPC
v 12 FHRRPC
v 13 HRRR
v 14 FHRRP
v 15 FRP
e 1 2  SRP__SRPP
e 2 3  SRPP__RBPC
e 2 4  SRPP__RIBPC
e 2 5  SRPP__REPC
e 6 7  EPP__SHRRP
e 7 8  SHRRP__SHRRPC
e 7 9  SHRRP__HRRAN
e 7 10  SHRRP__HRHA
e 8 11  SHRRPC__AHRRPC
e 9 13  HRRAN__HRRR
e 10 13  HRHA__HRRR
e 11 12  AHRRPC__FHRRPC
e 12 13  FHRRPC__HRRR
e 13 14  HRRR__FHRRP
e 14 15  FHRRP__FRP
e 5 6  REPC__EPP
e 4 6  RIBPC__EPP
e 3 6  RBPC__EPP

