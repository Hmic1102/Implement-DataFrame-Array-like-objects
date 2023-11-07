class BitList:
    def __init__(self, bits):
        allowed='10'
        if(all(ch in allowed for ch in bits)):
            self.bits=bits
        else:
            raise ValueError('Format is invalid; does not consist of only 0 and 1')
        
    def __eq__(self, other):
        return self.bits==other.bits
    
    @staticmethod
    def from_ints(*args):
        bits=''
        for arg in args:
            bits+=str(arg)
        allowed='10'
        if(all(ch in allowed for ch in bits)):
            return BitList(bits)
        else:
            raise ValueError('Format is invalid; does not consist of only 0 and 1')
    
    def __str__(self):
        return self.bits
    
    def arithmetic_shift_left(self):
        bits=str(self)[1:]+'0'
        self.bits = bits
    
    def arithmetic_shift_right(self):
        bits=str(self)[0]+str(self)[:-1]
        self.bits= bits 
        
    def bitwise_and(self, otherBitList):
        bits=''
        for a,b in zip(self.bits,str(otherBitList)):
            bits+=str(int(a)*int(b))
            
        return BitList(bits)
            
    def chunk(self,chunk_length):
        bits=str(self.bits)
        if(len(self.bits)%chunk_length!=0):
            raise ChunkError('Invalid length; length should be divisible by BitList')
        else:
            chunks = [list(bits[i:i+chunk_length]) for i in range(0, len(self.bits), chunk_length)]
            for i in range(len(chunks)):
                chunks[i]=list(map(int, chunks[i]))
            return chunks
            
    def decode(self, encoding='utf-8'):
        code=''
        if (encoding=='utf-8'):
            chunk=self.chunk(8)
            for i in range(len(chunk)):
                chunk[i]=list(map(str, chunk[i]))
            index=0
            while index < len(chunk):
                bits=''
                n=(''.join(chunk[0+index]))
                number=n.find('0')
                if(number not in [0,2,3,4]):
                    raise DecodeError('invalid leading byte')
                if(number==0):
                    code+=chr(int(n,2))
                    index+=1
                else:
                    bits+=n[number:]
                    for i in range(1+index,number+index):
                        temp=(''.join(chunk[i]))
                        if(temp.find('10')==0):
                            bits+=temp[2:]
                        else:
                            raise DecodeError('invalid continuation byte')
                    code+=chr(int(bits,2))
                index+=number
                    
            return code
        
        elif(encoding=='us-ascii'):
            chunk=self.chunk(7)
            for i in range(len(chunk)):
                chunk[i]=list(map(str, chunk[i]))
            for i in chunk:
                code+=chr(int(''.join(i),2))
            return code
                
            
        else:
            raise ValueError ('only utf-8 and us-ascii are accepted')
            
        
        
class ChunkError(Exception):
    pass
class DecodeError(Exception):
    pass
