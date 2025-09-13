

import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BPM Project")
    parser.add_argument("command", choices=["train", "predict"])
    args = parser.parse_args()

    if args.command == "train":
        print("train")
    elif args.command == "predict":
        print("predict")