v 1 W-Validate-application-suspend
v 2 W-Validate-application-resume
v 3 SUB_37
v 4 SUB_67
v 5 SUB_91

e 5 4 W-Complete-application-complete__W-Call-after-offers-schedule
e 4 1 O-Returned__W-Validate-application-suspend
e 4 2 O-Returned__W-Validate-application-resume
e 1 3 W-Validate-application-suspend__A-Denied
e 2 3 W-Validate-application-resume__A-Denied

