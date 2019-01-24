import sys, getopt


def main(argv):
    """
    Zum einstellen der IP Adresse
    :param argv:
    :return:
    """

    host = ''
    port = ''
    try:
        opts, args = getopt.getopt(argv, "hi:p:", ["host=", "port="])
    except getopt.GetoptError:
        print('test.py -h <ip_addresse> -p <port>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <ip_addresse> -p <port>')
            sys.exit()
        elif opt in ("-i", "--host"):
            host = arg
            check = host.split(".");
            if len(check) != 4:
               host = ''
            else:
                for nums in check:
                    if len(nums) != 3:
                        host = ''
                    else:
                        if nums.isdigit():
                            continue
                        else:
                            host = ''

        elif opt in ("-p", "--port"):
            port = arg
            if port.isdigit():
                continue
            else:
                port = ''
    print('Host is "', host)
    print('Port  is "', port)


if __name__ == "__main__":
    main(sys.argv[1:])
