v 1 SRP
v 2 SRPP
v 3 REPC
v 4 RIBPC
v 5 RBPC
v 6 FRPP
v 7 SHRRP
v 8 SHRRPC
v 9 AHRRPC
v 10 HRHA
v 11 FHRRPC
v 12 HRRAN
v 13 RHRRPC
v 14 SHRRPC
v 15 MHRRPC
v 16 FHRRPC
v 17 RHRRPC
v 18 SHRRPC
v 19 AHRRPC
v 20 HRRR
v 21 FHRRP
v 22 FRP
e 1 2  SRP__SRPP
e 2 3  SRPP__REPC
e 2 4  SRPP__RIBPC
e 2 5  SRPP__RBPC
e 3 6  REPC__FRPP
e 4 6  RIBPC__FRPP
e 5 6  RBPC__FRPP
e 7 8  SHRRP__SHRRPC
e 7 10  SHRRP__HRHA
e 7 12  SHRRP__HRRAN
e 8 9  SHRRPC__AHRRPC
e 9 11  AHRRPC__FHRRPC
e 10 20  HRHA__HRRR
e 11 13  FHRRPC__RHRRPC
e 12 20  HRRAN__HRRR
e 13 14  RHRRPC__SHRRPC
e 14 15  SHRRPC__MHRRPC
e 15 16  MHRRPC__FHRRPC
e 16 17  FHRRPC__RHRRPC
e 17 18  RHRRPC__SHRRPC
e 18 19  SHRRPC__AHRRPC
e 20 21  HRRR__FHRRP
e 21 22  FHRRP__FRP
e 6 7  FRPP__SHRRP
e 19 20  AHRRPC__HRRR

