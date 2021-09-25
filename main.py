from save_to_file import save_to_hwp
from crawling_koreantimes import get_koreantimes

def main():
    while True:
        num = int(input('몇 개의 news를 가져올까요?(10개 이하)'))
        if num > 10:
            print('다시 입력하세요.')
            continue
        content_koreantimes = get_koreantimes(num)
        save_to_hwp(content_koreantimes, 'koreatimes')
        break
    return
if __name__ == '__main__':
    main()