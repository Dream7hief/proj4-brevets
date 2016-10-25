import acp_times
import arrow

TEST_DATE = arrow.get('1995-03-23 00:00:00', 'YYYY-MM-DD HH:mm:ss')

def test_zero_control():
	correct_time = arrow.get('1995-03-23 01:00:00').isoformat()
	
	test_close_200 = acp_times.close_time(0, 200, TEST_DATE)
	print(test_close_200)
	test_close_400 = acp_times.close_time(0, 400, TEST_DATE)
	test_close_600 = acp_times.close_time(0, 600, TEST_DATE)
	test_close_1000 = acp_times.close_time(0, 1000, TEST_DATE)

	assert test_close_200 == correct_time
	assert test_close_400 == correct_time
	assert test_close_600 == correct_time
	assert test_close_1000 == correct_time

def test_control_overflow(): #test if control greater than 20% limit
	correct_time_240 = arrow.get('1995-03-23 16:00:00').isoformat()
	correct_time_481 = arrow.get('1995-03-23 00:00:00').isoformat()
	correct_time_720 = arrow.get('1995-03-25 02:30:00').isoformat()
	correct_time_1201 = arrow.get('1995-03-23 00:00:00').isoformat()

	test_close_240 = acp_times.close_time(240, 200, TEST_DATE) #PASS
	print(test_close_240)
	test_close_481 = acp_times.close_time(481, 400, TEST_DATE) #FAIL
	test_close_720 = acp_times.close_time(720, 600, TEST_DATE) #PASS
	test_close_1201 = acp_times.close_time(1201, 1000, TEST_DATE) #FAIll

	assert test_close_240 == correct_time_240
	assert test_close_481 == correct_time_481
	assert test_close_720 == correct_time_720
	assert test_close_1201 == correct_time_1201

def test_speed_table():	#check change in speed behavior
	correct_time_250 = arrow.get('1995-03-23 16:40:00').isoformat()
	correct_time_375= arrow.get('1995-03-24 01:00:00').isoformat()
	correct_time_650 = arrow.get('1995-03-24 20:23:00').isoformat()
	correct_time_975 = arrow.get('1995-03-26 00:49:00').isoformat()

	test_close_250 = acp_times.close_time(250, 1000, TEST_DATE)
	print(test_close_250)
	test_close_375 = acp_times.close_time(375, 1000, TEST_DATE) 
	test_close_650 = acp_times.close_time(650, 1000, TEST_DATE) 
	test_close_975 = acp_times.close_time(975, 1000, TEST_DATE) 

	assert test_close_250 == correct_time_250
	assert test_close_375 == correct_time_375
	assert test_close_650 == correct_time_650
	assert test_close_975 == correct_time_975