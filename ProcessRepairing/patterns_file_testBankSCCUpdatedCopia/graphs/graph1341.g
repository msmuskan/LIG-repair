v 1 SRP
v 2 FRPP
v 3 RIBPC
v 4 RBPC
v 5 REPC
v 6 SRPP
v 7 FRP
v 8 EPP
v 9 SHRRP
v 10 HRRAN
v 11 HRHA
v 12 SHRRPC
v 13 MHRRPC
v 14 FHRRPC
v 15 RHRRPC
v 16 SHRRPC
v 17 MHRRPC
v 18 FHRRPC
v 19 EPP
v 20 SLRRP
e 8 9  EPP__SHRRP
e 9 10  SHRRP__HRRAN
e 9 11  SHRRP__HRHA
e 9 12  SHRRP__SHRRPC
e 12 13  SHRRPC__MHRRPC
e 13 14  MHRRPC__FHRRPC
e 14 15  FHRRPC__RHRRPC
e 15 16  RHRRPC__SHRRPC
e 16 17  SHRRPC__MHRRPC
e 17 18  MHRRPC__FHRRPC
e 1 2  SRP__FRPP
e 2 3  FRPP__RIBPC
e 2 4  FRPP__RBPC
e 2 5  FRPP__REPC
e 5 6  REPC__SRPP
e 4 6  RBPC__SRPP
e 3 6  RIBPC__SRPP
e 7 8  FRP__EPP
e 6 7  SRPP__FRP
e 19 20  EPP__SLRRP
e 10 19  HRRAN__EPP
e 11 19  HRHA__EPP
e 18 19  FHRRPC__EPP

