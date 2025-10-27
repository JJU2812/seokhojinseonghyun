class Dog:
    count = 0
    def __init__(self, name):
        self.name = name
        Dog.count += 1
    def bark(self):
        print(f"{self.name}이/가 멍멍!하고 짖습니다,,")
    @classmethod
    def show_count(cls):
        print(f"현재 강아지의 수: {cls.count}")
    @staticmethod
    def sound():
        print("개는 멍멍 소리를 냅니다.")

dog1 = Dog("민규")
dog2 = Dog("삼다수")
dog1.bark()
Dog.sound()
Dog.show_count()