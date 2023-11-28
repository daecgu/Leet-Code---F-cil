class Solution:
    def same_len(self, s: str, t: str) -> bool:
        return len(s) == len(t)

    def same_ammount_different_characters(self, s: str, t:str):
        return (len(set(s)) == len(set(t)))


    def mapeo(self,s,t):
        # mapeo_s_a_t: dict = {}
        # mapeo_t_a_s: dict = {}
        # for caracter_s, caracter_t in zip(s, t):
        #     if (caracter_s in mapeo_s_a_t and mapeo_s_a_t[caracter_s] != caracter_t) or \
        #             (caracter_t in mapeo_t_a_s and mapeo_t_a_s[caracter_t] != caracter_s):
        #         return False
        #
        #     mapeo_s_a_t[caracter_s] = caracter_t
        #     mapeo_t_a_s[caracter_t] = caracter_s
        # return True
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

    def isIsomorphic(self, s: str, t: str) -> bool:
        if not self.same_len(s, t):
            return False

        if not self.same_ammount_different_characters(s,t):
            return False

        if not self.mapeo(s, t):
            return False

        return True





