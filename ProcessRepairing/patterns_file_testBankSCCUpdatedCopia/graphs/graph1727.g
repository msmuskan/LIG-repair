v 1 SRP
v 2 SRPP
v 3 RIBPC
v 4 RBPC
v 5 REPC
v 6 FRPP
v 7 EPP
v 8 SHRRP
v 9 SHRRPC
v 10 SLRRP
v 11 MHRRPC
v 12 HRHA
v 13 FHRRPC
v 14 RHRRPC
v 15 SHRRPC
v 16 AHRRPC
v 17 FHRRPC
v 18 HRRR
v 19 FHRRP
v 20 FRP
e 1 2  SRP__SRPP
e 2 3  SRPP__RIBPC
e 2 4  SRPP__RBPC
e 2 5  SRPP__REPC
e 3 6  RIBPC__FRPP
e 4 6  RBPC__FRPP
e 5 6  REPC__FRPP
e 6 7  FRPP__EPP
e 7 8  EPP__SHRRP
e 8 9  SHRRP__SHRRPC
e 8 12  SHRRP__HRHA
e 11 13  MHRRPC__FHRRPC
e 12 18  HRHA__HRRR
e 13 14  FHRRPC__RHRRPC
e 14 15  RHRRPC__SHRRPC
e 15 16  SHRRPC__AHRRPC
e 16 17  AHRRPC__FHRRPC
e 17 18  FHRRPC__HRRR
e 18 19  HRRR__FHRRP
e 19 20  FHRRP__FRP
e 9 10  SHRRPC__SLRRP
e 10 11  SLRRP__MHRRPC

