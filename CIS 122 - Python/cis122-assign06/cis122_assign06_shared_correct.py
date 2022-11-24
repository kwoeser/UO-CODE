

def pad_string(data, size, dir = 'L', chr = ' '):
   data = str(data)
   if len(data) > size:
      return data
   elif dir.upper() == 'L':
      return chr * (size - len(data)) + data
   else:
      return data + chr * (size - len(data))

def pad_left(data, size, chr = ' '):
   return pad_string(data, size, 'L', chr)

def pad_right(data, size, chr = ' '):
   return pad_string(data, size, 'R', chr)
