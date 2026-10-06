"""describe-stats-cli — 描述统计。

均值/中位数/众数/方差/分位数/偏态，文件输入。零第三方依赖。
"""
from __future__ import annotations

import math
import statistics as st


def describe(values: list[float]) -> dict:
    n = len(values)
    if n == 0:
        return {"count": 0}
    s = sorted(values)
    mean = sum(values) / n
    median = st.median(values)
    try:
        mode = st.mode(values)
    except st.StatisticsError:
        mode = s[0]
    var = st.pvariance(values) if n > 1 else 0.0
    p25 = _quantile(s, 0.25)
    p75 = _quantile(s, 0.75)
    if var > 0 and n > 2:
        m3 = sum((x - mean) ** 3 for x in values) / n
        skew = m3 / (math.sqrt(var) ** 3)
    else:
        skew = 0.0
    return {
        "count": n,
        "min": s[0], "max": s[-1],
        "mean": round(mean, 3),
        "median": median,
        "mode": mode,
        "variance": round(var, 3),
        "std": round(math.sqrt(var), 3),
        "p25": p25, "p75": p75,
        "skewness": round(skew, 3),
    }


def _quantile(sorted_vals: list[float], q: float) -> float:
    k = (len(sorted_vals) - 1) * q
    lo = int(k)
    hi = min(lo + 1, len(sorted_vals) - 1)
    return round(sorted_vals[lo] + (sorted_vals[hi] - sorted_vals[lo]) * (k - lo), 3)
