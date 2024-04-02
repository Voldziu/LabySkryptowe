import argparse
import Zad4
import Zad2


def parse_arguments():
    parser = argparse.ArgumentParser(description='Zadanie 5 parser')
    parser.add_argument("logfile", help="Path to the log file")
    parser.add_argument("--level", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
                        help="Minimum logging level")

    subparsers = parser.add_subparsers(title="Available commands", dest="command")

    subparsers.add_parser("Func2a", help="do Functionality 2a")
    subparsers.add_parser("Func2b", help="do Functionality 2b")
    subparsers.add_parser("Func2c", help="do Functionality 2c")
    subparsers.add_parser("Func2d", help="do Functionality 2d")

    subparsers.add_parser("Func3", help="do Functionality 3")

    func4a = subparsers.add_parser("Func4a", help="do Functionality 4a")
    func4a.add_argument("--n",default=3,type=int,help='podaj n')
    func4bparser = subparsers.add_parser("Func4b", help="do Functionality 4b")
    func4bparser.add_argument("--Global", action="store_true", help='True for all log, Flase for group by users')
    subparsers.add_parser("Func4c", help="do Functionality 4c")

    set_level_parser = subparsers.add_parser("set-level", help="Set minimum logging level")
    set_level_parser.add_argument("level", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], help="Minimum logging level")
    return parser.parse_args()


def main():
    args = parse_arguments()
    print(args)
    print(f'Analyzing log file from directory: {args.logfile}')
    file_dir = args.logfile
    if args.command == "Func2a":
        print(Zad2.zad2a(file_dir))
    elif args.command == "Func2b":
        print(Zad2.zad2b(file_dir))
    elif args.command == "Func2c":
        print(Zad2.zad2c(file_dir))
    elif args.command == "Func2d":
        print(Zad2.zad2d(file_dir))
    elif args.command == "Func4a":
        print(Zad4.zad4a(file_dir=args.logfile, n=args.n))
    elif args.command == "Func4b":
        print(Zad4.zad4b(file_dir, global_=args.Global))
    elif args.command == "Func4c":
        print(Zad4.zad4c(file_dir))


if __name__ == "__main__":
    main()
