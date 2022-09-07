
# Django_qr

  

This project is made with DJango web framework.

A big thanks to contributors of these open source libraries which are used in this project.

  

- https://github.com/lincolnloop/python-qrcode

- https://github.com/WhyNotHugo/python-barcode

![front end screen shot](https://github.com/canklot/Django_qr/blob/master/front_end.jpg?raw=true)

## API usage
To use the api send your data in json format. You should recieve a pdf file as a response. Or an error message in html or plan text format. 

> URL: website/qr_app/api
> 
> Format: JSON
> 
> Method: POST


Field | Type | Description
------|------------|------------
text | List of strings| Data you want to create the qr_code of
barcode_type_selection| String "qr_code" or "barcode_code128" | The type of barcode of qr_code you want to create

Example json object

    {"text":["Hello", "world"],"barcode_type_selection":"qr_code"}
