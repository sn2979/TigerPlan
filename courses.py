def cla_minor_courses():
    courses = {
        "Prerequisites": ['.*CLA .*', '.*CLG 108.*', '.*LAT 108.*'],
        "Basic Requirements": [".*CLA 203.*", ".*CLA 212.*"],
        "Greek 4": [
            '.*CLG 108.*', '.*CLG 2.*', '.*CLG 3.*', '.*CLG 4.*', '.*CLG 5.*',
            '.*CLA 200.*', '.*CLA 205.*', '.*CLA 216.*', '.*CLA 217.*', '.*CLA 303.*', '.*CLA 307.*',
            '.*CLA 313.*', '.*CLA 319.*', '.*CLA 326.*', '.*CLA 330.*', '.*CLA 357.*', '.*CLA 400.*',
            '.*CLA 412.*', '.*CLA 414.*', '.*CLA 502.*', '.*CLA 505.*', '.*CLA 506.*', '.*CLA 514.*',
            '.*CLA 515.*', '.*CLA 531.*', '.*CLA 536.*', '.*CLA 569.*'
        ],
        "Relevant Courses": [
            '.*CLA .*', '.*LAT .*', '.*HUM .*', '.*ART .*', '.*ARC .*',
            '.*HLS .*', '.*REL .*', '.*PHI .*', '.*CDH .*', '.*PAW .*'
        ],
        "Greek 5": [
            '.*CLG 108.*', '.*CLG 2.*', '.*CLG 3.*', '.*CLG 4.*', '.*CLG 5.*',
            '.*CLA 200.*', '.*CLA 205.*', '.*CLA 216.*', '.*CLA 217.*', '.*CLA 303.*', '.*CLA 307.*',
            '.*CLA 313.*', '.*CLA 319.*', '.*CLA 326.*', '.*CLA 330.*', '.*CLA 357.*', '.*CLA 400.*',
            '.*CLA 412.*', '.*CLA 414.*', '.*CLA 502.*', '.*CLA 505.*', '.*CLA 506.*', '.*CLA 514.*',
            '.*CLA 515.*', '.*CLA 531.*', '.*CLA 536.*', '.*CLA 569.*'
        ],
        "Latin 4": [
            '.*LAT 108.*', '.*LAT 2.*', '.*LAT 3.*', '.*LAT 4.*', '.*LAT 5.*',
            '.*CLA 240.*', '.*CLA 260.*', '.*CLA 309.*', '.*CLA 422.*', '.*CLA 503.*', '.*CLA 534.*', '.*CLA 538.*', '.*CLA 542.*'
        ],
        "Latin 5": [
            '.*LAT 108.*', '.*LAT 2.*', '.*LAT 3.*', '.*LAT 4.*', '.*LAT 5.*',
            '.*CLA 240.*', '.*CLA 260.*', '.*CLA 309.*', '.*CLA 422.*', '.*CLA 503.*', '.*CLA 534.*', '.*CLA 538.*', '.*CLA 542.*'
        ],
        "Medicine 5": ['.*CLA 226.*', '.*CLA 231.*', '.*CLA 313.*', '.*CLA 315.*',
                        '.*CLA 329.*', '.*CLA 330.*', '.*CLA 338.*', '.*CLA 531.*'],
        "Medicine 4": ['.*CLA 226.*', '.*CLA 231.*', '.*CLA 313.*', '.*CLA 315.*',
                        '.*CLA 329.*', '.*CLA 330.*', '.*CLA 338.*', '.*CLA 531.*'],
        "Historical Survey": ['.*CLA 216.*', '.*CLA 217.*', '.*CLA 218.*', '.*CLA 219.*'],
        "Track Requirements": [
            '.*CLA 200.*', '.*CLA 202.*', '.*CLA 207.*', '.*CLA 216.*', '.*CLA 217.*', '.*CLA 218.*', '.*CLA 219.*', '.*CLA 223.*',
            '.*CLA 247.*', '.*CLA 309.*', '.*CLA 326.*', '.*CLA 343.*', '.*CLA 398.*', '.*CLA 412.*', '.*CLA 413.*', '.*CLA 414.*',
            '.*CLA 418.*', '.*CLA 520.*', '.*CLA 522.*', '.*CLA 524.*', '.*CLA 531.*', '.*CLA 536.*', '.*CLA 545.*', '.*CLA 547.*', '.*CLA 548.*'
        ]
    }

    return courses

def env_minor_courses():
    courses = {
        'Foundation Above 300 2': [
        '.*ENV 303.*', '.*ENV 304.*', '.*ENV 343.*', 
        '.*ENV 354.*', '.*ENV 363.*', '.*ENV 367.*', '.*ENV 377.*', 
        '.*ENV 318.*', '.*ENV 334.*', '.*ENV 344.*', '.*ENV 321.*', 
        '.*ENV 365.*', '.*ENV 384.*', '.*ENV 417A.*', '.*ENV 417B.*', 
        '.*ENV 356.*', '.*ENV 362.*', '.*ENV 339.*', '.*ENV 394.*', 
        '.*ENV 319.*', '.*ENV 350.*', '.*ENV 405.*'
        ],
        'Foundation Above 300 1': [
            '.*ENV 303.*', '.*ENV 304.*', '.*ENV 343.*', 
            '.*ENV 354.*', '.*ENV 363.*', '.*ENV 367.*', '.*ENV 377.*', 
            '.*ENV 318.*', '.*ENV 334.*', '.*ENV 344.*', '.*ENV 321.*', 
            '.*ENV 365.*', '.*ENV 384.*', '.*ENV 417A.*', '.*ENV 417B.*', 
            '.*ENV 356.*', '.*ENV 362.*', '.*ENV 339.*', '.*ENV 394.*', 
            '.*ENV 319.*', '.*ENV 350.*', '.*ENV 405.*'
        ],
        'Foundation Below 300 1': [
            '.*ENV 102A.*', '.*ENV 200A.*', '.*ENV 200B.*', 
            '.*ENV 200C.*', '.*ENV 200D.*', '.*ENV 200E.*', '.*ENV 200F.*', 
            '.*ENV 210A.*', '.*ENV 210B.*', '.*ENV 238.*'
        ],
        'Elective Above 300 2': [
            '.*AMS 304.*', '.*AMS 354.*', '.*AMS 403.*', '.*AMS 415.*', 
            '.*ANT 322.*', '.*ANT 364.*', '.*ANT 387.*', '.*ANT 443.*', 
            '.*ANT 446.*', '.*ANT 452.*', '.*ARC 492.*', '.*ART 484.*', 
            '.*CEE 304.*', '.*CEE 306.*', '.*CEE 334.*', '.*CEE 392.*', 
            '.*CEE 401.*', '.*CEE 474.*', '.*CEE 518.*', '.*CEE 571.*', 
            '.*CEE 586.*', '.*CEE 587.*', '.*CHM 544.*', '.*ECO 355.*', 
            '.*ECS 378.*', '.*ECS 389.*', '.*ECS 489.*', '.*ENE 318.*', 
            '.*ENE 321.*', '.*ENE 372.*', '.*ENE 431.*', '.*ENG 384.*', 
            '.*ENV 302.*', '.*ENV 305.*', '.*ENV 310.*', '.*ENV 316.*', 
            '.*ENV 327.*', '.*ENV 330.*', '.*ENV 345.*', '.*ENV 347.*'
        ],
        'Elective Above 300 1': [
            '.*AMS 304.*', '.*AMS 354.*', '.*AMS 403.*', '.*AMS 415.*', 
            '.*ANT 322.*', '.*ANT 364.*', '.*ANT 387.*', '.*ANT 443.*', 
            '.*ANT 446.*', '.*ANT 452.*', '.*ARC 492.*', '.*ART 484.*', 
            '.*CEE 304.*', '.*CEE 306.*', '.*CEE 334.*', '.*CEE 392.*', 
            '.*CEE 401.*', '.*CEE 474.*', '.*CEE 518.*', '.*CEE 571.*', 
            '.*CEE 586.*', '.*CEE 587.*', '.*CHM 544.*', '.*ECO 355.*', 
            '.*ECS 378.*', '.*ECS 389.*', '.*ECS 489.*', '.*ENE 318.*', 
            '.*ENE 321.*', '.*ENE 372.*', '.*ENE 431.*', '.*ENG 384.*', 
            '.*ENV 302.*', '.*ENV 305.*', '.*ENV 310.*', '.*ENV 316.*', 
            '.*ENV 327.*', '.*ENV 330.*', '.*ENV 345.*', '.*ENV 347.*'
        ],
        'Elective Below 300 1': [
            '.*ANT 214.*', '.*ANT 219.*', '.*ANT 245.*', '.*ARC 205.*', 
            '.*CEE 207.*', '.*CLA 226.*', '.*CLA 247.*', '.*ENE 202.*', 
            '.*ENV 204.*', '.*ENV 212.*', '.*ENV 251.*', '.*FRE 230.*', 
            '.*GEO 202.*'
        ]
    }

    return courses

def cos_minor_courses():
    courses = {
        "Intro Course": ['.*COS 126.*', '.*ECE 115.*'],
        "ISC": ['.*ISC 231.*', '.*ISC 232.*', '.*ISC 233.*', '.*ISC 234.*'],
        "Core Course": ['.*COS 226.*', '.*COS 217.*'],
        "Electives": ['.*COS 2.*', '.*COS 3.*', '.*COS 4.*']
    }

    return courses

def fin_minor_courses():
    courses = {
        'MAT 175': ['.*MAT 175.*'],
        'Advanced Math': ['.*MAT 203.*', '.*MAT 204.*'],
        'BSE Math': ['.*MAT 201.*', '.*MAT 202.*'],
        'EGR': ['.*EGR 154.*', '.*EGR 156.*'],
        'Micro': ['.*ECO 300.*', '.*ECO 310.*'],
        'Probability/Stats': ['.*ORF 245.*', '.*ECO 202.*', '.*PSY 251.*', '.*SOC 301.*',
        '.*POL 345.*', '.*SPI 200.*'],
        'Core': ['.*ECO 362.*', '.*ECO 363.*'],
        'Finanical Applications 1': ['.*COS 473.*', '.*ECO 315.*', '.*ECO 325.*', '.*ECO 327.*', '.*ECO 342.*', '.*ECO 353.*', 
        '.*ECO 361.*', '.*ECO 416.*', '.*ECO 461.*', '.*ECO 462.*', '.*ECO 463.*', '.*ECO 464.*', 
        '.*ECO 465.*', '.*ECO 466.*', '.*ECO 467.*', '.*ECO 468.*', '.*ECO 469.*', '.*ECO 491.*', 
        '.*ECO 492.*', '.*ECO 493.*', '.*ECO 494.*', '.*EGR 395.*', '.*EGR 475.*', '.*EGR 491.*', 
        '.*ORF 335.*', '.*ORF 435.*', '.*ORF 445.*', '.*SPI 466.*', '.*SPI 524.*', '.*SPI 582f.*'],
        'Finanical Applications 2': ['.*COS 473.*', '.*ECO 315.*', '.*ECO 325.*', '.*ECO 327.*', '.*ECO 342.*', '.*ECO 353.*', 
        '.*ECO 361.*', '.*ECO 416.*', '.*ECO 461.*', '.*ECO 462.*', '.*ECO 463.*', '.*ECO 464.*', 
        '.*ECO 465.*', '.*ECO 466.*', '.*ECO 467.*', '.*ECO 468.*', '.*ECO 469.*', '.*ECO 491.*', 
        '.*ECO 492.*', '.*ECO 493.*', '.*ECO 494.*', '.*EGR 395.*', '.*EGR 475.*', '.*EGR 491.*', 
        '.*ORF 335.*', '.*ORF 435.*', '.*ORF 445.*', '.*SPI 466.*', '.*SPI 524.*', '.*SPI 582f.*'],
        'General Electives 1': ['.*APC 350.*', '.*CEE 460.*', '.*COS 324.*', '.*COS 333.*', '.*COS 423.*', '.*COS 424.*', 
        '.*COS 432.*', '.*COS 436.*', '.*COS 445.*', '.*COS 461.*', '.*ECO 311.*', '.*ECO 312.*', 
        '.*ECO 313.*', '.*ECO 317.*', '.*ECO 365.*', '.*ECO 414.*', '.*ECO 418.*', '.*ECO 488.*', 
        '.*MAE 305.*', '.*MAE 306.*', '.*MAT 325.*', '.*MAT 330.*', '.*MAT 335.*', '.*MAT 385.*', 
        '.*MAT 486.*', '.*ORF 307.*', '.*ORF 309.*', '.*ORF 311.*', '.*ORF 335.*', '.*ORF 350.*', 
        '.*ORF 363.*', '.*ORF 401.*', '.*ORF 405.*', '.*ORF 409.*', '.*ORF 455.*', '.*SPI 340.*'],
        'General Electives 2': ['.*APC 350.*', '.*CEE 460.*', '.*COS 324.*', '.*COS 333.*', '.*COS 423.*', '.*COS 424.*', 
        '.*COS 432.*', '.*COS 436.*', '.*COS 445.*', '.*COS 461.*', '.*ECO 311.*', '.*ECO 312.*', 
        '.*ECO 313.*', '.*ECO 317.*', '.*ECO 365.*', '.*ECO 414.*', '.*ECO 418.*', '.*ECO 488.*', 
        '.*MAE 305.*', '.*MAE 306.*', '.*MAT 325.*', '.*MAT 330.*', '.*MAT 335.*', '.*MAT 385.*', 
        '.*MAT 486.*', '.*ORF 307.*', '.*ORF 309.*', '.*ORF 311.*', '.*ORF 335.*', '.*ORF 350.*', 
        '.*ORF 363.*', '.*ORF 401.*', '.*ORF 405.*', '.*ORF 409.*', '.*ORF 455.*', '.*SPI 340.*']
    }

    return courses

def lin_minor_courses():
    courses = {
        'Prerequisites': ['.*LIN 201.*'],
        'Core Course': ['.*LIN 301.*', '.*LIN 302.*', '.*LIN 303.*', '.*LIN 306.*', 
        '.*PHI 334 / LIN 334.*'],
        'Methods': ['.*LIN 210.*', '.*LIN 310.*', '.*LIN 355.*', '.*LIN 356.*'],
        'Electives': ['.*LIN 2.*', '.*LIN 3.*', '.*LIN 4.*', '.*LIN 5.*']
    }

    return courses

def gss_minor_courses():
    courses = {
        'Intro': ['GSS 201'],
        'Thematic': ['.*GSS.*'],
        'Elective': ['.*GSS 3.*', '.*GSS 4.*']
    }

    return courses

def afs_minor_courses():
    courses = {
        'Core': ['.*AFS 2.*', '.*AFS 3.*'],
        'Humanities': ['.*AFS.*'],
        'African Language': ['.*TWI 101.*', '.*TWI 102.*', '.*TWI 103G.*', '.*TWI 105.*', '.*TWI 107.*',
                    '.*GEZ 101.*', '.*SWA 101.*', '.*SWA 102.*', '.*SWA 103K.*', '.*SWA 105.*', '.*SWA 107.*'],
        'Social Sciences': ['.*AFS.*'],
        'Other Electives': ['.*AFS.*', '.*TWI 101.*', '.*TWI 102.*', '.*TWI 103G.*', '.*TWI 105.*', '.*TWI 107.*',
                    '.*GEZ 101.*', '.*SWA 101.*', '.*SWA 102.*', '.*SWA 103K.*', '.*SWA 105.*', '.*SWA 107.*']
    }

    return courses

def asa_minor_courses():
    courses = {
        'Core': ['.*ASA 101.*'],
        'Electives': ['.*ASA.*'],
        'Advanced Seminar': ['.*AMS 403.*', '.*AMS 404.*', '.*AMS 406.*']
    }

    return courses

def chi_minor_courses():
    courses = {
        'Advanced Language': ['.*CHI 303.*', '.*CHI 304.*', '.*CHI 305.*', '.*CHI 306.*', 
                              '.*CHI 403.*', '.*CHI 404.*', '.*CHI 405.*', '.*CHI 406.*', '.*CHI 451.*'],
        'Other Language': ['.*CHI 303.*', '.*CHI 304.*', '.*CHI 305.*', '.*CHI 306.*', 
                              '.*CHI 403.*', '.*CHI 404.*', '.*CHI 405.*', '.*CHI 406.*', '.*CHI 451.*',
                              '.*CHI 1001.*', '.*CHI 1002.*', '.*CHI 101.*', '.*CHI 102.*', '.*CHI 103.*', 
                              '.*CHI 105.*', '.*CHI 107.*', '.*CHI 108.*'],
        'EAS/Cognate': ['.*EAS.*']
    }

    return courses

def cs_minor_courses():
    courses = {
        'Core 2': ['.*GEO 102.*', '.*GEO 103.*', '.*GEO 202.*', '.*GEO 203.*', 
                   '.*GEO 361.*', '.*GEO 363.*', '.*GEO 369.*', '.*GEO 370.*', 
                   '.*GEO 416.*', '.*GEO 417.*', '.*GEO 425.*', '.*GEO 428.*', 
                   '.*GEO 470.*'],
        'Core 3': ['.*GEO 102.*', '.*GEO 103.*', '.*GEO 202.*', '.*GEO 203.*', 
                   '.*GEO 361.*', '.*GEO 363.*', '.*GEO 369.*', '.*GEO 370.*', 
                   '.*GEO 416.*', '.*GEO 417.*', '.*GEO 425.*', '.*GEO 428.*', 
                   '.*GEO 470.*'],
        'Core 4': ['.*GEO 102.*', '.*GEO 103.*', '.*GEO 202.*', '.*GEO 203.*', 
                   '.*GEO 361.*', '.*GEO 363.*', '.*GEO 369.*', '.*GEO 370.*', 
                   '.*GEO 416.*', '.*GEO 417.*', '.*GEO 425.*', '.*GEO 428.*', 
                   '.*GEO 470.*'],
        'Capstone 3': ['.*GEO 360.*', '.*GEO 362.*', '.*GEO 366.*', '.*GEO 367.*',
                          '.*GEO 369.*', '.*GEO 370.*', '.*GEO 416.*', '.*GEO 417.*', 
                          '.*GEO 425.*', '.*GEO 428.*', '.*GEO 470.*'],
        'Capstone 2': ['.*GEO 360.*', '.*GEO 362.*', '.*GEO 366.*', '.*GEO 367.*',
                          '.*GEO 369.*', '.*GEO 370.*', '.*GEO 416.*', '.*GEO 417.*', 
                          '.*GEO 425.*', '.*GEO 428.*', '.*GEO 470.*'],
        'Capstone 1': ['.*GEO 360.*', '.*GEO 362.*', '.*GEO 366.*', '.*GEO 367.*',
                          '.*GEO 369.*', '.*GEO 370.*', '.*GEO 416.*', '.*GEO 417.*', 
                          '.*GEO 425.*', '.*GEO 428.*', '.*GEO 470.*']
    }

    return courses

def cwr_minor_courses():
    courses = {
        'CWR Hosted': ['CWR.*'],
        'CWR Electives': ['.*CWR.*']
    }

    return courses

def  dan_minor_courses():
    courses = {
        'Studio': ['.*DAN 204.*', '.*DAN 207.*', '.*DAN 208.*', '.*DAN 211.*', '.*DAN 215.*', '.*DAN 216.*',
                   '.*DAN 221.*', '.*DAN 229.*', '.*DAN 301.*', '.*DAN 303.*', '.*DAN 305.*', '.*DAN 324.*',
                   '.*DAN 326.*', '.*DAN 348.*', '.*DAN 351.*', '.*DAN 354.*', '.*DAN 401.*', '.*DAN 402.*',
                   '.*DAN 408.*', '.*DAN 419A.*', '.*DAN 420A.*', '.*DAN 431.*', '.*DAN 432.*'],
        'Seminar': ['.*DAN 215.*', '.*DAN 305.*', '.*DAN 308.*', '.*DAN 312.*', '.*DAN 314.*', '.*DAN 316.*',
                    '.*DAN 317.*', '.*DAN 321.*', '.*DAN 325.*', '.*DAN 329.*', '.*DAN 348.*', '.*DAN 393.*',
                    '.*DAN 406.*'],
        'Electives': ['.*DAN.*']
    }

    return courses

def eas_minor_courses():
    courses = {
        'Advanced Language': ['.*CHI 2.*', '.*CHI 3.*', '.*CHI 4.*',
                              '.*CHI 5.*', '.*JPN 2.*', '.*JPN 3.*',
                              '.*JPN 4.*', '.*JPN 5.*', '.*KOR 2.*',
                              '.*KOR 3.*', '.*KOR 4.*', '.*KOR 5.*'],
        'Other Language': ['.*CHI.*', '.*JPN.*', '.*KOR.*'],
        '200-Level Content': ['.*EAS 2.*'],
        'Other Content': ['.*EAS 1.*', '.*EAS 2.*', '.*EAS 3.*', '.*EAS 4.*', 
                          '.*EAS 5.*', '.*POL 434.*', '.*SOC 307.*',
                          '.*SPI 316.*']
    }

    return courses

def eng_minor_courses():
    courses = {
        'Seminars': ['.*ENG 256.*', '.*ENG 300.*', '.*ENG 305.*', '.*ENG 306.*', '.*ENG 310.*',
                        '.*ENG 311.*', '.*ENG 312.*', '.*ENG 331.*', '.*ENG 334.*', '.*ENG 344.*',
                        '.*ENG 346.*', '.*ENG 361.*', '.*ENG 379.*', '.*ENG 401.*', '.*ENG 402.*',
                        '.*ENG 403.*', '.*ENG 404.*', '.*ENG 405.*', '.*ENG 411.*', '.*ENG 412.*',
                        '.*ENG 413.*', '.*ENG 414.*', '.*ENG 417.*'],
        'English Courses': ['.*ENG.*']
    }

    return courses

def ghp_minor_courses():
    courses = {
        'ISC': ['.*ISC 231.*', '.*ISC 232.*', '.*ISC 233.*', 
                '.*ISC 234.*'],
        'Foundation': ['.*ANT 240.*', '.*GSS 201.*', '.*MOL 101.*', 
                       '.*MOL 211.*', '.*MOL 214.*', '.*SOC 217.*',
                       '.*URB 201.*', '.*EEB 309.*', '.*EEB 314.*', 
                       '.*EEB 327.*', '.*EEB 328.*'],
        'Statistics': ['.*ECO 202.*', '.*ECO 302.*', '.*ECO 312.*',
                          '.*MOL 290.*', '.*ORF 245.*', '.*ORF 405.*',
                          '.*POL 345.*', '.*PSY 251.*', '.*SML 201.*',
                          '.*SOC 301.*', '.*SPI 200.*'],
        'Core': ['.*GHP 350.*', '.*GHP 351.*'],
        'Advanced Electives 4': ['.*AAS 303.*', '.*AAS 314.*', '.*AAS 352.*',
                                '.*AMS 305.*', '.*AMS 404.*', '.*ANT 313.*',
                                '.*ANT 321.*', '.*ANT 339.*', '.*ANT 344.*',
                                '.*ANT 360.*', '.*ANT 390.*', '.*ANT 446.*',
                                '.*ANT 461.*', '.*ARC 492.*', '.*ART 361.*',
                                '.*ART 491.*', '.*CBE 411.*', '.*CBE 430.*',
                                '.*CBE 438.*', '.*CBE 442.*', '.*CEE 471.*',
                                '.*CEE 311.*', '.*CEE 325.*', '.*CEE 334.*',
                                '.*CHV 323.*', '.*CLA 326.*', '.*CLA 338.*',
                                '.*COM 329.*', '.*EAS 418.*', '.*ECE 451.*',
                                '.*ECE 452.*', '.*ECO 332.*', '.*ECO 355.*',
                                '.*ECS 376.*', '.*EEB 308.*', '.*EEB 325.*',
                                '.*EEB 327.*', '.*EEB 428.*', '.*EGR 277.*',
                                '.*ENE 321.*', '.*ENG 359.*', '.*ENG 384.*',
                                '.*ENV 302.*', '.*ENV 304.*', '.*ENV 305.*',
                                '.*ENV 343.*', '.*FRE 240.*', '.*FRE 420.*',
                                '.*GEO 360.*', '.*HIS 390.*', '.*HIS 393.*',
                                '.*HIS 494.*', '.*HUM 315.*', '.*HUM 360.*',
                                '.*ITA 319.*', '.*JDS 324.*', '.*LAS 308.*',
                                '.*MOL 340.*', '.*MOL 405.*', '.*MOL 433.*',
                                '.*MOL 445.*', '.*MOL 459.*', '.*MOL 460.*',
                                '.*NES 301.*', '.*NEU 331.*', '.*NEU 385.*',
                                '.*NEU 400.*', '.*NEU 420.*', '.*NEU 430.*',
                                '.*NEU 447.*', '.*PHI 356.*', '.*PSY 317.*',
                                '.*PSY 320.*', '.*PSY 332.*', '.*PSY 341.*',
                                '.*QCB 311.*', '.*QCB 408.*', '.*QCB 455.*',
                                '.*QCB 470.*', '.*REL 303.*', '.*REL 361.*',
                                '.*SOC 249.*', '.*SPI 332.*', '.*SPI 335.*',
                                '.*SPI 364.*', '.*SPI 368.*', '.*SPI 393.*',
                                '.*SPI 394.*', '.*SPI 405.*', '.*VIS 301.*'],
        'Advanced Electives 3': ['.*AAS 303.*', '.*AAS 314.*', '.*AAS 352.*',
                                '.*AMS 305.*', '.*AMS 404.*', '.*ANT 313.*',
                                '.*ANT 321.*', '.*ANT 339.*', '.*ANT 344.*',
                                '.*ANT 360.*', '.*ANT 390.*', '.*ANT 446.*',
                                '.*ANT 461.*', '.*ARC 492.*', '.*ART 361.*',
                                '.*ART 491.*', '.*CBE 411.*', '.*CBE 430.*',
                                '.*CBE 438.*', '.*CBE 442.*', '.*CEE 471.*',
                                '.*CEE 311.*', '.*CEE 325.*', '.*CEE 334.*',
                                '.*CHV 323.*', '.*CLA 326.*', '.*CLA 338.*',
                                '.*COM 329.*', '.*EAS 418.*', '.*ECE 451.*',
                                '.*ECE 452.*', '.*ECO 332.*', '.*ECO 355.*',
                                '.*ECS 376.*', '.*EEB 308.*', '.*EEB 325.*',
                                '.*EEB 327.*', '.*EEB 428.*', '.*EGR 277.*',
                                '.*ENE 321.*', '.*ENG 359.*', '.*ENG 384.*',
                                '.*ENV 302.*', '.*ENV 304.*', '.*ENV 305.*',
                                '.*ENV 343.*', '.*FRE 240.*', '.*FRE 420.*',
                                '.*GEO 360.*', '.*HIS 390.*', '.*HIS 393.*',
                                '.*HIS 494.*', '.*HUM 315.*', '.*HUM 360.*',
                                '.*ITA 319.*', '.*JDS 324.*', '.*LAS 308.*',
                                '.*MOL 340.*', '.*MOL 405.*', '.*MOL 433.*',
                                '.*MOL 445.*', '.*MOL 459.*', '.*MOL 460.*',
                                '.*NES 301.*', '.*NEU 331.*', '.*NEU 385.*',
                                '.*NEU 400.*', '.*NEU 420.*', '.*NEU 430.*',
                                '.*NEU 447.*', '.*PHI 356.*', '.*PSY 317.*',
                                '.*PSY 320.*', '.*PSY 332.*', '.*PSY 341.*',
                                '.*QCB 311.*', '.*QCB 408.*', '.*QCB 455.*',
                                '.*QCB 470.*', '.*REL 303.*', '.*REL 361.*',
                                '.*SOC 249.*', '.*SPI 332.*', '.*SPI 335.*',
                                '.*SPI 364.*', '.*SPI 368.*', '.*SPI 393.*',
                                '.*SPI 394.*', '.*SPI 405.*', '.*VIS 301.*'],
        'Advanced Electives 2': ['.*AAS 303.*', '.*AAS 314.*', '.*AAS 352.*',
                                '.*AMS 305.*', '.*AMS 404.*', '.*ANT 313.*',
                                '.*ANT 321.*', '.*ANT 339.*', '.*ANT 344.*',
                                '.*ANT 360.*', '.*ANT 390.*', '.*ANT 446.*',
                                '.*ANT 461.*', '.*ARC 492.*', '.*ART 361.*',
                                '.*ART 491.*', '.*CBE 411.*', '.*CBE 430.*',
                                '.*CBE 438.*', '.*CBE 442.*', '.*CEE 471.*',
                                '.*CEE 311.*', '.*CEE 325.*', '.*CEE 334.*',
                                '.*CHV 323.*', '.*CLA 326.*', '.*CLA 338.*',
                                '.*COM 329.*', '.*EAS 418.*', '.*ECE 451.*',
                                '.*ECE 452.*', '.*ECO 332.*', '.*ECO 355.*',
                                '.*ECS 376.*', '.*EEB 308.*', '.*EEB 325.*',
                                '.*EEB 327.*', '.*EEB 428.*', '.*EGR 277.*',
                                '.*ENE 321.*', '.*ENG 359.*', '.*ENG 384.*',
                                '.*ENV 302.*', '.*ENV 304.*', '.*ENV 305.*',
                                '.*ENV 343.*', '.*FRE 240.*', '.*FRE 420.*',
                                '.*GEO 360.*', '.*HIS 390.*', '.*HIS 393.*',
                                '.*HIS 494.*', '.*HUM 315.*', '.*HUM 360.*',
                                '.*ITA 319.*', '.*JDS 324.*', '.*LAS 308.*',
                                '.*MOL 340.*', '.*MOL 405.*', '.*MOL 433.*',
                                '.*MOL 445.*', '.*MOL 459.*', '.*MOL 460.*',
                                '.*NES 301.*', '.*NEU 331.*', '.*NEU 385.*',
                                '.*NEU 400.*', '.*NEU 420.*', '.*NEU 430.*',
                                '.*NEU 447.*', '.*PHI 356.*', '.*PSY 317.*',
                                '.*PSY 320.*', '.*PSY 332.*', '.*PSY 341.*',
                                '.*QCB 311.*', '.*QCB 408.*', '.*QCB 455.*',
                                '.*QCB 470.*', '.*REL 303.*', '.*REL 361.*',
                                '.*SOC 249.*', '.*SPI 332.*', '.*SPI 335.*',
                                '.*SPI 364.*', '.*SPI 368.*', '.*SPI 393.*',
                                '.*SPI 394.*', '.*SPI 405.*', '.*VIS 301.*'],
        '200-Level Electives 2': ['.*ANT 206.*', '.*ANT 219.*', '.*ANT 233.*',
                                '.*ANT 238.*', '.*ANT 240.*', '.*ASA 238.*',
                                '.*ASL 205.*', '.*CLA 227.*', '.*DAN 224.*',
                                '.*ENE 202.*', '.*ENV 251.*', '.*FRE 240.*',
                                '.*HIS 294.*', '.*LAS 229.*', '.*PSY 207.*',
                                '.*SPA 204.*', '.*SPA 205.*'],
        '200-Level Electives 1': ['.*ANT 206.*', '.*ANT 219.*', '.*ANT 233.*',
                                '.*ANT 238.*', '.*ANT 240.*', '.*ASA 238.*',
                                '.*ASL 205.*', '.*CLA 227.*', '.*DAN 224.*',
                                '.*ENE 202.*', '.*ENV 251.*', '.*FRE 240.*',
                                '.*HIS 294.*', '.*LAS 229.*', '.*PSY 207.*',
                                '.*SPA 204.*', '.*SPA 205.*']
    }

    return courses

def his_minor_courses():
    courses = {
        'HIS': ['.*HIS.*']
    }

    return courses

def hls_minor_courses():
    courses = {
        'Gateway Seminar': ['.*HLS 222.*'],
        '400-Level Seminar': ['.*HLS 410.*', '.*HLS 430.*'],
        'History, Society Religion': ['.*HLS 210.*', '.*HLS 212.*', 
                                    '.*HLS 217.*', '.*HLS 222.*',
                                    '.*HLS 227.*', '.*HLS 240.*', 
                                    '.*HLS 241.*', '.*HLS 251.*',
                                    '.*HLS 252.*', '.*HLS 303.*',
                                    '.*HLS 305.*', '.*HLS 322.*',
                                    '.*HLS 324.*', '.*HLS 335.*',
                                    '.*HLS 337.*', '.*HLS 340.*',
                                    '.*HLS 343.*', '.*HLS 345.*',
                                    '.*HLS 354.*', '.*HLS 358.*',  
                                    '.*HLS 361.*', '.*HLS 363.*',
                                    '.*HLS 367.*', '.*HLS 369.*',
                                    '.*HLS 373.*', '.*HLS 428.*'],
        'Language, Literature, Philosophy': ['.*HLS 101.*','.*HLS 102.*',
                                            '.*HLS 105.*', '.*HLS 107.*',
                                            '.*HLS 203.*', '.*HLS 208.*',
                                            '.*HLS 211.*', '.*HLS 217.*',
                                            '.*HLS 227.*', '.*HLS 240.*',
                                            '.*HLS 300.*', '.*HLS 302.*',
                                            '.*HLS 320.*', '.*HLS 322.*',
                                            '.*HLS 326.*', '.*HLS 338.*',
                                            '.*HLS 363.*', '.*HLS 367.*',
                                            '.*HLS 368.*', '.*HLS 434.*',
                                            '.*HLS 461.*'],
        'Visual, Material Culture and Music': ['.*HLS 205.*','.*HLS 206.*',
                                            '.*HLS 215.*', '.*HLS 228.*',
                                            '.*HLS 231.*', '.*HLS 301.*',
                                            '.*HLS 316.*', '.*HLS 410.*',
                                            '.*HLS 430.*']
    }

    return courses

def hstm_minor_courses():
    courses = {
        'Core': ['.*HIS 390.*'],
        'Selected Courses': ['.*EGR 277.*', '.*HIS 277.*', '.*HIS 290.*', '.*HIS 291.*', '.*HIS 292.*', '.*HIS 293.*',
                            '.*HIS 294.*', '.*HIS 295.*', '.*HIS 297.*', '.*STC 297.*', '.*HIS 298.*', '.*AAS 352.*',
                            '.*HIS 347.*', '.*ART 361.*', '.*HIS 355.*', '.*SPI 364.*', '.*HIS 368.*', '.*AAS 331.*',
                            '.*HIS 382.*', '.*HIS 390.*', '.*HIS 392.*', '.*HIS 393.*', '.*HIS 394.*', '.*HIS 395.*',
                            '.*HIS 396.*', '.*HIS 397.*', '.*HIS 398.*', '.*AMS 399.*', '.*HIS 399.*', '.*HIS 452.*',
                            '.*GSS 426.*', '.*HIS 472.*', '.*HIS 481.*', '.*HIS 489.*', '.*HIS 491.*', '.*HIS 492.*',
                            '.*HIS 493.*', '.*HIS 494.*', '.*HIS 495.*', '.*HIS 496.*', '.*HIS 497.*', '.*HIS 498.*',
                            '.*HIS 499.*'],
        'HOS/HIS Cognate': ['.*HOS.*', '.*HIS.*'],
        'History': ['.*HIS.*']
    }

    return courses

def hum_minor_courses():
    courses = {
        '200-Level Humanities': ['.*HUM 216', '.*HUM 217.*', '.*HUM 233.*', 
                                 '.*HUM 234.*', '.*HUM 247.*', '.*HUM 248.*'],
        'Tradition and Transformation': ['.*HUM 390.*',
                                        '.*HUM 216.*', '.*HUM 217.*',
                                        '.*HUM 218.*', '.*HUM 219.*',
                                        '.*HUM 230.*', '.*HUM 233.*',
                                        '.*HUM 234.*', '.*HUM 247.*',
                                        '.*HUM 248.*', '.*HUM 312.*',
                                        '.*HUM 412.*', '.*HUM 434.*',
                                        '.*HUM 227.*',
                                        '.*HUM 333.*'],
        'Global or Comparative Humanities': ['.*ART 361.*', 
                                            '.*CLA 212.*',
                                            '.*COM 310.*',
                                            '.*HUM 240.*', '.*HUM 290.*',
                                            '.*HUM 312.*', '.*HUM 335.*',
                                            '.*HUM 402.*', '.*HUM 423.*',
                                            '.*HUM 450.*', '.*HUM 470.*',
                                            '.*MED 227.*',
                                            '.*TRA 304.*'],
        'Engaged or Public Humanities': ['.*HUM 315.*','.*HUM 321.*',
                                        '.*HUM 339.*', '.*HUM 352.*',
                                        '.*HUM 353.*', '.*HUM 470.*',
                                        '.*SLA 368.*'],
        'Humanities and Sciences in Dialogue': ['.*ART 361.*',
                                            '.*HUM 315.*', '.*HUM 365.*',
                                            '.*PSY 210.*',
                                            '.*STC 297.*'],
        'Data and Culture': ['.*HUM 346.*', '.*HUM 307.*',
                             '.*HUM 475.*'],
        'Interdisciplinary Electives': ['.*HUM 390.*',
                                        '.*HUM 216.*', '.*HUM 217.*',
                                        '.*HUM 218.*', '.*HUM 219.*',
                                        '.*HUM 230.*', '.*HUM 233.*',
                                        '.*HUM 234.*', '.*HUM 247.*',
                                        '.*HUM 248.*', '.*HUM 312.*',
                                        '.*HUM 412.*', '.*HUM 434.*',
                                        '.*MED 227.*',
                                        '.*TRA 304.*',
                                        '.*ART 361.*', 
                                        '.*CLA 212.*',
                                        '.*COM 310.*',
                                        '.*HUM 240.*', '.*HUM 290.*',
                                        '.*HUM 312.*', '.*HUM 335.*',
                                        '.*HUM 402.*', '.*HUM 423.*',
                                        '.*HUM 450.*', '.*HUM 470.*',
                                        '.*MED 227.*',
                                        '.*TRA 304.*', 
                                        '.*HUM 315.*','.*HUM 321.*',
                                        '.*HUM 339.*', '.*HUM 352.*',
                                        '.*HUM 353.*', '.*HUM 470.*',
                                        '.*SLA 368.*',
                                        '.*ART 361.*',
                                        '.*HUM 315.*', '.*HUM 365.*',
                                        '.*PSY 210.*',
                                        '.*STC 297.*',
                                        '.*HUM 346.*', '.*HUM 307.*',
                                        '.*HUM 475.*']
    }

    return courses

def jpn_minor_courses():
    courses = {
        'Advanced Language': ['.*JPN 3.*', '.*JPN 4.*', '.*JPN 5.*'],
        'Other Language': ['.*JPN.*'],
        'EAS/Cognate': ['.*EAS.*']
    }

    return courses

def jrn_minor_courses():
    courses = {
        'Gateway': ['.*JRN 240.*', '.*JRN 260.*', '.*JRN 280.*'],
        'Advanced': ['.*JRN 3.*', '.*JRN 4.*', '.*JRN 5.*'],
        'Electives': ['.*JRN.*']
    }

    return courses

def kor_minor_courses():
    courses = {
        'Advanced Language': ['.*KOR 3.*', '.*KOR 4.*', '.*KOR 5.*'],
        'Other Language': ['.*KOR.*'],
        'EAS/Cognate': ['.*EAS.*']
    }

    return courses

def lao_minor_courses():
    courses = {
        'Required': ['.*AMS 101.*'],
        'Breadth': ['.*LAO.*'],
        'Advanced Seminar': ['.AMS 403.*', '.*AMS 404.*']
    }

    return courses

def med_minor_courses():
    courses = {
        'Single Course': ['.*MED 227.*', '.*HIS 210.*', '.*ART 228.*'],
        'Humanities Sequence': ['.*HUM 216.*', '.*HUM 217.*'],
        'Medieval Topics': ['.*ART 228.*', '.*ART 361.*', '.*CLA 565.*',
                            '.*ENG 361.*', '.*HIS 210.*', '.*HIS 344.*',
                            '.*HIS 536.*', '.*HIS 544.*', '.*HUM 372.*',
                            '.*MUS 338.*', '.*REL 251.*', '.*FRE 560.*']
    }

    return courses

def mpp_minor_courses():
    courses = {
        'Core': ['.*MUS 105.*'],
        'Materials and Making': ['.*MUS 209B.*', '.*MUS 209A.*', '.*MUS 329.*',
                                '.*MUS 319.*', '.*MUS 316.*', '.*MUS 312.*',
                                '.*MUS 248.*', '.*MUS 210.*', '.*MUS 106.*',
                                '.*MUS 345.*', '.*MUS 340.*', '.*MUS 314.*',
                                '.*MUS 308.*', '.*MUS 106.*', '.*MUS 560.*',
                                '.*MUS 204.*', '.*MUS 537.*', '.*MUS 528.*',
                                '.*MUS 351.*', '.*MUS 310.*'],
        'Culture and Criticism': ['.*MUS 230.*', '.*MUS 238.*', '.*MUS 248.*',
                                '.MUS 262.*', '.*MUS 203.*', '.*MUS 240.*',
                                '.*MUS 223.*', '.*MUS 232.*', '.*MUS 242.*',
                                '.*MUS 262.*', '.*MUS 203.*', '.*MUS 350.*'],
        'Elective': ['.*MUS.*', '.*MPP.*'],
        'Departmental': ['.*MPP.*']
    }

    return courses

def mqe_minor_courses():
    courses = {
        'Multivariable Calculus': ['.*MAT 201.*', '.*ECO 201.*',
                                   '.*MAT 203.*', '.*EGR 156.*'],
        'Linear Algebra': ['.*MAT 202.*', '.*EGR 154.*', '.*MAT 204.*'],
        'Statistics': ['.*ECO 202.*', '.*ORF 245.*'],
        'Core Courses': ['.*ECO 310.*', '.*ECO 311.*', '.*ECO 312.*'],
        'Electives': ['.*ECO 313.*', '.*ECO 315.*', '.*ECO 317.*',
                    '.*ECO 323.*', '.*ECO 327.*', '.*ECO 416.*',
                    '.ECO 418.*', '.*COS 445.*', '.*ORF 405.*']
    }

    return courses

def mse_minor_courses():
    courses = {
        '103-104 Sequence': ['.*PHY 103.*', '.*PHY 104.*'],
        '105-106 Sequence': ['.*PHY 105.*', '.*PHY 106.*'],
        '201-202 Sequence': ['.*CHM 201.*', '.*CHM 202.*'],
        'Chemistry': ['.*CHM 207.*', '.*CHM 215.*'],
        'Thermodynamics': ['.*CBE 246.*', '.*CHM 306.*', '.*CHM 406.*'
                           '.*ECE 342.*', '.*MAE 221.*', '.*PHY 301.*'],
        'Materials': ['.*MSE 301.*', '.*CEE 364.*', '.*MAE 324.*'],
        'Mathematics': ['.*MAT 103.*', '.*MAT 104.*', '.*MAT 201.*',
                          '.*MAT 202.*', '.*MAT 203.*', '.*MAT 204.*'],
        'Electives': ['.*MSE. 3*', '.*MSE 4*'],
        'Experimental Methods': ['.*MSE 302.*', '.*CHM 371.*', '.*ECE 308.*'
                                '.*GEO 369.*']
    }

    return courses

def mus_minor_courses():
    courses = {
        'Core': ['MUS 105'],
        'Materials and Making': ['.*MUS 209B.*', '.*MUS 209A.*', '.*MUS 329.*',
                                '.*MUS 319.*', '.*MUS 316.*', '.*MUS 312.*',
                                '.*MUS 248.*', '.*MUS 210.*', '.*MUS 106.*',
                                '.*MUS 345.*', '.*MUS 340.*', '.*MUS 314.*',
                                '.*MUS 308.*', '.*MUS 106.*', '.*MUS 560.*',
                                '.*MUS 204.*', '.*MUS 537.*', '.*MUS 528.*',
                                '.*MUS 351.*', '.*MUS 310.*'],
        'Culture and Criticism': ['.*MUS 230.*', '.*MUS 238.*', '.*MUS 248.*',
                                '.MUS 262.*', '.*MUS 203.*', '.*MUS 240.*',
                                '.*MUS 223.*', '.*MUS 232.*', '.*MUS 242.*',
                                '.*MUS 262.*', '.*MUS 203.*', '.*MUS 350.*'],
        'Music Electives': ['.*MUS.*']
    }

    return courses

def neu_minor_courses():
    courses = {
        'Fundamentals': ['.*NEU 200.*', '.*NEU 201.*'],
        'Intro': ['.*NEU 202.*'],
        'Molecular/Cellular/Disease': ['.*NEU 301.*', '.*NEU 331.*', '.*NEU 385.*',
                                        '.*NEU 400.*', '.*NEU 403.*', '.*NEU 413.*',
                                        '.*NEU 428.*', '.*NEU 430.*', '.*NEU 443.*',
                                        '.*NEU 447.*', '.*NEU 460.*', '.*NEU 475.*',
                                        '.*NEU 490.*', '.*NEU 501A.*', '.*ECE 452.*',
                                        '.*MOL 250.*', '.*MOL 433.*', '.*MOL 259.*',
                                        '.*MOL 460.*', '.*PHY 562.*', '.*PSY 207.*',
                                        '.*PSY 317.*', '.*QCB 515.*'],
        'Circuits & Systems': ['.*NEU 200.*', '.*NEU 260.*', '.*NEU 301.*',
                                '.*NEU 316.*', '.*NEU 325.*', '.*NEU 336.*',
                                '.*NEU 385.*', '.*NEU 413.*', '.*NEU 420.*',
                                '.*NEU 422.*', '.*NEU 427.*', '.*NEU 428.*',
                                '.*NEU 460.*', '.*NEU 457.*', '.*NEU 501A.*',
                                '.*NEU 502A.*', '.*PHY 562.*'],
        'Neural Computation': ['.*NEU 330.*', '.*NEU 338.*', '.*NEU 340.*',
                            '.*NEU 437.*', '.*NEU 443.*', '.*NEU 457.*',
                            '.*NEU 499.*', '.*COS 226.*', '.*COS 343.*',
                            '.*COS 402.*', '.*COS 429.*', '.*COS 324.*',
                            '.*COS 302.*', '.*COS 424.*', '.*COS 485.*',
                            '.*ECE 364.*','.*ECE 452.*', '.*MAT 323.*', 
                            '.*PSY 360.*', '.*QCB 515.*'],
        'Cognitive & Social Neuroscience': ['.*NEU 200.*', '.*NEU 306.*', 
                                        '.*NEU 316.*', '.*NEU 331.*',
                                        '.*NEU 330.*', '.*NEU 337.*', 
                                        '.*NEU 338.*', '.*NEU 340.*', 
                                        '.*NEU 422.*', '.*NEU 499.*', 
                                        '.*NEU 502A.*', '.*ECE 480.*', 
                                        '.*PSY 248.*', '.*PSY 409.*'],
        'Other Electives': ['.*NEU 301.*', '.*NEU 331.*', '.*NEU 385.*',
                            '.*NEU 400.*', '.*NEU 403.*', '.*NEU 413.*',
                            '.*NEU 428.*', '.*NEU 430.*', '.*NEU 443.*',
                            '.*NEU 447.*', '.*NEU 460.*', '.*NEU 475.*',
                            '.*NEU 490.*', '.*NEU 501A.*', '.*ECE 452.*',
                            '.*MOL 250.*', '.*MOL 433.*', '.*MOL 259.*',
                            '.*MOL 460.*', '.*PHY 562.*', '.*PSY 207.*',
                            '.*PSY 317.*', '.*QCB 515.*', '.*NEU 200.*', 
                            '.*NEU 260.*', '.*NEU 301.*', '.*NEU 316.*', 
                            '.*NEU 325.*', '.*NEU 336.*', '.*NEU 385.*', 
                            '.*NEU 413.*', '.*NEU 420.*', '.*NEU 422.*', 
                            '.*NEU 427.*', '.*NEU 428.*', '.*NEU 460.*', 
                            '.*NEU 457.*', '.*NEU 501A.*', '.*NEU 502A.*', 
                            '.*PHY 562.*', '.*NEU 330.*', '.*NEU 338.*', '.*NEU 340.*',
                            '.*NEU 437.*', '.*NEU 443.*', '.*NEU 457.*',
                            '.*NEU 499.*', '.*COS 226.*', '.*COS 343.*',
                            '.*COS 402.*', '.*COS 429.*', '.*COS 324.*',
                            '.*COS 302.*', '.*COS 424.*', '.*COS 485.*',
                            '.*ECE 364.*','.*ECE 452.*', '.*MAT 323.*', 
                            '.*PSY 360.*', '.*QCB 515.*', '.*NEU 200.*', '.*NEU 306.*', 
                            '.*NEU 316.*', '.*NEU 331.*', '.*NEU 330.*', 
                            '.*NEU 337.*', '.*NEU 338.*', '.*NEU 340.*', 
                            '.*NEU 422.*', '.*NEU 499.*', '.*NEU 502A.*', 
                            '.*ECE 480.*', '.*PSY 248.*', '.*PSY 409.*']
    }

    return courses

def phi_minor_courses():
    courses = {
        'Prerequisite': ['.*PHI.*'],
        'Advanced 5': ['.*PHI 3.*', '.*PHI 4.*', '.*PHI 5.*'],
        'Advanced 4': ['.*PHI 3.*', '.*PHI 4.*', '.*PHI 5.*'],
        'Advanced 3': ['.*PHI 3.*', '.*PHI 4.*', '.*PHI 5.*'],
        '200-Level 2': ['.*PHI 2.*'],
        '200-Level 1': ['.*PHI 2.*']
    }

    return courses

def res_minor_courses():
    subrequirements = {
        'History and Social Sciences': ['.*NES 362.*', '.*NES 364.*', '.*POL 360.*',
                                        '.*POL 374.*', '.*POL 432.*', '.*POL 433.*',
                                        '.*SLA 338.*', '.*SLA 368.*', '.*SLA 420.*',
                                        '.*SOC 308.*'],
        'Literature, Arts and Culture': ['.*ART 337.*', '.*ART 393.*', '.*ART 466.*', 
                                        '.*COM 404.*', '.*NES 404.*', '.*COM 410.*', '.*COM 415.*',
                                        '.*ECS 360.*', '.*ECS 391.*', '.*JDS 221.*',
                                        '.*MUS 339.*', '.*SLA 218.*', '.*SLA 219.*',
                                        '.*SLA 220.*', '.*SLA 221.*', '.*SLA 236.*',
                                        '.*SLA 301.*', '.*SLA 303.*', '.*SLA 304.*',
                                        '.*SLA 305.*', '.*SLA 307.*', '.*SLA 308.*',
                                        '.*SLA 309.*', '.*SLA 310.*', '.*SLA 312.*',
                                        '.*SLA 313.*', '.*SLA 314.*', '.*SLA 319.*',
                                        '.*SLA 322.*', '.*SLA 324.*', '.*SLA 326.*',
                                        '.*SLA 337.*', '.*SLA 345.*', '.*SLA 347.*',
                                        '.*SLA 350.*', '.*SLA 361.*', '.*SLA 365.*',
                                        '.*SLA 366.*', '.*SLA 367.*', '.*SLA 368.*',
                                        '.*SLA 369.*', '.*SLA 395.*', '.*SLA 396.*',
                                        '.*SLA 411.*', '.*SLA 412.*', '.*SLA 413.*',
                                        '.*SLA 415.*', '.*SLA 416.*', '.*SLA 417.*',
                                        '.*SLA 422.*'],
        'BCS': ['.*BCS 101.*', '.*BCS 102.*', '.*BCS 105.*', '.*BCS 107.*',],
        'CZE': ['.*CZE 101.*', '.*CZE 102.*', '.*CZE 105.*', '.*CZE 107.*'],
        'PLS': ['.*PLS 101.*', '.*PLS 102.*'],
        'RUS': ['.*RUS 101.*', '.*RUS 102.*', '.*RUS 103.*', '.*RUS 105.*', 
                '.*RUS 108.*', '.*RUS 107.*', '.*RUS 207.*', '.*RUS 208.*',
                '.*RUS 305.*', '.*RUS 407.*', '.*RUS 408.*', '.*RUS 409.*'],
        'TUR': ['.*TUR 101.*', '.*TUR 102.*', '.*TUR 105.*', '.*TUR 107.*',
                 '.*TUR 305.*'],
        'UKR': ['.*UKR 101.*', '.*UKR 102.*']
    }

    return subrequirements

def sas_minor_courses():
    courses = {
        'Core': ['.*SAS 200.*'],
        'Language': ['.*HIN 107.*', '.*URD 107.*', '.*SAN 107.*'],
        'Electives': ['.*SAS .*']
    }

    return courses

def sla_minor_courses():
    courses = {
        'First Requirement': ['.*RUS 107.*', '.*RUS 108.*'],
        'Second Requirement': ['.*RUS 207.*', '.*RUS 3.*'],
        'Departmentals': ['.*RUS 208.*', '.*RUS 3.*', '.*RUS 4.*',
                          '.*SLA 2.*', '.*SLA 3.*', '.*SLA 4.*']
    }

    return courses

def sml_minor_courses():
    courses = {
        'Statistics': ['.*ECO 202.*', '.*ORF 245.*', '.*POL 345.*', '.*PSY 251.*',
                        '.*SPI 200.*'],
        'Machine Learning': ['.*COS 324.*', '.*COS 424.*', '.*ECE 364.*',
                            '.*ECE 435.*', '.*MAT 490.*', '.*ORF 350.*'],
        'Electives': ['.*COS 429.*', '.*COS 484.*', '.*COS 485.*', '.*ORF 418.*', 
                      '.*SOC 306.*', '.*ECE 434.*', '.*MAT 385.*', '.*ORF 309.*', 
                      '.*ORF 363.*', '.*AST 303.*', '.*CEE 460.*', '.*ECO 302.*', 
                      '.*ECO 312.*', '.*ECO 313.*', '.*ECO 491.*', '.*ECE 382.*', 
                      '.*ECE 480.*', '.*GEO 422.*', '.*MAE 345.*', '.*NEU 330.*', 
                      '.*ORF 405.*', '.*ORF 473.*', '.*POL 346.*', '.*PSY 360.*',
                      '.*PSY 454.*', '.*QCB 408.*', '.*QCB 455.*', '.*SOC 400.*']
    }

    return courses

def tmt_minor_courses():
    courses = {
        'Introduction': ['.*THR 101.*'],
        'Additional Courses': ['.*THR .*', '.*MTD .*'],
        'Electives': ['.*THR .*', '.*MTD .*', '.*DAN .*', '.*MUS .*'],
        'Dramaturgical': ['.*AMS 403.*', '.*ATL 499.*', '.*DAN 305.*', '.*ENG 314.*', '.*ENG 319.*', '.*FRE 390.*',
                        '.*GSS 337.*', '.*THR 308.*', '.*THR 316.*', '.*THR 355.*', '.*COM 212.*', '.*DAN 206.*',
                        '.*DAN 208.*', '.*DAN 357.*', '.*ENG 354.*', '.*ENG 357.*', '.*FRE 228.*', '.*HUM 321.*',
                        '.*HUM 352.*', '.*THR 223.*', '.*THR 300.*', '.*THR 313.*', '.*THR 350.*', '.*ENG 354.*',
                        '.*ENG 407.*', '.*FRE 390.*', '.*HUM 340.*', '.*MTD 348.*', '.*MUS 350.*', '.*MUS 357.*',
                        '.*THR 220.*', '.*THR 359.*', '.*THR 391.*', '.*THR 400.*', '.*THR 416.*', '.*VIS 354.*',
                        '.*AMS 317.*', '.*DAN 310.*', '.*DAN 393.*', '.*ECS 362.*', '.*FRE 228.*', '.*HIN 305.*',
                        '.*LAS 308.*', '.*MTD 202.*', '.*MUS 334.*', '.*THR 316.*', '.*THR 402.*', '.*THR 405.*',
                        '.*VIS 354.*', '.*CLA 227.*', '.*DAN 215.*', '.*ENG 318.*', '.*ENG 361.*', '.*ENG 409.*',
                        '.*FRE 390.*', '.*GSS 322.*', '.*ITA 314.*', '.*MUS 350.*', '.*THR 205.*', '.*THR 302.*',
                        '.*THR 347.*', '.*THR 350.*', '.*THR 391.*', '.*THR 400.*', '.*ENG 319.*', '.*FRE 392.*',
                        '.*HUM 352.*', '.*MTD 217.*', '.*THR 203.*', '.*THR 205.*', '.*THR 300.*', '.*THR 305.*',
                        '.*THR 376.*', '.*THR 402.*', '.*FRE 389.*', '.*MTD 333.*', '.*THR 353.*']
    }

    return courses

def tra_minor_courses():
    courses = {
        'Core': ['.*TRA 200.*', '.*TRA 400.*'],
        'Upper-Level Course': ['.*SPA 380.*', '.*FRE 407.*', '.*ARA 308.*', 
                               '.*CWR 206.*', '.*CWR 306.*'],
        'Cross-listed by TRA': ['.*TRA 2.*', '.*TRA 3.*', '.*TRA 4.*'],
        'Understanding of Translation': ['.*ANT 326.*', '.*COM 236.*', '.*HIS 397.*', 
                               '.*ITA 300.*', '.*LIN 201.*', '.*NES 398.*',
                                '.*PHI 317.*'],
        'Other Additional Course': ['.*ANT 326.*', '.*COM 236.*', '.*HIS 397.*', 
                               '.*ITA 300.*', '.*LIN 201.*', '.*NES 398.*',
                                '.*PHI 317.*', '.*TRA 2.*', '.*TRA 3.*', '.*TRA 4.*',
                                '.*SPA 380.*', '.*FRE 407.*', '.*ARA 308.*', 
                               '.*CWR 206.*', '.*CWR 306.*']
    }

    return courses

def vis_minor_courses():
    courses = {
        'Studio': ['.*VIS 3.*', '.*VIS 4.*'],
        'Artist and Studio': ['.*VIS 392.*'],
        'Exhibition Issues and Methods': ['.*VIS 416.*'],
        'Art and Archaeology': ['.*ART .*'],
        'Elective': ['.*VIS .*', '.*ART .*']
    }

    return courses

def vpl_minor_courses():
    courses = {
        'Intro': ['.*PHI 202.*'],
        'Political Theory': ['.*POL 210.*', '.*SPI 370.*', '.*POL 301.*', 
                             '.*POL 302.*', '.*POL 303.*', '.*POL 305.*', 
                             '.*POL 306.*', '.*POL 307.*', '.*POL 309.*', 
                             '.*POL 313.*'],
        'Seminar': ['.*HIS 427.*', '.*CHV 479.*', '.*POL 403.*', '.*POL 477.*', 
                    '.*CHV 390.*', '.*CHV 395.*', '.*POL 471.*', '.*POL 474.*', 
                    '.*CHV 478.*', '.*PHI 380.*', '.*CHV 367.*', '.*CHV 390.*', 
                    '.*POL 403.*', '.*POL 418.*', '.*HIS 427.*', '.*PHI 411.*', 
                    '.*REL 394.*'],
        'Thematic Courses': ['.*PHI .*', '.*POL .*', '.*HIS .*', '.*REL .*', 
                             '.*CHV .*']
    }

    return courses

def get_courses(minor):
    if minor == 'CLA':
        return cla_minor_courses()
    elif minor == 'ENV':
        return env_minor_courses()
    elif minor == 'LIN':
        return lin_minor_courses()
    elif minor == 'COS':
        return cos_minor_courses()
    elif minor == 'FIN':
        return fin_minor_courses()
    elif minor == 'GSS':
        return gss_minor_courses()
    elif minor == 'AFS':
        return afs_minor_courses()
    elif minor == 'ASA':
        return asa_minor_courses()
    elif minor == 'CHI':
        return chi_minor_courses()
    elif minor == 'CS':
        return cs_minor_courses()
    elif minor == 'CWR':
        return cwr_minor_courses()
    elif minor == 'DAN':
        return dan_minor_courses()
    elif minor == 'EAS':
        return eas_minor_courses()
    elif minor == 'ENG':
        return eng_minor_courses()
    elif minor == 'GHP':
        return ghp_minor_courses()
    elif minor == 'HIS':
        return his_minor_courses()
    elif minor == 'HLS':
        return hls_minor_courses()
    elif minor == 'HSTM':
        return hstm_minor_courses()
    elif minor == 'HUM':
        return hum_minor_courses()
    elif minor == 'JPN':
        return jpn_minor_courses()
    elif minor == 'JRN':
        return jrn_minor_courses()
    elif minor == 'KOR':
        return kor_minor_courses()
    elif minor == 'LAO':
        return lao_minor_courses()
    elif minor == 'MED':
        return med_minor_courses()
    elif minor == 'MPP':
        return mpp_minor_courses()
    elif minor == 'MQE':
        return mqe_minor_courses()
    elif minor == 'MSE':
        return mse_minor_courses()
    elif minor == 'MUS':
        return mus_minor_courses()
    elif minor == 'NEU':
        return neu_minor_courses()
    elif minor == 'PHI':
        return phi_minor_courses()
    elif minor == 'RES':
        return res_minor_courses()
    elif minor == 'SAS':
        return sas_minor_courses()
    elif minor == 'SLA':
        return sla_minor_courses()
    elif minor == 'SML':
        return sml_minor_courses()
    elif minor == 'TMT':
        return tmt_minor_courses()
    elif minor == 'TRA':
        return tra_minor_courses()
    elif minor == 'VIS':
        return vis_minor_courses()
    elif minor == 'VPL':
        return vpl_minor_courses()
    else:
        return None
#---------------------------------------------------------------------
def cla_minor_requirements():
    subrequirements = {
        "Prerequisites": 1,
        "Basic Requirements": 1,
        "Greek 4": 2,
        "Relevant Courses": 1,
        "Greek 5": 3,
        "Latin 4": 2,
        "Latin 5": 3,
        "Medicine 5": 3,
        "Medicine 4": 2,
        "Historical Survey": 2,
        "Track Requirements": 2
    }

    return subrequirements

def env_minor_requirements():
    subrequirements = {
        'Foundation Above 300 2': 2,
        'Foundation Above 300 1': 1,
        'Foundation Below 300 1': 1,
        'Elective Above 300 2': 2,
        'Elective Above 300 1': 1,
        'Elective Below 300 1': 1
    }

    return subrequirements

def cos_minor_requirements():
    subrequirements = {
        "Intro Course": 1,
        "ISC": 4,
        "Core Course": 1,
        "Electives": 3
    }

    return subrequirements

def fin_minor_requirements():
    subrequirements = {
        'MAT 175': 1,
        'Advanced Math': 1,
        'BSE Math': 2,
        'EGR': 1,
        'Micro': 1,
        'Probability/Stats': 1,
        'Core': 2,
        'Finanical Applications 1': 1,
        'Finanical Applications 2': 2,
        'General Electives 1': 1,
        'General Electives 2': 2
    }

    return subrequirements

def lin_minor_requirements():
    subrequirements = {
        'Prerequisites': 1,
        'Core Course': 1,
        'Methods': 1,
        'Electives': 2
    }

    return subrequirements

def gss_minor_requirements():
    subrequirements = {
        'Intro': 1,
        'Thematic': 3,
        'Elective': 1
    }

    return subrequirements

def afs_minor_requirements():
    subrequirements = {
        'Core': 1,
        'Humanities': 1,
        'African Language': 1,
        'Social Sciences': 1,
        'Other Electives': 1
    }

    return subrequirements

def asa_minor_requirements():
    subrequirements = {
        'Core': 1,
        'Electives': 3,
        'Advanced Seminar': 1
    }

    return subrequirements

def chi_minor_requirements():
    subrequirements = {
        'Advanced Language': 2,
        'Other Language': 4,
        'EAS/Cognate': 1
    }

    return subrequirements

def cs_minor_requirements():
    subrequirements = {
        'Core 2': 2,
        'Core 3': 3,
        'Core 4': 4,
        'Capstone 3': 3,
        'Capstone 2': 2,
        'Capstone 1': 1
    }

    return subrequirements

def cwr_minor_requirements():
    subrequirements = {
        'CWR Hosted': 3,
        'CWR Electives': 2
    }

    return subrequirements

def dan_minor_requirements():
    subrequirements = {
        'Studio': 1,
        'Seminar': 1,
        'Electives': 3
    }

    return subrequirements

def eas_minor_requirements():
    subrequirements = {
        'Advanced Language': 2,
        'Other Language': 2,
        '200-Level Content': 1,
        'Other Content': 2
    }

    return  subrequirements

def eng_minor_requirements():
    subrequirements = {
        'Seminars': 2,
        'English Courses': 3
    }

    return subrequirements

def ghp_minor_requirements():
    subrequirements = {
        'ISC': 4,
        'Foundation': 1,
        'Statistics': 1,
        'Core': 2,
        'Advanced Electives 4': 4,
        'Advanced Electives 3': 3,
        'Advanced Electives 2': 2,
        '200-Level Electives 2': 2,
        '200-Level Electives 1': 1
    }

    return subrequirements

def his_minor_requirements():
    subrequirements = {
        'HIS': 5
    }

    return subrequirements

def hls_minor_requirements():
    subrequirements = {
        'Gateway Seminar': 1,
        '400-Level Seminar': 1,
        'History, Society Religion': 1,
        'Language, Literature, Philosophy': 1,
        'Visual, Material Culture and Music': 1
    }

    return subrequirements

def hstm_minor_requirements():
    subrequirements = {
        'Core': 1,
        'Selected Courses': 2,
        'HOS/HIS Cognate': 1,
        'History': 1
    }

    return subrequirements

def hum_minor_requirements():
    subrequirements = {
        '200-Level Humanities': 1,
        'Tradition and Transformation': 1,
        'Global or Comparative Humanities': 1,
        'Engaged or Public Humanities': 1,
        'Humanities and Sciences in Dialogue': 1,
        'Data and Culture': 1,
        'Interdisciplinary Electives': 2
    }

    return subrequirements

def jpn_minor_requirements():
    subrequirements = {
        'Advanced Language': 2,
        'Other Language': 4,
        'EAS/Cognate': 1
    }

    return subrequirements

def jrn_minor_requirements():
    subrequirements = {
        'Gateway': 1,
        'Advanced': 2,
        'Electives': 2
    }

    return subrequirements

def kor_minor_requirements():
    subrequirements = {
        'Advanced Language': 2,
        'Other Language': 4,
        'EAS/Cognate': 1
    }

    return subrequirements

def lao_minor_requirements():
    subrequirements = {
        'Required': 1,
        'Breadth': 3,
        'Advanced Seminar': 1
    }

    return subrequirements

def med_minor_requirements():
    subrequirements = {
        'Single Course': 1,
        'Humanities Sequence': 2,
        'Medieval Topics': 3
    }

    return subrequirements

def mpp_minor_requirements():
    subrequirements = {
        'Core': 1,
        'Materials and Making': 1,
        'Culture and Criticism': 1,
        'Elective': 1,
        'Departmental': 1
    }

    return subrequirements

def mqe_minor_requirements():
    subrequirements = {
        'Multivariable Calculus': 1,
        'Linear Algebra': 1,
        'Statistics': 1,
        'Core Courses': 2,
        'Electives': 3
    }

    return subrequirements

def mse_minor_requirements():
    subrequirements = {
        '103-104 Sequence': 2,
        '105-106 Sequence': 2,
        '201-202 Sequence': 2,
        'Chemistry': 1,
        'Thermodynamics': 1,
        'Materials': 1,
        'Mathematics': 2,
        'Electives': 3,
        'Experimental Methods': 1
    }

    return subrequirements

def mus_minor_requirements():
    subrequirements = {
        'Core': 1,
        'Materials and Making': 1,
        'Culture and Criticism': 1,
        'Music Electives': 2
    }

    return subrequirements

def neu_minor_requirements():
    subrequirements = {
        'Fundamentals': 1,
        'Intro': 1,
        'Molecular/Cellular/Disease': 1,
        'Circuits & Systems': 1,
        'Neural Computation': 1,
        'Cognitive & Social Neuroscience': 1,
        'Other Electives': 1
    }

    return subrequirements

def phi_minor_requirements():
    subrequirements = {
        'Prerequisite': 1,
        'Advanced 5': 5,
        'Advanced 4': 4,
        'Advanced 3': 3,
        '200-Level 2': 2,
        '200-Level 1': 1
    }

    return subrequirements

def res_minor_requirements():
    subrequirements = {
        'History and Social Sciences': 2,
        'Literature, Arts and Culture': 2,
        'BCS': 2,
        'CZE': 2,
        'PLS': 2,
        'RUS': 2,
        'TUR': 2,
        'UKR': 2
    }

    return subrequirements

def sas_minor_requirements():
    subrequirements = {
        'Core': 1,
        'Language': 1,
        'Electives': 3
    }

    return subrequirements

def sla_minor_requirements():
    subrequirements = {
        'First Requirement': 1,
        'Second Requirement': 1,
        'Departmentals': 3
    }

    return subrequirements

def sml_minor_requirements():
    subrequirements = {
        'Statistics': 1,
        'Machine Learning': 1,
        'Electives': 3
    }

    return subrequirements

def tmt_minor_requirements():
    subrequirements = {
        'Introduction': 1,
        'Additional Courses': 2,
        'Electives': 2,
        'Dramaturgical': 1
    }

    return subrequirements

def tra_minor_requirements():
    subrequirements = {
        'Core': 2,
        'Upper-Level Course': 1,
        'Cross-listed by TRA': 1,
        'Understanding of Translation': 1,
        'Other Additional Course': 1
    }

    return subrequirements

def vis_minor_requirements():
    subrequirements = {
        'Studio': 3,
        'Artist and Studio': 1,
        'Exhibition Issues and Methods': 1,
        'Art and Archaeology': 1,
        'Elective': 1
    }

    return subrequirements

def vpl_minor_requirements():
    subrequirements = {
        'Intro': 1,
        'Political Theory': 1,
        'Seminar': 1,
        'Thematic Courses': 2
    }

    return subrequirements

def get_minor_requirements(minor):
    if minor == 'CLA':
        return cla_minor_requirements()
    elif minor == 'ENV':
        return env_minor_requirements()
    elif minor == 'LIN':
        return lin_minor_requirements()
    elif minor == 'COS':
        return cos_minor_requirements()
    elif minor == 'FIN':
        return fin_minor_requirements()
    elif minor == 'GSS':
        return gss_minor_requirements()
    elif minor == 'AFS':
        return afs_minor_requirements()
    elif minor == 'ASA':
        return asa_minor_requirements()
    elif minor == 'CHI':
        return chi_minor_requirements()
    elif minor == 'CS':
        return cs_minor_requirements()
    elif minor == 'CWR':
        return cwr_minor_requirements()
    elif minor == 'DAN':
        return dan_minor_requirements()
    elif minor == 'EAS':
        return eas_minor_requirements()
    elif minor == 'ENG':
        return eng_minor_requirements()
    elif minor == 'GHP':
        return ghp_minor_requirements()
    elif minor == 'HIS':
        return his_minor_requirements()
    elif minor == 'HLS':
        return hls_minor_requirements()
    elif minor == 'HSTM':
        return hstm_minor_requirements()
    elif minor == 'HUM':
        return hum_minor_requirements()
    elif minor == 'JPN':
        return jpn_minor_requirements()
    elif minor == 'JRN':
        return jrn_minor_requirements()
    elif minor == 'KOR':
        return kor_minor_requirements()
    elif minor == 'LAO':
        return lao_minor_requirements()
    elif minor == 'MED':
        return med_minor_requirements()
    elif minor == 'MPP':
        return mpp_minor_requirements()
    elif minor == 'MQE':
        return mqe_minor_requirements()
    elif minor == 'MSE':
        return mse_minor_requirements()
    elif minor == 'MUS':
        return mus_minor_requirements()
    elif minor == 'NEU':
        return neu_minor_requirements()
    elif minor == 'PHI':
        return phi_minor_requirements()
    elif minor == 'RES':
        return res_minor_requirements()
    elif minor == 'SAS':
        return sas_minor_requirements()
    elif minor == 'SLA':
        return sla_minor_requirements()
    elif minor == 'SML':
        return sml_minor_requirements()
    elif minor == 'TMT':
        return tmt_minor_requirements()
    elif minor == 'TRA':
        return tra_minor_requirements()
    elif minor == 'VIS':
        return vis_minor_requirements()
    elif minor == 'VPL':
        return vpl_minor_requirements()
    else:
        return None
