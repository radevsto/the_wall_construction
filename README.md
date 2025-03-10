# The Wall Construction

## TL;DR;

Work assignment requirements covered (hopefully nothing is missed).
Assignment content at the bottom of this readme.

> Thanks for the entertaining task, `Game of Thrones` for the win, much appreciated! 

### Work Notes:
- Decided to keep the business logic outside of the model classes for separation of concerns.
- Tables created for `Day` and `Profile` - chosen segmentation based on above statement.
- A separate custom manage.py command added to execute the business logic and store the data.
- Logging added using the integrated django logging for both requests and business logic.

### Extras:
- API for Overall cost of a profile
- Web interface on homepage (http://localhost:8000/) that uses all of the APIs 

> Note: Implemented in html but does the job ... shame :)

![SHAME](https://github.com/user-attachments/assets/b1c39375-01ae-4f7b-aa2f-09eb478e23c3)


## Usage

Run
```
python.exe .\manage.py build_the_wall
```

Than
```
python.exe .\manage.py runserver
```

> Note: The `build_the_wall` custom command can be executed when the local server is running

### WEB API list
- http://localhost:8000/profiles/<profile_number>/days/<day_number>/ - Ice used for profile on day
- http://localhost:8000/profiles/<profile_number>/overvew/<day_number>/ - Cost for profile on day
- http://localhost:8000/profiles/overview/<day_number>/ - Overall cost on a day
- http://localhost:8000/profiles/<profile_number>/overview/ - Overall cost of a profile
- http://localhost:8000/profiles/overview/ - Total cost

Web interface available at http://localhost:8000/

### Logging

Runtime and custom command logging are using `logs\TheWall_web.log` file for logging events.
Each section stores a log file to track it's build under `logs\Profile_N-Section_N.log`.
Format of section loggers:
```
2025-03-10 10:17:03,589 - INFO - Height at beginning of the day - 22
2025-03-10 10:17:03,590 - INFO - High build - 1
2025-03-10 10:17:04,274 - INFO - Height at beginning of the day - 23
2025-03-10 10:17:04,274 - INFO - High build - 1
2025-03-10 10:17:04,309 - INFO - Height at beginning of the day - 24
2025-03-10 10:17:04,309 - INFO - High build - 1
2025-03-10 10:17:04,539 - INFO - Height at beginning of the day - 25
2025-03-10 10:17:04,539 - INFO - High build - 1
2025-03-10 10:17:04,588 - INFO - Height at beginning of the day - 26
2025-03-10 10:17:04,588 - INFO - High build - 1
2025-03-10 10:17:04,838 - INFO - Height at beginning of the day - 27
2025-03-10 10:17:04,838 - INFO - High build - 1
2025-03-10 10:17:05,091 - INFO - Height at beginning of the day - 28
2025-03-10 10:17:05,091 - INFO - High build - 1
2025-03-10 10:17:05,346 - INFO - Height at beginning of the day - 29
2025-03-10 10:17:05,354 - INFO - High build - 1
2025-03-10 10:17:05,356 - INFO - Section Section(identifier='Profile_3-Section_1', crews=[Crew(number=3, section_height=17, busy=True)], all_crews=[Crew(number=6, section_height=17, busy=False), Crew(number=5, section_height=22, busy=False)], height=30, profile_id=3, height_on_day=1, complete=True, logger=<Logger Profile_3-Section_1 (INFO)>) has been complete.
2025-03-10 10:17:05,357 - INFO - Crew 3 has been released from section Section(identifier='Profile_3-Section_1', crews=[], all_crews=[Crew(number=6, section_height=17, busy=False), Crew(number=5, section_height=22, busy=False), Crew(number=3, section_height=17, busy=False)], height=30, profile_id=3, height_on_day=1, complete=True, logger=<Logger Profile_3-Section_1 (INFO)>).

```

## Infrastructural setup

### Conda environment 
```
(the_wall) PS C:\the_wall_construction> conda list
# packages in environment at C:\ProgramData\Python\envs\the_wall:
#
# Name                    Version                   Build  Channel
asgiref                   3.8.1           py312haa95532_0    defaults
black                     24.10.0         py312haa95532_0    defaults
bzip2                     1.0.8                h2bbff1b_6    defaults
ca-certificates           2025.2.25            haa95532_0    defaults
click                     8.1.7           py312haa95532_0    defaults
colorama                  0.4.6           py312haa95532_0    defaults
coverage                  7.6.9           py312h827c3e9_0    defaults
django                    5.1.3           py312haa95532_0    defaults
django-extensions         3.2.3                    pypi_0    pypi
djangorestframework       3.15.2                   pypi_0    pypi
expat                     2.6.4                h8ddb27b_0    defaults
flake8                    7.1.1           py312haa95532_0    defaults
iniconfig                 1.1.1              pyhd3eb1b0_0    defaults
libffi                    3.4.4                hd77b12b_1    defaults
mccabe                    0.7.0              pyhd3eb1b0_0    defaults
mypy_extensions           1.0.0           py312haa95532_0    defaults
openssl                   3.0.16               h3f729d1_0    defaults
packaging                 24.2            py312haa95532_0    defaults
pathspec                  0.10.3          py312haa95532_0    defaults
pip                       24.2            py312haa95532_0    defaults
platformdirs              3.10.0          py312haa95532_0    defaults
pluggy                    1.5.0           py312haa95532_0    defaults
pycodestyle               2.12.1          py312haa95532_0    defaults
pyflakes                  3.2.0           py312haa95532_0    defaults
pytest                    7.4.4           py312haa95532_0    defaults
pytest-cov                6.0.0           py312haa95532_0    defaults
pytest-django             4.10.0                   pypi_0    pypi
python                    3.12.8               h14ffc60_0    defaults
pyyaml                    6.0.2           py312h827c3e9_0    defaults
setuptools                75.1.0          py312haa95532_0    defaults
sqlite                    3.45.3               h2bbff1b_0    defaults
sqlparse                  0.5.2           py312haa95532_0    defaults
tk                        8.6.14               h0416ee5_0    defaults
toml                      0.10.2             pyhd3eb1b0_0    defaults
typing                    3.10.0.0        py312haa95532_0    defaults
tzdata                    2024b                h04d1e81_0    defaults
vc                        14.40                haa95532_2    defaults
vs2015_runtime            14.42.34433          h9531ae6_2    defaults
wheel                     0.44.0          py312haa95532_0    defaults
xz                        5.4.6                h8cc25b3_1    defaults
yaml                      0.2.5                he774522_0    defaults
zlib                      1.2.13               h8cc25b3_1    defaults
(the_wall) PS C:\the_wall_construction> 
```
### Code quality and formatting
```
(the_wall) PS C:\the_wall_construction> black --check .
All done! ✨ 🍰 ✨
31 files would be left unchanged.
(the_wall) PS C:\the_wall_construction> flake8 . --config=tox.ini
```
### Unit tests execution
```
(the_wall) PS C:\the_wall_construction> pytest --cov=.\TheWall\ --cov-config=tox.ini
....................................                                                                                        [100%]

---------- coverage: platform win32, python 3.12.8-final-0 -----------
Name                                                                             Stmts   Miss   Cover   Missing
---------------------------------------------------------------------------------------------------------------
TheWall\__init__.py                                                                  0      0 100.00%
TheWall\admin.py                                                                     0      0 100.00%
TheWall\apps.py                                                                      4      0 100.00%
TheWall\construction_management.py                                                  58      0 100.00%
TheWall\construction_manager.py                                                     77     21  72.73%   118-142, 170-183
TheWall\custom_exceptions.py                                                         8      0 100.00%
TheWall\management\__init__.py                                                       0      0 100.00%
TheWall\management\commands\__init__.py                                              0      0 100.00%
TheWall\migrations\0001_initial.py                                                   5      0 100.00%
TheWall\migrations\0002_day_profile_delete_wallprofile_day_profile_and_more.py       5      0 100.00%
TheWall\migrations\__init__.py                                                       0      0 100.00%
TheWall\models.py                                                                   14      0 100.00%
TheWall\serializers.py                                                              12      0 100.00%
TheWall\tests\conftest.py                                                           58      0 100.00%
TheWall\tests\test_construction_management.py                                       53      0 100.00%
TheWall\tests\test_construction_manager.py                                          33      0 100.00%
TheWall\tests\test_custom_exceptions.py                                              6      0 100.00%
TheWall\tests\test_models.py                                                        21      0 100.00%
TheWall\tests\test_serializers.py                                                   38      0 100.00%
TheWall\tests\test_utilities.py                                                     37      0 100.00%
TheWall\tests\test_views.py                                                         41      0 100.00%
TheWall\urls.py                                                                      3      0 100.00%
TheWall\utilities.py                                                                37      0 100.00%
TheWall\views.py                                                                    34      0 100.00%
---------------------------------------------------------------------------------------------------------------
TOTAL                                                                              544     21  96.14%

36 passed in 2.02s
(the_wall) PS C:\the_wall_construction> 
```

## Technical assignment

```
The Wall

Story
- "The White Walkers sleep beneath the ice for thousands of years. And when they
wake up..."
- "And when they wake up... what?"
- "I hope the Wall is high enough."
The Wall is a colossal fortification which is being built to stretch for 100 leagues
(300 miles) along the northern border of the Seven Kingdoms. Its purpose is to
defend the realm from the wildlings who live beyond. The Wall is reported to be 30
foot tall and is made of solid ice. The Sworn Brothers of the Night's Watch have
arranged that each section has its own construction crew.

Task

Description
Write a program that keeps track of material quantities and cost for the
construction of the 30-foot wall.

You will be given a series of numbers. These numbers represent the initial heights
of different mile-long sections of the wall(Wall profile), in feet. Each of these
sections has its own construction crew that can add 1 foot of height per day. All
crews work simultaneously (see examples), meaning all sections that aren’t
completed (are less than 30 feet high) grow by 1 foot every day. When a section of
the wall is completed, its crew is relieved. Each foot added uses 195 cubic yards of
ice. To process one cubic yard, it costs the Night’s Watch 1900 "Gold Dragon"
coins for salaries and food for the brothers who work on it.

Your program needs to expose a rest API using Django and Django Rest
Framework that allows the managers of the process to keep track of how much
ice is used daily until the completion of the entire wall profile.
At the end, your program needs to expose two API endpoints one for checking the
amount of ice used during a particular day (given as a parameter) for a

particular wall profile and second that gives the overview of how much does the
construction cost until the given day per profile and overall.

Input
The input is a config file containing the wall profiles with one line for each profile,
containing numbers, separated by space.
Output
Daily API: Print the amount of ice used on a given day for a profile.
Overview API: Shows the final cost of the wall. Or if given a parameter shows the
cost per wall profile.
Constraints
The wall profile may contain up to 2000 sections
Starting height for each section is within range [0...30]

Multi-threaded version
Instead of automatically having a team for each section of the wall profile take as
an input also the number of available teams. Each team can work only one wall
section in one profile. The APIs should return the same results but each team that
finishes a section instead of being relieved will move to the next section and the
next wall profile if this is completed.
Implement the dynamic of the teams with a Pool of parallel processes / threads
that process one section every day and feed their job queue with the next section
if available. Each process/thread should write into a log file the section that it has
completed on the concrete day or “relieved” if there are no jobs.
Scroll down to see detailed examples.

Example
Input
21 25 28
17
17 22 17 19 17

Explanation:
On the first day, all crews work simultaneously, each adding 1 foot to
their section:
First profile: 3 crews x 195 = 585 cubic yards
Second profile: 1 crew x 195 = 195 cubic yards
Third profile: 5 crews x 195 = 975 cubic yards
In total: 1 755 cubic yards
On the second day, it’s the same. However, the last section of the first wall profile
reaches 30 feet and its crew is being relieved.
On the third day, only two crews work from the first wall profile, using up 390 cubic
yards in total.

Etc.

Output:
GET /profiles/1/days/1/
RETURNS: {

day: ”1”;
ice_amount: “585”
}

GET /profiles/1/overview/1/
RETURNS: {

day: ”1”;
cost: “1,111,500”
}

GET /profiles/overview/1/
RETURNS: {

day: ”1”;
cost: “3,334,500”
}

GET /profiles/overview/
RETURNS: {

day: None;
cost: “32,233,500”
}
```
