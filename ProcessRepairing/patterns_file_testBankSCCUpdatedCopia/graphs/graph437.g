v 1 SRP
v 2 SRPP
v 3 RBPC
v 4 REPC
v 5 RIBPC
v 6 EPP
v 7 SHRRP
v 8 HRHA
v 9 HRRAN
v 10 SHRRPC
v 11 MHRRPC
v 12 RHRRPC
v 13 SHRRPC
v 14 MHRRPC
v 15 FHRRPC
v 16 HRRR
v 17 FHRRP
v 18 FRP
e 1 2  SRP__SRPP
e 2 3  SRPP__RBPC
e 2 4  SRPP__REPC
e 2 5  SRPP__RIBPC
e 6 7  EPP__SHRRP
e 7 8  SHRRP__HRHA
e 7 9  SHRRP__HRRAN
e 7 10  SHRRP__SHRRPC
e 8 16  HRHA__HRRR
e 9 16  HRRAN__HRRR
e 10 11  SHRRPC__MHRRPC
e 12 13  RHRRPC__SHRRPC
e 13 14  SHRRPC__MHRRPC
e 14 15  MHRRPC__FHRRPC
e 15 16  FHRRPC__HRRR
e 16 17  HRRR__FHRRP
e 17 18  FHRRP__FRP
e 5 6  RIBPC__EPP
e 4 6  REPC__EPP
e 3 6  RBPC__EPP
e 11 12  MHRRPC__RHRRPC

