import json

import cv2
import requests
import sys

from kakaotrans import Translator

LIMIT_PX = 1024
LIMIT_BYTE = 1024*1024  # 1MB
LIMIT_BOX = 40


def kakao_ocr_resize(image_path: str):
    """
    ocr detect/recognize api helper
    ocr api의 제약사항이 넘어서는 이미지는 요청 이전에 전처리가 필요.

    pixel 제약사항 초과: resize
    용량 제약사항 초과  : 다른 포맷으로 압축, 이미지 분할 등의 처리 필요. (예제에서 제공하지 않음)

    :param image_path: 이미지파일 경로
    :return:
    """
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    if LIMIT_PX < height or LIMIT_PX < width:
        ratio = float(LIMIT_PX) / max(height, width)
        image = cv2.resize(image, None, fx=ratio, fy=ratio)
        height, width, _ = height, width, _ = image.shape

        # api 사용전에 이미지가 resize된 경우, recognize시 resize된 결과를 사용해야함.
        image_path = "{}_resized.jpg".format(image_path)
        cv2.imwrite(image_path, image)

        return image_path
    return None


def kakao_ocr(image_path: str, appkey: str):
    """
    OCR api request example
    :param image_path: 이미지파일 경로
    :param appkey: 카카오 앱 REST API 키
    """
    API_URL = 'https://dapi.kakao.com/v2/vision/text/ocr'

    headers = {'Authorization': 'KakaoAK {}'.format(appkey)}

    image = cv2.imread(image_path)
    jpeg_image = cv2.imencode(".jpg", image)[1]
    data = jpeg_image.tobytes()


    return requests.post(API_URL, headers=headers, files={"image": data})

def pre_processing(image_path: str):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    new_path = image_path.replace('.jpg', '_gray.jpg')
    cv2.imwrite(new_path, gray2)

    return new_path

def kakao_translator(text: str, target: str):
    # src = 'kr'
    translator = Translator()
    result = translator.translate(text, src='kr', tgt=target, separate_lines=True)
    return result


def main():

    image_path = '../media/images/1.jpg'
    appkey = "d1e155018697e1aa5510637a8554d043"

    pre_image_path = pre_processing(image_path)
    resize_impath = kakao_ocr_resize(pre_image_path)
    if resize_impath is not None:
        pre_image_path = resize_impath
        print("원본 대신 리사이즈된 이미지를 사용합니다.")

    output = kakao_ocr(pre_image_path, appkey).json()
    # print(type(output))
    # print(len(output['result']))
    # print("[OCR] output:\n{}\n".format(json.dumps(output, sort_keys=True, indent=2, ensure_ascii=False)))
    for i in range(len(output['result'])):
        text = output['result'][i]['recognition_words'][0]
        if text == "":
            continue
        result = kakao_translator(text, 'en')
        print(text, end=" ")
        print(result[0])

    # print(r_text)
    # result = kakao_translator(r_text, 'en')
    # print(result)

    #print("[OCR] output:\n{}\n".format(json.dumps(output, sort_keys=True, indent=2, ensure_ascii=False)))


if __name__ == "__main__":
    main()