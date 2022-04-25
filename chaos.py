# report03 Ibuki Yoshijima
import math
import numpy as np

def logistic(a):
    x = [0.001]  # x0
    for i in range(1000):
        tmp = round(a * x[-1] * (1 - x[-1]), 10)  # 小数点10桁組み込み
        x.append(tmp)
    return x[-300:]  # 後ろから300個の要素


a0 = 1+math.sqrt(6)  # a初期値
step = 0.0001  # a増加幅
period = 4  # 周期
error = 0.001  # 誤差

print('周期:{0}'.format(period))
print(a0, step, error)
for a in np.arange(a0, 4.0, step):
    x = logistic(a)

    if math.fabs(x[0]-x[period]) >= error:
        print(a)
        break

"""
周期:4
3.449489742783178 0.0001 0.001
3.543789742783377

周期:8
3.543789742783377 0.0001 0.001
3.5643897427834204

周期:16
3.5643897427834204 1e-06 0.0001
3.5686537427840164

周期:32
3.5686537427840164 1e-07 0.0001
3.569019842783417

周期:64
3.569019842783417 1e-07 0.0001
3.569908952782998

周期:128
3.569908952782998 1e-08 0.0001
3.569920312782929
"""
