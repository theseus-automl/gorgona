import pytest

from gorgona.stages.cleaners import NumberCleaner


@pytest.fixture()
def setup_number_cleaner():
    nc = NumberCleaner(
        '',
        '',
    )

    return nc


def test_positive_integer_single_digit_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("7") == ""


def test_positive_integer_single_digit_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("3") == ""


def test_positive_integer_single_digit_quote_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("9'5") == ""


def test_positive_integer_single_digit_quote_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("0'257175") == ""


def test_positive_integer_single_digit_apostrophe_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("9`9") == ""


def test_positive_integer_single_digit_apostrophe_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("0`985776") == ""


def test_positive_integer_single_digit_space_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("5 6") == ""


def test_positive_integer_single_digit_space_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("3 839118") == ""


def test_positive_integer_single_digit_eng_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("4k6") == ""


def test_positive_integer_single_digit_eng_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("3k504421") == ""


def test_positive_integer_single_digit_rus_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("4к4") == ""


def test_positive_integer_single_digit_rus_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("5к117864") == ""


def test_positive_integer_multiple_digits_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("774464") == ""


def test_positive_integer_multiple_digits_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("35655") == ""


def test_positive_integer_multiple_digits_quote_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("249910'9") == ""


def test_positive_integer_multiple_digits_quote_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("480142'838693") == ""


def test_positive_integer_multiple_digits_apostrophe_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("154095`1") == ""


def test_positive_integer_multiple_digits_apostrophe_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("85818`184705") == ""


def test_positive_integer_multiple_digits_space_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("306485 3") == ""


def test_positive_integer_multiple_digits_space_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("22721 546337") == ""


def test_positive_integer_multiple_digits_eng_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("464830k0") == ""


def test_positive_integer_multiple_digits_eng_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("955186k918058") == ""


def test_positive_integer_multiple_digits_rus_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("570511к2") == ""


def test_positive_integer_multiple_digits_rus_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("564964к869484") == ""


def test_negative_integer_single_digit_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-4") == ""


def test_negative_integer_single_digit_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-5") == ""


def test_negative_integer_single_digit_quote_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-0'0") == ""


def test_negative_integer_single_digit_quote_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-8'803962") == ""


def test_negative_integer_single_digit_apostrophe_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-0`5") == ""


def test_negative_integer_single_digit_apostrophe_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-7`895475") == ""


def test_negative_integer_single_digit_space_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-9 8") == ""


def test_negative_integer_single_digit_space_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-8 551966") == ""


def test_negative_integer_single_digit_eng_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-2k5") == ""


def test_negative_integer_single_digit_eng_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-3k484318") == ""


def test_negative_integer_single_digit_rus_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-2к5") == ""


def test_negative_integer_single_digit_rus_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-3к283697") == ""


def test_negative_integer_multiple_digits_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-138166") == ""


def test_negative_integer_multiple_digits_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-94352") == ""


def test_negative_integer_multiple_digits_quote_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-473778'5") == ""


def test_negative_integer_multiple_digits_quote_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-787864'453129") == ""


def test_negative_integer_multiple_digits_apostrophe_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-911004`4") == ""


def test_negative_integer_multiple_digits_apostrophe_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-392620`715189") == ""


def test_negative_integer_multiple_digits_space_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-908466 6") == ""


def test_negative_integer_multiple_digits_space_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-279418 645330") == ""


def test_negative_integer_multiple_digits_eng_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-591608k5") == ""


def test_negative_integer_multiple_digits_eng_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-997435k133244") == ""


def test_negative_integer_multiple_digits_rus_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-172174к1") == ""


def test_negative_integer_multiple_digits_rus_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-733910к513370") == ""


def test_left_text_positive_integer_single_digit_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 4") == "hello "


def test_left_text_positive_integer_single_digit_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 7") == "hello "


def test_left_text_positive_integer_single_digit_quote_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 3'5") == "hello "


def test_left_text_positive_integer_single_digit_quote_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 1'414237") == "hello "


def test_left_text_positive_integer_single_digit_apostrophe_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 2`5") == "hello "


def test_left_text_positive_integer_single_digit_apostrophe_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 6`792669") == "hello "


def test_left_text_positive_integer_single_digit_space_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 8 6") == "hello "


def test_left_text_positive_integer_single_digit_space_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 4 732535") == "hello "


def test_left_text_positive_integer_single_digit_eng_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 7k2") == "hello "


def test_left_text_positive_integer_single_digit_eng_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 9k798422") == "hello "


def test_left_text_positive_integer_single_digit_rus_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 0к2") == "hello "


def test_left_text_positive_integer_single_digit_rus_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 6к449708") == "hello "


def test_left_text_positive_integer_multiple_digits_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 84908") == "hello "


def test_left_text_positive_integer_multiple_digits_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 434178") == "hello "


def test_left_text_positive_integer_multiple_digits_quote_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 580178'5") == "hello "


def test_left_text_positive_integer_multiple_digits_quote_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 403087'446030") == "hello "


def test_left_text_positive_integer_multiple_digits_apostrophe_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 99510`9") == "hello "


def test_left_text_positive_integer_multiple_digits_apostrophe_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 880343`699877") == "hello "


def test_left_text_positive_integer_multiple_digits_space_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 525007 2") == "hello "


def test_left_text_positive_integer_multiple_digits_space_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 872947 296824") == "hello "


def test_left_text_positive_integer_multiple_digits_eng_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 450966k4") == "hello "


def test_left_text_positive_integer_multiple_digits_eng_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 993633k963503") == "hello "


def test_left_text_positive_integer_multiple_digits_rus_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 902081к2") == "hello "


def test_left_text_positive_integer_multiple_digits_rus_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 398410к5738") == "hello "


def test_left_text_negative_integer_single_digit_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -6") == "hello "


def test_left_text_negative_integer_single_digit_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -6") == "hello "


def test_left_text_negative_integer_single_digit_quote_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -6'2") == "hello "


def test_left_text_negative_integer_single_digit_quote_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -3'759377") == "hello "


def test_left_text_negative_integer_single_digit_apostrophe_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -7`1") == "hello "


def test_left_text_negative_integer_single_digit_apostrophe_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -1`502604") == "hello "


def test_left_text_negative_integer_single_digit_space_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -2 3") == "hello "


def test_left_text_negative_integer_single_digit_space_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -1 393569") == "hello "


def test_left_text_negative_integer_single_digit_eng_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -6k3") == "hello "


def test_left_text_negative_integer_single_digit_eng_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -1k432422") == "hello "


def test_left_text_negative_integer_single_digit_rus_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -5к5") == "hello "


def test_left_text_negative_integer_single_digit_rus_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -1к68404") == "hello "


def test_left_text_negative_integer_multiple_digits_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -518862") == "hello "


def test_left_text_negative_integer_multiple_digits_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -311825") == "hello "


def test_left_text_negative_integer_multiple_digits_quote_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -13646'6") == "hello "


def test_left_text_negative_integer_multiple_digits_quote_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -155588'658068") == "hello "


def test_left_text_negative_integer_multiple_digits_apostrophe_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -902010`6") == "hello "


def test_left_text_negative_integer_multiple_digits_apostrophe_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -339050`817304") == "hello "


def test_left_text_negative_integer_multiple_digits_space_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -923620 6") == "hello "


def test_left_text_negative_integer_multiple_digits_space_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -277075 908827") == "hello "


def test_left_text_negative_integer_multiple_digits_eng_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -770630k5") == "hello "


def test_left_text_negative_integer_multiple_digits_eng_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -543724k219469") == "hello "


def test_left_text_negative_integer_multiple_digits_rus_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -118460к2") == "hello "


def test_left_text_negative_integer_multiple_digits_rus_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -159072к256757") == "hello "


def test_right_text_positive_integer_single_digit_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("2 hello") == " hello"


def test_right_text_positive_integer_single_digit_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("1 hello") == " hello"


def test_right_text_positive_integer_single_digit_quote_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("6'4 hello") == " hello"


def test_right_text_positive_integer_single_digit_quote_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("3'58431 hello") == " hello"


def test_right_text_positive_integer_single_digit_apostrophe_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("0`5 hello") == " hello"


def test_right_text_positive_integer_single_digit_apostrophe_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("5`155738 hello") == " hello"


def test_right_text_positive_integer_single_digit_space_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("5 3 hello") == " hello"


def test_right_text_positive_integer_single_digit_space_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("2 912797 hello") == " hello"


def test_right_text_positive_integer_single_digit_eng_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("5k3 hello") == " hello"


def test_right_text_positive_integer_single_digit_eng_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("9k911768 hello") == " hello"


def test_right_text_positive_integer_single_digit_rus_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("3к3 hello") == " hello"


def test_right_text_positive_integer_single_digit_rus_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("3к750248 hello") == " hello"


def test_right_text_positive_integer_multiple_digits_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("42678 hello") == " hello"


def test_right_text_positive_integer_multiple_digits_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("215188 hello") == " hello"


def test_right_text_positive_integer_multiple_digits_quote_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("455258'3 hello") == " hello"


def test_right_text_positive_integer_multiple_digits_quote_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("806580'611928 hello") == " hello"


def test_right_text_positive_integer_multiple_digits_apostrophe_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("479352`5 hello") == " hello"


def test_right_text_positive_integer_multiple_digits_apostrophe_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("519252`685635 hello") == " hello"


def test_right_text_positive_integer_multiple_digits_space_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("928184 7 hello") == " hello"


def test_right_text_positive_integer_multiple_digits_space_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("489262 493403 hello") == " hello"


def test_right_text_positive_integer_multiple_digits_eng_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("34773k1 hello") == " hello"


def test_right_text_positive_integer_multiple_digits_eng_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("675960k827611 hello") == " hello"


def test_right_text_positive_integer_multiple_digits_rus_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("876524к5 hello") == " hello"


def test_right_text_positive_integer_multiple_digits_rus_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("55243к431074 hello") == " hello"


def test_right_text_negative_integer_single_digit_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-7 hello") == " hello"


def test_right_text_negative_integer_single_digit_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-1 hello") == " hello"


def test_right_text_negative_integer_single_digit_quote_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-5'2 hello") == " hello"


def test_right_text_negative_integer_single_digit_quote_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-9'814320 hello") == " hello"


def test_right_text_negative_integer_single_digit_apostrophe_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-0`8 hello") == " hello"


def test_right_text_negative_integer_single_digit_apostrophe_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-3`877194 hello") == " hello"


def test_right_text_negative_integer_single_digit_space_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-8 6 hello") == " hello"


def test_right_text_negative_integer_single_digit_space_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-3 873345 hello") == " hello"


def test_right_text_negative_integer_single_digit_eng_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-8k9 hello") == " hello"


def test_right_text_negative_integer_single_digit_eng_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-5k346049 hello") == " hello"


def test_right_text_negative_integer_single_digit_rus_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-4к6 hello") == " hello"


def test_right_text_negative_integer_single_digit_rus_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-9к703473 hello") == " hello"


def test_right_text_negative_integer_multiple_digits_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-190239 hello") == " hello"


def test_right_text_negative_integer_multiple_digits_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-839965 hello") == " hello"


def test_right_text_negative_integer_multiple_digits_quote_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-517738'9 hello") == " hello"


def test_right_text_negative_integer_multiple_digits_quote_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-764801'614671 hello") == " hello"


def test_right_text_negative_integer_multiple_digits_apostrophe_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-634963`9 hello") == " hello"


def test_right_text_negative_integer_multiple_digits_apostrophe_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-372948`939025 hello") == " hello"


def test_right_text_negative_integer_multiple_digits_space_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-760889 7 hello") == " hello"


def test_right_text_negative_integer_multiple_digits_space_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-7831 504330 hello") == " hello"


def test_right_text_negative_integer_multiple_digits_eng_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-837557k3 hello") == " hello"


def test_right_text_negative_integer_multiple_digits_eng_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-195729k572621 hello") == " hello"


def test_right_text_negative_integer_multiple_digits_rus_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("-355848к0 hello") == " hello"


def test_right_text_negative_integer_multiple_digits_rus_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("-665426к392704 hello") == " hello"


def test_both_text_positive_integer_single_digit_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 4 world") == "hello  world"


def test_both_text_positive_integer_single_digit_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 8 world") == "hello  world"


def test_both_text_positive_integer_single_digit_quote_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 6'2 world") == "hello  world"


def test_both_text_positive_integer_single_digit_quote_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 3'622671 world") == "hello  world"


def test_both_text_positive_integer_single_digit_apostrophe_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 6`0 world") == "hello  world"


def test_both_text_positive_integer_single_digit_apostrophe_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 8`757195 world") == "hello  world"


def test_both_text_positive_integer_single_digit_space_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 0 1 world") == "hello  world"


def test_both_text_positive_integer_single_digit_space_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 7 862462 world") == "hello  world"


def test_both_text_positive_integer_single_digit_eng_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 8k5 world") == "hello  world"


def test_both_text_positive_integer_single_digit_eng_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 3k314471 world") == "hello  world"


def test_both_text_positive_integer_single_digit_rus_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 2к5 world") == "hello  world"


def test_both_text_positive_integer_single_digit_rus_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 9к486783 world") == "hello  world"


def test_both_text_positive_integer_multiple_digits_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 805686 world") == "hello  world"


def test_both_text_positive_integer_multiple_digits_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 369355 world") == "hello  world"


def test_both_text_positive_integer_multiple_digits_quote_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 163343'0 world") == "hello  world"


def test_both_text_positive_integer_multiple_digits_quote_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 461408'736785 world") == "hello  world"


def test_both_text_positive_integer_multiple_digits_apostrophe_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 864015`2 world") == "hello  world"


def test_both_text_positive_integer_multiple_digits_apostrophe_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 647078`653487 world") == "hello  world"


def test_both_text_positive_integer_multiple_digits_space_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 222917 9 world") == "hello  world"


def test_both_text_positive_integer_multiple_digits_space_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 564211 641276 world") == "hello  world"


def test_both_text_positive_integer_multiple_digits_eng_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 440821k8 world") == "hello  world"


def test_both_text_positive_integer_multiple_digits_eng_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 845780k860446 world") == "hello  world"


def test_both_text_positive_integer_multiple_digits_rus_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello 81289к1 world") == "hello  world"


def test_both_text_positive_integer_multiple_digits_rus_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello 146234к484167 world") == "hello  world"


def test_both_text_negative_integer_single_digit_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -4 world") == "hello  world"


def test_both_text_negative_integer_single_digit_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -0 world") == "hello  world"


def test_both_text_negative_integer_single_digit_quote_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -4'9 world") == "hello  world"


def test_both_text_negative_integer_single_digit_quote_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -5'387080 world") == "hello  world"


def test_both_text_negative_integer_single_digit_apostrophe_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -3`8 world") == "hello  world"


def test_both_text_negative_integer_single_digit_apostrophe_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -0`385330 world") == "hello  world"


def test_both_text_negative_integer_single_digit_space_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -7 7 world") == "hello  world"


def test_both_text_negative_integer_single_digit_space_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -1 245555 world") == "hello  world"


def test_both_text_negative_integer_single_digit_eng_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -4k4 world") == "hello  world"


def test_both_text_negative_integer_single_digit_eng_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -7k737481 world") == "hello  world"


def test_both_text_negative_integer_single_digit_rus_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -3к8 world") == "hello  world"


def test_both_text_negative_integer_single_digit_rus_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -4к979649 world") == "hello  world"


def test_both_text_negative_integer_multiple_digits_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -579549 world") == "hello  world"


def test_both_text_negative_integer_multiple_digits_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -521868 world") == "hello  world"


def test_both_text_negative_integer_multiple_digits_quote_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -494030'8 world") == "hello  world"


def test_both_text_negative_integer_multiple_digits_quote_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -997018'388418 world") == "hello  world"


def test_both_text_negative_integer_multiple_digits_apostrophe_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -48935`6 world") == "hello  world"


def test_both_text_negative_integer_multiple_digits_apostrophe_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -115491`848265 world") == "hello  world"


def test_both_text_negative_integer_multiple_digits_space_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -373023 5 world") == "hello  world"


def test_both_text_negative_integer_multiple_digits_space_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -526547 383697 world") == "hello  world"


def test_both_text_negative_integer_multiple_digits_eng_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -304461k5 world") == "hello  world"


def test_both_text_negative_integer_multiple_digits_eng_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -308120k521264 world") == "hello  world"


def test_both_text_negative_integer_multiple_digits_rus_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("hello -230268к9 world") == "hello  world"


def test_both_text_negative_integer_multiple_digits_rus_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("hello -695525к628100 world") == "hello  world"


def test_inside_text_positive_integer_single_digit_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he4llo") == "he4llo"


def test_inside_text_positive_integer_single_digit_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he8llo") == "he8llo"


def test_inside_text_positive_integer_single_digit_quote_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he0'8llo") == "he0'8llo"


def test_inside_text_positive_integer_single_digit_quote_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he8'503290llo") == "he8'503290llo"


def test_inside_text_positive_integer_single_digit_apostrophe_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he3`3llo") == "he3`3llo"


def test_inside_text_positive_integer_single_digit_apostrophe_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he0`179192llo") == "he0`179192llo"


def test_inside_text_positive_integer_single_digit_space_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he2 4llo") == "he2 4llo"


def test_inside_text_positive_integer_single_digit_space_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he3 135087llo") == "he3 135087llo"


def test_inside_text_positive_integer_single_digit_eng_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he8k4llo") == "he8k4llo"


def test_inside_text_positive_integer_single_digit_eng_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he0k657610llo") == "he0k657610llo"


def test_inside_text_positive_integer_single_digit_rus_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he9к2llo") == "he9к2llo"


def test_inside_text_positive_integer_single_digit_rus_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he6к839529llo") == "he6к839529llo"


def test_inside_text_positive_integer_multiple_digits_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he513934llo") == "he513934llo"


def test_inside_text_positive_integer_multiple_digits_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he424141llo") == "he424141llo"


def test_inside_text_positive_integer_multiple_digits_quote_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he757949'6llo") == "he757949'6llo"


def test_inside_text_positive_integer_multiple_digits_quote_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he650035'989071llo") == "he650035'989071llo"


def test_inside_text_positive_integer_multiple_digits_apostrophe_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he849767`6llo") == "he849767`6llo"


def test_inside_text_positive_integer_multiple_digits_apostrophe_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he234327`915339llo") == "he234327`915339llo"


def test_inside_text_positive_integer_multiple_digits_space_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he703293 5llo") == "he703293 5llo"


def test_inside_text_positive_integer_multiple_digits_space_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he409856 70023llo") == "he409856 70023llo"


def test_inside_text_positive_integer_multiple_digits_eng_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he744620k6llo") == "he744620k6llo"


def test_inside_text_positive_integer_multiple_digits_eng_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he743290k231362llo") == "he743290k231362llo"


def test_inside_text_positive_integer_multiple_digits_rus_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he791511к3llo") == "he791511к3llo"


def test_inside_text_positive_integer_multiple_digits_rus_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he401092к788202llo") == "he401092к788202llo"


def test_inside_text_negative_integer_single_digit_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he-4llo") == "he-4llo"


def test_inside_text_negative_integer_single_digit_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he-8llo") == "he-8llo"


def test_inside_text_negative_integer_single_digit_quote_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he-3'3llo") == "he-3'3llo"


def test_inside_text_negative_integer_single_digit_quote_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he-4'290601llo") == "he-4'290601llo"


def test_inside_text_negative_integer_single_digit_apostrophe_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he-7`0llo") == "he-7`0llo"


def test_inside_text_negative_integer_single_digit_apostrophe_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he-6`707325llo") == "he-6`707325llo"


def test_inside_text_negative_integer_single_digit_space_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he-9 3llo") == "he-9 3llo"


def test_inside_text_negative_integer_single_digit_space_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he-0 183754llo") == "he-0 183754llo"


def test_inside_text_negative_integer_single_digit_eng_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he-1k4llo") == "he-1k4llo"


def test_inside_text_negative_integer_single_digit_eng_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he-3k878581llo") == "he-3k878581llo"


def test_inside_text_negative_integer_single_digit_rus_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he-0к0llo") == "he-0к0llo"


def test_inside_text_negative_integer_single_digit_rus_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he-6к377555llo") == "he-6к377555llo"


def test_inside_text_negative_integer_multiple_digits_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he-598986llo") == "he-598986llo"


def test_inside_text_negative_integer_multiple_digits_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he-393398llo") == "he-393398llo"


def test_inside_text_negative_integer_multiple_digits_quote_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he-890636'7llo") == "he-890636'7llo"


def test_inside_text_negative_integer_multiple_digits_quote_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he-834451'288314llo") == "he-834451'288314llo"


def test_inside_text_negative_integer_multiple_digits_apostrophe_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he-347856`8llo") == "he-347856`8llo"


def test_inside_text_negative_integer_multiple_digits_apostrophe_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he-504475`759252llo") == "he-504475`759252llo"


def test_inside_text_negative_integer_multiple_digits_space_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he-349749 9llo") == "he-349749 9llo"


def test_inside_text_negative_integer_multiple_digits_space_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he-184038 68144llo") == "he-184038 68144llo"


def test_inside_text_negative_integer_multiple_digits_eng_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he-289290k6llo") == "he-289290k6llo"


def test_inside_text_negative_integer_multiple_digits_eng_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he-964399k733553llo") == "he-964399k733553llo"


def test_inside_text_negative_integer_multiple_digits_rus_k_single_digit(setup_number_cleaner):
    assert setup_number_cleaner("he-63989к5llo") == "he-63989к5llo"


def test_inside_text_negative_integer_multiple_digits_rus_k_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner("he-403175к774771llo") == "he-403175к774771llo"


def test_positive_float_single_digit_dot_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("2.9") == ""


def test_positive_float_single_digit_dot_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("8.569333") == ""


def test_positive_float_single_digit_comma_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("5,0") == ""


def test_positive_float_single_digit_comma_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("1,780518") == ""


def test_positive_float_multiple_digits_dot_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("785313.5") == ""


def test_positive_float_multiple_digits_dot_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("537221.74655") == ""


def test_positive_float_multiple_digits_comma_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("391240,8") == ""


def test_positive_float_multiple_digits_comma_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("181004,460352") == ""


def test_negative_float_single_digit_dot_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("-9.6") == ""


def test_negative_float_single_digit_dot_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("-8.258030") == ""


def test_negative_float_single_digit_comma_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("-7,1") == ""


def test_negative_float_single_digit_comma_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("-0,885164") == ""


def test_negative_float_multiple_digits_dot_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("-864605.4") == ""


def test_negative_float_multiple_digits_dot_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("-355839.416791") == ""


def test_negative_float_multiple_digits_comma_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("-578243,4") == ""


def test_negative_float_multiple_digits_comma_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("-98767,817853") == ""


def test_left_text_positive_float_single_digit_dot_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello 4.6") == "hello "


def test_left_text_positive_float_single_digit_dot_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello 1.74914") == "hello "


def test_left_text_positive_float_single_digit_comma_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello 3,5") == "hello "


def test_left_text_positive_float_single_digit_comma_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello 2,8995") == "hello "


def test_left_text_positive_float_multiple_digits_dot_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello 128684.7") == "hello "


def test_left_text_positive_float_multiple_digits_dot_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello 832606.932249") == "hello "


def test_left_text_positive_float_multiple_digits_comma_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello 377802,4") == "hello "


def test_left_text_positive_float_multiple_digits_comma_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello 762367,135153") == "hello "


def test_left_text_negative_float_single_digit_dot_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello -1.8") == "hello "


def test_left_text_negative_float_single_digit_dot_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello -5.792708") == "hello "


def test_left_text_negative_float_single_digit_comma_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello -2,5") == "hello "


def test_left_text_negative_float_single_digit_comma_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello -5,888953") == "hello "


def test_left_text_negative_float_multiple_digits_dot_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello -486940.5") == "hello "


def test_left_text_negative_float_multiple_digits_dot_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello -716193.653169") == "hello "


def test_left_text_negative_float_multiple_digits_comma_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello -892150,7") == "hello "


def test_left_text_negative_float_multiple_digits_comma_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello -825361,420340") == "hello "


def test_right_text_positive_float_single_digit_dot_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("9.7 hello") == " hello"


def test_right_text_positive_float_single_digit_dot_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("8.668371 hello") == " hello"


def test_right_text_positive_float_single_digit_comma_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("6,9 hello") == " hello"


def test_right_text_positive_float_single_digit_comma_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("9,934089 hello") == " hello"


def test_right_text_positive_float_multiple_digits_dot_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("243369.1 hello") == " hello"


def test_right_text_positive_float_multiple_digits_dot_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("424756.17786 hello") == " hello"


def test_right_text_positive_float_multiple_digits_comma_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("922173,3 hello") == " hello"


def test_right_text_positive_float_multiple_digits_comma_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("829857,999977 hello") == " hello"


def test_right_text_negative_float_single_digit_dot_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("-1.8 hello") == " hello"


def test_right_text_negative_float_single_digit_dot_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("-5.743926 hello") == " hello"


def test_right_text_negative_float_single_digit_comma_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("-1,9 hello") == " hello"


def test_right_text_negative_float_single_digit_comma_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("-3,740022 hello") == " hello"


def test_right_text_negative_float_multiple_digits_dot_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("-746442.5 hello") == " hello"


def test_right_text_negative_float_multiple_digits_dot_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("-796358.785568 hello") == " hello"


def test_right_text_negative_float_multiple_digits_comma_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("-162965,8 hello") == " hello"


def test_right_text_negative_float_multiple_digits_comma_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("-510271,12306 hello") == " hello"


def test_both_text_positive_float_single_digit_dot_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello 2.6 world") == "hello  world"


def test_both_text_positive_float_single_digit_dot_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello 6.756683 world") == "hello  world"


def test_both_text_positive_float_single_digit_comma_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello 6,3 world") == "hello  world"


def test_both_text_positive_float_single_digit_comma_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello 1,84108 world") == "hello  world"


def test_both_text_positive_float_multiple_digits_dot_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello 430035.4 world") == "hello  world"


def test_both_text_positive_float_multiple_digits_dot_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello 547739.554345 world") == "hello  world"


def test_both_text_positive_float_multiple_digits_comma_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello 26171,1 world") == "hello  world"


def test_both_text_positive_float_multiple_digits_comma_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello 666557,952575 world") == "hello  world"


def test_both_text_negative_float_single_digit_dot_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello -1.0 world") == "hello  world"


def test_both_text_negative_float_single_digit_dot_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello -1.445504 world") == "hello  world"


def test_both_text_negative_float_single_digit_comma_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello -7,7 world") == "hello  world"


def test_both_text_negative_float_single_digit_comma_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello -3,87658 world") == "hello  world"


def test_both_text_negative_float_multiple_digits_dot_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello -477476.4 world") == "hello  world"


def test_both_text_negative_float_multiple_digits_dot_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello -541300.867811 world") == "hello  world"


def test_both_text_negative_float_multiple_digits_comma_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello -708842,4 world") == "hello  world"


def test_both_text_negative_float_multiple_digits_comma_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("hello -741041,952275 world") == "hello  world"


def test_inside_text_positive_float_single_digit_dot_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("he4.9llo") == "he4.9llo"


def test_inside_text_positive_float_single_digit_dot_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("he4.605648llo") == "he4.605648llo"


def test_inside_text_positive_float_single_digit_comma_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("he7,6llo") == "he7,6llo"


def test_inside_text_positive_float_single_digit_comma_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("he1,640808llo") == "he1,640808llo"


def test_inside_text_positive_float_multiple_digits_dot_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("he311010.5llo") == "he311010.5llo"


def test_inside_text_positive_float_multiple_digits_dot_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("he593407.960145llo") == "he593407.960145llo"


def test_inside_text_positive_float_multiple_digits_comma_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("he318574,7llo") == "he318574,7llo"


def test_inside_text_positive_float_multiple_digits_comma_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("he113354,321762llo") == "he113354,321762llo"


def test_inside_text_negative_float_single_digit_dot_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("he-1.7llo") == "he-1.7llo"


def test_inside_text_negative_float_single_digit_dot_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("he-5.347666llo") == "he-5.347666llo"


def test_inside_text_negative_float_single_digit_comma_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("he-1,5llo") == "he-1,5llo"


def test_inside_text_negative_float_single_digit_comma_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("he-0,785082llo") == "he-0,785082llo"


def test_inside_text_negative_float_multiple_digits_dot_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("he-19847.2llo") == "he-19847.2llo"


def test_inside_text_negative_float_multiple_digits_dot_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("he-163691.435539llo") == "he-163691.435539llo"


def test_inside_text_negative_float_multiple_digits_comma_with_single_digit_fraction(setup_number_cleaner):
    assert setup_number_cleaner("he-416740,2llo") == "he-416740,2llo"


def test_inside_text_negative_float_multiple_digits_comma_with_multiple_digits_fraction(setup_number_cleaner):
    assert setup_number_cleaner("he-117470,870470llo") == "he-117470,870470llo"
