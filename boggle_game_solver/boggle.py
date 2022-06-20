"""
File: boggle.py
Name: Han Tsai
----------------------------------------
This is the program that can search all the words based on input.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	This is the program that can search all the words based on input.
	"""
	# Load dictionary
	dic = read_dictionary()
	row1u = input("1 row of letters: ")
	row2u = input("2 row of letters: ")
	row3u = input("3 row of letters: ")
	row4u = input("4 row of letters: ")
	start = time.time()
	# Case-insensitive
	row1 = row1u.lower()
	row2 = row2u.lower()
	row3 = row3u.lower()
	row4 = row4u.lower()
	count = []
	for i in range(8):
		boggle(row1, row2, row3, row4, str(i+1), dic, count)
	num = "abcdefg"
	for ch in num:
		boggle(row1, row2, row3, row4, ch, dic, count)
	print("There are "+str(len(count))+" words in total.")
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle(row1, row2, row3, row4, current_str, dic, count):
	if len(current_str) <= 3:
		ans = ""
		for ch in current_str:
			if ch == "1":
				ans += row1[0]
			elif ch == "2":
				ans += row1[2]
			elif ch == "3":
				ans += row1[4]
			elif ch == "4":
				ans += row1[6]
			elif ch == "5":
				ans += row2[0]
			elif ch == "6":
				ans += row2[2]
			elif ch == "7":
				ans += row2[4]
			elif ch == "8":
				ans += row2[6]
			elif ch == "9":
				ans += row3[0]
			elif ch == "a":
				ans += row3[2]
			elif ch == "b":
				ans += row3[4]
			elif ch == "c":
				ans += row3[6]
			elif ch == "d":
				ans += row4[0]
			elif ch == "e":
				ans += row4[2]
			elif ch == "f":
				ans += row4[4]
			elif ch == "g":
				ans += row4[6]
		if has_prefix(ans, dic):
			if current_str[len(current_str)-1] == "1":
				if "2" not in current_str:
					current_str += "2"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "5" not in current_str:
					current_str += "5"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "6" not in current_str:
					current_str += "6"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "2":
				if "1" not in current_str:
					current_str += "1"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "5" not in current_str:
					current_str += "5"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "6" not in current_str:
					current_str += "6"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "7" not in current_str:
					current_str += "7"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "3" not in current_str:
					current_str += "3"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "3":
				if "2" not in current_str:
					current_str += "2"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "6" not in current_str:
					current_str += "6"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "7" not in current_str:
					current_str += "7"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "8" not in current_str:
					current_str += "8"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "4" not in current_str:
					current_str += "4"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "4":
				if "3" not in current_str:
					current_str += "3"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "7" not in current_str:
					current_str += "7"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "8" not in current_str:
					current_str += "8"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "5":
				if "1" not in current_str:
					current_str += "1"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "2" not in current_str:
					current_str += "2"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "6" not in current_str:
					current_str += "6"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "a" not in current_str:
					current_str += "a"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "9" not in current_str:
					current_str += "9"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "6":
				if "1" not in current_str:
					current_str += "1"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "2" not in current_str:
					current_str += "2"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "3" not in current_str:
					current_str += "3"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "7" not in current_str:
					current_str += "7"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "b" not in current_str:
					current_str += "b"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "a" not in current_str:
					current_str += "a"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "5" not in current_str:
					current_str += "5"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "9" not in current_str:
					current_str += "9"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "7":
				if "2" not in current_str:
					current_str += "2"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "3" not in current_str:
					current_str += "3"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "4" not in current_str:
					current_str += "4"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "8" not in current_str:
					current_str += "8"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "c" not in current_str:
					current_str += "c"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "b" not in current_str:
					current_str += "b"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "a" not in current_str:
					current_str += "a"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "6" not in current_str:
					current_str += "6"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "8":
				if "4" not in current_str:
					current_str += "4"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "3" not in current_str:
					current_str += "3"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "7" not in current_str:
					current_str += "7"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "b" not in current_str:
					current_str += "b"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "c" not in current_str:
					current_str += "c"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "9":
				if "5" not in current_str:
					current_str += "5"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "6" not in current_str:
					current_str += "6"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "a" not in current_str:
					current_str += "a"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "e" not in current_str:
					current_str += "e"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "d" not in current_str:
					current_str += "d"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "a":
				if "5" not in current_str:
					current_str += "5"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "6" not in current_str:
					current_str += "6"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "7" not in current_str:
					current_str += "7"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "b" not in current_str:
					current_str += "b"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "f" not in current_str:
					current_str += "f"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "e" not in current_str:
					current_str += "e"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "d" not in current_str:
					current_str += "d"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "9" not in current_str:
					current_str += "9"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "b":
				if "6" not in current_str:
					current_str += "6"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "7" not in current_str:
					current_str += "7"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "8" not in current_str:
					current_str += "8"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "c" not in current_str:
					current_str += "c"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "g" not in current_str:
					current_str += "g"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "f" not in current_str:
					current_str += "f"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "e" not in current_str:
					current_str += "e"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "a" not in current_str:
					current_str += "a"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "c":
				if "8" not in current_str:
					current_str += "8"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "7" not in current_str:
					current_str += "7"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "b" not in current_str:
					current_str += "b"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "f" not in current_str:
					current_str += "f"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "g" not in current_str:
					current_str += "g"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "d":
				if "9" not in current_str:
					current_str += "9"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "a" not in current_str:
					current_str += "a"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "e" not in current_str:
					current_str += "e"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "e":
				if "d" not in current_str:
					current_str += "d"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "9" not in current_str:
					current_str += "9"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "a" not in current_str:
					current_str += "a"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "b" not in current_str:
					current_str += "b"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "f" not in current_str:
					current_str += "f"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "f":
				if "e" not in current_str:
					current_str += "e"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "a" not in current_str:
					current_str += "a"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "b" not in current_str:
					current_str += "b"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "c" not in current_str:
					current_str += "c"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "g" not in current_str:
					current_str += "g"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "g":
				if "c" not in current_str:
					current_str += "c"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "b" not in current_str:
					current_str += "b"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "f" not in current_str:
					current_str += "f"
					boggle(row1, row2, row3, row4, current_str, dic, count)
	else:
		ans = ""
		for ch in current_str:
			if ch == "1":
				ans += row1[0]
			elif ch == "2":
				ans += row1[2]
			elif ch == "3":
				ans += row1[4]
			elif ch == "4":
				ans += row1[6]
			elif ch == "5":
				ans += row2[0]
			elif ch == "6":
				ans += row2[2]
			elif ch == "7":
				ans += row2[4]
			elif ch == "8":
				ans += row2[6]
			elif ch == "9":
				ans += row3[0]
			elif ch == "a":
				ans += row3[2]
			elif ch == "b":
				ans += row3[4]
			elif ch == "c":
				ans += row3[6]
			elif ch == "d":
				ans += row4[0]
			elif ch == "e":
				ans += row4[2]
			elif ch == "f":
				ans += row4[4]
			elif ch == "g":
				ans += row4[6]
		if ans in dic:
			if ans not in count:
				print("Found \""+ans+"\"")
				count.append(ans)
		if has_prefix(ans, dic):
			if current_str[len(current_str)-1] == "1":
				if "2" not in current_str:
					current_str += "2"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "5" not in current_str:
					current_str += "5"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "6" not in current_str:
					current_str += "6"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "2":
				if "1" not in current_str:
					current_str += "1"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "5" not in current_str:
					current_str += "5"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "6" not in current_str:
					current_str += "6"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "7" not in current_str:
					current_str += "7"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "3" not in current_str:
					current_str += "3"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "3":
				if "2" not in current_str:
					current_str += "2"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "6" not in current_str:
					current_str += "6"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "7" not in current_str:
					current_str += "7"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "8" not in current_str:
					current_str += "8"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "4" not in current_str:
					current_str += "4"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "4":
				if "3" not in current_str:
					current_str += "3"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "7" not in current_str:
					current_str += "7"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "8" not in current_str:
					current_str += "8"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "5":
				if "1" not in current_str:
					current_str += "1"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "2" not in current_str:
					current_str += "2"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "6" not in current_str:
					current_str += "6"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "a" not in current_str:
					current_str += "a"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "9" not in current_str:
					current_str += "9"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "6":
				if "1" not in current_str:
					current_str += "1"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "2" not in current_str:
					current_str += "2"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "3" not in current_str:
					current_str += "3"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "7" not in current_str:
					current_str += "7"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "b" not in current_str:
					current_str += "b"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "a" not in current_str:
					current_str += "a"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "5" not in current_str:
					current_str += "5"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "9" not in current_str:
					current_str += "9"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "7":
				if "2" not in current_str:
					current_str += "2"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "3" not in current_str:
					current_str += "3"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "4" not in current_str:
					current_str += "4"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "8" not in current_str:
					current_str += "8"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "c" not in current_str:
					current_str += "c"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "b" not in current_str:
					current_str += "b"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "a" not in current_str:
					current_str += "a"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "6" not in current_str:
					current_str += "6"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "8":
				if "4" not in current_str:
					current_str += "4"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "3" not in current_str:
					current_str += "3"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "7" not in current_str:
					current_str += "7"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "b" not in current_str:
					current_str += "b"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "c" not in current_str:
					current_str += "c"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "9":
				if "5" not in current_str:
					current_str += "5"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "6" not in current_str:
					current_str += "6"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "a" not in current_str:
					current_str += "a"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "e" not in current_str:
					current_str += "e"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "d" not in current_str:
					current_str += "d"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "a":
				if "5" not in current_str:
					current_str += "5"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "6" not in current_str:
					current_str += "6"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "7" not in current_str:
					current_str += "7"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "b" not in current_str:
					current_str += "b"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "f" not in current_str:
					current_str += "f"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "e" not in current_str:
					current_str += "e"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "d" not in current_str:
					current_str += "d"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "9" not in current_str:
					current_str += "9"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "b":
				if "6" not in current_str:
					current_str += "6"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "7" not in current_str:
					current_str += "7"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "8" not in current_str:
					current_str += "8"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "c" not in current_str:
					current_str += "c"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "g" not in current_str:
					current_str += "g"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "f" not in current_str:
					current_str += "f"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "e" not in current_str:
					current_str += "e"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "a" not in current_str:
					current_str += "a"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "c":
				if "8" not in current_str:
					current_str += "8"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "7" not in current_str:
					current_str += "7"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "b" not in current_str:
					current_str += "b"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "f" not in current_str:
					current_str += "f"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "g" not in current_str:
					current_str += "g"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "d":
				if "9" not in current_str:
					current_str += "9"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "a" not in current_str:
					current_str += "a"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "e" not in current_str:
					current_str += "e"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "e":
				if "d" not in current_str:
					current_str += "d"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "9" not in current_str:
					current_str += "9"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "a" not in current_str:
					current_str += "a"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "b" not in current_str:
					current_str += "b"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "f" not in current_str:
					current_str += "f"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "f":
				if "e" not in current_str:
					current_str += "e"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "a" not in current_str:
					current_str += "a"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "b" not in current_str:
					current_str += "b"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "c" not in current_str:
					current_str += "c"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "g" not in current_str:
					current_str += "g"
					boggle(row1, row2, row3, row4, current_str, dic, count)
			elif current_str[len(current_str)-1] == "g":
				if "c" not in current_str:
					current_str += "c"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "b" not in current_str:
					current_str += "b"
					boggle(row1, row2, row3, row4, current_str, dic, count)
					current_str = current_str[:len(current_str) - 1]
				if "f" not in current_str:
					current_str += "f"
					boggle(row1, row2, row3, row4, current_str, dic, count)


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dic = []
	with open(FILE, "r") as f:
		for line in f:
			line1 = line.strip()
			if 16 >= len(line1) >= 4:
				dic.append(line1)
	return dic


def has_prefix(sub_s, dic):
	"""
	:param sub_s: part of word
	:param dic: dictionary
	:return: True of False
	"""
	for voc in dic:
		if voc.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
