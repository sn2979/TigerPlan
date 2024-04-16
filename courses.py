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
        'Core Courses 1': ['.*LIN 301.*', '.*LIN 302.*', '.*LIN 303.*', '.*LIN 306.*', 
        '.*PHI 334 / LIN 334.*'],
        'Core Courses 2': ['.*LIN 301.*', '.*LIN 302.*', '.*LIN 303.*', '.*LIN 306.*', 
        '.*PHI 334 / LIN 334.*'],
        'Methods 1': ['.*LIN 210.*', '.*LIN 310.*', '.*LIN 355.*', '.*LIN 356.*'],
        'Methods 2': ['.*LIN 210.*', '.*LIN 310.*', '.*LIN 355.*', '.*LIN 356.*'],
        'Electives 1': ['.*LIN 2.*', '.*LIN 3.*', '.*LIN 4.*', '.*LIN 5.*'],
        'Electives 2': ['.*LIN 2.*', '.*LIN 3.*', '.*LIN 4.*', '.*LIN 5.*']
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
        'Core Courses 1': 1,
        'Core Courses 2': 2,
        'Methods 1': 1,
        'Methods 2': 2,
        'Electives 1': 1,
        'Electives 2': 2
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
    else:
        return None
