
import argparse
from ..plugins import plugfn  # import funkcí install/uninstall

def main():
    parser = argparse.ArgumentParser(
        description="Menu for GamePie plugins."
    )
    parser.add_argument(
        "--install",
        help="Install plugin from folder path or URL",
        default=None
    )
    parser.add_argument(
        "--uninstall",
        help="Uninstall plugin by specifying the name",
        default=None
    )

    args = parser.parse_args()

    if args.install:
        plugfn.install(args.install)

    if args.uninstall:
        plugfn.uninstall(args.uninstall)

if __name__ == "__main__":
    main()
