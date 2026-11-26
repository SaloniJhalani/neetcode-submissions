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
        length = 0
        i = 0
        while i < len(s):

            if s[i].isdigit():
                length = (length * 10) + int(s[i])
                i +=1
            else:
                decode_list.append(s[i+1:i+1+length])
                i = i + 1 + length
                length = 0

                
        print(decode_list)
        return decode_list