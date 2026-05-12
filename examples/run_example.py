import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import souffle


def main() -> None:
    output = souffle.run(
        "examples/family/ancestor.dl",
        "--output-dir",
        "-",
    )
    print(output)


if __name__ == "__main__":
    main()
