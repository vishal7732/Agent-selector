# Exercise 2
import random

def agents():
	users,names, time = [], [], {}
	for i in range(5):
		user = input("Enter Agent Names: ")
		name = []
		name.append(user)
		names.append(user)
		is_available = random.randint(0,1)         # 1 for Agent Available and 0 for agent is busy (so it look like real)
		name.append(is_available)
		if is_available == 1:
			available_since = random.randint(1,60)   # From how much time user is available (so it look like real)
			name.append(available_since)
			time[user] = available_since
		role = input("Enter Agent Role : ")
		name.append(role)
		users.append(name)

	def modes():
		mode = input("Select Agent Selection Mode By Typing This Mode Names (all available) (least busy) (random) : ")
		
		#all available
		if mode == "all available":
			for i in users:
				if i[1] == 0:
					print("All Agents are Not Available Please choose Differet Selection Mode")
					break
			else:
				print("Congrats! All agents are available and your issue is visible to them. Now they can pick the issue")


		#least busy
		elif mode == "least busy":
			try:
				max_t = max(time.values())
				def get_key(val):
					for key, value in time.items():
						if val == value:
							return key
				print(f"We have Selected {get_key(max_t)} as per least busy")
			except ValueError:
				print("Sorry All agent are Busy")
			
				
		#random
		elif mode == "random":
			a = random.choice(names)
			print(f"We randomly selected {a} agent for you ")
	
		else:
			print("Sorry!! you are Entered Wrong Mode. Try Agaig...")
			modes()
	modes()


agents()

