import discord, random
from discord.ext import commands

class ForzaGen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
      if message.content.find("!ForzaRandom") != -1:
          challanges()
          CarPicked = random.choice(Car)
          await message.channel.send("***Russian Roulette Of Forza 5!***\n\n**The Car Category is:  **"+ CarPicked)
          if CarPicked in Range1:
              R1 = ['30K', '40K', '50K', '60K', '70K', '80K', '90K', '100K']
              RP1 = random.choice(R1)
              await message.channel.send("**The Budget Is:  **" + RP1)
          elif CarPicked in Range2:
              R2 = ['100K', '110K', '120K', '130K', '140K', '150K', '160K', '170K','180K', '190K', '200K']
              RP2 = random.choice(R2)
              await message.channel.send("**The Budget Is:  **" + RP2)
          elif CarPicked in Range3:
              R3 = ['400K', '410K', '420K', '430K', '440K', '450K', '460K', '470K','480K', '490K', '500K']
              RP3 = random.choice(R3)
              await message.channel.send("**The Budget Is:  **" + RP3)
          elif CarPicked in Range4:
              R4 = ['500K', '550K', '600K', '650K', '700K']
              RP4 = random.choice(R4)
              await message.channel.send("**The Budget Is:  **" + RP4)
          RanTyres = random.choice(Tyres)
          RT1 = random.choice(Timings)
          await message.channel.send("**The Tyres Required In Your Car:  **" + RanTyres)
          await message.channel.send("**The Time To Complete Your Build Is:  **" + RT1)
          await message.channel.send("**The Challanges Are:  **" + C1 + " , " + C2 + " , " + C3)
        
      #await bot.process_commands(message)

      #------------------------Forza Randomiser!------------------------#
Car = ['GT Cars', 'Super GT', 'Super HotHatch', 'Modern Rally', 'Modern Muscle','Classic Muscle ', 'Extreme Track Toy', 'Modern Sports', 'Classic Sports','Modern Super', 'Hyper Cars', 'Super saloon', 'Pickups']
Range1 = ['Hot Hatch', 'Modern Rally', 'Modern Muscle', 'Classic Muscle ','Classic Sports', 'Super saloon', 'Pickups', 'GT Cars', 'Modern Sports','Super HotHatch']
Range2 = ['Super GT', 'Modern Super']
Range3 = ['Extreme Track Toys']
Range4 = ['Hyper Cars']
Timings = ['2m', '3m', '5m', '10m', '15m']
Challanges = ['Looks', 'Race', 'Drag', 'Max Price', 'Lowest Price', 'Top Speed','Fastest Build', 'Highest HP', 'Longest Jump', 'Fastest Trap Zone','Highest Rating']
Tyres = ["Street Tyres", "Sport Tyres", "Semi-Slick Tyres", "slick-Race Tyres", "Drift Tyres", "Offroad Tyres", "Offroad Race Tyres", "Snow Tyres", "Drag Tyres"]

def challanges():
    x = 0
    for i in range(0, 3):
        x += 1
        if x == 1:
            global C1
            C1 = random.choice(Challanges)
        if x == 2:
            global C2
            C2 = random.choice(Challanges)
            while C2 == C1:
                C2 = random.choice(Challanges)
        if x == 3:
            global C3
            C3 = random.choice(Challanges)
            while C3 == C1 or C3 == C2:
                C3 = random.choice(Challanges)
#------------------------Forza Randomiser!------------------------#
        pass

def setup(bot):
    bot.add_cog(ForzaGen(bot))