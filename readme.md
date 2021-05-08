## taew

this is a package that targets at technical analysis using Elliott wave.
currently providing python implementation for back tracking elliott wave
base on the method and Matlab code on the paper [ **Profitability of Elliott Waves and Fibonacci Retracement Levels in the Foreign Exchange Market
 ** ](http://arno.uvt.nl/show.cgi?fid=131569)

###motivation
since there are no opensource elliott wave labelling package. to facilitate the private project that me and my friend currently working on, this library is created.

### installation
```
pip install taew
```

### list of main method

listed methods are for the labelling of elliott wave

```python
def Alternative_ElliottWave_label_upward(data:list[number])->list[dict]:
    #identify full elliott impulse wave from a list of price, the wave will fits the fibonacci retracement and also fibonacci timezone for upward impulse wave
    
def Alternative_ElliottWave_label_downward(data:list[number])->list[dict]:
    #identify full elliott impulse wave from a list of price, the wave will fits the fibonacci retracement and also fibonacci timezone for downward impulse wave
    
def Traditional_ElliottWave_label_upward(data:list[number])->list[dict]:
    #identify full elliott impulse wave from a list of price, the wave will fits the fibonacci retracement for upward impulse wave

def Traditional_ElliottWave_label_downward(data:list[number])->list[dict]:
    #identify full elliott impulse wave from a list of price, the wave will fits the fibonacci retracement for downward impulse wave

def Practical_ElliottWave3_label_upward(data:list[number])->list[dict]:
    #identify the first 2 wave of all the candidate upward elliott wave from the data, good predictor of 3rd upward impulse wave
    
def Practical_ElliottWave3_label_downward(data:list[number])->list[dict]:
    #identify the first 3 wave of all the candidate downward elliott wave from the data, good predictor of 4th upward impulse wave

def Practical_ElliottWave5_label_upward(data:list[number])->list[dict]:
    #identify the first 4 wave of all the candidate upward elliott wave from the data, good predictor of 5tth upward impulse wave

```
### list of helper method
listed methods are for helping the identification of the labelling, if you try to create your own application of elliott wave labelling, this may help you

```python
def wave2_fibonacci_check(wave2_end, wave1_start, wave1_end):
    # check whether wave 2 satisfy principal of fibonacci retracement
def wave3_fibonacci_check(wave3_end, wave2_start, wave2_end):
    # check whether wave 3 satisfy principal of fibonacci retracement
def wave4_fibonacci_check(wave4_end, wave3_start, wave3_end):
    # check whether wave 4 satisfy principal of fibonacci retracement
def wave5_fibonacci_check(wave5_end, wave1_start, wave1_end, wave3_start, wave3_end, wave4_end):
    #check whether wave 5 satisfy principal of fibonacci retracement
def diff(data:list[number])->list[number]:
    #similar to diff in matlab, for nth num in list return nth - n-1th 
def otherThan(data:list[any], otherthan=any)->list[bool]:
    #similar to ~= in matlab means if list item=otherthan, output list on that pos will be false otherwise will be true
def trimming(data:list[number], determineArray:list[bool])->list[number]:
    #trim out data base on the determine array
```
### example usage

#### demo code
```python
import pandas as pd
import numpy as np
import taew
import pandas_datareader.data as web
import datetime

start = datetime.datetime(2019, 1, 1)
end = datetime.datetime(2020, 1, 27)

SP500 = web.DataReader(['sp500'], 'fred', start, end)

haha=taew.Alternative_ElliottWave_label_upward(np.array(SP500[['sp500']].values , dtype=np.double).flatten(order='C'))
print(haha)
```
####expected output
```python
'''
6555
successfully filter out candidate wave
6519
successfully filter out candidate wave 12
11210
successfully filter out candidate wave123
8566
successfully filter out candidate wave1234
70380
successfully filter out candidate wave12345

[{'x': [2447.89, 2796.11, 2743.07, 2917.52, 2870.72, 2954.18],
  'z': [2, 39, 48, 87, 92, 122],
  'searchIndex': 48},
 {'x': [2447.89, 2796.11, 2743.07, 2917.52, 2811.87, 2954.18],
  'z': [2, 39, 48, 87, 94, 122],
  'searchIndex': 48},...]
'''
```
####explaination of output

from the matlab code of original paper it first extract the high point and low point of the price curve. after that performing pattern recognization. However it makes an assumption that the array of high and low point that resemble elliott wave are all in a row. This is not the case in actual market. therefore his code fails to recognize Elliott wave in real markets. Even it can, it requires denoise or filterring with SMA or EMA.

this code does not use his approach. it uses a iterative approach to first identify all possible wave 1 in the graph then find valid wave 2 and repeatedly until wave 5 has found.although the computation time is long, it can shows elliott wave of different sizes. Denoise and filter are not required.

for each main method, it returns a list of dict, each dict is an Elliott wave identified.

* 'x' : price level of all elliot wave point
* 'z' : position(a.k.a. index) of price level in the list of data
* searchIndex: maynot be useful for user, but useful for the stepwise algorithm to keep track of what to search next in its internal list


### disclaimer
this library does not guarentee correct identification of all elliott wave, user use this to earn money from any market should bear their own risk. Author will not bear any risk(s) or benefit(s) if user of this library lose any money or earn any money respectively