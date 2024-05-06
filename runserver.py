import sys
import argparse
import application

def arg_parser():
    parser = argparse.ArgumentParser(
        description="The registrar application")
    parser.add_argument("port", help="the port at which the server \
                        should listen", type=int)
    args = parser.parse_args()
    return (args.port)

def main(arg_port):
    try:
        application.app.run(host='0.0.0.0', port=arg_port, debug=True)
    except Exception as ex:
        # print(ex, file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    arg_port = arg_parser()
    main(arg_port)
