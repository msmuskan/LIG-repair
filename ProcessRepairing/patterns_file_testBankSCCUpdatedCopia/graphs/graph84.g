v 1 SRP
v 2 SRPP
v 3 RIBPC
v 4 RBPC
v 5 REPC
v 6 EPP
v 7 SRP
v 8 FRP
v 9 HRRAN
v 10 HRHA
v 11 SHRRPC
v 12 AHRRPC
v 13 FHRRPC
v 14 HRRR
v 15 FHRRP
v 16 FRP
e 1 2  SRP__SRPP
e 2 3  SRPP__RIBPC
e 2 4  SRPP__RBPC
e 2 5  SRPP__REPC
e 9 14  HRRAN__HRRR
e 10 14  HRHA__HRRR
e 11 12  SHRRPC__AHRRPC
e 12 13  AHRRPC__FHRRPC
e 13 14  FHRRPC__HRRR
e 14 15  HRRR__FHRRP
e 15 16  FHRRP__FRP
e 5 6  REPC__EPP
e 4 6  RBPC__EPP
e 3 6  RIBPC__EPP
e 6 7  EPP__SRP
e 8 9  FRP__HRRAN
e 8 10  FRP__HRHA
e 8 11  FRP__SHRRPC
e 7 8  SRP__FRP

