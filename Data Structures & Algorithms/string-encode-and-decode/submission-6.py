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
        for i, ch in enumerate(s):
            if (len_str >= 0) and (str_present == True):
                temp_str = temp_str + s[i]
                len_str-=1

            elif (ch in ('0','1','2','3','4','5','6','7','8','9')) and (str_present == False):
                if len_str == -1:
                    len_str = int(ch)
                else:
                    len_str = (len_str * 10) + int(ch)
            elif (ch == '#') and (str_present == False):
                str_present = True
                            
                            
            if (len_str == 0) and (str_present == True):
                decode_list.append(temp_str)
                str_present = False
                temp_str = ""
                len_str = -1
       
            print(i)
                
        print(decode_list)
        return decode_list