# pp_cmd_rand
Postprocessing command "rand"
## Description
Adds column with random integers from 0 to 1000

### Arguments
- column - positional argument, text, required, new column name
- count - positional argument, integer, not required, default 10, number of rows to add. Ignored if input dataframe passed.

### Usage example
```
query: rand new_col, 4
```
```
   new_col
0      444
1       57
2      515
3      742

```
```
query: otl_v1 <# makeresults count=5#> | rand new_col, 2
```
```
            _time  new_col
Index                     
0      1679975374      353
1      1679975374      618
2      1679975374      738
3      1679975374      372
4      1679975374       36

```

## Getting started
### Installing
1. Create virtual environment with post-processing sdk 
```bash
    make dev
```
That command  
- downloads [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- creates python virtual environment with [postprocessing_sdk](https://github.com/ISGNeuroTeam/postprocessing_sdk)
- creates link to current command in postprocessing `pp_cmd` directory 

2. Configure `otl_v1` command. Example:  
```bash
    vi ./venv/lib/python3.9/site-packages/postprocessing_sdk/pp_cmd/otl_v1/config.ini
```
Config example:  
```ini
[spark]
base_address = http://localhost
username = admin
password = 12345678

[caching]
# 24 hours in seconds
login_cache_ttl = 86400
# Command syntax defaults
default_request_cache_ttl = 100
default_job_timeout = 100
```

3. Configure storages for `readFile` and `writeFile` commands:  
```bash
   vi ./venv/lib/python3.9/site-packages/postprocessing_sdk/pp_cmd/readFile/config.ini
   
```
Config example:  
```ini
[storages]
lookups = /opt/otp/lookups
pp_shared = /opt/otp/shared_storage/persistent
```

### Run rand
Use `pp` to run rand command:  
```bash
pp
Storage directory is /tmp/pp_cmd_test/storage
Commmands directory is /tmp/pp_cmd_test/pp_cmd
query: | otl_v1 <# makeresults count=100 #> |  rand new_col
```
## Deploy
Unpack archive `pp_cmd_rand` to postprocessing commands directory
## Test
Use `make test` and all test will run in Docker container. Please turn the vpn on so all the OTL dependencies would download.