def omzetting_seconden(seconden):
    days = 0
    hours = 0
    minutes = 0
    s_copy = seconden
    while seconden >= 60:
        minutes += 1
        if minutes >= 60:
            hours += 1
            minutes -= 60
            if hours >= 24:
                days += 1
                hours -= 24
        seconden -= 60
    print(f'{s_copy} seconden komt overeen met {days} dagen, {hours} uren, {minutes} minuten en {seconden} seconden.')

omzetting_seconden(78686969)
