v 1 start
v 2 A-Create-Application
v 3 W-Complete-application-schedule
v 4 W-Complete-application-start
v 5 A-Concept
v 6 A-Accepted
v 7 O-Create-Offer
v 8 O-Created
v 9 W-Complete-application-complete
v 10 W-Call-after-offers-schedule
v 11 W-Call-after-offers-start
v 12 A-Complete
v 13 W-Call-after-offers-complete
v 14 W-Validate-application-schedule
v 15 W-Validate-application-start
v 16 A-Validating
v 17 O-Returned
v 18 W-Validate-application-suspend
v 19 W-Validate-application-resume
v 20 W-Validate-application-suspend
v 21 W-Validate-application-resume
v 22 W-Validate-application-suspend
v 23 A-Denied
v 24 O-Refused
v 25 W-Validate-application-ate-abort
v 26 end
e 1 2  start__A-Create-Application
e 2 3  A-Create-Application__W-Complete-application-schedule
e 2 5  A-Create-Application__A-Concept
e 3 4  W-Complete-application-schedule__W-Complete-application-start
e 4 6  W-Complete-application-start__A-Accepted
e 5 6  A-Concept__A-Accepted
e 6 7  A-Accepted__O-Create-Offer
e 7 8  O-Create-Offer__O-Created
e 8 9  O-Created__W-Complete-application-complete
e 9 10  W-Complete-application-complete__W-Call-after-offers-schedule
e 10 11  W-Call-after-offers-schedule__W-Call-after-offers-start
e 11 12  W-Call-after-offers-start__A-Complete
e 13 14  W-Call-after-offers-complete__W-Validate-application-schedule
e 14 15  W-Validate-application-schedule__W-Validate-application-start
e 15 16  W-Validate-application-start__A-Validating
e 25 26  W-Validate-application-ate-abort__end
e 12 13  A-Complete__W-Call-after-offers-complete
e 16 17  A-Validating__O-Returned
e 17 18  O-Returned__W-Validate-application-suspend
e 17 19  O-Returned__W-Validate-application-resume
e 18 20  W-Validate-application-suspend__W-Validate-application-suspend
e 19 20  W-Validate-application-resume__W-Validate-application-suspend
e 24 25  O-Refused__W-Validate-application-ate-abort
e 20 21  W-Validate-application-suspend__W-Validate-application-resume
e 21 22  W-Validate-application-resume__W-Validate-application-suspend
e 22 23  W-Validate-application-suspend__A-Denied
e 23 24  A-Denied__O-Refused

