# List exercise
inivtation = "--------------(I would lovely lie to invite you to my diner at 6pm)---------------"
print(inivtation)
dinner_invites = ['John', 'Peter', 'Laslov']
for invite in dinner_invites:
    print(f"I would like to invite {invite.title()}, to my dinner!")

print(inivtation)
print(f"But my friend {dinner_invites[1].title()}, wont be able to participate in my dinner! :(")
dinner_invites[1] = 'Attila'

for invite in dinner_invites:
    print(f"I would like to invite {invite.title()}, to my dinner! (Updated)")

print(inivtation)
print("I am found a bigger table I'm inviting more people to! Hurray")

dinner_invites.insert(0, 'Daphne')
mid_list = int(len(dinner_invites) / 2 )
dinner_invites.insert(mid_list, 'David')
dinner_invites.append('Barbara')
dinner_invites.sort()

for invite in dinner_invites:
    print(f"I would like to invite {invite.title()}, to my dinner! sorry for another dinner invitation!")

print(f"Sent invitations: {len(dinner_invites)}")
print(inivtation)
print("Sorry I can't invite more than 2 people, my new dinner table wont arrive!")

print(inivtation)

invite = 0
while invite < len(dinner_invites)+1:
    rejected_invite = dinner_invites.pop(1)
    print(rejected_invite, "Sorry, but you no longer come invite to my dinner!")
    invite += 1

print(inivtation)
for invite in dinner_invites:
    print(f"You still invited to my dinner come to my house! {invite.title()}")

print(inivtation)
del dinner_invites[-1]
del dinner_invites[-1]
print("List: ", dinner_invites)
