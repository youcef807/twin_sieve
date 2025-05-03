# twin_sieve

A mathematical sieve to generate twin prime numbers using a structure based on 6k ± 1 forms.

## Features

- Fast filtering of twin primes without checking divisibility
- Based on prime structure theory
- Returns a list of prime twin pairs up to any given limit

## Example

```python
from twin_sieve import twin_prime_sieve

print(twin_prime_sieve(100))
