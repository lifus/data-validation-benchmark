# Overview

Benchmark for python data validation libraries

# Coverage

At this point, the following libraries are covered by this benchmark:

1. [cerberus][1]
2. [marshmallow][2]

**Note**: I do realize that [marshmallow][2] is an object serialization library, but it also provides data validation facilities

# Usage

## Prerequisites

[tox][3] is the only real prerequisite at the moment. It should take care of the rest.

## Run

```bash
tox
```

# Results

```
py27 installed: benchmark==0.1.5,Cerberus==0.9.2,marshmallow==2.2.1,python-dateutil==2.4.2,six==1.10.0,wheel==0.24.0
py27 runtests: PYTHONHASHSEED='3738075971'
py27 runtests: commands[0] | /home/lifus/PycharmProjects/data-validation-benchmark/.tox/py27/bin/python datavalidation/benchmark/runner.py

Benchmark Report
================

Validate complex valid data
---------------------------

       name | rank | runs |   mean |        sd | timesBaseline | worstCase | bestCase | stability
------------|------|------|--------|-----------|---------------|-----------|----------|----------
marshmallow |    1 |   10 |  0.255 |  0.001321 |           1.0 |    0.2583 |   0.2538 |       98%
   cerberus |    2 |   10 | 0.3048 | 0.0009132 | 1.19524092308 |    0.3073 |   0.3041 |       99%

Validate simple invalid data
----------------------------

       name | rank | runs |    mean |        sd | timesBaseline | worstCase | bestCase | stability
------------|------|------|---------|-----------|---------------|-----------|----------|----------
   cerberus |    1 |   10 | 0.01656 | 6.126e-05 |           1.0 |   0.01668 |  0.01646 |       99%
marshmallow |    2 |   10 | 0.03619 | 0.0001537 | 2.18493850689 |   0.03657 |  0.03603 |       99%

Validate simple valid data
--------------------------

       name | rank | runs |    mean |        sd | timesBaseline | worstCase | bestCase | stability
------------|------|------|---------|-----------|---------------|-----------|----------|----------
   cerberus |    1 |   10 | 0.01711 | 0.0001265 |           1.0 |   0.01745 |  0.01701 |       97%
marshmallow |    2 |   10 | 0.01968 | 0.0001001 | 1.15044273686 |   0.01996 |  0.01961 |       98%

Each of the above 60 runs were run in random, non-consecutive order by
`benchmark` v0.1.5 (http://jspi.es/benchmark) with Python 2.7.10+
Linux-4.1.0-1-amd64-x86_64 on 2015-11-15 20:01:45.

py34 installed: benchmark==0.1.5,Cerberus==0.9.2,marshmallow==2.2.1,python-dateutil==2.4.2,six==1.10.0,wheel==0.24.0
py34 runtests: PYTHONHASHSEED='3738075971'
py34 runtests: commands[0] | /home/lifus/PycharmProjects/data-validation-benchmark/.tox/py34/bin/python datavalidation/benchmark/runner.py

Benchmark Report
================

Validate complex valid data
---------------------------

       name | rank | runs |   mean |        sd |     timesBaseline | worstCase | bestCase | stability
------------|------|------|--------|-----------|-------------------|-----------|----------|----------
marshmallow |    1 |   10 | 0.2275 | 0.0002822 |               1.0 |    0.2279 |    0.227 |      100%
   cerberus |    2 |   10 | 0.2766 | 0.0004274 | 1.216086628708981 |    0.2775 |   0.2762 |      100%

Validate simple invalid data
----------------------------

       name | rank | runs |    mean |        sd |      timesBaseline | worstCase | bestCase | stability
------------|------|------|---------|-----------|--------------------|-----------|----------|----------
   cerberus |    1 |   10 | 0.01666 | 0.0001051 |                1.0 |   0.01675 |  0.01648 |       98%
marshmallow |    2 |   10 | 0.03706 | 0.0002575 | 2.2245011276861253 |   0.03763 |  0.03675 |       98%

Validate simple valid data
--------------------------

       name | rank | runs |    mean |        sd |      timesBaseline | worstCase | bestCase | stability
------------|------|------|---------|-----------|--------------------|-----------|----------|----------
   cerberus |    1 |   10 | 0.01769 | 5.532e-05 |                1.0 |   0.01778 |  0.01761 |       99%
marshmallow |    2 |   10 |  0.0181 | 0.0001117 | 1.0229666528781414 |   0.01832 |  0.01798 |       98%

Each of the above 60 runs were run in random, non-consecutive order by
`benchmark` v0.1.5 (http://jspi.es/benchmark) with Python 3.4.3+
Linux-4.1.0-1-amd64-x86_64 on 2015-11-15 20:01:51.

___________________________________________________________________________________ summary ___________________________________________________________________________________
  py27: commands succeeded
  py34: commands succeeded
  congratulations :)
```

# License
This project is available under the [Apache License, Version 2.0][5]

# Credits

This benchmark is based on [benchmark][4] and uses [tox][3] as it's runner

[1]: https://pypi.python.org/pypi/Cerberus
[2]: https://pypi.python.org/pypi/marshmallow
[3]: https://pypi.python.org/pypi/tox
[4]: https://pypi.python.org/pypi/benchmark
[5]: http://www.apache.org/licenses/LICENSE-2.0.html
