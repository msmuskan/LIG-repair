v 1 SRP
v 2 FRPP
v 3 RBPC
v 4 RIBPC
v 5 REPC
v 6 SRPP
v 7 REPP
v 8 REPP
v 9 FRPP
v 10 RBPC
v 11 RIBPC
v 12 SRPP
v 13 EPP
v 14 SHRRP
v 15 SHRRPC
v 16 SHRRPC
v 17 AHRRPC
v 18 HRHA
v 19 FHRRPC
v 20 RHRRPC
v 21 SHRRPC
v 22 MHRRPC
v 23 HRRAN
v 24 FHRRPC
v 25 EPP
v 26 SLRRP
e 13 14  EPP__SHRRP
e 14 15  SHRRP__SHRRPC
e 14 18  SHRRP__HRHA
e 14 23  SHRRP__HRRAN
e 17 19  AHRRPC__FHRRPC
e 19 20  FHRRPC__RHRRPC
e 20 21  RHRRPC__SHRRPC
e 21 22  SHRRPC__MHRRPC
e 22 24  MHRRPC__FHRRPC
e 1 2  SRP__FRPP
e 2 3  FRPP__RBPC
e 2 4  FRPP__RIBPC
e 2 5  FRPP__REPC
e 3 6  RBPC__SRPP
e 4 6  RIBPC__SRPP
e 5 6  REPC__SRPP
e 8 9  REPP__FRPP
e 6 7  SRPP__REPP
e 7 8  REPP__REPP
e 9 10  FRPP__RBPC
e 12 13  SRPP__EPP
e 10 11  RBPC__RIBPC
e 11 12  RIBPC__SRPP
e 15 16  SHRRPC__SHRRPC
e 16 17  SHRRPC__AHRRPC
e 25 26  EPP__SLRRP
e 18 25  HRHA__EPP
e 23 25  HRRAN__EPP
e 24 25  FHRRPC__EPP

