
from django.shortcuts import render



def orderBook(clientCode):
    import requests
    import json

    url = "https://iifluat.indiainfoline.com/OpenApi/Service1.svc/LoginRequestMobileForVendor"

    payload = "{\n    \"head\": {\n        \"appName\": \"IIFLMarPRATEEKS\",\n        \"appVer\": \"1.0\",\n        \"key\": \"w1oEjWXSLuHKE1mnsAetUdnpshkNRnnc\",\n        \"osName\": \"Android\",\n        \"requestCode\": \"IIFLMarRQLoginForVendor\",\n        \"userId\": \"8BoZHlyAxbd1iWvIAYzFyg==\",\n        \"password\": \"6zxc/N2uL6Nrh2Yz/+6Dxw==\"\n    },\n    \"body\": {\n        \"Email_id\": \"prateek.saraf@gmail.com\",\n        \"LocalIP\": \"192.168.88.41\",\n        \"PublicIP\": \"192.168.88.42\",\n        \"ContactNumber\":\"9739991769\"\n    }\n}"
    headers = {
        'content-type': "application/json",
        }

    orderbook_url = "https://iifluat.indiainfoline.com/openapi/service1.svc/V1/OrderBook"
    orderbook_payload = "{\n    \"head\": {\n        \"appName\": \"IIFLMarPRATEEKS\",\n        \"appVer\": \"1.0\",\n        \"key\": \"w1oEjWXSLuHKE1mnsAetUdnpshkNRnnc\",\n        \"osName\": \"Android\",\n        \"requestCode\": \"IIFLMarRQOrdBkV1\",\n        \"userId\": \"5BRPcwg3Dia\",\n        \"password\": \"UdrVa2u6tL8\"\n    },\n    \"body\": {\n\n\t\t\"ClientCode\": \"SURVINHA\"\n           }\n}"


    S = requests.Session()
    response = S.post(url, payload, headers=headers)
    # print(response.text)

    orderbook_response = S.post(orderbook_url,orderbook_payload,headers=headers)
    data = (json.loads(orderbook_response.text))
    # print(type(data))

    return data['body']['OrderBookV1data']




def home(request):
    resp_data = orderBook("SURVINHA")

    return render(request, 'home.html', {"data": resp_data}) 