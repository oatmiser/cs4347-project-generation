import random

# server (id, language, capacity)
serverCount = 5
for i in range(serverCount):
  print("insert into server values ("+str(i+1)+",'"+random.choice(["AR", "BR", "DE", "EN", "ES", "FR", "HI", "JA", "RU", "ZH"])+"',40);")
print()

field = [l.rstrip() for l in open("battlefield.txt","r").readlines() if l.strip()]
town = [l.rstrip() for l in open("town.txt","r").readlines() if l.strip()]

# map (map_id, audio_file, server)
print("insert into map values ",end="")
for i in range(1,len(field)+len(town)):
  print("("+str(i)+",0x"+str((i*130)**2)[:4]+","+str(random.randint(1,serverCount))+"), ", end="")
print("("+str(len(field)+len(town))+",0xabcd,1);")
print()

# adjacentmaps (map_id, map2_id)
print("insert into adjacentmaps values ",end="")
"""
for i in range(2,len(field)+len(town)):
  print("("+str(i)+","+str(i-1)+"), ("+str(i)+","+str(i+1)+"), ",end="")
print("("+str(len(field)+len(town))+","+str(len(field)+len(town)-1)+");")
"""
size = len(field)+len(town)
for i in range(1,size):
  map2 = random.randint(1,size)
  while map2==i:
    map2 = random.randint(1,size)
  print("("+str(i)+","+str(map2)+"), ("+str(map2)+","+str(i)+"), ",end="")
print("("+str(size-1)+", "+str(size)+"), ("+str(size)+","+str(size-1)+");")
print()

s = set(range(1,len(field)+len(town)+1))
# town (id, map, pop, name, loc)
print("insert into town values ",end="")
for i in range(1,len(town)):
  id = random.choice(list(s))
  s.remove(id)
  print("("+str(i)+","+str(id)+","+str(random.randint(10,200))+",'"+town[i-1]+"','location'), ", end="")
id=random.choice(list(s))
s.remove(id)
print("("+str(len(town))+","+str(id)+","+str(random.randint(10,200))+",'"+town[-1]+"','location');")
print()

# npc (id, town, name, race, age, job, dialog)
npc = [l.rstrip() for l in open("npc.txt","r").readlines() if l.strip()]
race = [l.rstrip() for l in open("species2.txt","r").readlines() if l.strip()]
job = [l.rstrip() for l in open("job.txt","r").readlines() if l.strip()]
print("insert into npc values ",end="")
# every npc (random race, random job) is put in a random town
for i in range(1,len(npc)):
  val = [str(i),str(random.randint(1,len(town))),"'"+npc[i-1]+"'","'"+race[random.randint(0,len(race)-1)]+"'",str(random.randint(10,100)),"'"+job[random.randint(0,len(job)-1)]+"'","null"]
  print("("+",".join(val)+"), ",end="")
val = [str(len(npc)),"10","'"+npc[-1]+"'","'Human'","52","'Blacksmith'","'love my anvil'"]
print("("+",".join(val)+");")
print()

# building (id, town, name, islocked, type)
building = [l.rstrip() for l in open("building.txt","r").readlines() if l.strip()]
print("insert into building values ",end="")
# every town has 3+ buildings
id = 1
for i in range(1,len(town)):
  count = random.randint(3,10)
  for j in range(count):
    val = [id, i, "'"+random.choice(building)+"'", random.randint(0,1), random.choice(["residential", "restaurant", "store", "industrial", "government", "military", "hospital", "school", "university", "workshop", "barracks", "market", "farm"])]
    print("("+",".join([str(i) for i in val[:4]])+",'"+val[4]+"'), ",end="")
    id += 1
print("("+str(id)+","+str(len(town))+",'Number 1 Shop',0,'store');")  
print()

# battlefield (field_id, solo, name, desc, m id)
print("insert into battlefield values ",end="")
for i in range(1,len(field)):
  id = random.choice(list(s))
  s.remove(id)
  print("("+str(i)+","+str(random.choice([0,0,0,1]))+",'"+field[i-1]+"','description',"+str(id)+"), ",end="")
id=random.choice(list(s))
s.remove(id)
print("("+str(len(field))+",0,'"+field[-1]+"','description','"+str(id)+"');")
print()

# stats (id, maxhp, hp, maxmp, mp, attack, defense, intelligence, resistance, speed)
statCount = 50
print("insert into stats values ",end="")
for i in range(1,statCount):
  val = [i, random.randint(1,2001),0, random.randint(2,21),0, 5*random.randint(1,11), 10*random.randint(1,11), random.randint(1,11), 3*random.randint(1,6), random.randint(5,13)]
  val[2] = int(val[1]*random.uniform(0.1,1.0))
  val[4] = int(val[3]*random.uniform(0.1,1.0))
  print("("+",".join([str(i) for i in val])+"), ",end="")
print("("+str(statCount)+",1,1,1,1,1,1,1,1,1);")
print()

# genericstats (id, hp, attack, defense, intelligence, resistance, speed)
print("insert into genericstats values ",end="")
for i in range(1,statCount):
  val = [i, random.randint(1,2001), 5*random.randint(1,11), 10*random.randint(1,11), random.randint(1,11), 3*random.randint(1,6), random.randint(5,13)]
  print("("+",".join([str(i) for i in val])+"), ",end="")
print("("+str(statCount)+",1,1,1,1,1,1);")
print()

monster = [l.rstrip() for l in open("monster.txt","r").readlines() if l.strip()]
race = [l.rstrip() for l in open("species.txt","r").readlines() if l.strip()]
# monster (id, field, name, species, rank, level, stat, xp, death sound)
print("insert into monster values ",end="")
# each monster (random id, random race) in random field
for i in range(1,len(monster)):
  val = [i, random.randint(1,len(field)), "'"+monster[i-1]+"'", "'"+race[random.randint(0,len(race)-1)]+"'", random.randint(1,11), random.randint(1,51), random.randint(1,statCount), 10*random.randint(1,11), "0xab34"]
  print("("+",".join([str(i) for i in val])+"), ",end="")
print("("+str(len(monster))+",1,'Bowser','Koopa',10,100,1,20,0x882b);")
print()

player = [l.rstrip() for l in open("username.txt","r").readlines() if l.strip()]
# account (id, server, map)
print("insert into account values ",end="")
for i in range(1,len(player)):
  srvr = str(random.randint(1,serverCount))
  stuff = random.choice(["null", srvr, srvr, srvr])
  print("("+str(i)+","+stuff+","+("null" if stuff=="null" else str(random.randint(1,size)))+"), ",end="")
print("("+str(len(player))+",null,null);")
print()
# player (a_id, password, email, username)
print("insert into player values ",end="")
for i in range(1,len(player)):
  val = [i, "'"+"*"*random.randint(1,8)+"'", "'"+player[i-1][:6].lower()+"@gmail.com'", "'"+player[i-1]+"'"]
  print("("+",".join([str(i) for i in val])+"), ",end="")
val = [len(player), "'"+"*"*random.randint(1,8)+"'", "'"+player[-1][:6].lower()+"@gmail.com'", "'"+player[-1]+"'"]
print("("+",".join([str(i) for i in val])+");")
print()

# guild (name, level, leader)
guild = [l.rstrip() for l in open("guild.txt","r").readlines() if l.strip()]
print("insert into guild values ",end="")
# every guild have random account as leader
for i in range(1,len(guild)):
  val = ["'"+guild[i-1]+"'", random.randint(1,101), random.randint(1,len(player))]
  print("("+",".join([str(i) for i in val])+"), ",end="")
print("('"+",".join([str(i) for i in [guild[-1]+"'", random.randint(1,101), random.randint(1,len(player))]])+");")
print()

# skill (id, name, desc)
skill = [l.strip() for l in open("skill.txt", "r").readlines() if l.strip()]
print("insert into skills values ",end="")
for i in range(int(len(skill)/3 - 1)):
  #val = [int(skill[i*3])+1, skill[i*3+1], skill[i*3+2]]
  print("("+",".join([str(int(skill[3*i+0])+1), "'"+skill[3*i+1]+"'", "'"+skill[3*i+2]])+"'), ",end="")
print("("+str(int(skill[-3])+1)+",'"+skill[-2]+"','"+skill[-1]+"');")
print("insert into skills values ("+str(int(len(skill)/3+1))+",'Lycanthropy','Get a better nose.');")
print()

# class (name, stat, skill, skill2, skill3)
#print("insert into class values ",end="")
#('Wizard',"+"1,1);")
#for s in ["Warrior", "Wizard", "Archer", "Cleric"]:
#  print("("+"),",end="")
#print("('Tracker',1,1);")

# character (id, account, guild, ign, money, level, xp, levelup-xp, stat, class, skill, skill, skill)
print("insert into characters values ",end="")
# each account have 1-4 characters
cid = 1
for i in range(1,len(player)):
  amount = random.choice([1,1,1,1,2,2,3,4])
  for j in range(amount):
    skill2 = random.randint(0,int(len(skill)/3))
    if skill2==0:
      skill2="null"
    skill3 = random.randint(0,int(len(skill)/3))
    if skill3==0 or skill2=="null":
      skill3="null"
    g = "null" if random.randint(1,10)==1 else "'"+random.choice(guild)+"'"
    val = [cid, i, g, "'"+player[i-1][-8:]+"'", random.randint(1,1000), random.randint(1,50), random.randint(1,1000), random.randint(1200,2000), random.randint(1,statCount), "'"+random.choice(["Warrior", "Wizard", "Archer", "Cleric"])+"'", random.randint(1,int(len(skill)/3)), skill2, skill3]
    cid+=1
    print("("+",".join([str(i) for i in val])+"), ",end="")
print("("+str(cid)+",1,'HUBRIS','leeroyjnks',1,1,1,10,1,'Wizard',1,null,null);")
print()

# item (id, name, character, value)
# each item and sword is owned by some character, sword is a weapon gear type
item = [l.strip() for l in open("item.txt","r").readlines()]
print("insert into item values ",end="")
for i in range(1,len(item)):
  val = [i,"'"+item[i-1]+"'", random.randint(1,cid), random.randint(1,50)]
  print("("+",".join([str(i) for i in val])+"), ",end="")
print("("+",".join([str(i) for i in [len(item),"'"+item[-1]+"'",1, random.randint(1,50)]])+");")
weapon = [l.strip() for l in open("sword.txt","r").readlines()]
print("insert into item values ",end="")
for i in range(1,len(weapon)):
  val = [len(item)+i,"'"+weapon[i-1]+"'", random.randint(1,cid), random.randint(1,50)]
  print("("+",".join([str(i) for i in val])+"), ",end="")
print("("+",".join([str(i) for i in [len(item)+len(weapon),"'"+weapon[-1]+"'",1,random.randint(1,50)]])+");")

# equipment (id, type, description, stat, item)
equipment = [l.strip() for l in open("weapon.txt","r").readlines()]
print("insert into equipment values ",end="")
for i in range(10):
  val = [i+1, "'"+equipment[random.randint(0,len(equipment)-1)]+"'", "'description'", random.randint(1,statCount), len(item)+random.randint(1,len(weapon))]
  print("("+",".join([str(i) for i in val])+"), ",end="")
print("(11,'Boots','Made for walking',12,"+str(len(item)+random.randint(1,len(weapon)))+");")
print()

# quest (id, name, npc)
quest = [l.strip() for l in open("quest.txt","r").readlines()]
q1 = quest[:quest.index("")]
q2 = quest[quest.index("")+1:]
q3 = q2[q2.index("")+1:]
q2 = q2[:q2.index("")]
print("insert into quest values ",end="")
# each npc has random [1,5] quest
qid = 1
for i in range(1,len(npc)):
  count = random.randint(1,5)
  for j in range(count):
    qname = "'"+" ".join([q1[random.randint(0,len(q1)-1)], q2[random.randint(0,len(q2)-1)], q3[random.randint(0,len(q3)-1)]])+"'"
    val = [qid, qname, i]
    print("("+",".join([str(i) for i in val])+"), ",end="")
    qid += 1
print("("+",".join([str(i) for i in [qid, "'"+" ".join([q1[random.randint(0,len(q1)-1)], q2[random.randint(0,len(q2)-1)], q3[random.randint(0,len(q3)-1)]])+"'", len(npc)]])+");")
print()

# questreward (id (not pk), xp, money, item, character)
# characters may have many quests
# different characters may have the same active quest
print("insert into questreward values ",end="")
# each quest assigned to 1-20 characters
for i in range(1,qid):
  amount = random.randint(1,20)
  itm = "null" if random.randint(1,5)==1 else random.randint(1, len(item)+len(weapon))
  val = [i, 10*random.randint(1,11), random.randint(5,81), itm, "character"]
  for j in range(random.choice([1,1,1,1,2,2,amount,amount])):
    val[4] = random.randint(1,cid)
    print("("+",".join([str(i) for i in val])+"), ",end="")
print("("+",".join([str(i) for i in [id, 10*random.randint(1,11), random.randint(5,81), "null", random.randint(1,cid)]])+");")
print()



print("""#select * from adjacentmaps join map on map.map_id=adjacentmaps.map_id;
#select * from town join npc;
#select q_name, xp_reward, money_reward, item_id, c_id
#  from npc join quest join questreward;
#select * from battlefield where name like '%kong%';

#select m_id as ID, b_id as Field, m_name as Name, species from monster;
# select map_id from adjacentmaps where # all map2_id is field
# select m_name as _, species from monster where level>20;
select * from guild where guild_level=(select max(guild_level) from guild);
select username from player limit 5;
select * from player where length(password)=1;
select gear_type as Item,stat_bonus StatID, item_name Name, c_id Owner from equipment join item on equipment.item_id=item.item_id;""")
