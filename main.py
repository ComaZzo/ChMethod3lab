from equations import *


def checker(x1, x2, y1, y2):
    print('-' * 20 + 'Using simple derivatives' + '-' * 20)
    x_middle = (x1 + x2) / 2
    y_middle = (y1 + y2) / 2

    d = func_second_dy(x_middle, y_middle) * func_first_dx(x_middle, y_middle) - \
        func_first_dy(x_middle, y_middle) * func_second_dx(x_middle, y_middle)
    next_x = x_middle - \
             (func_second_dy(x_middle, y_middle) * func_first(x_middle, y_middle) -
              func_first_dy(x_middle, y_middle) * func_second(x_middle, y_middle)) / d
    next_y = y_middle - \
             (func_first_dx(x_middle, y_middle) * func_second(x_middle, y_middle) -
              func_second_dx(x_middle, y_middle) * func_first(x_middle, y_middle)) / d

    for i in range(1, 100):
        x_middle = next_x
        y_middle = next_y

        d = func_second_dy(x_middle, y_middle) * func_first_dx(x_middle, y_middle) - \
            func_first_dy(x_middle, y_middle) * func_second_dx(x_middle, y_middle)
        next_x = x_middle - \
                 (func_second_dy(x_middle, y_middle) * func_first(x_middle, y_middle) -
                  func_first_dy(x_middle, y_middle) * func_second(x_middle, y_middle)) / d
        next_y = y_middle - \
                 (func_first_dx(x_middle, y_middle) * func_second(x_middle, y_middle) -
                  func_second_dx(x_middle, y_middle) * func_first(x_middle, y_middle)) / d

        if abs(next_x - x_middle) <= epsilon and abs(next_y - y_middle) <= epsilon:
            print('x: {:.6f} y: {:.6f}'.format(next_x, next_y))
            print(f'Iterations: {i}')
            print('Different in x: {:+.10f}'.format(round(next_x - x_middle, 10)))
            print('Different in y: {:+.10f}'.format(round(next_y - y_middle, 10)))
            break
    print('-' * 70)


def checker_ch(x1, x2, y1, y2):
    print('-' * 20 + 'Using numerical derivatives' + '-' * 20)
    x_middle = (x1 + x2) / 2
    y_middle = (y1 + y2) / 2

    d = func_second_dy_ch(x_middle, y_middle) * func_first_dx_ch(x_middle, y_middle) - \
        func_first_dy_ch(x_middle, y_middle) * func_second_dx_ch(x_middle, y_middle)
    next_x = x_middle - \
             (func_second_dy_ch(x_middle, y_middle) * func_first(x_middle, y_middle) -
              func_first_dy_ch(x_middle, y_middle) * func_second(x_middle, y_middle)) / d
    next_y = y_middle - \
             (func_first_dx_ch(x_middle, y_middle) * func_second(x_middle, y_middle) -
              func_second_dx_ch(x_middle, y_middle) * func_first(x_middle, y_middle)) / d

    for i in range(1, 100):
        x_middle = next_x
        y_middle = next_y

        d = func_second_dy_ch(x_middle, y_middle) * func_first_dx_ch(x_middle, y_middle) - \
            func_first_dy_ch(x_middle, y_middle) * func_second_dx_ch(x_middle, y_middle)
        next_x = x_middle - \
                 (func_second_dy_ch(x_middle, y_middle) * func_first(x_middle, y_middle) -
                  func_first_dy_ch(x_middle, y_middle) * func_second(x_middle, y_middle)) / d
        next_y = y_middle - \
                 (func_first_dx_ch(x_middle, y_middle) * func_second(x_middle, y_middle) -
                  func_second_dx_ch(x_middle, y_middle) * func_first(x_middle, y_middle)) / d

        if abs(next_x - x_middle) <= epsilon and abs(next_y - y_middle) <= epsilon:
            print('x: {:.6f} y: {:.6f}'.format(next_x, next_y))
            print(f'Iterations: {i}')
            print('Different in x: {:+.10f}'.format(next_x - x_middle))
            print('Different in y: {:+.10f}'.format(next_y - y_middle))
            break
    print('-' * 70)


if __name__ == '__main__':
    checker(0, -5, 1.75, 4)
    checker_ch(0, -5, 1.75, 4)
