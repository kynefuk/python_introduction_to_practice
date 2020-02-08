# from b64 import decoder, encoderのパッケージが
# インポートされる際に実行される
# from .decoder import base64_to_str
# from .encoder import str_to_base64

# __all__に指定したモジュールは *importで使用できるようになる
# __all__ = ["base64_to_str", "str_to_base64"]

# 同階層のモジュールは__init__内でimportしなくても
# __all__に設定することができる
# __all__ = ["encoder", "decoder"]

print(f"init:{__name__=}")
