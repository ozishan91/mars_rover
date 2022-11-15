# mars_rover

## Installing

Requirements : Python3, pip

##Running the build
```
   git clone https://github.com/ozishan91/mars_rover.git
   cd mars_rover
   make build 
```
Once the build is complete, the wheel file gets generated inside the `dist` directory. 

## How to use:
### Running the app using the test input
Once the build completes, run the below commands
```
    cd dist
    pip3 install mars_rover-0.1-py2.py3-none-any.whl --force-reinstall
    cd ../marsrover
    python3 runner.py
```
This will take the test input from ```inputFile.txt``` and print the Rover(s) final position(s) to stdout.
    
## Running the tests
```
make test
```