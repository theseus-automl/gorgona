from gorgona.stages.base.splitter import Splitter
from gorgona.stages.base.stripper import Stripper
from gorgona.stages.cleaners import *
from gorgona.stages.lang_detector import LanguageDetector
from gorgona.stages.normalizers import *

ALIASES = {
    'replace': Replacer,
    'strip': Stripper,
    'split': Splitter,
    'unicode': UnicodeNormalizer,
    'whitespace': WhitespaceNormalizer,
    'html': HtmlCleaner,
    'email': EmailCleaner,
    'phone': PhoneNumberCleaner,
    'url': UrlCleaner,
    'emoji': EmojiCleaner,
    'lang-detection': LanguageDetector,
    'lower': Lowercaser,
    'mention': MentionCleaner,
    'special': SpecialSymbolsCleaner,
    'number': NumberCleaner,
}
