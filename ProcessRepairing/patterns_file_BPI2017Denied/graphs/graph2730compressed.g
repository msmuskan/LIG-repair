v 1 SUB_10
v 2 SUB_22
v 3 SUB_29
v 4 SUB_34
v 5 SUB_54
v 6 SUB_64

e 6 1 A-Concept__W-Complete-application-suspend
e 6 1 W-Complete-application-start__W-Complete-application-suspend
e 1 6 W-Complete-application-resume__W-Complete-application-suspend
e 6 5 O-Created__W-Complete-application-ate-abort
e 6 5 O-Sent-mail-and-online__W-Complete-application-ate-abort
e 2 4 A-Validating__W-Validate-application-suspend
e 2 4 A-Validating__W-Validate-application-resume
e 5 3 O-Returned__W-Validate-application-complete
e 3 2 W-Call-incomplete-files-resume__W-Validate-application-schedule

