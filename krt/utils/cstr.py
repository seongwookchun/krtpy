class Cstr(str):
    ord_upper = ord('天')
    ord_lower = ord('地')
    ord_const_upper = ord_upper - ord('A')
    ord_const_lower = ord_lower - ord('a')
    def __init__(self, obj):
        super().__init__()
        self.content = obj
    
    def to_specialChr(self):
        for idx, c in enumerate(self.content):
            if ord(c) >= ord('A') and ord(c) <= ord('Z'):
                self.content = (self.content[:idx] + 
                                chr(ord(c) + self.ord_const_upper) + 
                                self.content[idx+1:])
            elif ord(c) >= ord('a') and ord(c) <= ord('z'):
                self.content = (self.content[:idx] + 
                                chr(ord(c) + self.ord_const_lower) + 
                                self.content[idx+1:])
        return Cstr(self.content)

    def to_originChr(self):
        #print('to_originChr')
        for idx, c in enumerate(self.content):
            if ord(c) >= self.ord_upper and ord(c) <= (self.ord_upper +25):
                self.content = (self.content[:idx] + 
                                chr(ord(c) - self.ord_const_upper) + 
                                self.content[idx+1:])
            elif ord(c) >= self.ord_lower and ord(c) <= (self.ord_lower +25):
                self.content = (self.content[:idx] + 
                                chr(ord(c) - self.ord_const_lower) + 
                                self.content[idx+1:])
        return Cstr(self.content)
