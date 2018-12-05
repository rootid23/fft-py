
def get_hash_code_by_horner(s) :
  if(not s) : return None
  hash_code = 0
  for i in range(len(s)) :
    hash_code += ord(s[i]) * 31
  return hash_code


def get_hash_code(s):
  return get_hash_code_by_horner(s)

print(get_hash_code('werwerwerwerwerwerw') )
assert(get_hash_code('werwerwerwerwerwerw') == get_hash_code("werwerwerwerwerwerw"))
assert(get_hash_code('werwerwerwerwerwerw') != get_hash_code("werwerwerwerwerwerw1"))
