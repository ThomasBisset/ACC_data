# up to date as of 1.8.12

import time
import math

def sessionType(sessionType):
    if sessionType == -1:
        return "Unknown"
    elif sessionType == 0:
        return "Practice"
    elif sessionType == 1:
        return "Qualifying"
    elif sessionType == 2:
        return "Race"
    elif sessionType == 3:
        return "Hotlap"
    elif sessionType == 4:
        return "Time Attack"
    elif sessionType == 5:
        return "Drift"
    elif sessionType == 6:
        return "Drag"
    elif sessionType == 7:
        return "Hot Stint"
    elif sessionType == 8:
        return "Hot Stint Superpole"
    else:
        return "NULL"

def gripStatus(gripStatus):
    if gripStatus == 0:
        return "Green"
    elif gripStatus == 1:
        return "Fast"
    elif gripStatus == 2:
        return "Optimum"
    elif gripStatus == 3:
        return "Greasy"
    elif gripStatus == 4:
        return "Damp"
    elif gripStatus == 5:
        return "Wet"
    elif gripStatus == 6:
        return "Flooded"
    else:
        return "NULL"

def rainStatus(rainStatus):
    if rainStatus == 0:
        return "No Rain"
    elif rainStatus == 1:
        return "Drizzle"
    elif rainStatus == 2:
        return "Light Rain"
    elif rainStatus == 3:
        return "Medium Rain"
    elif rainStatus == 4:
        return "Heavy Rain"
    elif rainStatus == 5:
        return "Thunderstorm"
    else:
        return "NULL"

def car(car):
    if car == "amr_v12_vantage_gt3":
        return "Aston Martin Vantage V12 GT3 2013"
    elif car == "audi_r8_lms":
        return "Audi R8 LMS 2015"
    elif car == "bentley_continental_gt3_2016":
        return "Bentley Continental GT3 2015"
    elif car == "bentley_continental_gt3_2018":
        return "Bentley Continental GT3 2018"
    elif car == "bmw_m6_gt3":
        return "BMW M6 GT3 2017"
    elif car == "jaguar_g3":
        return "Emil Frey Jaguar G3 2012"
    elif car == "ferrari_488_gt3":
        return "Ferrari 488 GT3 2018"
    elif car == "honda_nsx_gt3":
        return "Honda NSX GT3 2017"
    elif car == "lamborghini_gallardo_rex":
        return "Lamborghini Gallardo G3 Reiter 2017"
    elif car == "lamborghini_huracan_gt3":
        return "Lamborghini Huracan GT3 2015"
    elif car == "lamborghini_huracan_st":
        return "Lamborghini Huracan ST 2015"
    elif car == "lexus_rc_f_gt3":
        return "Lexus RCF GT3 2016"
    elif car == "mclaren_650s_gt3":
        return "McLaren 650S GT3 2015"
    elif car == "mercedes_amg_gt3":
        return "Mercedes AMG GT3 2015"
    elif car == "nissan_gt_r_gt3_2017":
        return "Nissan GTR Nismo GT3 2015"
    elif car == "nissan_gt_r_gt3_2018":
        return "Nissan GTR Nismo GT3 2018"
    elif car == "porsche_991_gt3_r":
        return "Porsche 991 GT3 R 2018"
    elif car == "porsche_991ii_gt3_cup":
        return "Porsche9 91 II GT3 Cup 2017"
    elif car == "amr_v8_vantage_gt3":
        return "Aston Martin V8 Vantage GT3 2019"
    elif car == "audi_r8_lms_evo":
        return "Audi R8 LMS Evo 2019"
    elif car == "honda_nsx_gt3_evo":
        return "Honda NSX GT3 Evo 2019"
    elif car == "lamborghini_huracan_gt3_evo":
        return "Lamborghini Huracan GT3 EVO 2019"
    elif car == "mclaren_720s_gt3":
        return "McLaren 720S GT3 2019"
    elif car == "porsche_991ii_gt3_r":
        return "Porsche 911 II GT3 R 2019"
    elif car == "alpine_a110_gt4":
        return "Alpine A110 GT4 2018"
    elif car == "amr_v8_vantage_gt4":
        return "Aston Martin Vantage AMR GT4 2018"
    elif car == "audi_r8_gt4":
        return "Audi R8 LMS GT4 2016"
    elif car == "bmw_m4_gt4":
        return "BMW M4 GT42 018"
    elif car == "chevrolet_camaro_gt4r":
        return "Chevrolet Camaro GT4 R 2017"
    elif car == "ginetta_g55_gt4":
        return "Ginetta G55 GT4 2012"
    elif car == "ktm_xbow_gt4":
        return "Ktm Xbow GT4 2016"
    elif car == "maserati_mc_gt4":
        return "Maserati Gran Turismo MC GT4 2016"
    elif car == "mclaren_570s_gt4":
        return "McLaren 570s GT4 2016"
    elif car == "mercedes_amg_gt4":
        return "Mercedes AMG GT4 2016"
    elif car == "porsche_718_cayman_gt4_mr":
        return "Porsche 718 Cayman GT4 MR 2019"
    elif car == "ferrari_488_gt3_evo":
        return "Ferrari 488 GT3 Evo 2020"
    elif car == "mercedes_amg_gt3_evo":
        return "Mercedes AMG GT3 Evo 2020"
    elif car == "bmw_m4_gt3":
        return "BMW M4 vGT3 2021"
    elif car == "audi_r8_lms_evo_ii":
        return "Audi R8 LMS Evo II 2022"
    elif car == "bmw_m2_cs_racing":
        return "BMW M2 Cup 2020"
    elif car == "ferrari_488_challenge_evo":
        return "Ferrari 488 Challenge Evo 2020"
    elif car == "lamborghini_huracan_st_evo2":
        return "Lamborghini Huracan ST Evo2 2021"
    elif car == "porsche_992_gt3_cup":
        return "Porsche 992 GT3 Cup 2021 "
    else:
        return "NULL"

def secondsToTime(s):
    output = time.strftime("%H:%M:%S", time.gmtime(s))
    return output

def millisecondsToTime(ms):
    if ms == "NULL" or ms == 2147483647:
        return "NULL"
    else:
        s = ms / 1000
        new_ms = int(round((math.modf(s)[0]) * 1000, 3))
        output = time.strftime("%M:%S", time.gmtime(s)) + "." + str(new_ms)
        return output