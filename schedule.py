### schedule definitions
from datetime import time

sun_open = []
sun_close = []
mon_open = []
mon_swing = []
mon_close = []
tues_open = []
tues_swing = []
tues_close = []
wed_open = []
wed_swing = []
wed_close = []
thurs_open = []
thurs_swing = []
thurs_close = []
fri_open = []
fri_swing = []
fri_close = []
sat_open = []
sat_close = []

sunday = [sun_open, sun_close]
monday = [mon_open, mon_swing, mon_close]
tuesday = [tues_open, tues_swing, tues_close]
wednesday = [wed_open, wed_swing, wed_close]
thursday = [thurs_open, thurs_swing, thurs_close]
friday = [fri_open, fri_swing, fri_close]
saturday = [sat_open, sat_close]

week = [sunday, monday, tuesday, wednesday, thursday, friday, saturday]

