import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'src="http(?:s)?://(?:www.)?youtube\.com/embed/(\w+)"'
    match = re.search(pattern,s)

    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    
    return None

if __name__ == "__main__":
    main()