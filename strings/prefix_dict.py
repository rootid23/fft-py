#Give a String[] as follows. After you have entered a capital letter and a few lowercase letters,
#implement autocomplete.
#Capital letters must all match. The feeling is to use Trie, but how do you save it? Welcome to
#discuss.
#String[]  className {
#        "GraphView",
#        "DataGraphView",
#        "DataController",.
#        "GraphViewController",
#        "DataScienceView"
#}
#autocomplete(String[] className, "Data"); --> {"DataGraphView", "DataController",
#"DataScienceView"};
#autocomplete(String[] className, "GVi");   -->  {"GraphView",  "GraphViewController"};
#autocomplete(String[] className, "GraphController");   -->  {""};

import re
lst = [ "GraphView",
        "DataGraphView",
        "DataController",
        "GraphViewController",
        "DataScienceView" ]

prefix_dict = {}

for str in lst:
  # print(str)
  key = re.sub(r'[^A-Z]', '', str)
  for i in range(1, len(key) + 1) :
     prfx = key[:i]
     print(prfx)
    #  sfx = [:i]
     if(prfx not in prefix_dict) :
      prefix_dict[prfx] = []
     prefix_dict[prfx] += [ str ]
#print(prefix_dict)

qry = [ 'Data', 'GVi', 'GraphController' ]
for q in qry :
  fq = re.sub(r'[^A-Z]', '', q)
  print (fq)
  if(fq in prefix_dict) :
    print(prefix_dict[fq])
