import pytest
import requests
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


class TestAPI:
    @pytest.mark.api
    def test_get_request(self):
        # URL из curl-запроса
        url = "https://chat.autofaq.ai/api/webhooks/widget/6c24eb52-b1ab-4d78-8463-8556d4ee04b3/messages"

        # Заголовки из curl-запроса
        headers = {
            "Accept": "*/*",
            "Accept-Language": "ru,en;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Cookie": "__ddg1_=TM0kzuEE02uPPUPcFhZQ; _ym_uid=1734543761393705529; _ym_d=1734543761; _ym_isad=2; session-id=b4c8ac8b-2da7-47c3-bdc0-9d4a407916dd; _gid=GA1.2.1265551793.1734543762; __ddg9_=89.169.48.228; _gat=1; _ym_visorc=w; __ddg8_=Mhqn5CUQoRjRxxNQ; __ddg10_=1734549294; _ga_YVP1GWJ4L1=GS1.1.1734549283.2.1.1734549294.49.0.0; _ga=GA1.2.170561209.1734543762",
            "Origin": "https://autofaq.ai",
            "Referer": "https://autofaq.ai/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 YaBrowser/24.10.0.0 Safari/537.36",
            "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "YaBrowser";v="24.10", "Yowser";v="2.5"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
            "session-id": "b4c8ac8b-2da7-47c3-bdc0-9d4a407916dd"
        }

        # Параметры из curl-запроса
        params = {
            "ts": "1734549303057"
        }

        # Выполнение GET-запроса
        response = requests.get(url, headers=headers, params=params)

        # Логирование текста ответа
        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Text: {response.text}")

        # Проверка статуса ответа
        assert response.status_code == 200, (
            f"Expected 200, got {response.status_code}. Response: {response.text}"
        )


    @pytest.mark.api
    def test_post_message(self):
        # URL для POST-запроса
        url = "https://chat.autofaq.ai/api/webhooks/widget/6c24eb52-b1ab-4d78-8463-8556d4ee04b3/messages"

        # Заголовки для запроса
        headers = {
            "Accept": "application/json",
            "Accept-Language": "ru,en;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary9mkpuysHqlLMdajB",
            "Origin": "https://autofaq.ai",
            "Referer": "https://autofaq.ai/",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 YaBrowser/24.10.0.0 Safari/537.36",
            "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "YaBrowser";v="24.10", "Yowser";v="2.5"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "macOS",
            "session-id": "cb0441f7-4d70-4cdf-8826-8559b0b909e3",
        }

        # Полезная нагрузка
        payload = (
            "------WebKitFormBoundary9mkpuysHqlLMdajB\r\n"
            "Content-Disposition: form-data; name=\"payload\"\r\n\r\n"
            '{"id":"b51b1615-f040-43a9-9d3a-5e4745aba436","ts":1734550668706,"text":"555"}\r\n'
            "------WebKitFormBoundary9mkpuysHqlLMdajB--\r\n"
        )

        # Выполнение POST-запроса
        response = requests.post(url, headers=headers, data=payload)



        # Проверка статуса ответа
        assert response.status_code == 200, (
            f"Expected 200, got {response.status_code}. Response: {response.text}"
        )

        # Проверка содержимого ответа
        response_json = response.json()
        assert "text" in response_json, "Поле 'text' отсутствует в ответе сервера"
        assert response_json["text"] == "555", (
            f"Expected text to be '555', got {response_json['text']}"
        )
