v 1 W-Complete-application-ate-abort
v 2 SUB_1
v 3 SUB_25
v 4 SUB_40
v 5 SUB_58
v 6 SUB_84
v 7 SUB_87

e 6 5 A-Concept__W-Complete-application-suspend
e 6 5 W-Complete-application-start__W-Complete-application-suspend
e 5 3 W-Complete-application-resume__W-Complete-application-suspend
e 3 6 W-Complete-application-resume__W-Complete-application-suspend
e 6 1 O-Created__W-Complete-application-ate-abort
e 6 1 O-Sent-mail-and-online__W-Complete-application-ate-abort
e 1 2 W-Complete-application-ate-abort__W-Call-after-offers-schedule
e 4 2 O-Created__W-Call-after-offers-ate-abort
e 2 4 W-Call-after-offers-suspend__O-Create-Offer
e 2 7 O-Returned__W-Validate-application-suspend
e 2 7 O-Returned__W-Validate-application-resume

