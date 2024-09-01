import base64

a = "嘟嘟dudu7615"

b = base64.encodebytes(a.encode("utf-8"))
print(b.decode("utf-8"))
print(base64.decodebytes(b).decode("utf-8"))