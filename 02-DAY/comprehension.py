net_prices = [19000, 28500, 990000, 130000]
vat_rate_in_percent = 27
gross_prices = []

# for net_price in net_prices:
#     gross_prices.append(net_price * (1 + vat_rate_in_percent / 100))


gross_prices = [net_price * (1 + vat_rate_in_percent / 100)
                for net_price in net_prices]
print(gross_prices)

grades_list = [1, 2, 3, 3, 4, 5, 5, 4, 3, 6, 7, 4, 5, 6, 7]
ok_greades_list = [i for i in grades_list if 0 < i < 6]
print(ok_greades_list)

matrix = [[j for j in range(5)] for _ in range(5)]
print(matrix)

flatted_matrix = [j for i in matrix for j in i]

for i in matrix:
    for j in i:
        print(j)

print(10 + 10)
