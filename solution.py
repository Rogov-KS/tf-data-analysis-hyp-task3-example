import pandas as pd
import numpy as np
import scipy.stats as sps


chat_id = 1022061330 # Ваш chat ID, не меняйте название переменной


def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.03
    
    res_pvalue = sps.ttest_ind(x, y)[1]
    
    do_reject = (res_pvalue < alpha)
    return do_reject # Ваш ответ, True или False
