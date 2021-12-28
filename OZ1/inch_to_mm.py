def inch_to_mm(inch):
    return round((inch * 25.4), 2)

print('8.5" x 11" in converted to milimeters is: ' f'{inch_to_mm(8.5)}mm x {inch_to_mm(11)}mm')
