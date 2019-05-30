#How to improve it?
#How to optimize it?

#Union find application
def nameResolver(nvpair, syn) :

  #Can we reduce the reverse?
  label = {}
  rev_label = {}
  idx = 0
  rst = []
  for name, cnt in nvpair :
    label[name] = idx
    rev_label[idx] = name
    idx += 1
  uf = [0] * idx

  for i in range(idx) :
    uf[i] = i

  #Modularize it
  for u,v in syn :
    if(u in label and v in label) :
      u1 = label[u]
      v1 = label[v]
      uv = uf[u1]
      vv = uf[v1]
      for i in range(idx) :
        if(uv == uf[i]) :
          uf[i] = vv
  rst = {}
  #use maping
  for name, cnt in nvpair :
      idx = label[name]
      root = uf[idx]
      key = rev_label[root]
      rst[key] = cnt + rst.get(key, 0)

  print(rst)


nameResolver( [ ("John", 20), ("Jon", 30), ("john", 20), ("Kris", 13), ("Chris", 4), ("Chirsto", 19) ] , [("John", "Jon"), ("Jon", "john"), ("John", "Johny"), ("Chris", "Kris"), ("Chris", "Chirsto")])




