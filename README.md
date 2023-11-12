# CS361 Partner's Microservice

## How to Programmatically Request Data:

To request data from the microservice, you can utilize the `subprocess` module in Python. For more information on the `subprocess` module, refer to the [Python documentation](https://docs.python.org/3/library/subprocess.html#module-subprocess).

Use the `subprocess.run()` method as demonstrated below:

```python
import subprocess

# Replace '<microservice file path>', '<monthly income>', and '<monthly expenses>' with your specific values.
process = subprocess.run(
    ['python', '<microservice file path>', '<monthly income>', '<monthly expenses>'],
    text=True,
    capture_output=True
)
```

## How to Programmatically Receive Data:

To receive data from the microservice, it's best to first make sure there was no error.

Then, you have to deserialize the result of the `subprocess.run()` call which will leave you with a Python dictionary containing the data to work with:

```python 
# Get and deserialize the result if everything worked
if process.returncode == 0:
    result = json.loads(process.stdout)
else:
    print(f'Error: {process.stderr}')
```

## UML Sequence Diagram:
![image](https://github.com/dobell733/Partner-s-Microservice/assets/86816915/883eb365-0a5d-4d80-ba97-4c4cbbc5a1d1)
