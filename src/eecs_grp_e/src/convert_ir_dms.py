# 25 cm ==> 924.22 ==> 36.9688
# 20 cm ==> 1097.389 ==> 54.86945
# 15 cm ==> 1413.833 ==> 94.2555
# 10 cm ==> 2064.759 ==> 206.4759
# 5  cm ==> 2688.91 ==> 537.782
# conv: 186.07033 = [sens] / [cm]
# conv: [cm] = [sens] / k

K = 186.07033

def convert_dms_cm(dms_val):
    return dms_val / K


def convert_ir_cm(ir_val):
    return ir_val / K
