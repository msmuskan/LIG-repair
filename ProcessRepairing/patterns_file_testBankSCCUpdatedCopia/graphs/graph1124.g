v 1 SRP
v 2 SRPP
v 3 REPC
v 4 RIBPC
v 5 RBPC
v 6 FRPP
v 7 REPP
v 8 SRPP
v 9 RIBPC
v 10 REPC
v 11 FRPP
v 12 EPP
v 13 HRRAN
v 14 SHRRPC
v 15 HRHA
v 16 MHRRPC
v 17 FHRRPC
v 18 RHRRPC
v 19 SHRRPC
v 20 MHRRPC
v 21 FHRRPC
v 22 EPP
v 23 SLRRP
e 1 2  SRP__SRPP
e 2 3  SRPP__REPC
e 2 4  SRPP__RIBPC
e 2 5  SRPP__RBPC
e 3 6  REPC__FRPP
e 4 6  RIBPC__FRPP
e 5 6  RBPC__FRPP
e 6 7  FRPP__REPP
e 7 8  REPP__SRPP
e 8 9  SRPP__RIBPC
e 8 10  SRPP__REPC
e 9 11  RIBPC__FRPP
e 10 11  REPC__FRPP
e 11 12  FRPP__EPP
e 14 16  SHRRPC__MHRRPC
e 16 17  MHRRPC__FHRRPC
e 17 18  FHRRPC__RHRRPC
e 18 19  RHRRPC__SHRRPC
e 19 20  SHRRPC__MHRRPC
e 20 21  MHRRPC__FHRRPC
e 12 13  EPP__HRRAN
e 12 14  EPP__SHRRPC
e 12 15  EPP__HRHA
e 22 23  EPP__SLRRP
e 13 22  HRRAN__EPP
e 15 22  HRHA__EPP
e 21 22  FHRRPC__EPP

