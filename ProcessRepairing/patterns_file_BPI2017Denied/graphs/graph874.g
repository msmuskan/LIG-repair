v 1 start
v 2 A-Create-Application
v 3 W-Complete-application-schedule
v 4 W-Complete-application-start
v 5 A-Concept
v 6 A-Accepted
v 7 O-Create-Offer
v 8 O-Created
v 9 O-Sent-mail-and-online
v 10 W-Complete-application-complete
v 11 W-Call-after-offers-schedule
v 12 W-Call-after-offers-start
v 13 A-Complete
v 14 W-Call-after-offers-suspend
v 15 O-Create-Offer
v 16 O-Created
v 17 O-Sent-mail-and-online
v 18 W-Call-after-offers-resume
v 19 W-Call-after-offers-suspend
v 20 W-Call-after-offers-resume
v 21 W-Call-after-offers-suspend
v 22 O-Create-Offer
v 23 O-Created
v 24 O-Sent-mail-and-online
v 25 W-Call-after-offers-resume
v 26 W-Call-after-offers-suspend
v 27 W-Call-after-offers-ate-abort
v 28 W-Validate-application-schedule
v 29 W-Validate-application-start
v 30 A-Validating
v 31 O-Returned
v 32 W-Validate-application-suspend
v 33 W-Validate-application-resume
v 34 W-Validate-application-suspend
v 35 W-Validate-application-resume
v 36 A-Denied
v 37 O-Refused
v 38 O-Refused
v 39 O-Refused
v 40 W-Validate-application-complete
v 41 end
e 1 2  start__A-Create-Application
e 2 3  A-Create-Application__W-Complete-application-schedule
e 2 5  A-Create-Application__A-Concept
e 3 4  W-Complete-application-schedule__W-Complete-application-start
e 4 6  W-Complete-application-start__A-Accepted
e 5 6  A-Concept__A-Accepted
e 6 7  A-Accepted__O-Create-Offer
e 7 8  O-Create-Offer__O-Created
e 7 9  O-Create-Offer__O-Sent-mail-and-online
e 8 10  O-Created__W-Complete-application-complete
e 9 10  O-Sent-mail-and-online__W-Complete-application-complete
e 10 11  W-Complete-application-complete__W-Call-after-offers-schedule
e 11 12  W-Call-after-offers-schedule__W-Call-after-offers-start
e 12 13  W-Call-after-offers-start__A-Complete
e 13 14  A-Complete__W-Call-after-offers-suspend
e 13 18  A-Complete__W-Call-after-offers-resume
e 27 28  W-Call-after-offers-ate-abort__W-Validate-application-schedule
e 28 29  W-Validate-application-schedule__W-Validate-application-start
e 29 30  W-Validate-application-start__A-Validating
e 40 41  W-Validate-application-complete__end
e 17 28  O-Sent-mail-and-online__W-Validate-application-schedule
e 14 15  W-Call-after-offers-suspend__O-Create-Offer
e 15 16  O-Create-Offer__O-Created
e 16 17  O-Created__O-Sent-mail-and-online
e 18 19  W-Call-after-offers-resume__W-Call-after-offers-suspend
e 26 27  W-Call-after-offers-suspend__W-Call-after-offers-ate-abort
e 19 20  W-Call-after-offers-suspend__W-Call-after-offers-resume
e 20 21  W-Call-after-offers-resume__W-Call-after-offers-suspend
e 21 22  W-Call-after-offers-suspend__O-Create-Offer
e 22 23  O-Create-Offer__O-Created
e 23 24  O-Created__O-Sent-mail-and-online
e 24 25  O-Sent-mail-and-online__W-Call-after-offers-resume
e 25 26  W-Call-after-offers-resume__W-Call-after-offers-suspend
e 30 31  A-Validating__O-Returned
e 31 32  O-Returned__W-Validate-application-suspend
e 31 33  O-Returned__W-Validate-application-resume
e 32 34  W-Validate-application-suspend__W-Validate-application-suspend
e 33 34  W-Validate-application-resume__W-Validate-application-suspend
e 39 40  O-Refused__W-Validate-application-complete
e 34 35  W-Validate-application-suspend__W-Validate-application-resume
e 35 36  W-Validate-application-resume__A-Denied
e 36 37  A-Denied__O-Refused
e 37 38  O-Refused__O-Refused
e 38 39  O-Refused__O-Refused

