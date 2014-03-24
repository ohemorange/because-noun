import time
import calendar

def begin_timestamp(month, day, year):
    begin_struct = time.struct_time((year,month,day,0,0,0,0,0,0))
    begin = calendar.timegm(begin_struct)
    return begin

def end_timestamp(month, day, year):
    end_struct = time.struct_time((year, month, day, 23, 59, 59, 0, 0, 0))
    end = calendar.timegm(end_struct)
    return end
