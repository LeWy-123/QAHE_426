# List exercise
invitation = "--------------(I would lovely lie to invite you to my diner at 6pm)---------------"
print(invitation)
dinner_invites = ['John', 'Peter', 'Laszlo']
for invite in dinner_invites:
    print(f"I would like to invite {invite.title()}, to my dinner!")

print(invitation)
print(f"But my friend {dinner_invites[1].title()}, wont be able to participate in my dinner! :(")
dinner_invites[1] = 'Attila'

for invite in dinner_invites:
    print(f"I would like to invite {invite.title()}, to my dinner! (Updated)")

print(invitation)
print("I am found a bigger table I'm inviting more people to! Hurray")

dinner_invites.insert(0, 'Daphne')
mid_list = int(len(dinner_invites) / 2 )
dinner_invites.insert(mid_list, 'David')
dinner_invites.append('Barbara')
dinner_invites.sort()

for invite in dinner_invites:
    print(f"I would like to invite {invite.title()}, to my dinner! sorry for another dinner invitation!")

print(f"Sent invitations: {len(dinner_invites)}")
print(invitation)
print("Sorry I can't invite more than 2 people, my new dinner table wont arrive!")

print(invitation)

invite = 0
while invite < len(dinner_invites)+1:
    rejected_invite = dinner_invites.pop(1)
    print(rejected_invite, "Sorry, but you no longer come invite to my dinner!")
    invite += 1

print(invitation)
for invite in dinner_invites:
    print(f"You still invited to my dinner come to my house! {invite.title()}")

print(invitation)
del dinner_invites[-1]
del dinner_invites[-1]
print("List: ", dinner_invites)

print('-------------test codes------------------')

new_invites = [*dinner_invites[:], *(X for X in range(15)), 'End list', 'Element', 'File']
print(f'type of the variable: {type(new_invites)}, and the length of the list are: {len(new_invites)}', new_invites, sep='\n')
rectangle ='\t \U000025A3'
for O in new_invites:
    print(rectangle, O)
