# Python Programming: Best Practices and Advanced Concepts

## Python Fundamentals

### Data Types
Python's built-in types include integers, floats, strings, booleans, lists, tuples, sets, and dictionaries. Python is dynamically typed. Type hints (PEP 484) add optional static typing: `def greet(name: str) -> str`.

### List Comprehensions
List comprehensions provide a concise way to create lists: `squares = [x**2 for x in range(10)]`. Generator expressions use parentheses and are memory-efficient for large datasets.

## Object-Oriented Programming

### Classes and Inheritance
Python supports single and multiple inheritance. The `super()` function calls parent class methods. `__init__` is the constructor; dunder methods (`__repr__`, `__str__`, `__eq__`) customize object behavior. Dataclasses (Python 3.7+) auto-generate boilerplate.

### Decorators
Decorators are higher-order functions that wrap other functions. `@property` creates managed attributes; `@staticmethod` and `@classmethod` define alternative method types.

## Asynchronous Python

### asyncio
Python's asyncio enables concurrent I/O-bound operations using coroutines. `async def` defines coroutines; `await` suspends execution pending a result. `asyncio.gather()` runs multiple coroutines concurrently. FastAPI and aiohttp leverage asyncio.

### Threading vs Multiprocessing
The Global Interpreter Lock (GIL) limits true parallelism for CPU-bound tasks in CPython. Use `threading` for I/O-bound work; `multiprocessing` spawns separate processes for CPU-bound parallelism.

## Python Ecosystem

### Package Management
`pip` installs packages from PyPI. Virtual environments (`venv`, `conda`) isolate project dependencies. `pyproject.toml` (PEP 518) is the modern standard. Poetry and uv are popular modern package managers.

### Testing
`pytest` is the de facto testing framework. Fixtures manage test setup/teardown; parametrize runs tests with multiple inputs. `coverage.py` measures code coverage.

## Data Science Libraries

### NumPy
NumPy provides N-dimensional array objects and mathematical functions. Broadcasting enables operations on arrays of different shapes. Vectorized operations are orders of magnitude faster than Python loops.

### Pandas
Pandas offers DataFrame and Series structures for tabular data. Key operations: `groupby`, `merge`, `pivot_table`, `apply`. Pandas 2.0 introduced PyArrow-backed dtypes for better memory efficiency.

## Performance Optimization

### Profiling
`cProfile` and `line_profiler` identify bottlenecks. `memory_profiler` tracks memory usage. `timeit` benchmarks small code snippets. Always profile before optimizing.

### Cython and Numba
Cython compiles Python to C for speed. Numba uses LLVM JIT compilation, particularly effective for numerical loops. Both can achieve C-like performance for compute-intensive Python code.
