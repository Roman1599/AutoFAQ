
class Locators:

    BUTTON_CHAT = ("xpath", "//*[@id='chat21-launcher-button']")
    CHAT_HEADER = ("xpath", "//*[@class='chat21-sheet-header']")
    BUTTON_CLOSE_CHAT_UP = ("xpath", "//*[@class='chat21-sheet-header-button-icon-white']")
    BUTTON_CLOSE_CHAT_DOWN = ("xpath", "//*[@id='chat21-launcher-button']")
    TEXT_FIELD = ("xpath","//*[@class='f21textarea']")
    SEND_BUTTON = ("xpath", "(//*[@class='chat21-textarea-button active'])[3]")
    FIRST_MESSAGE = ("xpath", "(//*[@class='msg_content SanitizedHtml'])[1]")
    UPLOAD_BUTTON = ("xpath", "(//*[@class='chat21-textarea-button active'])[2]")
    FILE_INPUT = ("xpath", "(//*[@type='file'])[2]")
    EMOJI_BUTTON = ("xpath", "(//*[@class='chat21-textarea-button active'])[1]")
    EMODJI_FIRST = ("xpath", "(//*[@data-unified='1f600'])")
    EMODJI_SECOND = ("xpath", "(//*[@data-unified='1f603'])[1]")
    FORM_NAME = ("xpath", "//*[@name='senderFullName']")
    FORM_EMAIL = ("xpath", "//*[@name='senderEmail']")
    FORM_SEND_BUTTON = ("xpath", "//*[@class='form_panel_action form_panel_action-submit']")
    FORM_PANEL_LABEL = ("xpath", "(//*[@class='form_panel_field-label'])[1]")
    FORM_PANEL_LABEL_EMAIL = ("xpath", "(//*[@class='form_panel_field-label'])[2]")
