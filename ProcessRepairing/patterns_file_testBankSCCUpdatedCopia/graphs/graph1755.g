v 1 SRP
v 2 FRPP
v 3 REPC
v 4 RBPC
v 5 RIBPC
v 6 SRPP
v 7 EPP
v 8 SRP
v 9 FRP
v 10 SHRRPC
v 11 MHRRPC
v 12 HRHA
v 13 FHRRPC
v 14 EPP
v 15 SLRRP
e 10 11  SHRRPC__MHRRPC
e 11 13  MHRRPC__FHRRPC
e 1 2  SRP__FRPP
e 2 3  FRPP__REPC
e 2 4  FRPP__RBPC
e 2 5  FRPP__RIBPC
e 5 6  RIBPC__SRPP
e 4 6  RBPC__SRPP
e 3 6  REPC__SRPP
e 6 7  SRPP__EPP
e 7 8  EPP__SRP
e 9 10  FRP__SHRRPC
e 9 12  FRP__HRHA
e 8 9  SRP__FRP
e 14 15  EPP__SLRRP
e 7 14  EPP__EPP

