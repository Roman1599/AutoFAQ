FROM python:3.11-slim

# Устанавливаем необходимые зависимости
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    ca-certificates \
    libx11-dev \
    libgconf-2-4 \
    libnss3 \
    libgdk-pixbuf2.0-0 \
    libgtk-3-0 \
    libasound2 \
    libdbus-1-3 \
    libxtst6 \
    libxss1 \
    libappindicator3-1 \
    libu2f-udev \
    libfontconfig1 \
    gnupg2 \
    lsb-release \
    && rm -rf /var/lib/apt/lists/*

# Добавляем репозиторий Google Chrome и устанавливаем ключ
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | tee /etc/apt/trusted.gpg.d/google.asc
RUN DISTRO=$(lsb_release -c | awk '{print $2}') && \
    echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/google.asc] https://dl.google.com/linux/chrome/deb/ $DISTRO main" | tee /etc/apt/sources.list.d/google-chrome.list

# Обновляем репозитории и устанавливаем Google Chrome


# Устанавливаем pip и библиотеки для Selenium и pytest
RUN pip install --upgrade pip
RUN pip install selenium pytest webdriver-manager allure-pytest

# Копируем проект в контейнер
COPY . /app
WORKDIR /app

# Запускаем тесты
CMD ["pytest", "tests/test_chat_front.py", "--alluredir=allure-results"]
