def main():
    police_car = 'パトカー'
    taxi = 'タクシー'

    police_car_arr = list(police_car)
    taxi_arr = list(taxi)

    c_arr = []
    for i in range(len(police_car_arr)):
        c_arr.append(police_car_arr[i])
        c_arr.append(taxi_arr[i])
    result = ''.join(c_arr)
    print(result)

    return result

if __name__=='__main__':
    main()