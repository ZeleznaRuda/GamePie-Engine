import sys
import argparse

def main():
    from ..utils.func import build

    parser = argparse.ArgumentParser(
        description="Build a GamePie script into an executable."
    )
    parser.add_argument("script_path", help="Path to the Python script to build.")
    parser.add_argument(
        "--icon",
        help="Path to the icon file.",
        default=None
    )
    parser.add_argument(
        "--windowed",
        action="store_true",
        help="Build with windowed mode (no console)."
    )
    parser.add_argument(
        "--output",
        help="Output directory for the build.",
        default=None
    )

    args = parser.parse_args()

    build(
        args.script_path,
        icon=args.icon,
        windowed=args.windowed,
        output_dir=args.output,
    )


if __name__ == "__main__":
    main()
