# Pi Value Estimation
This project implements several numerical methods to estimate the value of $\pi$. The four methods included are Monte Carlo, Leibniz, Nilakantha, and Gauss-Legendre.

## Table of Contents
- [Required libraries](#RequiredLibraries)
- [Installation](#Installation)
- [Methods](#Methods)
- [Contributing](#Contributing)
- [References](#References)

## Required Libraries
Two libraries used in this python script, math and random. Both of them are part of Python’s standard library. This means they're built-in and available for you to use right away without any additional installation.

## Installation
1. Open terminal
2. Clone the repository:
```bash
git clone https://github.com/LittleBigPluton/Pi-Estimation.git
```
3. Change directory:
```bash
cd Pi-Estimation
```
4. To run the python script on terminal:
```bash
python3 main.py
```

## Methods
### Monte Carlo[(1)](https://en.wikipedia.org/wiki/Monte_Carlo_method)
#### Theory

The Monte Carlo method uses random sampling to estimate quantities that are difficult to calculate directly. We use a geometric probability approach based on the areas of a circle and a square. We generate N random points uniformly distributed over the square. Since the points are uniformly distributed, the probability that a point falls within any subregion is proportional to the area of that subregion relative to the total area of the square. Consider a circle of radius 1 inscribed in a square of side length 2.   
- The area of the circle is given by:
  $$A_{\text{circle}} = \pi \times 1^2 = \pi$$  
- The area of the square is:
  $$A_{\text{square}} = 2 \times 2 = 4$$
- The probability P that a randomly chosen point falls inside the circle is:
$$P = \frac{A_{\text{circle}}}{A_{\text{square}}} = \frac{\pi}{4}$$

Let N be the number of points in the square. As N becomes larger, the ratio converges to the true probability:
$$\frac{N_{\text{inside}}}{N} \approx \frac{\pi}{4}$$

By rearranging the relation, we obtain:
$$\pi \approx 4 \times \frac{N_{\text{inside}}}{N}$$  
So by counting the fraction of points inside the circle and multiplying by 4, we can estimate the value of $\pi$.


The accuracy of the Monte Carlo estimation improves with the number of samples N. As N increases, the ratio $\frac{N_{\text{inside}}}{N}$ converges to the true probability $\frac{\pi}{4}$ by the law of large numbers[(2)](https://en.wikipedia.org/wiki/Law_of_large_numbers), leading to an increasingly accurate approximation of $\pi$.

This approach shows how the fraction of points that fall within a specific region (the circle) is directly related to the area of that region relative to the total area of the space (the square).

#### Application

For MC_PI_calculator function in pi_estimate.py file, two positive random numbers between [0.0,1.0] are selected to represent x and y coordinate pairs in Cartesian coordinate system. Imagine there is a square with side length 2 is lying on the first region of the coordinate system where left bottom corner of it is at the origin. Inside this square, there is a circle which origin is at (1,1) in the coordinate system.

```python
# Generate data points
for i in range(0,attempts):
  x = 1-random.uniform(0.0,2.0)
  y = 1-random.uniform(0.0,2.0)
```

Then, it is checked the distance of this point from origin of the circle to see if it is inside the circle or not.
```python
# Calculate point's distance from center of circle
point = math.sqrt(x*x+y*y)
# Check if the point is in the circle area or not
if point<=1:
  inside_circle += 1
```
This procedure is repeated a million times, $10^6$, this number can be specified in main.py file, and the points inside the unit circle are counted. Finally, the ratio of the points inside the circle to the total number of points gives a quarter of the value of pi.
```python
# Calculate ratio of data point inside
return(inside_circle/attempts*4)
```
The following table shows how estimated $\pi$ values change for different attempts as a result of our simulation.

| Number of attempt | Approximated \pi Value  |
| ----------------- | ----------------------- |
| 10                | 2.0                     |
| $10^2$            | 2.92                    |
| $10^3$            | 3.14                    |
| $10^4$            | 3.124                   |
| $10^5$            | 3.14112                 |
| $10^6$            | 3.14142                 |

### Leibniz Formula[(3)](https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80)
#### Theory

The Leibniz formula (also known as the Gregory-Leibniz series) for $\pi$ is an infinite series that converges to . It is derived from the Taylor series expansion of the arctan function:

$$
\arctan(x) = \sum_{k=0}^{\infty} (-1)^k \frac{x^{2k+1}}{2k+1}, \quad |x| \leq 1
$$

By setting x = 1, we obtain:

$$
\arctan(1) = \frac{\pi}{4} = \sum_{k=0}^{\infty} (-1)^k \frac{1}{2k+1}
$$

Multiplying both sides by 4 gives the Leibniz formula for $\pi$:

$$
\pi = 4 \sum_{k=0}^{\infty} (-1)^k \frac{1}{2k+1} = 4\left( 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \cdots \right)
$$

#### Application

In practice, Leibniz_Formula function in pi_estimate.py file, the infinite series is truncated to a finite number of terms to approximate $\pi$, it can be changed in main.py file.
```python
estimation = 0
  for k in range(attempts):
      division = 1/(2*k+1)
      if k%2 == 0:
          estimation += division
      else:
          estimation -= division
  return 4*estimation
```
Every for loop, the denominator is recalculated with respect to the current iteration. Then, to ensure the sign of the division, the k value is checked whether it is even or not and added or substitute from the cumulative value of estimation. Finally, the estimation is multiplied by 4 to return final result of the estimation after desired iteration reached. The approximation improves as the number of terms increases, though the convergence is relatively slow. For example, in our simulation results, the table shows how the approximation of $\pi$ becomes more accurate as more terms are included in the series.

| Number of Terms | Approximated \pi Value |
| --------------- | -------------------- |
| $10$            | 3.04184              |
| $10^2$          | 3.13159              |
| $10^3$          | 3.14060              |
| $10^4$          | 3.14149              |
| $10^5$          | 3.14160              |
| $10^6$          | 3.14159              |



### Nilakantha Series[(4)](https://en.wikipedia.org/wiki/Pi#Rate_of_convergence)
#### Theory

The Nilakantha series is an infinite series that provides an efficient approximation for $\pi$ with faster convergence compared to some other series, such as the Leibniz formula. The series is defined as:

$$
\pi = 3 + 4 \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{(2n)(2n+1)(2n+2)}
$$

This can be written out explicitly as:

$$
\pi = 3 + 4\left( \frac{1}{2\cdot3\cdot4} - \frac{1}{4\cdot5\cdot6} + \frac{1}{6\cdot7\cdot8} - \frac{1}{8\cdot9\cdot10} + \cdots \right)
$$

The series begins with the constant 3 and then adds and subtracts successive terms that involve the product of three consecutive even or odd numbers. The alternating signs and the decreasing magnitude of the terms ensure that the series converges to the value of $\pi$.

#### Application

In practical applications, the infinite series is truncated to a finite number of terms to approximate $\pi$ like Leibniz formula. As more terms are included, the approximation becomes more accurate.
```python
for i in range(attempts):
    n = (i+1)*2
    estimation += 4*(-1)**i/n/(n+1)/(n+2)
return estimation
```
During the finite iteration, the variable n is calculated according to the current attempt. Then, Estimation of $\pi$ digits can be calculated with this current n value by adding cumulative estimation started from 3. After all desired iterations, the estimation for $\pi$ value is achieved. For example, in our simulation results, with an increasing number of terms, the series yields a more precise approximation.

| Number of Terms | Approximated $\pi$ Value |
| --------------- | -------------------- |
| 1 term          | 3.16667              |
| 2 terms         | 3.13333              |
| 3 terms         | 3.14524              |
| 4 terms         | 3.13968              |
| 5 terms         | 3.14271              |
| 10 terms        | 3.14141              |
| 100 terms       | 3.14152              |
| 1000 terms      | 3.14159              |

### Gauss-Legendre[(5)](https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm)

#### Theory

The Gauss-Legendre algorithm is an iterative method that converges extremely quickly to $\pi$. It is based on the arithmetic-geometric mean (AGM) process and refines estimates of $\pi$ through a series of updates. The algorithm is initialized with:

- $a_0$ = 1, $b_0$ = $\frac{1}{\sqrt{2}}$, $t_0$ = $\frac{1}{4}$, $p_0$ = 1

Then, for each iteration  n $\geq$ 0, compute:

- $a_{n+1} = \frac{a_n + b_n}{2}$
- $b_{n+1} = \sqrt{a_n \, b_n}$
- $t_{n+1} = t_n - p_n \, (a_n - a_{n+1})^2$
- $p_{n+1} = 2 \, p_n$

After a sufficient number of iterations, the approximation for $\pi$ is given by:

$$
\pi \approx \frac{(a_N + b_N)^2}{4 \, t_N}
$$

This formula rapidly converges to $\pi$ due to the quadratic convergence of the arithmetic-geometric mean process.

#### Application

In practice, only a few iterations are needed to achieve high precision. After initialization of a,b,t and p values at the beginning, the inline functions for iterative values for $a_0$,$b_0$,$t_0$ and $p_0$ defined.
```python
#Initialize values
a, b, t, p = 1, 1/math.sqrt(2), 1/4, 1
#Define next values of variables as inline function
a_next = lambda a,b: (a+b)/2
b_next = lambda a,b: math.sqrt(a*b)
t_next = lambda a,a_next,p,t: t-p*(a-a_next)**2
```
After this initializations, iterations occur by updating a,b,t and p values in each iteration.
```python
#Calculate variables at the desired iteration
for _ in range(attempts):
    a_n1 = a_next(a,b)
    b = b_next(a,b)
    t = t_next(a,a_n1,p,t)
    p = p*2
    a = a_n1
```
Finally, the estimated $\pi$ value can be achieved after desired iterations.
```python
#Return estimation
return ((a+b)**2)/4/t
```
For instance, after just 3 or 4 iterations, the approximation of $\pi$ is extremely close to its true value:

| Iteration | Approximated $\pi$ Value |
| --------- | -------------------- |
| 1         | 3.1405792            |
| 2         | 3.1415926            |
| 3         | 3.1415926            |

In real-world applications, the Gauss-Legendre algorithm can be used to compute $\pi$ to millions of digits with very few iterations because of its rapid convergence. However, because of the memory issue of Gauss-Legendre algorithm, it is not the first choice to calculate larger digits.

## Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes.
4. Push your branch: `git push origin feature-name`.
5. Create a pull request.

## References
1. [Monte Carlo method](https://en.wikipedia.org/wiki/Monte_Carlo_method)
2. [Law of large numbers](https://en.wikipedia.org/wiki/Law_of_large_numbers)
3. [Leibniz formula](https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80)
4. [Nilakantha series](https://en.wikipedia.org/wiki/Pi#Rate_of_convergence)
5. [Gauss-Legendre](https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm)
