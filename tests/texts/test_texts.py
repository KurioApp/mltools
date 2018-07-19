from mltools.texts import clean_whitespaces, unescape_text
from mltools.texts import process_hashtags
from mltools.texts import normalize_username
from mltools.texts import normalize_number


def test_clean_whitespaces():
    text = "One  Two    three\tfour:\n five"
    expected = "One Two three four: five"
    assert clean_whitespaces(text) == expected


def test_unescape_texts():
    texts = [
        "Some logic: 2 &gt; 1 &amp; 99 &lt; 100",
        "Some text with &nbsp; non-breaking space.",
        "Then someone say, &quot;All is well&quot;",
        "There&apos;s always those who like &copy; symbol",
        "One of the currency looks like this: &yen;, &pound;, and &euro;"
    ]
    expected_results = [
        "Some logic: 2 > 1 & 99 < 100",
        "Some text with   non-breaking space.",
        "Then someone say, \"All is well\"",
        "There's always those who like (c) symbol",
        "One of the currency looks like this: Y=, PS, and EUR"
    ]
    for text, expected in zip(texts, expected_results):
        res = unescape_text(text)
        assert res == expected



def test_process_hashtags():
    text = "Some sentence might contain #hashtag like #ThisIsCool!"
    expected = "Some sentence might contain hashtag like This Is Cool!"
    assert process_hashtags(text) == expected


def test_normalize_username():
    text = "Some sentence might contain @username like @us3r and @user.official."
    expected = "Some sentence might contain NORM_USERNAME like NORM_USERNAME and NORM_USERNAME."
    assert normalize_username(text) == expected

    text = "But some might be malformed like this@user.@wow"
    expected = "But some might be malformed like this@user.@wow"
    assert normalize_username(text) == expected


def test_normalize_numbers():
    text = "Contains Rp 1.000,00 and $123.00."
    expected = "Contains Rp NORM_NUMBER and $NORM_NUMBER."
    assert normalize_number(text) == expected

    text = "With -1000 * 1/3 equals -333.3333 floating point is difficult"
    expected = "With NORM_NUMBER * NORM_NUMBER/NORM_NUMBER equals NORM_NUMBER floating point is difficult"
    assert normalize_number(text) == expected

    text = "Something happens yesterday (2/1/2006)"
    expected = "Something happens yesterday (NORM_NUMBER/NORM_NUMBER/NORM_NUMBER)"
    assert normalize_number(text) == expected
