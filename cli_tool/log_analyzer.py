import argparse

def analyze_log(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    print(f"Total lines in log: {len(lines)}")

def main():
    parser = argparse.ArgumentParser(description="Simple Log Analyzer")
    parser.add_argument('logfile', help='Path to the log file')
    args = parser.parse_args()
    analyze_log(args.logfile)

if __name__ == '__main__':
    main()
