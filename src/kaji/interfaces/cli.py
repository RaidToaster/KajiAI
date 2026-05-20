"""CLI interface — command-line claim submission."""


import argparse
from kaji.flow import KajiFlow


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="KajiSF-DJ — claim analysis tool")
    parser.add_argument("claim", type=str, help="Claim to analyse")
    parser.add_argument("--domain", type=str, default="general", help="Domain profile")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    result = KajiFlow().kickoff(inputs={"claim": args.claim, "domain": args.domain})
    if hasattr(result, "raw"):
        print(result.raw)
    else:
        print(result)
