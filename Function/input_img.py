from PIL import Image
import cv2
import requests

from kakaotrans import Translator

LIMIT_PX = 1024
LIMIT_BYTE = 1024 * 1024  # 1MB
LIMIT_BOX = 40

KAKAO_LANGUAGE_DICT = {'English': 'en', 'Japanese': 'jp', 'chinese': 'cn', 'vietnamese': 'vi',
                       'Indonesia': 'id', 'arabic': 'ar', 'Bengal': 'bn', 'german': 'de',
                       'spanish': 'es', 'french': 'fr', 'Hindi': 'hi', 'italian': 'it',
                       'malaysian': 'ms', 'dutch': 'nl', 'portukal ': 'pt', 'russian': 'ru',
                       'thai': 'th', 'turkish': 'tr'}


def kakao_ocr_resize(image_path: str):
    """
    ocr detect/recognize api helper
    ocr api의 제약사항이 넘어서는 이미지는 요청 이전에 전처리가 필요.

    pixel 제약사항 초과: resize
    용량 제약사항 초과  : 다른 포맷으로 압축, 이미지 분할 등의 처리 필요. (예제에서 제공하지 않음)

    :param image_path: 이미지파일 경로
    :return:
    """
    print("2==================", image_path)
    image = cv2.imread(image_path)
    height, width, _ = image.shape
    print("3==================", height, width)
    if LIMIT_PX < height or LIMIT_PX < width:
        ratio = float(LIMIT_PX) / max(height, width)
        image = cv2.resize(image, None, fx=ratio, fy=ratio)
        height, width, _ = height, width, _ = image.shape

        # api 사용전에 이미지가 resize된 경우, recognize시 resize된 결과를 사용해야함.
        image_path = "{}_resized.jpg".format(image_path)
        print("4==================", image_path)
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
    print("image:",image_path)
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
    translator = Translator()
    result = translator.translate(text, src='kr', tgt=target, separate_lines=True)
    return result


def img_translated(url: str, lang: str):

    # 웹에서 실행 기준 프로젝트 경로에서 시작
    # 프로젝트 경로에 있는 media의 url(images\이미지 이름)
    image_path = "media\\" + url
    print("1==================", image_path)
    # 언어별 코드로 변환해주기 위해 DICT를 이용
    k_lang = KAKAO_LANGUAGE_DICT[lang]

    appkey = "d1e155018697e1aa5510637a8554d043"

    # 이미지 추출 문자를 담아줄 변수
    img_text = ""
    # 추출한 문자를 변역한 문자를 담아줄 변수
    img_text_result = ""

    pre_image_path = image_path
    resize_impath = kakao_ocr_resize(image_path)
    if resize_impath is not None:
        pre_image_path = resize_impath
        print("원본 대신 리사이즈된 이미지를 사용합니다.")

    output = kakao_ocr(pre_image_path, appkey).json()

    for i in range(len(output['result'])):
        text = output['result'][i]['recognition_words'][0]
        if text == "":
            continue
        result = kakao_translator(text, k_lang)
        img_text += text + ","
        img_text_result += result[0] + ","

    return img_text[:-1], img_text_result[:-1]