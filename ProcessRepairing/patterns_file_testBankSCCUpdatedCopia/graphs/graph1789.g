v 1 SRP
v 2 SRPP
v 3 RIBPC
v 4 SHRRP
v 5 RBPC
v 6 REPC
v 7 FRPP
v 8 REPP
v 9 FRPP
v 10 RBPC
v 11 RIBPC
v 12 SRPP
v 13 REPP
v 14 FRPP
v 15 RBPC
v 16 REPC
v 17 RIBPC
v 18 SRPP
v 19 EPP
v 20 SRP
v 21 FRP
v 22 HRHA
v 23 SHRRPC
v 24 AHRRPC
v 25 HRRAN
v 26 FHRRPC
v 27 EPP
v 28 SLRRP
e 1 2  SRP__SRPP
e 2 3  SRPP__RIBPC
e 2 5  SRPP__RBPC
e 2 6  SRPP__REPC
e 5 7  RBPC__FRPP
e 6 7  REPC__FRPP
e 7 8  FRPP__REPP
e 23 24  SHRRPC__AHRRPC
e 24 26  AHRRPC__FHRRPC
e 4 7  SHRRP__FRPP
e 3 4  RIBPC__SHRRP
e 8 9  REPP__FRPP
e 11 12  RIBPC__SRPP
e 9 10  FRPP__RBPC
e 10 11  RBPC__RIBPC
e 12 13  SRPP__REPP
e 14 15  FRPP__RBPC
e 14 16  FRPP__REPC
e 14 17  FRPP__RIBPC
e 13 14  REPP__FRPP
e 17 18  RIBPC__SRPP
e 16 18  REPC__SRPP
e 15 18  RBPC__SRPP
e 18 19  SRPP__EPP
e 19 20  EPP__SRP
e 21 22  FRP__HRHA
e 21 23  FRP__SHRRPC
e 21 25  FRP__HRRAN
e 20 21  SRP__FRP
e 27 28  EPP__SLRRP
e 22 27  HRHA__EPP
e 25 27  HRRAN__EPP
e 26 27  FHRRPC__EPP

