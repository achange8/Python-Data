a = 10
b = 20
k = {
    "足し算": a + b,
    "減算": a - b,
    "乗算": a * b,
    "除算": a / b,
    "剰余": a % b
}
for key, value in k.items():
    print(f"a と b との{key}の結果= {value}")
