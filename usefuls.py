# Austin TX zip codes
atx_zip_codes = [78610, 78613, 78617, 78641, 78652, 78653, 78660, 
        78664, 78681, 78701, 78702, 78703, 78704, 78705, 78712, 78717, 
        78719, 78721, 78722, 78723, 78724, 78725, 78726, 78727, 78728, 
        78729, 78730, 78731, 78732, 78733, 78734, 78735, 78736, 78737, 
        78738, 78739, 78741, 78742, 78744, 78745, 78746, 78747, 78748, 
        78749, 78750, 78751, 78752, 78753, 78754, 78756, 78757, 78758, 78759]
# Same, but as a paramenter for Census API wrapper
zipcode_tabulation_area = 'zip code tabulation area: 78610, 78613, 78617, 78641, 78652, 78653, 78660, 78664, 78681, 78701, 78702, 78703, 78704,78705, 78712, 78717, 78719, 78721, 78722, 78723, 78724, 78725, 78726,78727, 78728, 78729, 78730, 78731, 78732, 78733, 78734, 78735, 78736,78737, 78738, 78739, 78741, 78742, 78744, 78745, 78746, 78747, 78748, 78749, 78750, 78751, 78752, 78753, 78754, 78756, 78757,78758, 78759'

# Combine similar offenses
similar_offense_type = {'ABUSE OF 911': 'Other',
                        'ABUSE OF CORPSE': 'Other',
                        'ABUSE OF OFFICIAL CAPACITY': 'Other',
                        'AGG ASLT ENHANC STRANGL/SUFFOC': 'Aggravated Assault',
                        'AGG ASLT STRANGLE/SUFFOCATE': 'Aggravated Assault',
                        'AGG ASLT W/MOTOR VEH FAM/DAT V': 'Aggravated Assault',
                        'AGG ASSAULT': 'Aggravated Assault',
                        'AGG ASSAULT FAM/DATE VIOLENCE': 'Aggravated Assault',
                        'AGG ASSAULT ON PUBLIC SERVANT': 'Aggravated Assault',
                        'AGG ASSAULT WITH MOTOR VEH': 'Aggravated Assault',
                        'AGG FORCED SODOMY': 'Sexual Assault',
                        'AGG FORCED SODOMY OF CHILD': 'Sexual Assault',
                        'AGG KIDNAPPING': 'Other',
                        'AGG KIDNAPPING FAM VIO': 'Other',
                        'AGG PERJURY': 'Other',
                        'AGG PROMOTION OF PROSTITUTION': 'Other',
                        'AGG RAPE': 'Sexual Assault',
                        'AGG RAPE OF A CHILD': 'Sexual Assault',
                        'AGG ROBBERY BY ASSAULT': 'Robbery',
                        'AGG ROBBERY/DEADLY WEAPON': 'Robbery',
                        'AGG SEXUAL ASSAULT CHILD/OBJEC': 'Sexual Assault',
                        'AGG SEXUAL ASSAULT W OBJECT': 'Sexual Assault',
                        'AGG SODOMY': 'Sexual Assault',
                        'AIRPORT - BOMB THREAT': 'Other',
                        'AIRPORT - BREACH OF SECURITY': 'Other',
                        'AIRPORT - CRIMINAL TRESPASS': 'Other',
                        'AIRPORT - FEDERAL VIOL': 'Other',
                        'AIRPORT - SUSPICIOUS PERSON': 'Other',
                        'AIRPORT PLACES WEAPON PROHIBIT': 'Other',
                        'AMPLIFIED MUSIC / VEHICLE': 'Other',
                        'APPLIC TO REVOKE PROBATION': 'Other',
                        'ARSON': 'Arson',
                        'ARSON WITH BODILY INJURY': 'Arson',
                        'ASSAULT  CONTACT-SEXUAL NATURE': 'Sexual Assault',
                        'ASSAULT - SCHOOL PERSONNEL': 'Aggravated Assault',
                        'ASSAULT BY CONTACT': 'Aggravated Assault',
                        'ASSAULT BY CONTACT FAM/DATING': 'Aggravated Assault',
                        'ASSAULT BY THREAT': 'Aggravated Assault',
                        'ASSAULT BY THREAT FAM/DATING': 'Aggravated Assault',
                        'ASSAULT ON PEACE OFFICER': 'Aggravated Assault',
                        'ASSAULT ON PUBLIC SERVANT': 'Aggravated Assault',
                        'ASSAULT W/INJURY-FAM/DATE VIOL': 'Aggravated Assault',
                        'ASSAULT WITH INJURY': 'Aggravated Assault',
                        'ATTACK ON ASSISTANCE ANIMAL': 'Other',
                        'AUTO THEFT': 'Motor Vehicle Theft',
                        'AWOL': 'Other',
                        'BAIL JUMPING/FAIL TO APPEAR': 'Other',
                        'BANK KITING': 'Other',
                        'BESTIALITY': 'Other',
                        'BOATING WHILE INTOXICATED': 'Other',
                        'BOMB THREAT': 'Other',
                        'BOMB THREAT - AIRCRAFT': 'Other',
                        'BREACH OF COMPUTER SECURITY': 'Other',
                        'BRIBERY': 'Other',
                        'BURG NON RESIDENCE SHEDS': 'Burglary',
                        'BURG OF RES - FAM/DATING ASLT': 'Burglary',
                        'BURG OF RES - SEXUAL NATURE': 'Burglary',
                        'BURGLARY NON RESIDENCE': 'Burglary',
                        'BURGLARY OF COIN-OP MACHINE': 'Burglary',
                        'BURGLARY OF RESIDENCE': 'Burglary',
                        'BURGLARY OF VEHICLE': 'Burglary',
                        'BWI-EXPIRED USE 2110': 'Other',
                        'CAPITAL MURDER': 'Murder',
                        'CHILD CUSTODY INTERFERE': 'Other',
                        'CHILD ENDANGERMENT- ABANDONMEN': 'Other',
                        'CIVIL DISTURBANCE/DEMO': 'Other',
                        'COMMUNICATING GAMBLING INFO': 'Other',
                        'COMPELLING PROSTITUTION': 'Other',
                        'CONT SEX ABUSE OF CHILD': 'Sexual Assault',
                        'CONTEMPT OF COURT': 'Other',
                        'CONTROLLED SUB VIOL - OTHER': 'Other',
                        'COUNTERFEITING': 'Other',
                        'CRASH/FAIL STOP AND RENDER AID': 'Other',
                        'CRASH/INTOX MANSLAUGHTER': 'Manslaughter',
                        'CRASH/INTOXICATION ASSAULT': 'Aggravated Assault',
                        'CRASH/MANSLAUGHTER': 'Manslaughter',
                        'CRASH/MURDER': 'Murder',
                        'CRED CARD ABUSE - EXPIR-CANCEL': 'Other',
                        'CRED CARD ABUSE - OTHER': 'Other',
                        'CRED CARD ABUSE BY FORGERY': 'Other',
                        'CRIM NEG HOMICIDE/NON TRAFFIC': 'Negligent Homicide',
                        'CRIMES AGAINST ELDERLY': 'Other',
                        'CRIMINAL CONSPIRACY': 'Other',
                        'CRIMINAL MISCHIEF': 'Other',
                        'CRIMINAL MISCHIEF BY ARSON': 'Arson',
                        'CRIMINAL NONSUPPORT': 'Other',
                        'CRIMINAL SOLICITATION': 'Other',
                        'CRIMINAL SOLICITATION OF MINOR': 'Other',
                        'CRIMINAL TRESPASS': 'Other',
                        'CRIMINAL TRESPASS/HOTEL': 'Other',
                        'CRIMINAL TRESPASS/IN VEHICLE': 'Other',
                        'CRIMINAL TRESPASS/TRANSIENT': 'Other',
                        'CRUELTY TO ANIMALS': 'Other',
                        'CUSTODY ARREST TRAFFIC WARR': 'Other',
                        'DAMAGE CITY PROP': 'Other',
                        'DAMAGE CITY VEHICLE': 'Other',
                        'DANG DRUG VIOL - OTHER': 'Other',
                        'DATING DISTURBANCE': 'Other',
                        'DEADLY CONDUCT': 'Aggravated Assault',
                        'DEADLY CONDUCT FAM/DATE VIOL': 'Aggravated Assault',
                        'DEBIT CARD ABUSE': 'Other',
                        'DEL CONTROLLED SUB/NARCOTIC': 'Other',
                        'DEL CONTROLLED SUB/OTHER': 'Other',
                        'DEL CONTROLLED SUB/SYN NARC': 'Other',
                        'DEL MARIJUANA': 'Other',
                        'DEL OF ALCOHOL TO MINOR': 'Other',
                        'DEL OF DANG DRUG': 'Other',
                        'DEL SYNTHETIC MARIJUANA': 'Other',
                        'DELIVERY OF PRESCRIPTION FORM': 'Other',
                        'DEPENDENT AND NEGLECTED CHILD': 'Other',
                        'DESECRATION VENERATED OBJECT': 'Other',
                        'DESERTION': 'Other',
                        'DISCLOS/PROMO INTIMATE VISUAL': 'Other',
                        'DISPOSAL OF SOLID WASTE': 'Other',
                        'DISRUPTING MEETING/PROCESSION': 'Other',
                        'DISRUPTION OF CLASSES': 'Other',
                        'DISRUPTIVE ACTS AT SCHOOLS': 'Other',
                        'DISTRIB HARMFUL MATERIAL MINOR': 'Other',
                        'DISTURBANCE - OTHER': 'Other',
                        'DOC ABUSE OR THREAT': 'Other',
                        'DOC ABUSIVE LANGUAGE': 'Other',
                        'DOC CREATING NOXIOUS ODOR': 'Other',
                        'DOC DISCHARGE GUN - PUB PLACE': 'Other',
                        'DOC DISCHARGE GUN - PUB ROAD': 'Other',
                        'DOC DISPLAY GUN/DEADLY PUB PLC': 'Other',
                        'DOC EXPOSURE': 'Other',
                        'DOC FIGHTING': 'Other',
                        'DOC OFFENSIVE GESTURE': 'Other',
                        'DOC UNREASONABLE NOISE': 'Other',
                        'DOC WINDOW PEEPING - HOTEL': 'Other',
                        'DOC WINDOW PEEPING - PUB AREA': 'Other',
                        'DOC WINDOW PEEPING-RESIDENCE': 'Other',
                        'DOMESTIC VIOLENCE/ALARM': 'Aggravated Assault',
                        'DRINKING AFTER CURFEW': 'Other',
                        'DRIVING WHILE INTOX / FELONY': 'Other',
                        'DUI - AGE 16 AND UNDER': 'Other',
                        'DUI - AGE 17 TO 20': 'Other',
                        'DUMPING REFUSE NEAR HIGHWAY': 'Other',
                        'DWI': 'Other',
                        'DWI  .15 BAC OR ABOVE': 'Other',
                        'DWI - CHILD PASSENGER': 'Other',
                        'DWI - DRUG RECOGNITION EXPERT': 'Other',
                        'DWI 2ND': 'Other',
                        'ENTICING A CHILD': 'Other',
                        'ESCAPE FROM CUSTODY': 'Other',
                        'EVADING / FOOT': 'Other',
                        'EVADING / VEHICLE PURSUIT': 'Other',
                        'EVADING VEHICLE': 'Other',
                        'EXP-VIOL CITY ORDINANCE - TAXI': 'Other',
                        'EXPIRED-EVADING ARREST': 'Other',
                        'EXPLOITATION OF CHILD/ELDERLY': 'Other',
                        'EXPLOSIVE ORDNANCE DISPOSAL': 'Other',
                        'FAIL DISPLAY HANDGUN LICENSE': 'Other',
                        'FAILURE TO IDENTIFY': 'Other',
                        'FAILURE TO REG AS SEX OFFENDER': 'Other',
                        'FALSE ALARM OR REPORT': 'Other',
                        'FALSE ID AS A PEACE OFFICER': 'Other',
                        'FALSE REPORT TO CPS': 'Other',
                        'FALSE REPORT TO PEACE OFFICER': 'Other',
                        'FALSE STATEMENT -OBTAIN CREDIT': 'Other',
                        'FAMILY DISTURBANCE': 'Other',
                        'FAMILY DISTURBANCE/PARENTAL': 'Other',
                        'FEDERAL VIOL/OTHER': 'Other',
                        'FELONY ENHANCEMENT/ASSLT W/INJ': 'Aggravated Assault',
                        'FIREARMS ON SCHOOL PROP': 'Other',
                        'FORCED SODOMY': 'Sexual Assault',
                        'FORCED SODOMY OF CHILD': 'Sexual Assault',
                        'FORGERY - OTHER': 'Other',
                        'FORGERY AND PASSING': 'Other',
                        'FORGERY BY ALTERATION': 'Other',
                        'FORGERY BY MAKING': 'Other',
                        'FORGERY OF IDENTIFICATION': 'Other',
                        'FORGERY- CERTIFICATE OF TITLE': 'Other',
                        'FRAUD - OTHER': 'Other',
                        'FRAUD DESTRUCTION OF A WRITING': 'Other',
                        'FRAUD FILING FINANCE STATEMENT': 'Other',
                        'FRAUD-CARD SKIMMER': 'Other',
                        'GAMBLING': 'Other',
                        'GAMBLING PROMOTION': 'Other',
                        'GIFT TO PUBLIC SERVANT': 'Other',
                        'GRAFFITI': 'Other',
                        'HARASSMENT': 'Other',
                        'HARASSMENT OF A PUBLIC SERVANT': 'Other',
                        'HARASSMENT ONLINE': 'Other',
                        'HARBORING RUNAWAY CHILD': 'Other',
                        'HAZING': 'Other',
                        'HINDER SECURED CREDITORS': 'Other',
                        'HINDERING APPREHENSION': 'Other',
                        'HINDERING PROCEEDING': 'Other',
                        'IDENTITY THEFT': 'Other',
                        'IDENTITY THEFT-TAX RETURNS': 'Other',
                        'ILLEGAL LABELLING OF RECORDING': 'Other',
                        'ILLUMIN AIRCRAFT INTENSE LIGHT': 'Other',
                        'IMMIGRATION HOLD/ARREST': 'Other',
                        'IMPERSONATING PUBLIC SERVANT': 'Other',
                        'IMPROPER CONTACT-SEX ASLT VICT': 'Sexual Assault',
                        'INDECENCY WITH A CHILD/CONTACT': 'Sexual Assault',
                        'INDECENCY WITH CHILD/EXPOSURE': 'Sexual Assault',
                        'INDECENT EXPOSURE': 'Sexual Assault',
                        'INHALANT ABUSE': 'Other',
                        'INJ TO DISABLED  FAM/DATE VIOL': 'Other',
                        'INJ TO ELDERLY   FAM/DATE VIOL': 'Other',
                        'INJ/CHILD FV (NO CARE/CUSTODY)': 'Other',
                        'INJURY DISABLED INDIVIDUAL': 'Other',
                        'INJURY TO CHILD': 'Other',
                        'INJURY TO CHILD (CARE/CUSTODY)': 'Other',
                        'INJURY TO ELDERLY PERSON': 'Other',
                        'INTER EMERG PHONECALL FAM/DATE': 'Other',
                        'INTERFERE W PO SERVICE ANIMALS': 'Other',
                        'INTERFERENCE PUBLIC DUTIES': 'Other',
                        'INTERFERING W/EMERG PHONE CALL': 'Other',
                        'INVASIVE VISUAL RECORDING': 'Other',
                        'ISSUANCE OF BAD CHECK': 'Other',
                        'JUSTIFIED HOMICIDE': 'Other',
                        'KEEPING GAMBLING PLACE': 'Other',
                        'KIDNAPPING': 'Other',
                        'KIDNAPPING FAM VIO': 'Other',
                        'LIQUOR LAW VIOLATION/OTHER': 'Other',
                        'LITTERING': 'Other',
                        'LOITERING ON SCHOOL PROP': 'Other',
                        'MAKING TOBACCO AVAIL TO MINOR': 'Other',
                        'MANF CONTROLLED SUB - OTHER': 'Other',
                        'MANF CONTROLLED SUB- SYN NARC': 'Other',
                        'MANSLAUGHTER': 'Manslaughter',
                        'MISAPPLY FIDUCIARY PROP': 'Other',
                        'MISREP AGE BY MINOR': 'Other',
                        'MISUSE OF OFFICIAL INFO': 'Other',
                        'MONEY LAUNDERING': 'Other',
                        'MURDER': 'Murder',
                        'NUISANCE ABATEMENT': 'Other',
                        'OBSCENE DISPLAY - DISTRIBUTION': 'Other',
                        'OBSCENITY': 'Other',
                        'OBTAIN CONTROLLED SUB BY FRAUD': 'Other',
                        'OBTAIN DANG DRUG BY FRAUD': 'Other',
                        'OFFICIAL MISCONDUCT': 'Other',
                        'OFFICIAL OPPRESSION': 'Other',
                        'ONLINE IMPERSONATION': 'Other',
                        'ONLINE SOLICITATION OF A MINOR': 'Other',
                        'PAROLE VIOL': 'Other',
                        'PERJURY': 'Other',
                        'PIGEON DROP': 'Other',
                        'POCKET PICKING': 'Other',
                        'POSS CONTROLLED SUB/NARCOTIC': 'Other',
                        'POSS CONTROLLED SUB/OTHER': 'Other',
                        'POSS CONTROLLED SUB/SYN NARC': 'Other',
                        'POSS CRIMINAL INSTRUMENT': 'Other',
                        'POSS DANG DRUG': 'Other',
                        'POSS MARIJUANA': 'Other',
                        'POSS OF ALCOHOL - AGE 17 TO 20': 'Other',
                        'POSS OF ALCOHOL-AGE 16 & UNDER': 'Other',
                        'POSS OF DRUG PARAPHERNALIA': 'Other',
                        'POSS OF FIREARM BY FELON': 'Other',
                        'POSS OF GAMBLING EQUIPMENT': 'Other',
                        'POSS OF GAMBLING PARAPHERNALIA': 'Other',
                        'POSS OF LIQ ON SCHOOL PROP': 'Other',
                        'POSS OF PRESCRIPTION FORM': 'Other',
                        'POSS OF PROHIBITED WEAPON': 'Other',
                        'POSS SYNTHETIC MARIJUANA': 'Other',
                        'POSS/PROMO CHILD PORNOGRAPHY': 'Other',
                        'POSSESSION OF FORGED WRITING': 'Other',
                        'PRACTICE MEDICINE W/OUT LICENS': 'Other',
                        'PROBATION VIOL': 'Other',
                        'PROHIBITED SEX CONDUCT-INCEST': 'Other',
                        'PROMOTION OF PROSTITUTION': 'Other',
                        'PROSTITUTION': 'Other',
                        'PROTECTIVE ORDER': 'Other',
                        'PROWLER': 'Other',
                        'PUBLIC INTOX-SOBERING CENTER': 'Other',
                        'PUBLIC INTOXICATION': 'Other',
                        'PUBLIC LEWDNESS': 'Other',
                        'PURCHASING PROSTITUTION': 'Other',
                        'PURSE SNATCHING': 'Other',
                        'RAPE': 'Sexual Assault',
                        'RAPE OF A CHILD': 'Sexual Assault',
                        'RECKLESS CONDUCT': 'Other',
                        'RECKLESS DAMAGE': 'Other',
                        'RENTAL CAR/FAIL TO RETURN': 'Other',
                        'RESISTING ARREST OR SEARCH': 'Other',
                        'RETALIATION': 'Other',
                        'ROBBERY BY ASSAULT': 'Robbery',
                        'ROBBERY BY THREAT': 'Robbery',
                        'RUNAWAY CHILD': 'Other',
                        'SALE OF LIQ IN PROHIB AREA': 'Other',
                        'SALE OF LIQ WITHOUT PERMIT': 'Other',
                        'SALE OR PURCHASE OF CHILD': 'Other',
                        'SECURING EXEC-DOC BY DECEPTION': 'Other',
                        'SERIOUS INJURY TO A CHILD': 'Other',
                        'SEXTING DEPICTING A MINOR': 'Other',
                        'SEXUAL ASSAULT OF CHILD/OBJECT': 'Sexual Assault',
                        'SEXUAL ASSAULT W/ OBJECT': 'Sexual Assault',
                        'SEXUAL PERFORMANCE BY CHILD': 'Sexual Assault',
                        'SIT AND LIE ORDINANCE VIOL': 'Other',
                        'SMUGGLING ILLEGAL ALIEN': 'Other',
                        'SOLICITATION - BEGGING': 'Other',
                        'STALKING': 'Other',
                        'STATUTORY RAPE OF CHILD': 'Sexual Assault',
                        'STAY AWAY ORDER': 'Other',
                        'SUSPICIOUS PERSON': 'Other',
                        'TAKE WEAPON FRM POLICE OFFICER': 'Other',
                        'TAMPERING WITH CONSUMER PROD': 'Other',
                        'TAMPERING WITH EVIDENCE': 'Other',
                        'TAMPERING WITH GOV RECORD': 'Other',
                        'TAMPERING WITH ID NUMBER': 'Other',
                        'TAMPERING WITH WITNESS': 'Other',
                        'TELECOMMUNICATION CRIMES/OTHER': 'Other',
                        'TERRORISTIC THREAT': 'Other',
                        'TERRORISTIC THREAT-FAM/DAT VIO': 'Other',
                        'TERRORISTIC THREAT-MASS CASLTY': 'Other',
                        'THEFT': 'Theft',
                        'THEFT BY CHECK': 'Theft',
                        'THEFT BY EMBEZZLEMENT': 'Theft',
                        'THEFT BY EXTORTION': 'Theft',
                        'THEFT BY FALSE PRETEXT/BUNCO': 'Theft',
                        'THEFT BY PUBLIC SERVANT': 'Theft',
                        'THEFT BY SHOPLIFTING': 'Theft',
                        'THEFT CATALYTIC CONVERTER': 'Theft',
                        'THEFT FROM AUTO': 'Theft',
                        'THEFT FROM BUILDING': 'Theft',
                        'THEFT FROM PERSON': 'Theft',
                        'THEFT OF AUTO PARTS': 'Theft',
                        'THEFT OF BICYCLE': 'Theft',
                        'THEFT OF HEAVY EQUIPMENT': 'Theft',
                        'THEFT OF LICENSE PLATE': 'Theft',
                        'THEFT OF METAL': 'Theft',
                        'THEFT OF SERVICE': 'Theft',
                        'THEFT OF TELECOMMUNICATION SRV': 'Theft',
                        'THEFT OF TRAILER': 'Theft',
                        'THEFT- APPROPRIATE STOLEN PROP': 'Theft',
                        'THEFT/TILL TAPPING': 'Theft',
                        'TOBACCO VIOL - AGE 17': 'Other',
                        'TOBACCO VIOL - UNDER AGE 17': 'Other',
                        'TRADEMARK COUNTERFEITING': 'Other',
                        'TRAFFICKING OF PERSONS': 'Other',
                        'TRUANCY': 'Other',
                        'UCW LICENSE PREMISE': 'Other',
                        'UNAUTHORIZED USE VEH-EXPIRED': 'Other',
                        'UNLAWFUL CARRY-LIC HOLDER': 'Other',
                        'UNLAWFUL CARRYING WEAPON': 'Other',
                        'UNLAWFUL INTERCEPTION': 'Other',
                        'UNLAWFUL RESTRAINT': 'Other',
                        'UNLAWFUL RESTRAINT FAM/DAT VIO': 'Other',
                        'URINATING IN PUBLIC PLACE': 'Other',
                        'VIOL CITY ORDINANCE -  GAME RM': 'Other',
                        'VIOL CITY ORDINANCE - AIRPORT': 'Other',
                        'VIOL CITY ORDINANCE - CURFEW': 'Other',
                        'VIOL CITY ORDINANCE - DOG': 'Other',
                        'VIOL CITY ORDINANCE - OTHER': 'Other',
                        'VIOL CITY ORDINANCE - SMOKING': 'Other',
                        'VIOL CITY ORDINANCE - SOUND': 'Other',
                        'VIOL CITY ORDINANCE - TAXI': 'Other',
                        'VIOL CITY ORDINANCE - TITLE 10': 'Other',
                        'VIOL CITY ORDINANCE - WRECKER': 'Other',
                        'VIOL CITY ORDINANCE -FIREWORK': 'Other',
                        'VIOL CIVIL RIGHTS PRISONER': 'Other',
                        'VIOL GLASS CONTAINER': 'Other',
                        'VIOL OF BOND CONDITIONS': 'Other',
                        'VIOL OF CAMPING ORDINANCE': 'Other',
                        'VIOL OF COURT ORDER-NON EPO-PO': 'Other',
                        'VIOL OF EMERG PROTECTIVE ORDER': 'Other',
                        'VIOL OF PARK CURFEW': 'Other',
                        'VIOL OF PRISONERS RIGHT': 'Other',
                        'VIOL OF PROTECTIVE ORDER': 'Other',
                        'VIOL PO / SEXUAL ASLT VICTIM': 'Other',
                        'VIOL STATE LAW - OTHER': 'Other',
                        'VIOL STATE MASSAGE REGULATIONS': 'Other',
                        'VIOL STAY AWAY ORDER': 'Other',
                        'VIOL TEMP EX PARTE  ORDER': 'Other',
                        'VIOL WATER SAFETY ACT': 'Other',
                        'VOCO - ALCOHOL  CONSUMPTION': 'Other',
                        'VOCO AMPLIFIED MUSIC/VEHICLE': 'Other',
                        'VOCO SOLICITATION PROHIBIT': 'Other',
                        'WARRANT ARREST NON TRAFFIC': 'Other',
                        'WEAPON VIOL - OTHER': 'Other'
}