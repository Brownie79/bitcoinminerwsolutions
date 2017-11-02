import hashlib, struct, codecs
 
ver = 
prev_block = ""
mrkl_root = ""  
time_ =  
bits = 
nonce = 0 

# https://en.bitcoin.it/wiki/Difficulty
exp = bits >> 24
mant = bits & 0xffffff
target_hexstr = '%064x' % (mant * (1<<(8*(exp - 3))))
target_str = codecs.decode(target_hexstr, "hex")
 

header = ( struct.pack("<L", ver) + codecs.decode(prev_block, "hex")[::-1] +
      codecs.decode(mrkl_root, "hex")[::-1] + struct.pack("<LLL", time_, bits, nonce))
hash = hashlib.sha256(hashlib.sha256(header).digest()).digest()
print( nonce, codecs.encode(hash[::-1], "hex"))
if hash[::-1] < target_str:
    print('success')
else
    print('try again!')

