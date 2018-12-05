
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    T, N, Q, A, QS = 0,0,0, [], []
    qs = []
    while True:
        try :
            i = input()
            T = int(i)
            for _ in range(T) :
                tmp = input().split()
                N = int(tmp[0])
                Q = int(tmp[1])
                A = input().split()
                for _ in range(Q) :
                    tmp = input().split()
                    QS += [ ( int(tmp[0]), int(tmp[1])) ]

                t_lst = []
                for idx in range(len(QS)) :

                    (x, y) = QS[idx][0], QS[idx][1]
                    mx = max(x,y)
                    cnt = 1
                    psz = 0
                    if(len(t_lst) > 0) :
                        t_lst += [ set(x,y) ]
                    else :
                        for i in range( len(t_lst) ):
                            tmp_set = t_lst[i]
                            if(x in tmp_set or y in tmp_set) :
                                tmp_set.add(x)
                                tmp_set.add(y)


        except EOFError :
            break

    return 0

if __name__ == '__main__':
    main()
