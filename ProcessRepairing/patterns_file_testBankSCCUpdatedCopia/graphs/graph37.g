v 1 SRP
v 2 FRPP
v 3 RBPC
v 4 REPC
v 5 RIBPC
v 6 SRPP
v 7 REPP
v 8 FRPP
v 9 RIBPC
v 10 REPC
v 11 RBPC
v 12 SRPP
v 13 EPP
v 14 SHRRP
v 15 HRRAN
v 16 SHRRPC
v 17 HRHA
v 18 MHRRPC
v 19 LRIRV
v 20 FHRRPC
v 21 RHRRPC
v 22 SHRRPC
v 23 REPC
v 24 MHRRPC
v 25 FHRRPC
v 26 HRRR
v 27 FHRRP
v 28 FRP
e 13 14  EPP__SHRRP
e 14 15  SHRRP__HRRAN
e 14 16  SHRRP__SHRRPC
e 14 17  SHRRP__HRHA
e 15 26  HRRAN__HRRR
e 16 18  SHRRPC__MHRRPC
e 17 26  HRHA__HRRR
e 20 21  FHRRPC__RHRRPC
e 21 22  RHRRPC__SHRRPC
e 24 25  MHRRPC__FHRRPC
e 25 26  FHRRPC__HRRR
e 26 27  HRRR__FHRRP
e 27 28  FHRRP__FRP
e 1 2  SRP__FRPP
e 2 3  FRPP__RBPC
e 2 4  FRPP__REPC
e 2 5  FRPP__RIBPC
e 3 6  RBPC__SRPP
e 4 6  REPC__SRPP
e 5 6  RIBPC__SRPP
e 7 8  REPP__FRPP
e 6 7  SRPP__REPP
e 8 9  FRPP__RIBPC
e 12 13  SRPP__EPP
e 9 10  RIBPC__REPC
e 10 11  REPC__RBPC
e 11 12  RBPC__SRPP
e 18 19  MHRRPC__LRIRV
e 19 20  LRIRV__FHRRPC
e 22 23  SHRRPC__REPC
e 23 24  REPC__MHRRPC

