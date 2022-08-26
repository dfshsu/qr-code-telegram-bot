import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder

def main(file):
    url = "https://www.qrrd.ru/?action=ajaxfunc&sa=load_qrimg"

    encoder = MultipartEncoder(
        fields={
            "delete_url": "https://www.qrrd.ru/?action=ajaxfunc",
            "custom_url": "/qrread/",
            "custom_dir": "/qrread/",
            "files": ("hueta.png", open(file, "rb"), "multipart/form-data")
        }
    )

    response = requests.post(

        url=url,
        data=encoder,
        headers={"Content-Type": encoder.content_type},
        
    )

    text = json.loads(response.text)
    files = text['files']
    for i in files:
        j = i
    
    try:
        qrcode_viever = j['description2'] + ' ' + j['description']
        
    
        return qrcode_viever
    except KeyError:
        print_except = 'Не удалось распознать'
        return print_except