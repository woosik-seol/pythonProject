from dataclasses import dataclass
from typing import Optional, Union

@dataclass
class User:
    name: str
    age: int

def process_data(input_data: str) \
        -> Optional[Union[User, int, str]]:
    if input_data == "user":
        return User(name="Alice", age=30)
    elif input_data == "int":
        return 42
    elif input_data == "none":
        return None
    else:
        return "No valid data"

# 함수 사용 예시
result1 = process_data("user")
result2 = process_data("int")
result3 = process_data("other")
result4 = process_data("none")

print(result1)  # 출력: User(name='Alice', age=30)
print(result2)  # 출력: 42
print(result3)  # 출력: No valid data
print(result4)  # 출력: None