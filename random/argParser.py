import argparse


def parse_cmd (args=None):
    """ Function to check command line arguments """

    parse = argparse.ArgumentParser(description="Script to add dns records")

    parse.add_argument('-n', '--name', help='Hostname', required=True)
    parse.add_argument('-i', '--ip', help='IP Address')
    parse.add_argument('-c', '--cname', help='CNAME of the host', action='store_true')
    parse.add_argument('-f', '--fqdn', help='Host that CNAME points to')

    result = parse.parse_args(args)

    return(result.name, result.ip, result.cname, result.fqdn)

def main():
    full_name, ip, cname, fqdn = parse_cmd(sys.argv[1:])
