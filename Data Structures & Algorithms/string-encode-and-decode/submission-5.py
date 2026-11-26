class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for s in strs:
            encode_str = encode_str + str(len(s)) + "#" + s
        print(encode_str)
        return encode_str



    def decode(self, s: str) -> List[str]:
        print(s)
        decode_list = []
        len_str = -1
        temp_str = ""
        str_present = False
        t = -1
        for i, ch in enumerate(s):
            # print(ch)
            if t > 0:
                t-=1
                continue

            if (ch in ('0','1','2','3','4','5','6','7','8','9')) and (str_present == False):
                if len_str == -1:
                    len_str = int(ch)
                else:
                    len_str = (len_str * 10) + int(ch)
                # print(len_str)
            elif (ch == '#') and (str_present == False) and (len_str>=0):
                str_present = True
                t = len_str
                for j in range(i+1,i+1+len_str):
                    temp_str = temp_str + s[j]
                    len_str -=1
                if len_str == 0:
                    decode_list.append(temp_str)
                    str_present = False
                    temp_str = ""
                    len_str = -1
            

                
            print(i)
                
        print(decode_list)
        return decode_list