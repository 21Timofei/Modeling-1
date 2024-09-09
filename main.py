import math

def decart_to_polar(x, y, precision):
    r = math.sqrt(x ** 2 + y ** 2)
    theta = math.atan2(y, x)

    r = round(r, precision)
    theta = round(math.degrees(theta), precision)
    return r, theta

def polar_to_decart(r, theta_deg, precision):
    theta_rad = math.radians(theta_deg)

    x = r * math.cos(theta_rad)
    y = r * math.sin(theta_rad)

    x = round(x, precision)
    y = round(y, precision)
    return x, y

if __name__ == "__main__":
    print("Выберите операцию:")
    print("1. Перевод из декартовой системы координат в полярную \n2. Перевод из полярной системы координат в декартовую")
    choice = input("Введите 1 или 2: ")

    if choice == "1":
        x = float(input("Введите координату x: "))
        y = float(input("Введите координату y: "))
        precision = int(input("Введите точность (количество знаков после запятой): "))

        r, theta = decart_to_polar(x, y, precision)
        print(f"Полярные координаты: r = {r}, θ = {theta} градусов")
        print("Формулы для перевода \nr^2 = x^2 + y^2  \nθ = arctg(y/x)")

    elif choice == "2":
        r = float(input("Введите радиус r: "))
        theta_deg = float(input("Введите угол θ (в градусах): "))
        precision = int(input("Введите точность (количество знаков после запятой): "))

        x, y = polar_to_decart(r, theta_deg, precision)
        print(f"Декартовы координаты: x = {x}, y = {y}")
        print("Формулы для перевода \nx = r*cos(θ)  \ny = r*sin(θ)")

    else:
        print("Неверный выбор операции.")

