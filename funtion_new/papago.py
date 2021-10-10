# 4. 번역 API(파파고)와 연결
# pip install -U pypapago
from pypapago import Translator

# 불러올 파일 명 입력
file_name = r'C:/Users/gold7/Desktop/text/eun.txt'

# 객체 할당, 번역할 파일 열기
translator = Translator()
with open(file_name, encoding ='utf-8', errors='ignore') as f :
        # 줄을 읽어 저장, byte를 string으로 디코딩
        line = f.readline()
        print(line)        # 파일 내 텍스트 출력
        print(type(line))  # 텍스트 타입 출력

# 여기서부터 문제 해결 해야함!!!!!
# # 번역할 문자를 입력
# forTranslateString = line
#
# # 번역하기  \n(엔터)이 나오면 오류 발생 문자열 처리 필요) kor -> eng
# result = translator.translate(forTranslateString, source='ko', target='en', verbose=False)
#
# # 결과 출력
# print(result)                          # 번역된 텍스트 출력
# with open('Translte.txt', 'w') as f : # 번역 완료된 텍스트 저장
#     f.write(result)