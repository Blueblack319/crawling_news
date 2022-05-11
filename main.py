from save_to_file import save_to_hwp
from crawling_koreantimes import get_koreantimes
from tools import get_category

category = {"Business": 743, "Editorial": 761}
category_keys = list(category.keys())
category_values = list(category.values())


def main():
    idx = get_category()
    start = int(input("몇 페이지부터 가져올까요?"))
    end = int(input("몇 페이지까지 가져올까요?"))
    content_koreantimes = get_koreantimes(start, end, category_values[idx])
    save_to_hwp(content_koreantimes, "koreatimes", start, end, category_keys[idx])
    return


if __name__ == "__main__":
    main()
