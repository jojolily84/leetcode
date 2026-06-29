class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        for cs, ct in zip(s, t):
            if cs in s_to_t:
                if s_to_t[cs] != ct:
                    return False
            else:                 #cs 尚未 mapping → 檢查 ct 是否已被佔用
                if ct in t_to_s:  # 但 ct 已經被別的 char 佔走了
                    return False
                s_to_t[cs] = ct
                t_to_s[ct] = cs
        return True
