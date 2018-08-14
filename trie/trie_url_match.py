

def main() :
    #Process input
    input_lst = []
    query_list = []
    is_query_start = False
    while True :
        try :
           input = raw_input()
           if (input.startswith('#')) :
                is_query_start = True
                continue
           if(is_query_start) :
               query_list += [ input ]
           else :
               request, endpoint = input.split()
               input_lst += [ ( request, endpoint ) ]
        except EOFError:
            break

    #Buid Trie
    trie_root = build_trie(input_lst)

    #Query Urls
    rst = query_urls(trie_root, query_list)

    #Output result
    output_result(rst)


def build_trie(input_lst) :
    trie = {}
    for idx in range( len(input_lst) ) :
        nodes, endpoint = input_lst[idx][0].split('/'), \
                          input_lst[idx][1]
        current_node = trie
        for node in nodes :
            if(node not in current_node) :
                current_node[ node ] = {}
            current_node = current_node[ node ]
        current_node['#'] = endpoint
    return trie

def query_urls(trie, query_list) :
    rst = []
    for idx in range( len(query_list)) :
       qry = query_list[idx]
       rst += [ get_matching_url(trie, qry)]
    return rst


def get_matching_url(trie, qry) :
    t_ptr = trie
    nodes = qry.split('/')
    path_not_found = False
    nxt_possible_nodes = []
    idx = 0
    for node in nodes :
        if('X' in t_ptr) :
          nxt_possible_nodes += [ (idx+1, t_ptr['X']) ]
        if(node in t_ptr) :
          t_ptr = t_ptr[node]
        elif('X' in t_ptr) :
          t_ptr = t_ptr['X']
        else :
          path_not_found = True
          break
        idx += 1

    if(path_not_found == True) :
        ept = ""
        for idx_tv_tuple in nxt_possible_nodes[::-1]:
            path_f = explore(idx_tv_tuple, nodes)
            if("" != path_f) :
              ept = path_f
              return ept
        return ept
    return get_url(t_ptr)


def explore(idx_tv_tuple, nodes) :
    idx, t_ptr = idx_tv_tuple

    t_len = len(nodes)
    path_not_found = False
    while idx < t_len :
        node = nodes[idx]
        if (node in t_ptr) :
           t_ptr = t_ptr[node]
        else :
           path_not_found = True
           break
        idx += 1
    if(path_not_found == True) : return ""
    return get_url(t_ptr)


def get_url(t_ptr) :
    if('#' in t_ptr) :
      return(t_ptr['#'])
    return ""

def get_reg_url_match(t_ptr) :
   if('X' in t_ptr) :
      return t_ptr['X']
   return None


def output_result(rst) :
    for r in rst :
        if(r == "") : print "404"
        else : print r

if __name__ == '__main__':
    main()

