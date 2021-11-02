from save_to_file import save_to_hwp
from crawling_koreantimes import get_koreantimes


def main():
    start = int(input("몇 페이지부터 가져올까요?"))
    end = int(input("몇 페이지까지 가져올까요?"))
    content_koreantimes = get_koreantimes(start, end)
    save_to_hwp(content_koreantimes, "koreatimes", start, end)
    return


if __name__ == "__main__":
    main()
