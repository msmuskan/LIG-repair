v 1 SRP
v 2 FRPP
v 3 RBPC
v 4 RIBPC
v 5 REPC
v 6 SRPP
v 7 EPP
v 8 SRP
v 9 FRP
v 10 HRRAN
v 11 HRHA
v 12 SHRRPC
v 13 MHRRPC
v 14 FHRRPC
v 15 EPP
v 16 SLRRP

e 12 13 SHRRPC__MHRRPC
e 13 14 MHRRPC__FHRRPC
e 1 2 SRP__FRPP
e 2 3 FRPP__RBPC
e 2 4 FRPP__RIBPC
e 2 5 FRPP__REPC
e 5 6 REPC__SRPP
e 4 6 RIBPC__SRPP
e 3 6 RBPC__SRPP
e 6 7 SRPP__EPP
e 7 8 EPP__SRP
e 9 10 FRP__HRRAN
e 9 11 FRP__HRHA
e 9 12 FRP__SHRRPC
e 8 9 SRP__FRP
e 15 16 EPP__SLRRP
e 10 15 HRRAN__EPP
e 11 15 HRHA__EPP
e 14 15 FHRRPC__EPP

