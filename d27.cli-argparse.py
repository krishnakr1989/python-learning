import argparse
from collections import Counter


def analyze_log(filename, top_n):
    error_count = Counter()

    try:
        with open(filename, "r") as file:
            for line in file:
                if "ERROR" in line:
                    # Extract message after " - "
                    parts = line.split(" - ", 1)

                    if len(parts) == 2:
                        error_message = parts[1].strip()
                        error_count[error_message] += 1

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    print(f"\nTop {top_n} Error Messages")
    print("-" * 50)

    for message, count in error_count.most_common(top_n):
        print(f"{count:5} : {message}")


def main():
    parser = argparse.ArgumentParser(
        description="Analyze application logs and display top N errors"
    )

    parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="Path to application log file"
    )

    parser.add_argument(
        "-n",
        "--top",
        type=int,
        default=5,
        help="Number of top errors to display (default: 5)"
    )

    args = parser.parse_args()

    analyze_log(args.file, args.top)


if __name__ == "__main__":
    main()


#python d27.cli-argParse.py -f d26.log.log -n 3