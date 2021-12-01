#/usr/bin/env python3

import random

import discord

import bisect

from dateutil import parser

# provided: read in the discord token
with open('discord_token.txt','r') as f:
    DISCORD_TOKEN = f.readline().strip()

# provided: variables
start_date = parser.parse('1/1/2021')
start_date_lunar_idx = 19 - 1
date_to_lunar_day = []
date_to_lunar_day_info = []
special_days = []

#####################  TO DO #######################################
# word to wake up the bot
expected_activation_word = 'calendar'

# create a reply given message content and the sender of the message
def make_reply( msg_content,user_name):
    pass
####################################################################


# provided: find lunar day
def get_lunar_day_idx(date):
    date = parser.parse(date)
    left_idx = bisect.bisect_left(special_days, start_date)    
    right_idx = bisect.bisect_right(special_days, date) 
    day_diff = (date-start_date).days+(right_idx - left_idx)+start_date_lunar_idx
    lunar_day_idx = day_diff % 30
    return lunar_day_idx

# provided: determine if a string is a date, and parse the date
def is_date(msg):
    try:
        date = parser.parse(msg)
        return True 
    except ValueError:
        return False
def get_date(msg):
    date = parser.parse(msg)
    return date

# provided: read in lunar calendar info
def warm_up():
    with open('calendar_special_day.txt','r') as f:
        for line in f:
            date = get_date(line.strip())
            special_days.append(date)
    with open('calendar_lunar_day_name.txt','r') as f:
        for line in f:
            name, date = line.strip().split()
            date_to_lunar_day.append(name)
    
    with open('calendar_lunar_day_info.txt','r') as f:
        for line in f:
            date, *info = line.strip().split()
            info = ' '.join(info)
            date_to_lunar_day_info.append(info)

# provided: discord bot
class CalendarBot(discord.Client):
    async def on_ready(self):
        # Runs when successfully connected to the server
        print('Logged on as', self.user)
        warm_up()

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        # This passes the message's text and author name as 
        reply = make_reply(message.content, message.author.name)

        if reply:
            await message.channel.send(reply)

if __name__ == "__main__":
    client = CalendarBot()
    client.run(DISCORD_TOKEN)
