from typing import Generator
def fool(start, end):
    total = 0
    for item in range(start, end):
        total += item
    return total

assert fool(1,1)==0

def echo_round() -> Generator[int, float, str]:
    sent = yield 0
    while sent >= 0:
        sent = yield round(sent)
    return 'Done'
for index in range(3):
    print(echo_round())