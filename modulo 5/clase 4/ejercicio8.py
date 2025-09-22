from scipy.stats import norm

p = 1 - norm.cdf(1.25)

print(f'la probabilidad de P(Z) > 1.50 es: {p:.5f}')



p1 = norm.sf(1.25)

print(f'{p1:.5f}')