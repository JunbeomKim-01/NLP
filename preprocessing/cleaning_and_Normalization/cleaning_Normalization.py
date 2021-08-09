# 정제 및 정규화
# 길이가 1~2인 단어들을 정규 표현식을 이용하여 제거
import re
if __name__ == '__main__':
    text = "I was wondering if anyone out there could enlighten me on this car."
    shortword = re.compile(r'\W*\b\w{1,2}\b')
    print('')
    print(shortword.sub('', text))
    # 출력되는 값= was wondering anyone out there could enlighten this car.